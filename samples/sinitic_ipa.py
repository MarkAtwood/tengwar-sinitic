#!/usr/bin/env python3
"""
Sinitic IPA to Tengwar Converter

Converts IPA transcriptions of any Sinitic language to Tengwar Unicode.
Languages without standardized romanization can use this directly.

See docs/sinitic-ipa.md for the phoneme inventory and design rationale.

Codepoints follow Wu/Gan convention (systematic column layout).
Note: Mandarin converter uses different codepoints - a known inconsistency.
"""

import re

# === TENGWAR CODEPOINTS (Alcarin Tengwar) ===
# Following Wu/Gan systematic layout:
# Column I (Alveolar): U+E00x, Column II (Labial): U+E01x, Column III (Velar): U+E02x

TENGWAR = {
    # Column I - Alveolar
    'tinco': '',      # Grade 1: /t/
    'ando': '',       # Grade 2: /d/ (B) or /tʰ/ (A)
    'thule': '',      # Grade 3: /s/
    'anto': '',       # Grade 4: /z/ voiced (Group B)
    'numen': '',      # Grade 5: /n/
    'lambe': '',      # Grade 6: /l/

    # Column II - Labial
    'parma': '',      # Grade 1: /p/
    'umbar': '',      # Grade 2: /b/ (B) or /pʰ/ (A)
    'formen': '',     # Grade 3: /f/
    'ampa': '',       # Grade 4: /v/ voiced (Group B)
    'malta': '',      # Grade 5: /m/
    'vala': '',       # Glide /w/

    # Column III - Velar
    'calma': '',      # Grade 1: /k/ or /tʂ/
    'anga': '',       # Grade 2: /g/ (B) or /kʰ/ (A)
    'hwesta': '',     # Grade 3: /x/ or /ʂ/
    'unque': '',      # Grade 4: /ɣ/ voiced (Group B)
    'noldo': '',      # Grade 5: /ŋ/

    # Aliases for modes using different column assignments
    'quesse': '',     # alias calma
    'ungwe': '',      # alias anga
    'harma': '',      # alias hwesta
    'ore': '',        # /ɻ/ retroflex approximant

    # Extended stem - Affricates
    'tinco_ext': '',  # /ts/
    'ando_ext': '',   # /dz/ (B) or /tsʰ/ (A)

    # Approximants/glides
    'anna': '',       # /j/

    # Carriers and special
    'telco': '',      # zero initial / short carrier
    'halla': '',      # glottal stop /ʔ/
}

TEHTAR = {
    'a': '',      # three dots
    'e': '',      # acute stroke
    'i': '',      # single dot
    'o': '',      # left curl
    'u': '',      # right curl
    'syllabic': '',   # unutixe / underdot (apical vowel)
    'underdot': '',   # alias
}

PALATAL_MARK = ''     # double dot below
W_CURL = ''           # w-curl below (labialization)

TONE_MARKS = {
    'level': '',      # flat bar
    'rising': '',     # acute stroke
    'falling': '',    # grave stroke
    'dipping': '',    # caron/chevron below
}

REGISTER_MODS = {
    'high': '',             # no modifier
    'mid': '',        # single dot
    'low': '',        # double dot
}

# === IPA TO TENGWAR MAPPINGS ===

# Group A: aspiration semantics (Mandarin, Cantonese, Hakka, Gan, Xiang)
# Group B: voicing semantics (Jin, Min, Wu)

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
    'ʔ': 'halla',

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
    'ʔ': 'halla',

    # Voiced affricates
    'ts': 'tinco_ext',
    'dz': 'ando_ext',
    'tɕ': ('calma', PALATAL_MARK),
    'dʑ': ('anga', PALATAL_MARK),

    # Voiced fricatives
    'f': 'formen',
    'v': 'ampa',
    's': 'thule',
    'z': 'anto',
    'ɕ': ('hwesta', PALATAL_MARK),
    'ʑ': ('hwesta', PALATAL_MARK),
    'x': 'harma',
    'ɣ': 'unque',
    'h': 'harma',
    'ɦ': 'unque',
    'ʐ': 'hwesta',  # voiced retroflex

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
    'ɿ': 'syllabic',  # apical vowel (alternate notation)
}


def parse_tone(tone_str):
    """
    Parse numeric tone to contour + register.

    Examples:
        '51' -> ('falling', 'high')
        '35' -> ('rising', 'mid')
        '214' -> ('dipping', 'low')
        '55' or '5' -> ('level', 'high')
    """
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
    if start in '54':
        register = 'high'
    elif start in '3':
        register = 'mid'
    else:
        register = 'low'

    return contour, register


def ipa_to_tengwar(ipa, group='A'):
    """
    Convert an IPA syllable to Tengwar.

    Args:
        ipa: IPA string, e.g., 'ma51' or 'tchi35'
        group: 'A' for aspiration semantics, 'B' for voicing semantics

    Returns:
        Tengwar Unicode string
    """
    consonants = CONSONANTS_A if group.upper() == 'A' else CONSONANTS_B
    result = []

    # Extract tone (trailing digits)
    tone_match = re.search(r'([1-5]+)$', ipa)
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
    while pos < len(ipa_core) and ipa_core[pos] in 'iueo':
        pos += 1

    # Parse coda
    while pos < len(ipa_core):
        chunk = ipa_core[pos]
        if chunk == 'n':
            result.append(TENGWAR['numen'])
            pos += 1
        elif chunk == 'N' or (pos + 1 < len(ipa_core) and ipa_core[pos:pos+2] == 'ng'):
            result.append(TENGWAR['noldo'])
            pos += 2 if ipa_core[pos:pos+2] == 'ng' else 1
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
        elif chunk == '?':  # glottal stop
            result.append(TENGWAR['halla'])
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
            ('ma55', 'A'),    # T1 high level
            ('ma35', 'A'),    # T2 rising
            ('ma214', 'A'),   # T3 dipping
            ('ma51', 'A'),    # T4 falling
        ]),
        ("Jin entering tone (Group B)", [
            ('pa?5', 'B'),    # checked syllable with glottal
            ('i?5', 'B'),     # yi (one)
        ]),
        ("Wu voiced initial (Group B)", [
            ('bu23', 'B'),    # voiced /b/
            ('da11', 'B'),    # voiced /d/
        ]),
    ]

    for title, items in examples:
        print(f"{title}:")
        for ipa, group in items:
            tengwar = ipa_to_tengwar(ipa, group)
            print(f"  /{ipa}/ -> {tengwar}")
        print()
