#!/usr/bin/env python3
"""
Tengwar Jin (Taiyuan) Converter

Converts Jin Chinese IPA or romanization to Tengwar Unicode.
First mode to use the Sinitic IPA intermediate layer.

Jin is Group B (voicing semantics):
- Grade 1 = voiceless
- Grade 2 = voiced
- Aspiration marked with diacritic

Key features:
- Voiced fricatives: v, z, ɣ, ʐ
- Preserved entering tone: final glottal stop /ʔ/
- 5 tones including checked category
"""

import re
import sys
sys.path.insert(0, str(__file__).rsplit('/', 2)[0])  # add samples/ to path

# ponytail: import from shared IPA layer when codepoints are filled in
# from sinitic_ipa import ipa_to_tengwar

# === TENGWAR CODEPOINTS (Alcarin Tengwar) ===
# Copied from Gan converter as baseline, adjusted for Group B

TENGWAR = {
    # Column I - Alveolar
    'tinco': '',
    'ando': '',
    'thule': '',
    'numen': '',
    'lambe': '',
    'esse': '',  # for voiced /z/

    # Column II - Labial
    'parma': '',
    'umbar': '',
    'formen': '',
    'malta': '',
    'ampa': '',  # for voiced /v/

    # Column III - Retroflex/Velar
    'calma': '',
    'anga': '',
    'hwesta': '',
    'noldo': '',

    # Column IV - Velar
    'quesse': '',
    'ungwe': '',
    'harma': '',

    # Extended stem - Affricates
    'tinco_ext': '',
    'ando_ext': '',

    # Approximants/glides
    'anna': '',
    'vala': '',

    # Carriers
    'telco': '',
}

PALATAL_MARK = ''
ASPIRATION_MARK = ''  # breath mark for Group B aspiration
VOICING_MARK = ''     # voicing diacritic

TEHTAR = {
    'a': '',
    'e': '',
    'i': '',
    'o': '',
    'u': '',
    'syllabic': '',  # unutixe for apical vowel
}

TONE_MARKS = {
    'level': '',
    'rising': '',
    'falling': '',
    'chevron': '',
}

REGISTER_MODS = {
    'high': '',
    'mid': '',
    'low': '',
}


# === JIN ROMANIZATION TO IPA ===

INITIALS_TO_IPA = {
    'b': 'p', 'p': 'pʰ', 'm': 'm', 'f': 'f', 'v': 'v',
    'd': 't', 't': 'tʰ', 'n': 'n', 'l': 'l',
    'z': 'ts', 'c': 'tsʰ', 's': 's', 'rz': 'z',
    'zh': 'tʂ', 'ch': 'tʂʰ', 'sh': 'ʂ', 'r': 'ʐ',
    'j': 'tɕ', 'q': 'tɕʰ', 'x': 'ɕ',
    'g': 'k', 'k': 'kʰ', 'h': 'x', 'hh': 'ɣ',
    'ng': 'ŋ', 'ny': 'ɲ',
}

VOWELS_TO_IPA = {
    'a': 'a', 'e': 'ə', 'o': 'ɤ',
    'i': 'i', 'u': 'u', 'yu': 'y',
    'ii': 'ɿ',
    'ai': 'ai', 'ao': 'au', 'ei': 'ei', 'ou': 'əu',
    'an': 'ã',
}


def get_tone_marks(tone):
    """
    Return tone marks for Jin tones 1-5.

    T1 (213): dipping - chevron
    T2 (33): mid level - flat + mid dot
    T3 (412): falling-dipping - falling + chevron
    T4 (53): falling - falling stroke
    T5 (5ʔ): high checked - flat bar
    """
    if tone == 1:
        return TONE_MARKS['chevron']
    elif tone == 2:
        return TONE_MARKS['level'] + REGISTER_MODS['mid']
    elif tone == 3:
        return TONE_MARKS['falling'] + TONE_MARKS['chevron']
    elif tone == 4:
        return TONE_MARKS['falling']
    elif tone == 5:
        return TONE_MARKS['level']
    return ''


def romanization_to_tengwar(syllable, tone=None):
    """
    Convert a Jin romanization syllable to Tengwar.

    Args:
        syllable: romanized syllable (e.g., 'tai', 'jin', 'baq')
        tone: tone number 1-5

    Returns:
        Tengwar Unicode string
    """
    result = []
    syllable = syllable.lower()
    pos = 0

    # Parse initial
    initial = None
    aspirated = False
    voiced_fric = False

    # Check multi-char initials first
    for length in (2, 1):
        chunk = syllable[pos:pos+length]
        if chunk in INITIALS_TO_IPA:
            ipa = INITIALS_TO_IPA[chunk]
            aspirated = 'ʰ' in ipa
            voiced_fric = ipa in ('v', 'z', 'ɣ', 'ʐ')

            # Map to tengwa
            if chunk in ('b', 'd', 'g'):
                initial = {'b': 'parma', 'd': 'tinco', 'g': 'quesse'}[chunk]
            elif chunk in ('p', 't', 'k'):
                initial = {'p': 'parma', 't': 'tinco', 'k': 'quesse'}[chunk]
            elif chunk == 'm':
                initial = 'malta'
            elif chunk == 'n':
                initial = 'numen'
            elif chunk == 'l':
                initial = 'lambe'
            elif chunk == 'f':
                initial = 'formen'
            elif chunk == 'v':
                initial = 'ampa'
            elif chunk in ('z', 'c', 's'):
                initial = {'z': 'tinco_ext', 'c': 'tinco_ext', 's': 'thule'}[chunk]
            elif chunk == 'rz':
                initial = 'esse'
            elif chunk in ('zh', 'ch', 'sh', 'r'):
                initial = {'zh': 'calma', 'ch': 'calma', 'sh': 'hwesta', 'r': 'hwesta'}[chunk]
            elif chunk in ('j', 'q', 'x'):
                initial = {'j': 'calma', 'q': 'calma', 'x': 'hwesta'}[chunk]
            elif chunk == 'h':
                initial = 'harma'
            elif chunk == 'hh':
                initial = 'harma'
                voiced_fric = True
            elif chunk == 'ng':
                initial = 'noldo'
            elif chunk == 'ny':
                initial = 'numen'

            pos += length
            break

    # Add initial tengwa
    if initial:
        result.append(TENGWAR[initial])
        if chunk in ('j', 'q', 'x', 'ny'):
            result.append(PALATAL_MARK)
        if aspirated:
            result.append(ASPIRATION_MARK)
        if voiced_fric:
            result.append(VOICING_MARK)
    else:
        result.append(TENGWAR['telco'])

    # Parse final
    final = syllable[pos:]

    # Handle medial glides
    if final.startswith('i') and len(final) > 1 and final[1] in 'aeou':
        result.append(TENGWAR['anna'])
        final = final[1:]
    elif final.startswith('u') and len(final) > 1 and final[1] in 'aeio':
        result.append(TENGWAR['vala'])
        final = final[1:]
    elif final.startswith('yu') and len(final) > 2:
        result.append(TENGWAR['anna'])
        result.append(PALATAL_MARK)
        final = final[2:]

    # Handle vowel
    if final.startswith('ii'):
        result.append(TEHTAR['syllabic'])
        final = final[2:]
    elif final.startswith('yu'):
        result.append(TEHTAR['u'])
        result.append(TEHTAR['i'])
        final = final[2:]
    elif final and final[0] in 'aeiou':
        result.append(TEHTAR[final[0]])
        final = final[1:]

    # Skip diphthong offglides
    while final and final[0] in 'iuo':
        final = final[1:]

    # Handle coda
    if final == 'ng':
        result.append(TENGWAR['noldo'])
    elif final == 'n':
        result.append(TENGWAR['numen'])
    elif final == 'q':  # glottal stop
        result.append(TENGWAR['telco'])

    # Add tone
    if tone:
        result.append(get_tone_marks(tone))

    return ''.join(result)


def parse_numbered(text):
    """Parse romanization with tone numbers (e.g., 'tai2 yuan2')."""
    pattern = r"([a-z]+)([1-5])?"
    syllables = []
    for match in re.finditer(pattern, text.lower()):
        syl = match.group(1)
        tone = int(match.group(2)) if match.group(2) else None
        syllables.append((syl, tone))
    return syllables


def convert_text(text):
    """Convert romanized Jin text to Tengwar."""
    syllables = parse_numbered(text)
    return ''.join(romanization_to_tengwar(s, t) for s, t in syllables)


# === SAMPLES ===

SAMPLES = {
    'greetings': [
        ('ni2 hao3', '你好', 'hello'),
        ('xie4 xie4', '谢谢', 'thank you'),
    ],
    'numbers': [
        ('yiq5', '一', 'one'),
        ('liang3', '两', 'two'),
        ('san1', '三', 'three'),
        ('sii4', '四', 'four'),
        ('wu3', '五', 'five'),
        ('luq5', '六', 'six'),
        ('qi1', '七', 'seven'),
        ('baq5', '八', 'eight'),
        ('jiu3', '九', 'nine'),
        ('shiq5', '十', 'ten'),
    ],
    'places': [
        ('tai2 yuan2', '太原', 'Taiyuan'),
        ('shan1 xi1', '山西', 'Shanxi'),
    ],
}


if __name__ == '__main__':
    print("=== Tengwar Jin (Taiyuan) Converter Demo ===\n")

    print("Numbers with entering tone (checked syllables):")
    for rom, hz, en in SAMPLES['numbers']:
        tengwar = convert_text(rom)
        print(f"  {rom:12} {hz} ({en}): {tengwar}")

    print("\nPlaces:")
    for rom, hz, en in SAMPLES['places']:
        tengwar = convert_text(rom)
        print(f"  {rom:12} {hz} ({en}): {tengwar}")
