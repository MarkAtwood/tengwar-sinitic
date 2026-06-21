#!/usr/bin/env python3
"""
HarfBuzz-based text renderer for Tengwar.

Uses HarfBuzz for proper OpenType shaping (mark positioning)
and FreeType + Pillow for rasterization.
"""

import uharfbuzz as hb
import freetype
from PIL import Image, ImageDraw
from pathlib import Path


class TengwarRenderer:
    """Renders text with proper OpenType mark positioning."""

    def __init__(self, font_path, font_size=48):
        self.font_size = font_size

        # Load font for HarfBuzz (shaping)
        with open(font_path, 'rb') as f:
            font_data = f.read()
        face = hb.Face(font_data)
        self.hb_font = hb.Font(face)
        self.hb_font.scale = (font_size * 64, font_size * 64)  # 26.6 fixed point

        # Load font for FreeType (rasterization)
        self.ft_face = freetype.Face(str(font_path))
        self.ft_face.set_char_size(font_size * 64)

        # Units per em for scaling
        self.upem = face.upem

    def shape_text(self, text):
        """Shape text and return glyph positions."""
        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        hb.shape(self.hb_font, buf)

        positions = []
        x, y = 0, 0
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            positions.append({
                'glyph_id': info.codepoint,
                'x': x + pos.x_offset // 64,
                'y': y - pos.y_offset // 64,  # flip y for image coords
                'x_advance': pos.x_advance // 64,
                'y_advance': pos.y_advance // 64,
            })
            x += pos.x_advance // 64
            y += pos.y_advance // 64

        return positions, x  # positions and total width

    def render_glyph(self, glyph_id):
        """Render a single glyph to a bitmap."""
        self.ft_face.load_glyph(glyph_id, freetype.FT_LOAD_RENDER)
        bitmap = self.ft_face.glyph.bitmap
        if bitmap.width == 0 or bitmap.rows == 0:
            return None, 0, 0

        # Convert bitmap to image
        data = bytes(bitmap.buffer)
        img = Image.frombytes('L', (bitmap.width, bitmap.rows), data)

        # Glyph positioning offsets
        left = self.ft_face.glyph.bitmap_left
        top = self.ft_face.glyph.bitmap_top

        return img, left, top

    def render_line(self, text, color=(0, 0, 0)):
        """Render a line of text to an RGBA image."""
        positions, total_width = self.shape_text(text)

        # Calculate bounds
        ascender = self.ft_face.size.ascender // 64
        descender = abs(self.ft_face.size.descender // 64)
        height = ascender + descender
        width = max(total_width + 20, 100)  # padding

        # Create image
        img = Image.new('RGBA', (width, height), (255, 255, 255, 0))

        # Render each glyph
        baseline_y = ascender
        for pos in positions:
            glyph_img, left, top = self.render_glyph(pos['glyph_id'])
            if glyph_img is None:
                continue

            # Position glyph
            x = pos['x'] + left
            y = baseline_y - top + pos['y']

            # Create colored glyph
            colored = Image.new('RGBA', glyph_img.size, (*color, 255))
            img.paste(colored, (x, y), glyph_img)

        return img


def render_sample_png(lines_data, output_path, fonts, font_sizes=None):
    """
    Render sample to PNG with multiple fonts.

    Args:
        lines_data: list of (pinyin, hanzi, tengwar, names) tuples
        output_path: where to write PNG
        fonts: dict of {name: font_path}
        font_sizes: dict of {name: size} (optional)
    """
    sizes = font_sizes or {'pinyin': 24, 'hanzi': 34, 'tengwar': 48, 'names': 16}

    # Create renderers
    renderers = {}
    for name, path in fonts.items():
        if Path(path).exists():
            renderers[name] = TengwarRenderer(path, sizes.get(name, 32))

    # Render each line
    line_images = []
    row_gap = 8
    block_gap = 24

    for pinyin, hanzi, tengwar, names in lines_data:
        block = []

        # Pinyin (use system font fallback)
        if 'pinyin' in renderers:
            block.append(renderers['pinyin'].render_line(pinyin, color=(100, 100, 100)))

        # Hanzi
        if 'hanzi' in renderers:
            block.append(renderers['hanzi'].render_line(hanzi, color=(0, 0, 0)))

        # Tengwar
        if 'tengwar' in renderers:
            block.append(renderers['tengwar'].render_line(tengwar, color=(0, 0, 0)))

        # Names (monospace)
        if 'names' in renderers:
            block.append(renderers['names'].render_line(names, color=(150, 150, 150)))

        line_images.append(block)

    # Calculate total dimensions
    max_width = 100
    total_height = 20  # top padding

    for block in line_images:
        for img in block:
            max_width = max(max_width, img.width)
        block_height = sum(img.height for img in block) + row_gap * (len(block) - 1)
        total_height += block_height + block_gap

    # Compose final image
    final = Image.new('RGB', (max_width + 40, total_height), (255, 255, 255))
    y = 20

    for block in line_images:
        for img in block:
            final.paste(img, (20, y), img)
            y += img.height + row_gap
        y += block_gap - row_gap  # extra gap between blocks

    final.save(output_path)
    return output_path


def find_system_fonts():
    """Find system fonts for different scripts on macOS."""
    import subprocess
    fonts = {}

    # Common font locations
    candidates = {
        'latin': [
            '/System/Library/Fonts/Helvetica.ttc',
            '/System/Library/Fonts/SFNSText.ttf',
            '/Library/Fonts/Arial.ttf',
        ],
        'cjk': [
            '/System/Library/Fonts/STSong.ttf',
            '/System/Library/Fonts/Supplemental/Songti.ttc',
            '/Library/Fonts/Songti.ttc',
            '/System/Library/Fonts/PingFang.ttc',
        ],
        'mono': [
            '/System/Library/Fonts/Menlo.ttc',
            '/System/Library/Fonts/Monaco.ttf',
            '/Library/Fonts/Courier New.ttf',
        ],
    }

    for name, paths in candidates.items():
        for p in paths:
            if Path(p).exists():
                fonts[name] = p
                break

    return fonts


def render_multiline_png(lines_data, output_path, tengwar_font, font_sizes=None):
    """
    Render sample with pinyin, hanzi, tengwar, and names.

    Uses HarfBuzz for tengwar, Pillow for other text.
    """
    from PIL import ImageFont

    sizes = font_sizes or {'pinyin': 24, 'hanzi': 36, 'tengwar': 48, 'names': 14}
    sys_fonts = find_system_fonts()

    # Create tengwar renderer
    tengwar_renderer = TengwarRenderer(str(tengwar_font), sizes['tengwar'])

    # Load PIL fonts for other text
    try:
        latin_font = ImageFont.truetype(sys_fonts.get('latin', '/System/Library/Fonts/Helvetica.ttc'), sizes['pinyin'])
        cjk_font = ImageFont.truetype(sys_fonts.get('cjk', '/System/Library/Fonts/PingFang.ttc'), sizes['hanzi'])
        mono_font = ImageFont.truetype(sys_fonts.get('mono', '/System/Library/Fonts/Menlo.ttc'), sizes['names'])
    except Exception:
        # Fallback to default
        latin_font = ImageFont.load_default()
        cjk_font = latin_font
        mono_font = latin_font

    # Calculate dimensions
    row_gap = 10
    block_gap = 30
    padding = 20

    # First pass: measure
    max_width = 400
    total_height = padding

    for pinyin, hanzi, tengwar, names in lines_data:
        # Measure each row
        _, tengwar_width = tengwar_renderer.shape_text(tengwar)
        max_width = max(max_width, tengwar_width + 40)
        # Estimate height: 4 rows per block
        block_height = sizes['pinyin'] + sizes['hanzi'] + sizes['tengwar'] + sizes['names'] + row_gap * 3
        total_height += block_height + block_gap

    total_height += padding

    # Create image
    img = Image.new('RGB', (max_width + padding * 2, total_height), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    y = padding
    for pinyin, hanzi, tengwar, names in lines_data:
        x = padding

        # Pinyin (grey)
        draw.text((x, y), pinyin, font=latin_font, fill=(100, 100, 100))
        y += sizes['pinyin'] + row_gap

        # Hanzi (black)
        draw.text((x, y), hanzi, font=cjk_font, fill=(0, 0, 0))
        y += sizes['hanzi'] + row_gap

        # Tengwar (HarfBuzz rendered)
        tengwar_img = tengwar_renderer.render_line(tengwar, color=(0, 0, 0))
        img.paste(tengwar_img, (x, y), tengwar_img)
        y += sizes['tengwar'] + row_gap

        # Names (grey monospace)
        draw.text((x, y), names, font=mono_font, fill=(150, 150, 150))
        y += sizes['names'] + block_gap

    img.save(output_path)
    return output_path


if __name__ == '__main__':
    from pathlib import Path
    from tengwar_mandarin import convert_text, tengwar_to_names

    font_dir = Path(__file__).parent.parent.parent / 'fonts' / 'Alcarin-Tengwar' / 'Font source' / 'build'
    tengwar_font = font_dir / 'AlcarinTengwar-Regular.otf'

    if tengwar_font.exists():
        # Test full render
        test_data = [
            ('nǐ hǎo', '你好', convert_text('ni3 hao3'), tengwar_to_names(convert_text('ni3 hao3'))),
            ('zài jiàn', '再见', convert_text('zai4 jian4'), tengwar_to_names(convert_text('zai4 jian4'))),
        ]
        render_multiline_png(test_data, '/tmp/test_full.png', tengwar_font)
        print("Test image saved to /tmp/test_full.png")
    else:
        print(f"Font not found: {tengwar_font}")
