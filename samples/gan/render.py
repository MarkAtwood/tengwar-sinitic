#!/usr/bin/env python3
"""
Render Gan (Nanchang) Tengwar samples to SVG.

Usage:
    python render.py                    # render all samples
    python render.py gan-common-phrases # render specific sample
"""

import sys
import re
from pathlib import Path

# Font location
FONT_DIR = Path(__file__).parent.parent.parent / 'fonts' / 'Alcarin-Tengwar' / 'Font source' / 'build'
FONT_FILE = FONT_DIR / 'AlcarinTengwar-Regular.otf'

# Output directories
OUT_DIR = Path(__file__).parent
SVG_DIR = OUT_DIR / 'svg'


def render_text_to_svg(lines_data, output_path, font_size=48):
    """
    Render lines with Gan romanization, hanzi, tengwar, and romanized names to SVG.

    Args:
        lines_data: list of (romanization, hanzi, tengwar, names) tuples
        output_path: where to write the SVG
        font_size: base font size (tengwar uses this, others smaller)
    """
    row_height = font_size + 10
    block_height = row_height * 4 + 20
    height = block_height * len(lines_data) + 20
    width = 1000

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">',
        '<defs><style>',
        f'.gan {{ font-family: sans-serif; font-size: {int(font_size*0.5)}px; fill: #666; }}',
        f'.hanzi {{ font-family: "Songti SC", "Noto Serif CJK SC", serif; font-size: {int(font_size*0.7)}px; }}',
        f'.tengwar {{ font-family: "Alcarin Tengwar"; font-size: {font_size}px; }}',
        f'.names {{ font-family: monospace; font-size: {int(font_size*0.35)}px; fill: #999; }}',
        '</style></defs>',
        f'<rect width="{width}" height="{height}" fill="white"/>',
    ]

    y = 30
    for romanization, hanzi, tengwar, names in lines_data:
        svg.append(f'<text x="20" y="{y}" class="gan">{romanization}</text>')
        y += row_height
        svg.append(f'<text x="20" y="{y}" class="hanzi">{hanzi}</text>')
        y += row_height
        svg.append(f'<text x="20" y="{y}" class="tengwar">{tengwar}</text>')
        y += row_height
        svg.append(f'<text x="20" y="{y}" class="names">{names}</text>')
        y += row_height + 20

    svg.append('</svg>')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))

    return output_path


def render_sample(name):
    """Render a single sample to SVG."""
    from tengwar_gan import convert_text, tengwar_to_names

    md_path = OUT_DIR / f'{name}.md'
    if not md_path.exists():
        print(f"Sample not found: {md_path}")
        return

    SVG_DIR.mkdir(exist_ok=True)

    # Parse markdown and re-generate tengwar from romanization
    lines_data = []
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Gan table format: | Chinese | Romanization | English | Tengwar | Names |
    for line in content.split('\n'):
        if '|' in line and not line.startswith('|--'):
            parts = [p.strip() for p in line.split('|')]
            # parts[0] is empty (before first |), parts[-1] may be empty
            # Expected: ['', 'Chinese', 'Romanization', 'English', 'Tengwar', 'Names', '']
            if len(parts) >= 4:
                hanzi = parts[1]
                romanization = parts[2]
                # Skip header rows and separator rows
                if romanization and hanzi and 'Romanization' not in romanization and '---' not in hanzi:
                    # Check for CJK characters to ensure it's a data row
                    has_cjk = any('\u4e00' <= c <= '\u9fff' for c in hanzi)
                    if has_cjk:
                        try:
                            tengwar = convert_text(romanization)
                            names = tengwar_to_names(tengwar)
                            lines_data.append((romanization, hanzi, tengwar, names))
                        except Exception as e:
                            print(f"  Warning: could not convert '{romanization}': {e}")

    if lines_data:
        svg_path = SVG_DIR / f'{name}.svg'
        render_text_to_svg(lines_data, svg_path)
        print(f"  SVG: {svg_path} ({len(lines_data)} entries)")
    else:
        print(f"  No data found in {name}.md")


def main():
    # Available samples (derived from markdown files)
    samples = ['gan-common-phrases', 'gan-proverbs']

    # Filter by command line args if provided
    if len(sys.argv) > 1:
        samples_to_render = sys.argv[1:]
        for s in samples_to_render:
            if s not in samples:
                print(f"Unknown sample: {s}")
                print(f"Available: {samples}")
                sys.exit(1)
    else:
        samples_to_render = samples

    print("Rendering Gan (Nanchang) Tengwar samples...")
    for name in samples_to_render:
        print(f"\n{name}:")
        render_sample(name)


if __name__ == '__main__':
    main()
