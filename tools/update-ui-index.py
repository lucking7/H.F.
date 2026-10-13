#!/usr/bin/env python3
"""Refresh the combined UI index without removing existing image references."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = (
    ('Ink', 'UI-Handdrawn-Ink.json'),
    ('Minimal', 'UI-Minimal.json'),
    ('Relief', 'Strategy.json'),
    ('Relief Color', 'StrategyColor.json'),
)


def main():
    path = ROOT / 'UI.json'
    combined = json.loads(path.read_text())
    icons = combined['icons']
    seen = {icon['url'] for icon in icons}
    if len(seen) != len(icons):
        raise ValueError('Existing UI.json contains duplicate URLs; resolve before updating')
    for prefix, filename in COLLECTIONS:
        collection = json.loads((ROOT / filename).read_text())
        for icon in collection['icons']:
            if icon['url'] not in seen:
                icons.append({'name': f"{prefix} - {icon['name']}", 'url': icon['url']})
                seen.add(icon['url'])
    if len({icon['name'] for icon in icons}) != len(icons):
        raise ValueError('UI icon names must be unique')
    for icon in icons:
        relative = icon['url'].split('/main/', 1)[-1]
        if not (ROOT / relative).is_file():
            raise ValueError(f"Missing image: {icon['url']}")
    combined['description'] = (
        'Combined UI collection: original icons, decorative ink drawings, black line icons, '
        'and both Relief appearances. Unique image URLs; family prefixes distinguish new icon names.'
    )
    path.write_text(json.dumps(combined, ensure_ascii=False, indent=2) + '\n')
    print(f'UI.json: {len(icons)} icons')


if __name__ == '__main__':
    main()
