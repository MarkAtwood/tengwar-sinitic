#!/usr/bin/env python3
"""Generate Wu (Shanghainese) sample markdown files with proper tengwar."""

import sys
sys.path.insert(0, '.')
from tengwar_wu import convert_text, tengwar_to_names
from pathlib import Path

OUT_DIR = Path(__file__).parent

# === SAMPLE DATA ===

# Tones: Shanghainese has 5 tones
TONES = {
    'title': 'Tone Demonstration',
    'intro': '''Shanghainese has 5 citation tones with a yin/yang register split.
Voiceless initials (b, d, g, etc.) occur with yin (high) tones.
Voiced initials (bb, dd, gg, etc.) occur with yang (low) tones.

| Tone | Name | Chao Value | Contour |
|------|------|------------|---------|
| T1 | yin-ping | 53 | high falling |
| T2 | yang-ping | 31 | low falling |
| T3 | yin-shang | 55 | high level |
| T4 | yin-qu | 34 | mid rising |
| T5 | yang-qu | 13 | low rising |
''',
    'sets': [
        ('Sample Minimal Pairs', [
            ('da1', '搭', 'to build', 'T1 (53) high falling'),
            ('dda2', '達', 'to reach', 'T2 (31) low falling'),
            ('da3', '答', 'to answer', 'T3 (55) high level'),
            ('da4', '打', 'to hit', 'T4 (34) mid rising'),
            ('dda5', '大', 'big', 'T5 (13) low rising'),
        ]),
    ],
}

# Numbers 1-10 and extended
# Using Qian Nairong romanization with proper tone numbers (1-5 only)
NUMBERS = [
    ('iq5', '一', 'one'),
    ('liang3', '兩', 'two'),
    ('se1', '三', 'three'),
    ('sy3', '四', 'four'),
    ('ng3', '五', 'five'),
    ('loq5', '六', 'six'),
    ('qiq5', '七', 'seven'),
    ('baq5', '八', 'eight'),
    ('jieu3', '九', 'nine'),
    ('zeq5', '十', 'ten'),
    ('iq5 baq3', '一百', 'one hundred'),
    ('iq5 qi1', '一千', 'one thousand'),
]

# Greetings
# Multi-syllable words use spaces between syllables
GREETINGS = [
    ('nong2 ho3', '儂好', 'hello (informal)'),
    ('ze4 we4', '再會', 'goodbye'),
    ('xia4 xia4', '謝謝', 'thank you'),
    ('dde4 veq5 qi3', '對勿起', 'sorry'),
    ('veq5 khe4 qi3', '勿客氣', "you're welcome"),
    ('zao3 an1', '早安', 'good morning'),
    ('nong2', '儂', 'you'),
    ('ngu2', '我', 'I/me'),
    ('yi2', '伊', 'he/she'),
    ('zaq5 ve4 mo2', '食飯嘸', 'have you eaten?'),
]

# Places - Shanghai districts and nearby cities
# Proper romanization with syllable separation
PLACES = [
    ('zaang3 he3', '上海', 'Shanghai'),
    ('bu3 dong1', '浦東', 'Pudong'),
    ('zing4 an1', '靜安', 'Jing\'an'),
    ('zzy2 jia1 we4', '徐家匯', 'Xujiahui'),
    ('hong2 keu3', '虹口', 'Hongkou'),
    ('lu2 we1', '盧灣', 'Luwan'),
    ('zaq5 beq5', '閘北', 'Zhabei'),
    ('hang2 zeu1', '杭州', 'Hangzhou'),
    ('su1 zeu1', '蘇州', 'Suzhou'),
    ('ning2 bo1', '寧波', 'Ningbo'),
]

# Voicing contrasts - the key Wu feature (three-way laryngeal contrast)
VOICING = {
    'title': 'Three-Way Voicing Contrast',
    'intro': '''Wu Chinese preserves the Middle Chinese three-way laryngeal contrast:
- **Voiceless unaspirated** (b, d, g): Like French or Spanish stops
- **Voiceless aspirated** (p, t, k): Like English initial stops
- **Voiced** (bb, dd, gg): True voiced stops, unique among major Chinese languages

This is THE defining phonological feature of Wu. Mandarin and Cantonese have lost voiced obstruents entirely.

In Qian Nairong romanization:
- `bb`, `dd`, `gg` = voiced stops /b, d, g/
- `b`, `d`, `g` = voiceless unaspirated /p, t, k/
- `p`, `t`, `k` = voiceless aspirated /ph, th, kh/
''',
    'triads': [
        ('Bilabial /p, ph, b/', [
            ('ba1', '巴', 'eight (literary)', '/pa/ voiceless unasp'),
            ('pa1', '怕', 'afraid', '/pha/ voiceless asp'),
            ('bba2', '爬', 'to climb', '/ba/ voiced'),
        ]),
        ('Alveolar /t, th, d/', [
            ('da1', '搭', 'to build', '/ta/ voiceless unasp'),
            ('ta1', '他', 'he (literary)', '/tha/ voiceless asp'),
            ('dda2', '達', 'to reach', '/da/ voiced'),
        ]),
        ('Velar /k, kh, g/', [
            ('ga1', '嘎', 'particle', '/ka/ voiceless unasp'),
            ('ka1', '卡', 'card', '/kha/ voiceless asp'),
            ('gga2', '軋', 'to press', '/ga/ voiced'),
        ]),
        ('Alveolar Affricate /ts, tsh, dz/', [
            ('za1', '紮', 'to tie', '/tsa/ voiceless unasp'),
            ('ca1', '擦', 'to wipe', '/tsha/ voiceless asp'),
            ('zza2', '雜', 'mixed', '/dza/ voiced'),
        ]),
        ('Alveolo-Palatal /tc, tch, dz/', [
            ('ji1', '雞', 'chicken', '/tci/ voiceless unasp'),
            ('qi1', '欺', 'to bully', '/tchi/ voiceless asp'),
            ('jji2', '齊', 'together', '/dzi/ voiced'),
        ]),
        ('Voiced Fricatives (Wu-specific)', [
            ('va1', '花', 'flower', '/va/ voiced labiodental'),
            ('ssa3', '詞', 'word', '/za/ voiced alveolar'),
            ('xxa3', '徐', 'surname', '/za/ voiced alv-pal'),
        ]),
    ],
}


def write_table(f, header, rows):
    """Write a markdown table."""
    f.write(f'\n| {" | ".join(header)} |\n')
    f.write(f'|{"|".join(["---"] * len(header))}|\n')
    for row in rows:
        f.write(f'| {" | ".join(row)} |\n')


def gen_tones():
    """Generate tones.md"""
    with open(OUT_DIR / 'tones.md', 'w') as f:
        f.write(f'# {TONES["title"]}\n\n{TONES["intro"]}\n')
        for set_name, items in TONES['sets']:
            f.write(f'\n## {set_name}\n')
            rows = []
            for wu, hanzi, eng, desc in items:
                teng = convert_text(wu)
                names = tengwar_to_names(teng)
                rows.append([wu, hanzi, eng, teng, f'`{names}`', desc])
            write_table(f, ['Wu Pinyin', '吳字', 'English', 'Tengwar', 'Names', 'Tone'], rows)


def gen_numbers():
    """Generate numbers.md"""
    with open(OUT_DIR / 'numbers.md', 'w') as f:
        f.write('# Numbers\n\nShanghainese numbers 1-10 and extended numerals.\n')
        rows = []
        for wu, hanzi, eng in NUMBERS:
            teng = convert_text(wu)
            names = tengwar_to_names(teng)
            rows.append([wu, hanzi, eng, teng, f'`{names}`'])
        write_table(f, ['Wu Pinyin', '吳字', 'English', 'Tengwar', 'Names'], rows)


def gen_greetings():
    """Generate greetings.md"""
    with open(OUT_DIR / 'greetings.md', 'w') as f:
        f.write('# Greetings\n\nCommon Shanghainese greetings and expressions.\n')
        rows = []
        for wu, hanzi, eng in GREETINGS:
            teng = convert_text(wu)
            names = tengwar_to_names(teng)
            rows.append([wu, hanzi, eng, teng, f'`{names}`'])
        write_table(f, ['Wu Pinyin', '吳字', 'English', 'Tengwar', 'Names'], rows)


def gen_places():
    """Generate places.md"""
    with open(OUT_DIR / 'places.md', 'w') as f:
        f.write('# Places\n\nShanghai districts and nearby Wu-speaking cities.\n')
        rows = []
        for wu, hanzi, eng in PLACES:
            teng = convert_text(wu)
            names = tengwar_to_names(teng)
            rows.append([wu, hanzi, eng, teng, f'`{names}`'])
        write_table(f, ['Wu Pinyin', '吳字', 'English', 'Tengwar', 'Names'], rows)


def gen_voicing():
    """Generate voicing.md - the key Wu feature"""
    with open(OUT_DIR / 'voicing.md', 'w') as f:
        f.write(f'# {VOICING["title"]}\n\n{VOICING["intro"]}\n')
        for triad_name, items in VOICING['triads']:
            f.write(f'\n## {triad_name}\n')
            rows = []
            for wu, hanzi, eng, desc in items:
                teng = convert_text(wu)
                names = tengwar_to_names(teng)
                rows.append([wu, hanzi, eng, teng, f'`{names}`', desc])
            write_table(f, ['Wu Pinyin', '吳字', 'English', 'Tengwar', 'Names', 'Phonetics'], rows)


if __name__ == '__main__':
    gen_tones()
    gen_numbers()
    gen_greetings()
    gen_places()
    gen_voicing()
    print('Generated: tones.md, numbers.md, greetings.md, places.md, voicing.md')
