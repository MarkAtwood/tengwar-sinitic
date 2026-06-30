#!/usr/bin/env python3
"""Generate Xiang (Changsha) sample markdown files with tengwar rendering.

Uses Beta 5.0 romanization. Reads .md files and fills in Tengwar column.
"""

import sys
import re
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from tengwar_xiang import convert_text, TENGWAR, TEHTAR, TONE_MARKS, PALATAL_MARK, NASAL_VOWEL, UNDERBAR

OUT_DIR = Path(__file__).parent


# Import tone marks
from tengwar_xiang import CONTOUR_RISING, CONTOUR_FALLING, REGISTER_MID, REGISTER_LOW

# Base tengwar names (consonants)
_TENGWAR_NAMES = {
    TENGWAR['tinco']: 'tinco',
    TENGWAR['ando']: 'ando',
    TENGWAR['thuule']: 'thuule',
    TENGWAR['nuumen']: 'nuumen',
    TENGWAR['lambe']: 'lambe',
    TENGWAR['parma']: 'parma',
    TENGWAR['umbar']: 'umbar',
    TENGWAR['formen']: 'formen',
    TENGWAR['malta']: 'malta',
    TENGWAR['calma']: 'calma',
    TENGWAR['anga']: 'anga',
    TENGWAR['hwesta']: 'hwesta',
    TENGWAR['noldo']: 'noldo',
    TENGWAR['quesse']: 'quesse',
    TENGWAR['ungwe']: 'ungwe',
    TENGWAR['harma']: 'harma',
    TENGWAR['oore']: 'oore',
    TENGWAR['tinco_ext']: 'tinco_ext',
    TENGWAR['ando_ext']: 'ando_ext',
    TENGWAR['anna']: 'anna',
    TENGWAR['vala']: 'vala',
    TENGWAR['carrier_short']: 'telco',
    TENGWAR['carrier_long']: 'aara',
}

# Tehtar (vowel marks)
_TEHTAR_SET = set(TEHTAR.values())

# Diacritics that need context-aware naming
# PALATAL_MARK and REGISTER_LOW share the same codepoint (U+E043)
_DOUBLE_DOT = PALATAL_MARK  # = REGISTER_LOW = '\ue043'


def tengwar_to_names(tengwar_str):
    """Convert tengwar unicode to descriptive names for debugging.

    Uses context to disambiguate shared codepoints:
    - U+E043 after a consonant = +pal (palatal mark)
    - U+E043 after a tone contour = ..low (low register)
    """
    result = []
    prev_was_contour = False

    for c in tengwar_str:
        # Check for base tengwar
        if c in _TENGWAR_NAMES:
            result.append('{' + _TENGWAR_NAMES[c] + '}')
            prev_was_contour = False
        # Check for tehtar
        elif c in _TEHTAR_SET:
            for vowel, code in TEHTAR.items():
                if code == c:
                    result.append(f'[{vowel}]')
                    break
            prev_was_contour = False
        # Tone contours
        elif c == CONTOUR_RISING:
            result.append('/rise')
            prev_was_contour = True
        elif c == CONTOUR_FALLING:
            result.append('\\fall')
            prev_was_contour = True
        # Context-dependent double-dot (palatal vs low register)
        elif c == _DOUBLE_DOT:
            if prev_was_contour:
                result.append('..low')
            else:
                result.append('+pal')
            prev_was_contour = False
        # Register mid
        elif c == REGISTER_MID:
            result.append('.mid')
            prev_was_contour = False
        # Nasal vowel tilde
        elif c == NASAL_VOWEL:
            result.append('~')
            prev_was_contour = False
        # Underbar (rusheng marker)
        elif c == UNDERBAR:
            result.append('_bar')
            prev_was_contour = False
        # Unknown
        else:
            result.append(f'?{ord(c):04X}')
            prev_was_contour = False

    return ''.join(result)


# === SAMPLE DATA ===

# Numbers 1-10 in Changsha Xiang (Beta 5.0 romanization)
# Based on research: Changsha dialect has 6 tones, T6 = rusheng (entering tone)
# References: tengwar-xiang.md specification, academic sources
NUMBERS = [
    ('i6', '一', 'one'),        # T6 (rusheng) - historical *it
    ('o5', '二', 'two'),        # T5 (yang-qu)
    ('san1', '三', 'three'),    # T1 (yin-ping)
    ('si4', '四', 'four'),      # T4 (yin-qu)
    ('u3', '五', 'five'),       # T3 (shang)
    ('liu6', '六', 'six'),      # T6 (rusheng) - historical *liuk
    ('qi6', '七', 'seven'),     # T6 (rusheng) - historical *tsit
    ('pa6', '八', 'eight'),     # T6 (rusheng) - historical *paat
    ('qiu3', '九', 'nine'),     # T3 (shang)
    ('se6', '十', 'ten'),       # T6 (rusheng) - historical *sip
]

# Common greetings and phrases in Changsha
GREETINGS = [
    ('ni3 ho3', '你好', 'hello'),
    ('nga1', '我', 'I/me (colloquial)'),
    ('tha1', '他/她', 'he/she'),
    ('xie4 xie4', '谢谢', 'thank you'),
    ('mo5 khie4 khi4', '冇客气', "you're welcome"),
    ('cai4 qian4', '再见', 'goodbye'),
    ('co3 san1 ho3', '早上好', 'good morning'),
    ('man3 san4 ho3', '晚上好', 'good evening'),
    ('ni3 qhi4 fan5 la3 mo5', '你吃饭了冇', 'have you eaten?'),
    ('ho3 qhi4', '好吃', 'delicious'),
]

# Hunanese proverbs and sayings
# Selected for cultural significance and phonetic variety
PROVERBS = [
    ('qhi4 fan5 phi4 ho5 qhi4', '吃饭皮好吃', 'Eating is best enjoyed slowly'),
    ('thi1 li3 mo5 qhi2', '天里冇晴', 'No sunshine in the sky (bad luck)'),
    ('san1 nan2 mo5 phie2', '山南冇坪', 'No flat land south of mountains'),
    ('lo3 hu3 pu4 qhi4 qi6 ci3', '老虎不吃亲生子', "Tigers don't eat their own cubs"),
    ('i6 pu4 co4 o5 pu4 xiu1', '一不做二不休', 'If you start, see it through'),
]

# Tone demonstration set
TONES = {
    'title': 'Tone Demonstration',
    'intro': 'Changsha Xiang has 6 lexical tones. Tone 6 (rusheng) marks historical entering tone syllables that have lost their stop codas.',
    'sets': [
        ('ma Set', [
            ('ma1', '妈', 'mother', 'T1 (34) mid-rising'),
            ('ma2', '麻', 'hemp', 'T2 (13) low-rising'),
            ('ma3', '马', 'horse', 'T3 (42) falling'),
            ('ma4', '骂', 'scold', 'T4 (45) high-rising'),
            ('ma5', '蚂', 'ant', 'T5 (21) low-falling'),
        ]),
        ('Rusheng (T6) Examples', [
            ('pa6', '百', 'hundred', 'T6 (14) *pak'),
            ('se6', '色', 'color', 'T6 (14) *sek'),
            ('qi6', '七', 'seven', 'T6 (14) *tsit'),
            ('mo6', '墨', 'ink', 'T6 (14) *mok'),
            ('fu6', '福', 'fortune', 'T6 (14) *fuk'),
        ]),
    ],
}

# Nasalized vowel examples
NASAL_VOWELS = [
    ('kon3', '狗', 'dog'),
    ('sen1', '生', 'to live'),
    ('hon2', '红', 'red'),
    ('men4', '门', 'door'),
]


def write_table(f, header, rows):
    """Write a markdown table."""
    f.write(f'\n| {" | ".join(header)} |\n')
    f.write(f'|{"|".join(["---"] * len(header))}|\n')
    for row in rows:
        f.write(f'| {" | ".join(row)} |\n')


def gen_common_phrases():
    """Generate xiang-common-phrases.md"""
    with open(OUT_DIR / 'xiang-common-phrases.md', 'w', encoding='utf-8') as f:
        f.write('# Changsha Xiang Common Phrases\n\n')
        f.write('Romanization uses Beta 5.0. Tone numbers 1-6.\n')

        # Greetings section
        f.write('\n## Greetings\n')
        rows = []
        for xiang, hanzi, eng in GREETINGS:
            teng = convert_text(xiang)
            names = tengwar_to_names(teng)
            rows.append([xiang, hanzi, eng, teng, f'`{names}`'])
        write_table(f, ['Romanization', 'Hanzi', 'English', 'Tengwar', 'Names'], rows)

        # Numbers section
        f.write('\n## Numbers (1-10)\n')
        f.write('\nNote: Several numerals are rusheng (T6), reflecting historical stop codas now lost.\n')
        rows = []
        for xiang, hanzi, eng in NUMBERS:
            teng = convert_text(xiang)
            names = tengwar_to_names(teng)
            rows.append([xiang, hanzi, eng, teng, f'`{names}`'])
        write_table(f, ['Romanization', 'Hanzi', 'English', 'Tengwar', 'Names'], rows)

        # Nasalized vowels section
        f.write('\n## Nasalized Vowels\n')
        f.write('\nChangsha Xiang has phonemic nasalized vowels /o/ and /e/, written with -n when no nasal coda follows.\n')
        rows = []
        for xiang, hanzi, eng in NASAL_VOWELS:
            teng = convert_text(xiang)
            names = tengwar_to_names(teng)
            rows.append([xiang, hanzi, eng, teng, f'`{names}`'])
        write_table(f, ['Romanization', 'Hanzi', 'English', 'Tengwar', 'Names'], rows)


def gen_proverbs():
    """Generate xiang-proverbs.md"""
    with open(OUT_DIR / 'xiang-proverbs.md', 'w', encoding='utf-8') as f:
        f.write('# Changsha Xiang Proverbs\n\n')
        f.write('Hunanese sayings in Beta 5.0 romanization.\n')

        f.write('\n## Sayings\n')
        rows = []
        for xiang, hanzi, eng in PROVERBS:
            teng = convert_text(xiang)
            names = tengwar_to_names(teng)
            rows.append([xiang, hanzi, eng, teng])
        write_table(f, ['Romanization', 'Hanzi', 'English', 'Tengwar'], rows)

        # Tone demonstration
        f.write(f'\n## {TONES["title"]}\n\n{TONES["intro"]}\n')
        for set_name, items in TONES['sets']:
            f.write(f'\n### {set_name}\n')
            rows = []
            for xiang, hanzi, eng, desc in items:
                teng = convert_text(xiang)
                names = tengwar_to_names(teng)
                rows.append([xiang, hanzi, eng, teng, f'`{names}`', desc])
            write_table(f, ['Romanization', 'Hanzi', 'English', 'Tengwar', 'Names', 'Tone'], rows)


def main():
    gen_common_phrases()
    gen_proverbs()
    print('Generated: xiang-common-phrases.md, xiang-proverbs.md')


if __name__ == '__main__':
    main()
