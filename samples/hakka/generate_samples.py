#!/usr/bin/env python3
"""Generate Hakka sample markdown files with proper tengwar."""

import sys
sys.path.insert(0, '.')
from tengwar_hakka import convert_text, tengwar_to_names
from pathlib import Path

OUT_DIR = Path(__file__).parent

TONES = {
    'title': 'Tone Demonstration',
    'intro': 'Sixian Hakka has 6 lexical tones.',
    'sets': [
        ('都 (du) Set', [
            ('du1', '都', 'capital', 'T1 mid-rising'),
            ('du2', '肚', 'belly', 'T2 low level'),
            ('du3', '妒', 'jealous', 'T3 mid-falling'),
            ('du4', '杜', 'surname', 'T4 high level'),
            ('duk5', '督', 'supervise', 'T5 low checked'),
            ('duk6', '讀', 'read', 'T6 high checked'),
        ]),
    ],
}

NUMBERS = [
    ('id5', '一', 'one'),
    ('ngi4', '二', 'two'),
    ('sam1', '三', 'three'),
    ('xi4', '四', 'four'),
    ('ng3', '五', 'five'),
    ('liug5', '六', 'six'),
    ('qid5', '七', 'seven'),
    ('bad5', '八', 'eight'),
    ('giu3', '九', 'nine'),
    ('siib6', '十', 'ten'),
    ('siib6 id5', '十一', 'eleven'),
    ('ngi4 siib6', '二十', 'twenty'),
    ('id5 bag5', '一百', 'hundred'),
]

GREETINGS = [
    ('ngi2 ho3', '你好', 'hello'),
    ('ngai1', '涯', 'I/me'),
    ('ngi2', '你', 'you'),
    ('ki2', '佢', 'he/she'),
    ('do1 xia4', '多謝', 'thank you'),
    ('mo2 se4', '毋使', "you're welcome"),
    ('zoi4 gien4', '再見', 'goodbye'),
    ('zo3 an1', '早安', 'good morning'),
    ('an1 zo3', '安早', 'good morning (alt)'),
    ('sib6 fan4 mo2', '食飯毋', 'have you eaten?'),
]

PLACES = [
    ('moi2 zu1', '梅州', 'Meizhou'),
    ('hoi3 liug5', '海陸', 'Hailu'),
    ('meu2 lid5', '苗栗', 'Miaoli'),
    ('xin1 zug5', '新竹', 'Hsinchu'),
    ('toi2 bed5', '台北', 'Taipei'),
    ('toi2 zung1', '台中', 'Taichung'),
    ('pin2 dung1', '屏東', 'Pingtung'),
    ('toi2 van2', '台灣', 'Taiwan'),
    ('gong3 dung1', '廣東', 'Guangdong'),
    ('fug5 gien4', '福建', 'Fujian'),
]

def write_table(f, header, rows):
    """Write a markdown table.

    Canonical column format:
    | Romanization | Hanzi | English | Tengwar | Names |
    """
    f.write(f'\n| {" | ".join(header)} |\n')
    f.write(f'|{"|".join(["---"] * len(header))}|\n')
    for row in rows:
        f.write(f'| {" | ".join(row)} |\n')

def gen_tones():
    with open(OUT_DIR / 'tones.md', 'w') as f:
        f.write(f'# {TONES["title"]}\n\n{TONES["intro"]}\n')
        for set_name, items in TONES['sets']:
            f.write(f'\n## {set_name}\n')
            rows = []
            for hakka, hanzi, eng, desc in items:
                teng = convert_text(hakka)
                names = tengwar_to_names(teng)
                rows.append([hakka, hanzi, eng, teng, f'`{names}`', desc])
            write_table(f, ['Romanization', 'Hanzi', 'English', 'Tengwar', 'Names', 'Tone'], rows)

def gen_numbers():
    with open(OUT_DIR / 'numbers.md', 'w') as f:
        f.write('# Numbers\n')
        rows = []
        for hakka, hanzi, eng in NUMBERS:
            teng = convert_text(hakka)
            names = tengwar_to_names(teng)
            rows.append([hakka, hanzi, eng, teng, f'`{names}`'])
        write_table(f, ['Romanization', 'Hanzi', 'English', 'Tengwar', 'Names'], rows)

def gen_greetings():
    with open(OUT_DIR / 'greetings.md', 'w') as f:
        f.write('# Greetings\n')
        rows = []
        for hakka, hanzi, eng in GREETINGS:
            teng = convert_text(hakka)
            names = tengwar_to_names(teng)
            rows.append([hakka, hanzi, eng, teng, f'`{names}`'])
        write_table(f, ['Romanization', 'Hanzi', 'English', 'Tengwar', 'Names'], rows)

def gen_places():
    with open(OUT_DIR / 'places.md', 'w') as f:
        f.write('# Places\n')
        rows = []
        for hakka, hanzi, eng in PLACES:
            teng = convert_text(hakka)
            names = tengwar_to_names(teng)
            rows.append([hakka, hanzi, eng, teng, f'`{names}`'])
        write_table(f, ['Romanization', 'Hanzi', 'English', 'Tengwar', 'Names'], rows)

if __name__ == '__main__':
    gen_tones()
    gen_numbers()
    gen_greetings()
    gen_places()
    print('Generated: tones.md, numbers.md, greetings.md, places.md')
