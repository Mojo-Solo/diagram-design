#!/usr/bin/env python3
"""Fail a page that uses colours outside its diagram-design profile.

Usage: check_palette.py PAGE.html [--profile SLUG]
Without --profile, reads `profile: <slug>` from the nearest .diagram-design marker above PAGE.
Allowed colours: every hex and rgb() triple in the profile's `### Semantic roles` table,
plus #fff/#000. CSS comments and data: URIs are skipped. Exit 1 lists each stray colour with its line.
"""
import re, sys, pathlib, argparse

HEX = re.compile(r'#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b')
# A colour in page source sits after `:`, `=`, `(` or `,` (CSS values, SVG attributes); prose like "PR #491" does not.
COLOUR = re.compile(r'[:=(,]\s*["\']?(#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3}))\b')
RGB = re.compile(r'rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)')

def norm(h):
    h = h.lower().lstrip('#')
    return '#' + (''.join(c * 2 for c in h) if len(h) == 3 else h)

def profile_slug(page):
    for d in [page.resolve().parent, *page.resolve().parents]:
        m = d / '.diagram-design'
        if m.is_file():
            g = re.fullmatch(r'profile:\s*([a-z0-9][a-z0-9-]{0,63})\s*\n?', m.read_text())
            if g:
                return g.group(1)
    sys.exit('no --profile and no valid .diagram-design marker above the page')

def allowed(slug):
    t = (pathlib.Path.home() / '.diagram-design/profiles' / f'{slug}.md').read_text()
    table = t.split('### Semantic roles', 1)[1].split('\n#', 1)[0]
    ok = {norm(h) for h in HEX.findall(table)} | {'#ffffff', '#000000'}
    ok |= {'#%02x%02x%02x' % tuple(map(int, m)) for m in RGB.findall(table)}
    return ok

def main():
    a = argparse.ArgumentParser(); a.add_argument('page'); a.add_argument('--profile')
    o = a.parse_args(); page = pathlib.Path(o.page)
    slug = o.profile or profile_slug(page); ok = allowed(slug)
    src = page.read_text()
    src = re.sub(r'/\*.*?\*/', lambda m: '\n' * m.group().count('\n'), src, flags=re.S)
    src = re.sub(r'data:[^"\')\s]+', 'data:', src)
    bad = []
    for n, line in enumerate(src.split('\n'), 1):
        for h in COLOUR.findall(line):
            if norm(h) not in ok: bad.append((n, h))
        for m in RGB.findall(line):
            c = '#%02x%02x%02x' % tuple(map(int, m))
            if c not in ok: bad.append((n, f'rgb({",".join(m)})'))
    if bad:
        print(f'FAIL {page.name}: {len(bad)} colour(s) outside profile "{slug}"')
        for n, c in bad: print(f'  line {n}: {c}')
        sys.exit(1)
    print(f'OK {page.name}: every colour is in profile "{slug}"')

main()
