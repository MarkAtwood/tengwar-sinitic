#!/usr/bin/env python3
"""
Render Tengwar samples to SVG and PNG.

Requires:
    pip install fonttools cairosvg pillow

Usage:
    python render.py              # render all samples
    python render.py jing_ye_si   # render specific sample
"""

import sys
import os
import re
from pathlib import Path

# Numbered pinyin → accented pinyin
TONE_MARKS = {
    'a': 'āáǎàa', 'e': 'ēéěèe', 'i': 'īíǐìi',
    'o': 'ōóǒòo', 'u': 'ūúǔùu', 'ü': 'ǖǘǚǜü',
}

def _add_tone(vowels, tone):
    """Add tone mark to vowel string, return modified string."""
    if tone == 5 or tone == 0:
        return vowels
    # a/e always get the mark; 'ou' → mark on o; else last vowel
    for v in 'ae':
        if v in vowels:
            return vowels.replace(v, TONE_MARKS[v][tone-1], 1)
    if 'ou' in vowels:
        return vowels.replace('o', TONE_MARKS['o'][tone-1], 1)
    # last vowel
    for i in range(len(vowels)-1, -1, -1):
        if vowels[i] in TONE_MARKS:
            return vowels[:i] + TONE_MARKS[vowels[i]][tone-1] + vowels[i+1:]
    return vowels

def numbered_to_accented(text):
    """Convert 'ni3 hao3' → 'nǐ hǎo'."""
    def convert_syllable(m):
        syl, tone = m.group(1), int(m.group(2) or 5)
        # find vowel cluster
        match = re.search(r'([aeiouü]+)', syl, re.I)
        if not match:
            return syl
        pre, vowels, post = syl[:match.start()], match.group(1), syl[match.end():]
        return pre + _add_tone(vowels.lower(), tone) + post
    return re.sub(r'([a-züA-ZÜ]+)([1-5])?', convert_syllable, text)

# Font location (two levels up from samples/mandarin/)
FONT_DIR = Path(__file__).parent.parent.parent / 'fonts' / 'Alcarin-Tengwar' / 'Font source' / 'build'
FONT_FILE = FONT_DIR / 'AlcarinTengwar-Regular.otf'

# Output directories
OUT_DIR = Path(__file__).parent
SVG_DIR = OUT_DIR / 'svg'
PNG_DIR = OUT_DIR / 'png'


def ensure_font():
    """Check font exists, give build instructions if not."""
    if not FONT_FILE.exists():
        print(f"Font not found: {FONT_FILE}")
        print("\nBuild the font first:")
        print(f"  cd {FONT_DIR.parent}")
        print("  python build.py")
        sys.exit(1)


def render_text_to_svg(lines_data, output_path, font_size=48):
    """
    Render lines with pinyin, hanzi, tengwar, and romanized names to SVG.

    Args:
        lines_data: list of (pinyin, hanzi, tengwar, names) tuples
        output_path: where to write the SVG
        font_size: base font size (tengwar uses this, others smaller)
    """
    # four rows per line: pinyin, hanzi, tengwar, names
    row_height = font_size + 10
    block_height = row_height * 4 + 20
    height = block_height * len(lines_data) + 20
    width = 1000

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">',
        '<defs><style>',
        f'.pinyin {{ font-family: sans-serif; font-size: {int(font_size*0.5)}px; fill: #666; }}',
        f'.hanzi {{ font-family: "Songti SC", "Noto Serif CJK SC", serif; font-size: {int(font_size*0.7)}px; }}',
        f'.tengwar {{ font-family: "Alcarin Tengwar"; font-size: {font_size}px; }}',
        f'.names {{ font-family: monospace; font-size: {int(font_size*0.35)}px; fill: #999; }}',
        '</style></defs>',
        f'<rect width="{width}" height="{height}" fill="white"/>',
    ]

    y = 30
    for pinyin, hanzi, tengwar, names in lines_data:
        svg.append(f'<text x="20" y="{y}" class="pinyin">{pinyin}</text>')
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


def render_png_harfbuzz(lines_data, png_path):
    """Render PNG using HarfBuzz for proper OpenType mark positioning."""
    try:
        from render_harfbuzz import render_multiline_png
        render_multiline_png(lines_data, str(png_path), FONT_FILE)
        return png_path
    except ImportError as e:
        print(f"HarfBuzz renderer not available: {e}")
        print("Run: pip install uharfbuzz freetype-py pillow")
        return None
    except Exception as e:
        print(f"HarfBuzz render failed: {e}")
        return None


def render_sample(name, sample_data, use_carrier_tones=False):
    """Render a sample to SVG and PNG with pinyin, hanzi, tengwar, and names."""
    from tengwar_mandarin import convert_text, tengwar_to_names

    SVG_DIR.mkdir(exist_ok=True)
    PNG_DIR.mkdir(exist_ok=True)

    # Build (pinyin, hanzi, tengwar, names) tuples
    lines_data = []
    if 'pinyin' in sample_data:
        for pinyin, hanzi in zip(sample_data['pinyin'], sample_data['chinese']):
            tengwar = convert_text(pinyin, use_carrier_tones)
            names = tengwar_to_names(tengwar)
            lines_data.append((numbered_to_accented(pinyin), hanzi, tengwar, names))
    elif 'items' in sample_data:
        for pinyin, hanzi, english in sample_data['items']:
            tengwar = convert_text(pinyin, use_carrier_tones)
            names = tengwar_to_names(tengwar)
            lines_data.append((numbered_to_accented(pinyin), hanzi, tengwar, names))

    # Render
    svg_path = SVG_DIR / f'{name}.svg'
    png_path = PNG_DIR / f'{name}.png'

    render_text_to_svg(lines_data, svg_path)
    print(f"  SVG: {svg_path}")

    if render_png_harfbuzz(lines_data, png_path):
        print(f"  PNG: {png_path}")


def generate_markdown(name, sample_data):
    """Generate markdown source file for a sample."""
    from tengwar_mandarin import convert_text, tengwar_to_names

    lines = []

    if 'title_zh' in sample_data:
        # Poem format - show all four per line
        lines.append(f"# {sample_data['title_zh']} — {sample_data['title_en']}")
        lines.append('')
        lines.append(f"**Author:** {sample_data['author']}")
        lines.append('')
        lines.append('| Pinyin | 汉字 | Tengwar | Romanized |')
        lines.append('|--------|------|---------|-----------|')
        for pinyin, hanzi in zip(sample_data['pinyin'], sample_data['chinese']):
            tengwar = convert_text(pinyin)
            names = tengwar_to_names(tengwar)
            lines.append(f'| {numbered_to_accented(pinyin)} | {hanzi} | {tengwar} | `{names}` |')
        lines.append('')
        lines.append('## Translation')
        lines.append('')
        for line in sample_data['translation']:
            lines.append(f'*{line}*')
        lines.append('')
        lines.append('## Rendered')
        lines.append('')
        lines.append(f'![{name}](svg/{name}.svg)')
        lines.append('')
    else:
        # Practical list format
        lines.append(f"# {sample_data['title']}")
        lines.append('')
        lines.append('| Pinyin | 汉字 | English | Tengwar | Romanized |')
        lines.append('|--------|------|---------|---------|-----------|')
        for pinyin, hanzi, english in sample_data['items']:
            tengwar = convert_text(pinyin)
            names = tengwar_to_names(tengwar)
            lines.append(f'| {numbered_to_accented(pinyin)} | {hanzi} | {english} | {tengwar} | `{names}` |')
        lines.append('')
        lines.append('## Rendered')
        lines.append('')
        lines.append(f'![{name}](svg/{name}.svg)')
        lines.append('')

    md_path = OUT_DIR / f'{name}.md'
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"  MD: {md_path}")


def main():
    from tengwar_mandarin import SAMPLES, PRACTICAL

    all_samples = {**SAMPLES, **PRACTICAL}

    # Filter by command line args if provided
    if len(sys.argv) > 1:
        names = sys.argv[1:]
        samples_to_render = {k: v for k, v in all_samples.items() if k in names}
        if not samples_to_render:
            print(f"Unknown samples: {names}")
            print(f"Available: {list(all_samples.keys())}")
            sys.exit(1)
    else:
        samples_to_render = all_samples

    # Check font exists before rendering
    # (markdown generation works without font)
    font_exists = FONT_FILE.exists()
    if not font_exists:
        print(f"Note: Font not found at {FONT_FILE}")
        print("Generating markdown only. Build font for SVG/PNG.\n")

    for name, data in samples_to_render.items():
        print(f"\n{name}:")
        generate_markdown(name, data)
        if font_exists:
            render_sample(name, data)


if __name__ == '__main__':
    main()
