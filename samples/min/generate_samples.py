#!/usr/bin/env python3
"""Generate Min sample markdown files with proper tengwar.

Table format: | Romanization | Hanzi | English | Tengwar | Names |
"""

import sys
sys.path.insert(0, '.')
from tengwar_min import convert_text, tengwar_to_names
from pathlib import Path

OUT_DIR = Path(__file__).parent

TONES = [
    ('su1', '書', 'book', 'T1 high level'),
    ('su2', '輸', 'lose', 'T2 high falling'),
    ('su3', '四', 'four', 'T3 low falling'),
    ('su5', '樹', 'tree', 'T5 rising'),
    ('su7', '數', 'count', 'T7 mid level'),
    ('sut4', '術', 'skill', 'T4 low checked'),
    ('sut8', '實', 'real', 'T8 high checked'),
]

NUMBERS = [
    ('tsit8', '一', 'one'),
    ('nng7', '兩', 'two'),
    ('sann1', '三', 'three'),
    ('si3', '四', 'four'),
    ('goo7', '五', 'five'),
    ('lak8', '六', 'six'),
    ('tshit4', '七', 'seven'),
    ('peh4', '八', 'eight'),
    ('kau2', '九', 'nine'),
    ('tsap8', '十', 'ten'),
    ('pah4', '百', 'hundred'),
    ('tshing1', '千', 'thousand'),
]

GREETINGS = [
    ('li2 ho2', '你好', 'hello'),
    ('gua2', '我', 'I/me'),
    ('li2', '你', 'you'),
    ('i1', '伊', 'he/she'),
    ('to1 sia7', '多謝', 'thank you'),
    ('m7 bian2', '毋免', "you're welcome"),
    ('tsai3 hue7', '再會', 'goodbye'),
    ('tsa2 khí2', '早起', 'good morning'),
    ('tsiah8 pa3 bue7', '食飽未', 'have you eaten?'),
    ('ho2 lah4', '好啦', 'OK'),
]

PLACES = [
    ('tai5 uan5', '台灣', 'Taiwan'),
    ('tai5 pak4', '台北', 'Taipei'),
    ('tai5 lam5', '台南', 'Tainan'),
    ('ko1 hiong5', '高雄', 'Kaohsiung'),
    ('hok4 kian3', '福建', 'Fujian'),
    ('e7 mng5', '廈門', 'Xiamen'),
    ('tsuan5 tsiu1', '泉州', 'Quanzhou'),
    ('tsiang1 tsiu1', '漳州', 'Zhangzhou'),
    ('sin1 ka1 pho1', '新加坡', 'Singapore'),
    ('ma2 lai5', '馬來', 'Malaysia'),
]

NASAL = [
    ('sann1', '三', 'three'),
    ('tinn1', '甜', 'sweet'),
    ('phinn7', '鼻', 'nose'),
    ('hinn7', '耳', 'ear'),
    ('kinn3', '見', 'see'),
    ('guann5', '寒', 'cold'),
    ('suann1', '山', 'mountain'),
    ('kuann1', '關', 'close'),
    ('mng5', '門', 'door'),
    ('ang5', '紅', 'red'),
]

def write_table(f, header, rows):
    f.write(f'\n| {" | ".join(header)} |\n')
    f.write(f'|{"|".join(["---"] * len(header))}|\n')
    for row in rows:
        f.write(f'| {" | ".join(row)} |\n')

def gen_tones():
    with open(OUT_DIR / 'tones.md', 'w') as f:
        f.write('# Tone Demonstration\n\nHokkien has 7 tones (8 with checked variants).\n')
        f.write('\n## 書 (su) Set\n')
        rows = []
        for tailo, hanzi, eng, desc in TONES:
            teng = convert_text(tailo)
            names = tengwar_to_names(teng)
            rows.append([tailo, hanzi, eng, teng, f'`{names}`', desc])
        write_table(f, ['Romanization', 'Hanzi', 'English', 'Tengwar', 'Names', 'Tone'], rows)

def gen_numbers():
    with open(OUT_DIR / 'numbers.md', 'w') as f:
        f.write('# Numbers\n')
        rows = []
        for tailo, hanzi, eng in NUMBERS:
            teng = convert_text(tailo)
            names = tengwar_to_names(teng)
            rows.append([tailo, hanzi, eng, teng, f'`{names}`'])
        write_table(f, ['Romanization', 'Hanzi', 'English', 'Tengwar', 'Names'], rows)

def gen_greetings():
    with open(OUT_DIR / 'greetings.md', 'w') as f:
        f.write('# Greetings\n')
        rows = []
        for tailo, hanzi, eng in GREETINGS:
            teng = convert_text(tailo)
            names = tengwar_to_names(teng)
            rows.append([tailo, hanzi, eng, teng, f'`{names}`'])
        write_table(f, ['Romanization', 'Hanzi', 'English', 'Tengwar', 'Names'], rows)

def gen_places():
    with open(OUT_DIR / 'places.md', 'w') as f:
        f.write('# Places\n')
        rows = []
        for tailo, hanzi, eng in PLACES:
            teng = convert_text(tailo)
            names = tengwar_to_names(teng)
            rows.append([tailo, hanzi, eng, teng, f'`{names}`'])
        write_table(f, ['Romanization', 'Hanzi', 'English', 'Tengwar', 'Names'], rows)

def gen_nasal():
    with open(OUT_DIR / 'nasal_vowels.md', 'w') as f:
        f.write('# Nasal Vowels\n\nHokkien has distinctive nasal vowels marked with -nn in Tai-lo.\n')
        rows = []
        for tailo, hanzi, eng in NASAL:
            teng = convert_text(tailo)
            names = tengwar_to_names(teng)
            rows.append([tailo, hanzi, eng, teng, f'`{names}`'])
        write_table(f, ['Romanization', 'Hanzi', 'English', 'Tengwar', 'Names'], rows)

if __name__ == '__main__':
    gen_tones()
    gen_numbers()
    gen_greetings()
    gen_places()
    gen_nasal()
    print('Generated: tones.md, numbers.md, greetings.md, places.md, nasal_vowels.md')
