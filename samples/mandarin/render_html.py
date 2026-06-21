#!/usr/bin/env python3
"""
Render Tengwar samples to PNG via HTML + headless Chrome.
Uses browser's OpenType engine for proper mark positioning.
"""

import subprocess
import sys
from pathlib import Path

FONT_DIR = Path(__file__).parent.parent / 'fonts' / 'Alcarin-Tengwar' / 'Font source' / 'build'
FONT_FILE = FONT_DIR / 'AlcarinTengwar-Regular.otf'
OUT_DIR = Path(__file__).parent
PNG_DIR = OUT_DIR / 'png'
HTML_DIR = OUT_DIR / 'html'


def render_to_html_and_png(name, tengwar_lines, title=""):
    """Create HTML and capture to PNG."""
    HTML_DIR.mkdir(exist_ok=True)
    PNG_DIR.mkdir(exist_ok=True)

    html_path = HTML_DIR / f'{name}.html'
    png_path = PNG_DIR / f'{name}.png'

    # Create HTML with embedded font
    html = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
@font-face {{
    font-family: "Alcarin Tengwar";
    src: url("file://{FONT_FILE.absolute()}");
}}
body {{
    background: white;
    padding: 20px;
    margin: 0;
}}
.tengwar {{
    font-family: "Alcarin Tengwar", sans-serif;
    font-size: 48px;
    line-height: 1.6;
    color: black;
}}
h1 {{
    font-family: sans-serif;
    font-size: 18px;
    color: #666;
    margin: 0 0 10px 0;
}}
</style>
</head>
<body>
'''
    if title:
        html += f'<h1>{title}</h1>\n'
    html += '<div class="tengwar">\n'
    for line in tengwar_lines:
        html += f'{line}<br>\n'
    html += '</div>\n</body></html>'

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    # Find Chrome
    chrome_paths = [
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser',
    ]
    chrome = next((p for p in chrome_paths if Path(p).exists()), None)

    if not chrome:
        print(f"  HTML: {html_path} (no Chrome found for PNG)")
        return html_path, None

    # Capture with headless Chrome
    try:
        result = subprocess.run([
            chrome,
            '--headless=new',
            '--disable-gpu',
            '--no-sandbox',
            f'--screenshot={png_path}',
            '--window-size=800,600',
            '--default-background-color=ffffffff',
            f'file://{html_path.absolute()}'
        ], capture_output=True, timeout=15)

        if png_path.exists() and png_path.stat().st_size > 1000:
            print(f"  PNG: {png_path}")
            return html_path, png_path
        else:
            print(f"  HTML: {html_path} (PNG capture failed)")
            return html_path, None

    except Exception as e:
        print(f"  HTML: {html_path} (Chrome error: {e})")
        return html_path, None


def main():
    from tengwar_mandarin import SAMPLES, PRACTICAL, convert_text

    all_samples = {**SAMPLES, **PRACTICAL}

    if not FONT_FILE.exists():
        print(f"Font not found: {FONT_FILE}")
        print("Download from upstream or build the font first.")
        sys.exit(1)

    for name, data in all_samples.items():
        print(f"\n{name}:")

        # Get title
        if 'title_zh' in data:
            title = f"{data['title_zh']} — {data['title_en']}"
        else:
            title = data.get('title', name)

        # Convert to Tengwar
        tengwar_lines = []
        if 'pinyin' in data:
            for line in data['pinyin']:
                tengwar_lines.append(convert_text(line, use_carrier_tones=False))
        elif 'items' in data:
            for pinyin, chinese, english in data['items']:
                tengwar_lines.append(convert_text(pinyin, use_carrier_tones=False))

        render_to_html_and_png(name, tengwar_lines, title)


if __name__ == '__main__':
    main()
