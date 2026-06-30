#!/usr/bin/env python3
"""
Render Tengwar samples to PDF with embedded vector paths.

Text is converted to outlines so PDFs work without fonts installed.
Uses HarfBuzz for shaping, fonttools for glyph outlines, reportlab for PDF.
"""

import re
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.recordingPen import RecordingPen
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont as RLTTFont
import uharfbuzz as hb


# Tone number to accent conversion (supports tones 1-8)
TONE_ACCENTS = {
    'a': ['ā', 'á', 'ǎ', 'à', 'a', 'a', 'a', 'a'],
    'e': ['ē', 'é', 'ě', 'è', 'e', 'e', 'e', 'e'],
    'i': ['ī', 'í', 'ǐ', 'ì', 'i', 'i', 'i', 'i'],
    'o': ['ō', 'ó', 'ǒ', 'ò', 'o', 'o', 'o', 'o'],
    'u': ['ū', 'ú', 'ǔ', 'ù', 'u', 'u', 'u', 'u'],
    'ü': ['ǖ', 'ǘ', 'ǚ', 'ǜ', 'ü', 'ü', 'ü', 'ü'],
    # For syllabic nasals (m, ng), use macron/acute on following placeholder or drop tone
    'm': ['m̄', 'ḿ', 'm̌', 'm̀', 'm', 'm', 'm', 'm'],
    'n': ['n̄', 'ń', 'ň', 'ǹ', 'n', 'n', 'n', 'n'],
}

def numbered_to_accented(text):
    """Convert numbered romanization (ni3 hao3) to accented (nǐ hǎo)."""
    def convert_syllable(match):
        syllable = match.group(1)
        tone = int(match.group(2))
        if tone < 1 or tone > 8:
            return syllable + str(tone)
        tone_idx = tone - 1

        vowels = 'aeiouü'
        syllable_lower = syllable.lower()

        # Find vowel to mark (pinyin rules: a/e take it, in ou o takes it, else last vowel)
        mark_pos = -1
        if 'a' in syllable_lower:
            mark_pos = syllable_lower.index('a')
        elif 'e' in syllable_lower:
            mark_pos = syllable_lower.index('e')
        elif 'ou' in syllable_lower:
            mark_pos = syllable_lower.index('o')
        else:
            for i in range(len(syllable_lower) - 1, -1, -1):
                if syllable_lower[i] in vowels:
                    mark_pos = i
                    break

        # Handle syllabic nasals (m, ng) - no vowel
        if mark_pos == -1:
            if syllable_lower in ('m', 'ng', 'n'):
                char = syllable_lower[0]
                if char in TONE_ACCENTS and tone_idx < len(TONE_ACCENTS[char]):
                    return TONE_ACCENTS[char][tone_idx] + syllable[1:]
            return syllable  # drop tone number for display

        # Apply accent to vowel
        result = list(syllable)
        vowel = syllable_lower[mark_pos]
        if vowel in TONE_ACCENTS and tone_idx < len(TONE_ACCENTS[vowel]):
            accented = TONE_ACCENTS[vowel][tone_idx]
            if syllable[mark_pos].isupper():
                accented = accented.upper()
            result[mark_pos] = accented

        return ''.join(result)

    # Match syllable + tone number 1-8 (including already-accented vowels)
    result = re.sub(r'([a-zA-ZüÜāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ]+)([1-8])', convert_syllable, text)
    # Strip any remaining tone numbers that weren't converted (edge cases)
    result = re.sub(r'([āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ])([1-8])', r'\1', result)
    return result


# Font paths
FONT_DIR = Path(__file__).parent.parent / 'fonts' / 'Alcarin-Tengwar' / 'Font source' / 'build'
TENGWAR_FONT = FONT_DIR / 'AlcarinTengwar-Regular.otf'

# System fonts
CJK_FONT = Path('/System/Library/Fonts/STHeiti Light.ttc')
CJK_FONT_ALT = Path('/System/Library/Fonts/Hiragino Sans GB.ttc')
LATIN_FONT = Path('/System/Library/Fonts/Helvetica.ttc')

# Register fonts
_fonts_registered = False
def register_fonts():
    global _fonts_registered
    if _fonts_registered:
        return True
    # Latin font with extended characters (pinyin diacritics)
    if LATIN_FONT.exists():
        try:
            pdfmetrics.registerFont(RLTTFont('Latin', str(LATIN_FONT), subfontIndex=0))
        except:
            pass
    # CJK font
    for font_path in [CJK_FONT, CJK_FONT_ALT]:
        if font_path.exists():
            try:
                pdfmetrics.registerFont(RLTTFont('CJK', str(font_path), subfontIndex=0))
                _fonts_registered = True
                return True
            except:
                continue
    return False


class GlyphOutlineRenderer:
    """Render text as vector outlines in PDF."""

    def __init__(self, font_path, font_size=48):
        self.font_size = font_size

        # Load for HarfBuzz shaping
        with open(font_path, 'rb') as f:
            font_data = f.read()
        face = hb.Face(font_data)
        self.hb_font = hb.Font(face)
        self.upem = face.upem

        # Load for glyph outlines
        self.tt_font = TTFont(font_path)
        self.glyph_set = self.tt_font.getGlyphSet()

        # Scale factor: font units to points
        self.scale = font_size / self.upem

    def shape_text(self, text):
        """Shape text and return glyph IDs with positions."""
        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        hb.shape(self.hb_font, buf)

        result = []
        x = 0
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            glyph_name = self.tt_font.getGlyphName(info.codepoint)
            result.append({
                'glyph_name': glyph_name,
                'x': x + pos.x_offset,
                'y': pos.y_offset,
                'x_advance': pos.x_advance,
            })
            x += pos.x_advance
        return result, x  # glyphs and total width

    def draw_text(self, c, text, x, y, color=(0, 0, 0)):
        """Draw text as vector paths on a reportlab canvas."""
        glyphs, _ = self.shape_text(text)

        c.saveState()
        c.setFillColorRGB(*color)

        for g in glyphs:
            if g['glyph_name'] not in self.glyph_set:
                continue

            glyph = self.glyph_set[g['glyph_name']]
            pen = RecordingPen()
            glyph.draw(pen)

            # Draw glyph outline
            gx = x + g['x'] * self.scale
            gy = y + g['y'] * self.scale

            path = c.beginPath()
            for op, args in pen.value:
                if op == 'moveTo':
                    px, py = args[0]
                    path.moveTo(gx + px * self.scale, gy + py * self.scale)
                elif op == 'lineTo':
                    px, py = args[0]
                    path.lineTo(gx + px * self.scale, gy + py * self.scale)
                elif op == 'curveTo':
                    pts = [(gx + p[0] * self.scale, gy + p[1] * self.scale) for p in args]
                    path.curveTo(*pts[0], *pts[1], *pts[2])
                elif op == 'qCurveTo':
                    # Convert quadratic bezier to cubic approximation
                    # For each quadratic segment, use the end point
                    if args:
                        px, py = args[-1]
                        path.lineTo(gx + px * self.scale, gy + py * self.scale)
                elif op == 'closePath':
                    path.close()
            c.drawPath(path, fill=1, stroke=0)

        c.restoreState()

    def get_text_width(self, text):
        """Get width of text in points."""
        _, width = self.shape_text(text)
        return width * self.scale


def render_sample_pdf(sample_dir, output_path):
    """Render all .md samples in a directory to a single PDF."""

    if not TENGWAR_FONT.exists():
        print(f"Font not found: {TENGWAR_FONT}")
        return None

    tengwar_renderer = GlyphOutlineRenderer(str(TENGWAR_FONT), font_size=36)
    has_cjk = register_fonts()

    c = canvas.Canvas(str(output_path), pagesize=letter)
    width, height = letter
    margin = 0.75 * inch

    # Find all markdown files
    md_files = sorted(Path(sample_dir).glob('*.md'))
    md_files = [f for f in md_files if f.name not in ('README.md', 'sample_texts.md')]

    for md_file in md_files:
        # Start new page for each file
        y = height - margin

        # Title
        c.setFont('Helvetica-Bold', 16)
        title = md_file.stem.replace('_', ' ').title()
        c.drawString(margin, y, title)
        y -= 30

        # Parse markdown table
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract table rows
        in_table = False
        for line in content.split('\n'):
            if '|' in line and not line.startswith('|--'):
                parts = [p.strip() for p in line.split('|')]
                if len(parts) >= 3:
                    col1 = parts[1]  # romanization
                    col2 = parts[2]  # hanzi

                    # Skip header
                    if any(h in col1 for h in ['Jyutping', 'Pinyin', 'Romanization', 'Wu', 'Hakka', 'Tai-lo', 'Gan', 'Xiang', 'Beta']):
                        continue
                    if not col1 or col1.startswith('#'):
                        continue

                    # Find tengwar (PUA characters)
                    tengwar = ''
                    for p in parts[3:]:
                        if re.search(r'[\ue000-\ue0ff]', p):
                            tengwar = p.strip()
                            break

                    if not tengwar:
                        continue

                    # Check page break
                    if y < margin + 60:
                        c.showPage()
                        y = height - margin
                        c.setFont('Helvetica-Bold', 14)
                        c.drawString(margin, y, f"{title} (continued)")
                        y -= 25

                    # Draw row: romanization, hanzi, tengwar
                    c.setFont('Latin', 12)
                    c.setFillColorRGB(0.4, 0.4, 0.4)
                    c.drawString(margin, y, numbered_to_accented(col1))

                    c.setFillColorRGB(0, 0, 0)
                    if has_cjk:
                        c.setFont('CJK', 12)
                    c.drawString(margin + 120, y, col2)
                    c.setFont('Latin', 12)

                    # Draw tengwar as vector paths
                    tengwar_renderer.draw_text(c, tengwar, margin + 200, y - 8)

                    y -= 45

        c.showPage()

    c.save()
    print(f"  PDF: {output_path}")
    return output_path


def main():
    """Render PDFs for all sample directories."""
    samples_dir = Path(__file__).parent
    pdf_dir = samples_dir / 'pdf'
    pdf_dir.mkdir(exist_ok=True)

    # Find sample directories
    sample_dirs = [
        samples_dir / 'mandarin',
        samples_dir / 'cantonese',
        samples_dir / 'hakka',
        samples_dir / 'min',
        samples_dir / 'wu',
        samples_dir / 'gan',
        samples_dir / 'xiang',
    ]

    for sample_dir in sample_dirs:
        if sample_dir.exists():
            name = sample_dir.name
            print(f"\n{name}:")
            output = pdf_dir / f'tengwar-{name}-samples.pdf'
            render_sample_pdf(sample_dir, output)


if __name__ == '__main__':
    main()
