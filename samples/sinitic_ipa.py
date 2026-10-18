#!/usr/bin/env python3
"""
Sinitic IPA to Tengwar Converter

Converts IPA transcriptions of any Sinitic language to Tengwar Unicode.
Languages without standardized romanization can use this directly.

See docs/sinitic-ipa.md for the phoneme inventory and design rationale.
"""

import re

# === TENGWAR CODEPOINTS (Alcarin Tengwar) ===
# TODO: Fill in codepoints from existing converters (tengwar_mandarin.py, etc.)
# ponytail: skeleton - codepoints left empty, fill from reference converter when integrating

TENGWAR = {
    # Column I - Alveolar
    'tinco': '',
    'ando': '',
    'thule': '',
    'numen': '',
    'lambe': '',

    # Column II - Labial
    'parma': '',
    'umbar': '',
    'formen': '',
    'malta': '',

    # Column III - Velar (or Retroflex in Mandarin mode)
    'calma': '',
    'anga': '',
    'hwesta': '',
    'noldo': '',
    'harma': '',

    # Extended stem - Affricates
    'tinco_ext': '',
    'ando_ext': '',

    # Approximants
    'anna': '',
    'vala': '',
    'ore': '',

    # Carriers
    'telco': '',
}

TEHTAR = {
    'a': '',
    'e': '',
    'i': '',
    'o': '',
    'u': '',
    'syllabic': '',  # unutixe
    'underdot': '',
}

PALATAL_MARK = ''
W_CURL = ''

TONE_MARKS = {
    'level': '',
    'rising': '',
    'falling': '',
    'dipping': '',
}

REGISTER_MODS = {
    'high': '',
    'mid': '',
    'low': '',
}

# === IPA TO TENGWAR MAPPINGS ===

# Group A: aspiration semantics (Mandarin, Cantonese, Hakka, Gan, Xiang)
# Group B: voicing semantics (Min, Wu)

CONSONANTS_A = {
    # Stops
    'p': 'parma',
    'pʰ': 'umbar',
    't': 'tinco',
    'tʰ': 'ando',
    'k': 'calma',
    'kʰ': 'anga',
    'kʷ': ('calma', W_CURL),
    'kʷʰ': ('anga', W_CURL),
    'ʔ': 'telco',

    # Affricates
    'ts': 'tinco_ext',
    'tsʰ': 'ando_ext',
    'tʂ': 'calma',  # retroflex uses col III
    'tʂʰ': 'anga',
    'tɕ': ('calma', PALATAL_MARK),
    'tɕʰ': ('anga', PALATAL_MARK),

    # Fricatives
    'f': 'formen',
    's': 'thule',
    'ʂ': 'hwesta',
    'ɕ': ('hwesta', PALATAL_MARK),
    'x': 'harma',
    'h': 'harma',

    # Nasals
    'm': 'malta',
    'n': 'numen',
    'ɲ': ('numen', PALATAL_MARK),
    'ŋ': 'noldo',

    # Approximants
    'l': 'lambe',
    'ɻ': 'ore',
    'j': 'anna',
    'w': 'vala',
    'ɥ': ('anna', PALATAL_MARK),
}

CONSONANTS_B = {
    # Voiced stops map to Grade 2
    'p': 'parma',
    'b': 'umbar',
    't': 'tinco',
    'd': 'ando',
    'k': 'calma',
    'g': 'anga',
    'ʔ': 'telco',

    # Voiced affricates
    'ts': 'tinco_ext',
    'dz': 'ando_ext',
    'tɕ': ('calma', PALATAL_MARK),
    'dʑ': ('anga', PALATAL_MARK),

    # Voiced fricatives
    'f': 'formen',
    'v': 'vala',  # ponytail: reuse vala for /v/
    's': 'thule',
    'z': 'thule',  # would need diacritic for true voicing contrast
    'ɕ': ('hwesta', PALATAL_MARK),
    'ʑ': ('hwesta', PALATAL_MARK),
    'h': 'harma',
    'ɦ': 'harma',

    # Nasals (same as A)
    'm': 'malta',
    'n': 'numen',
    'ɲ': ('numen', PALATAL_MARK),
    'ŋ': 'noldo',

    # Approximants (same as A)
    'l': 'lambe',
    'j': 'anna',
    'w': 'vala',
    'ɥ': ('anna', PALATAL_MARK),
}

VOWELS = {
    'a': 'a', 'ɑ': 'a', 'ä': 'a',
    'e': 'e', 'ɛ': 'e', 'ə': 'e',
    'i': 'i', 'ɪ': 'i',
    'o': 'o', 'ɔ': 'o',
    'u': 'u', 'ʊ': 'u', 'ʉ': 'u',
    'y': ('u', 'i'),  # front rounded = u + i tehtar
    'œ': ('o', 'i'),
    'ø': ('o', 'i'),
    'ɨ': 'syllabic',  # apical vowel
}


def parse_tone(tone_str):
    """
    Parse Chao tone letters or numeric tone to contour + register.

    Examples:
        '˥˩' or '51' -> ('falling', 'high')
        '˧˥' or '35' -> ('rising', 'mid')
        '˨˩˦' or '214' -> ('dipping', 'low')
        '˥' or '55' or '5' -> ('level', 'high')
    """
    # Convert numeric to Chao letters
    num_to_chao = {'5': '˥', '4': '˦', '3': '˧', '2': '˨', '1': '˩'}
    if tone_str and tone_str[0].isdigit():
        tone_str = ''.join(num_to_chao.get(c, c) for c in tone_str)

    if not tone_str:
        return None, None

    # Determine contour
    if len(tone_str) == 1 or tone_str[0] == tone_str[-1]:
        contour = 'level'
    elif len(tone_str) >= 3 and tone_str[1] < tone_str[0] and tone_str[-1] > tone_str[1]:
        contour = 'dipping'
    elif tone_str[-1] > tone_str[0]:
        contour = 'rising'
    else:
        contour = 'falling'

    # Determine register from starting pitch
    start = tone_str[0]
    if start in '˥˦5 4':
        register = 'high'
    elif start in '˧3':
        register = 'mid'
    else:
        register = 'low'

    return contour, register


def ipa_to_tengwar(ipa, group='A'):
    """
    Convert an IPA syllable to Tengwar.

    Args:
        ipa: IPA string, e.g., 'ma˥˩' or 'tɕʰi˧˥'
        group: 'A' for aspiration semantics, 'B' for voicing semantics

    Returns:
        Tengwar Unicode string
    """
    consonants = CONSONANTS_A if group.upper() == 'A' else CONSONANTS_B
    result = []

    # Extract tone (Chao letters at end, or trailing digits)
    tone_match = re.search(r'([˥˦˧˨˩]+|[1-5]+)$', ipa)
    tone_str = tone_match.group(1) if tone_match else ''
    ipa_core = ipa[:tone_match.start()] if tone_match else ipa

    pos = 0
    initial_found = False

    # Parse initial consonant (greedy match longest)
    for length in (3, 2, 1):
        chunk = ipa_core[pos:pos+length]
        if chunk in consonants:
            mapping = consonants[chunk]
            if isinstance(mapping, tuple):
                result.append(TENGWAR[mapping[0]])
                result.append(mapping[1])
            else:
                result.append(TENGWAR[mapping])
            pos += length
            initial_found = True
            break

    if not initial_found:
        result.append(TENGWAR['telco'])

    # Parse medial glides
    if pos < len(ipa_core) and ipa_core[pos] == 'j':
        result.append(TENGWAR['anna'])
        pos += 1
    elif pos < len(ipa_core) and ipa_core[pos] == 'w':
        result.append(TENGWAR['vala'])
        pos += 1
    elif pos < len(ipa_core) and ipa_core[pos] == 'ɥ':
        result.append(TENGWAR['anna'])
        result.append(PALATAL_MARK)
        pos += 1

    # Parse vowel
    if pos < len(ipa_core):
        v = ipa_core[pos]
        if v in VOWELS:
            mapping = VOWELS[v]
            if isinstance(mapping, tuple):
                for t in mapping:
                    result.append(TEHTAR[t])
            else:
                result.append(TEHTAR[mapping])
            pos += 1

    # Skip glide offsets in diphthongs (ai, au, etc.)
    while pos < len(ipa_core) and ipa_core[pos] in 'iuɪʊ':
        pos += 1

    # Parse coda
    while pos < len(ipa_core):
        chunk = ipa_core[pos]
        if chunk == 'n':
            result.append(TENGWAR['numen'])
            pos += 1
        elif chunk == 'ŋ':
            result.append(TENGWAR['noldo'])
            pos += 1
        elif chunk == 'm':
            result.append(TENGWAR['malta'])
            pos += 1
        elif chunk in 'ptk':
            # Unreleased stop codas
            if chunk == 'p':
                result.append(TENGWAR['parma'])
            elif chunk == 't':
                result.append(TENGWAR['tinco'])
            else:
                result.append(TENGWAR['calma'])
            pos += 1
        elif chunk == '̚':  # unreleased marker, skip
            pos += 1
        else:
            pos += 1  # skip unknown

    # Add tone mark
    contour, register = parse_tone(tone_str)
    if contour:
        result.append(TONE_MARKS[contour])
        if register and REGISTER_MODS[register]:
            result.append(REGISTER_MODS[register])

    return ''.join(result)


def convert_text(ipa_text, group='A'):
    """Convert space/dot-separated IPA syllables to Tengwar."""
    syllables = re.split(r'[\s.]+', ipa_text)
    return ''.join(ipa_to_tengwar(s, group) for s in syllables if s)


if __name__ == '__main__':
    # Demo
    print("=== Sinitic IPA to Tengwar Demo ===\n")

    examples = [
        ("Mandarin 'ma' tones", [
            ('ma˥', 'A'),    # T1
            ('ma˧˥', 'A'),   # T2
            ('ma˨˩˦', 'A'),  # T3
            ('ma˥˩', 'A'),   # T4
        ]),
        ("Cantonese 'nei hou'", [
            ('nei˩˧', 'A'),
            ('hou˧˥', 'A'),
        ]),
        ("Wu voiced initial (Group B)", [
            ('bu˨˧', 'B'),   # voiced /b/
            ('da˩˩', 'B'),   # voiced /d/
        ]),
    ]

    for title, items in examples:
        print(f"{title}:")
        for ipa, group in items:
            tengwar = ipa_to_tengwar(ipa, group)
            print(f"  /{ipa}/ -> {tengwar}")
        print()
