#!/usr/bin/env python3
"""Build the combined subscription for apps, flags, UI, and network policy groups."""

import json
import re
from collections import Counter
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
RAW_PREFIX = 'https://raw.githubusercontent.com/lucking7/H.F./main/'
INDEXES = (
    'Routing-Policy.json',
    'Routing-Policy144px.json',
    'Apps.json',
    'Apps144px.json',
    'Flags.json',
    'Flags-macOS.json',
    'Flags-macOS144px.json',
    'UI.json',
    'UI-Handdrawn-Ink.json',
    'Region-Symbols.json',
    'Region-Symbols144px.json',
    'Region-Letters-Color.json',
    'Region-Letters-Color144px.json',
)
COLLECTION_LABELS = {'flags': 'Flags', 'logo': 'Apps', 'signal': 'UI'}
REGION_LABELS = {'symbols': 'Symbol', 'letters': 'Letters'}
REGION_SIZES = {'png': '1024px', '144px': '144px'}


def local_image_path(url):
    if not isinstance(url, str) or not url.startswith(RAW_PREFIX):
        raise ValueError(f'Expected an image URL in this repository, got {url!r}')
    encoded_path = url[len(RAW_PREFIX):]
    if re.search(r'%(?![0-9a-fA-F]{2})|[?#\x00-\x20\x7f]', encoded_path):
        raise ValueError(f'Invalid image URL: {url!r}')
    path = unquote(encoded_path, errors='strict')
    parts = path.split('/')
    if (
        parts[0] not in COLLECTION_LABELS
        or any(part in ('', '.', '..') for part in parts)
        or '\\' in path
        or '\0' in path
        or not path.lower().endswith('.png')
    ):
        raise ValueError(f'Invalid repository image path: {path!r}')
    image = ROOT / path
    if not image.resolve().is_relative_to(ROOT) or not image.is_file():
        raise ValueError(f'Image missing from the repository: {path!r}')
    return path


def combined_icons():
    icons_by_path = {}
    for filename in INDEXES:
        source = json.loads((ROOT / filename).read_text(encoding='utf-8'))
        icons = source.get('icons') if isinstance(source, dict) else None
        if not isinstance(icons, list):
            raise ValueError(f'{filename} must have an icons array')
        for line, icon in enumerate(icons, start=1):
            try:
                name = icon.get('name') if isinstance(icon, dict) else None
                if not isinstance(name, str) or not name.strip():
                    raise ValueError('Expected a non-empty icon name')
                url = icon.get('url')
                path = local_image_path(url)
            except ValueError as error:
                raise ValueError(f'{filename}, icon {line}: {error}') from error
            entry = icons_by_path.setdefault(path, {'name': name, 'url': url})
            # Prefer the app title over the file-derived alias in Apps.json.
            if filename == 'Apps144px.json' and entry['name'].casefold() == f'{Path(path).stem.casefold()}-144px':
                entry['name'] = name

    for path, icon in icons_by_path.items():
        if path.startswith('logo/ai-glass/144px/'):
            # Keep the size visible when a narrow picker clips the label.
            icon['name'] = '144px · ' + icon['name'].removesuffix(' (144px)')
        elif path.startswith('flags/regions/'):
            _, _, style, size, _ = path.split('/')
            icon['name'] = f"{icon['name']} ({REGION_LABELS[style]} · {REGION_SIZES[size]})"

    base_counts = Counter(icon['name'].casefold() for icon in icons_by_path.values())
    for path, icon in icons_by_path.items():
        name = icon['name']
        if base_counts[name.casefold()] > 1:
            category = path.split('/', 1)[0]
            qualifier = COLLECTION_LABELS[category]
            if path.startswith('signal/routing-policy/'):
                qualifier = f'{Path(path).parent.name}px'
            icon['name'] = f'{name} ({qualifier})'

    label_counts = Counter(icon['name'].casefold() for icon in icons_by_path.values())
    used_labels = {}
    for path, icon in icons_by_path.items():
        name = icon['name']
        if label_counts[name.casefold()] > 1:
            name = f'{name} [{Path(path).with_suffix("").as_posix()}]'
            icon['name'] = name
        previous = used_labels.setdefault(name.casefold(), path)
        if previous != path:
            raise ValueError(f'Icon label {name!r} is ambiguous for {previous!r} and {path!r}')
    return list(icons_by_path.values())


def main():
    icons = combined_icons()
    catalog = {
        'name': "LUCK's 全部图标",
        'description': 'Apps, flags, UI, and network policy groups, with distinct styles and sizes.',
        'icons': icons,
    }
    output = ROOT / 'All.json'
    content = (json.dumps(catalog, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    if not output.exists() or output.read_bytes() != content:
        with TemporaryDirectory(dir=ROOT) as directory:
            draft = Path(directory) / output.name
            draft.write_bytes(content)
            draft.replace(output)
    print(f'{output.name}: {len(icons)} icons from {len(INDEXES)} indexes')


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError) as error:
        raise SystemExit(str(error)) from None
