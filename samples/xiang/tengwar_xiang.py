#!/usr/bin/env python3
"""
Tengwar Xiang (Changsha) Converter

Converts Beta 5.0 romanization (with tone numbers) to Tengwar Unicode for the
Changsha Xiang mode. Uses Alcarin Tengwar codepoints (PUA U+E000-E0FF).

Based on the mapping in tengwar-xiang.md:
- Grade 1 (single bow) = voiceless unaspirated
- Grade 2 (double bow) = voiceless aspirated
- Column I = alveolar, II = labial, III = velar
- Uses Group A semantics (compatible with Mandarin/Cantonese/Hakka)

Key differences from Mandarin:
- 6 tones (including rusheng/entering tone as T6)
- Aspiration marked explicitly with 'h' suffix (ph, th, kh, ch, qh)
- Initial ng- permitted
- Nasalized vowels (on, en) marked with tilde-below
- Palatals: q, qh, x (not j, q, x as in Pinyin)
"""

# === TENGWAR CODEPOINTS (Alcarin Tengwar) ===

# Base consonants - mapped per Alcarin character table
TENGWAR = {
    # Column I - Alveolar
    'tinco': '\ue000',      # Grade 1: t /t/
    'ando': '\ue004',       # Grade 2: th /tʰ/
    'thuule': '\ue008',     # Grade 3: s /s/
    'nuumen': '\ue010',     # Grade 5: n /n/
    'lambe': '\ue022',      # Grade 6: l /l/

    # Column II - Labial
    'parma': '\ue001',      # Grade 1: p /p/
    'umbar': '\ue005',      # Grade 2: ph /pʰ/
    'formen': '\ue009',     # Grade 3: f /f/
    'malta': '\ue011',      # Grade 5: m /m/

    # Column III - Velar
    'calma': '\ue002',      # Grade 1: k /k/
    'anga': '\ue006',       # Grade 2: kh /kʰ/
    'hwesta': '\ue00b',     # Grade 3: h /x/
    'noldo': '\ue012',      # Grade 5: ng /ŋ/

    # Column IV - Retroflex (marginal in Changsha, optional support)
    'quesse': '\ue003',     # Grade 1: zr /tʂ/
    'ungwe': '\ue007',      # Grade 2: chr /tʂʰ/
    'harma': '\ue00a',      # Grade 3: sr /ʂ/
    'oore': '\ue014',       # Grade 6: r /ɻ/

    # Extended stem - Alveolar affricates
    'tinco_ext': '\ue018',  # c /ts/ (unaspirated)
    'ando_ext': '\ue01c',   # ch /tsʰ/ (aspirated)

    # Approximants/glides
    'anna': '\ue016',       # Glide /j/ (medial i-)
    'vala': '\ue015',       # Glide /w/ (medial u-)

    # Carriers
    'carrier_short': '\ue02e',  # telco - zero initial
    'carrier_long': '\ue02c',   # ára - for long vowels
}

# Tehtar (vowel marks) - placed above preceding consonant
TEHTAR = {
    'a': '\ue040',      # three dots above (amatixe)
    'o': '\ue04c',      # left curl
    'e': '\ue046',      # acute stroke
    'i': '\ue044',      # single dot above
    'u': '\ue04a',      # right curl
}

# Diacritics
PALATAL_MARK = '\ue043'     # two dots below - marks palatal consonants (q, qh, x)
NASAL_VOWEL = '\ue052'      # tilde - marks nasalized vowels (on, en)
UNDERBAR = '\ue051'         # doubler/macron below - marks Tone 6 (rusheng)

# Tone marks for below-tengwa placement
# Xiang has 6 tones using contour + register system
# Contours: rising (U+E046 acute below -> U+E047), falling (U+E054 grave)
# Register: none = high, single dot = mid, double dot = low
#
# Per tengwar-xiang.md:
# T1 (34): rising + single dot (mid-rising)
# T2 (13): rising + double dot (low-rising)
# T3 (42): falling (high-falling)
# T4 (45): rising bare (high-rising)
# T5 (21): falling + double dot (low-falling)
# T6 (14/24): rising + under-bar (entering tone marker)

# Contour marks (below-tengwa position)
CONTOUR_RISING = '\ue047'    # acute below
CONTOUR_FALLING = '\ue054'   # grave (used below)

# Register modifiers
REGISTER_MID = '\ue045'      # single dot below (mid register)
REGISTER_LOW = '\ue043'      # double dot below (low register)

# Composed tone marks
TONE_MARKS = {
    1: (CONTOUR_RISING, REGISTER_MID),    # T1: rising + mid-dot
    2: (CONTOUR_RISING, REGISTER_LOW),    # T2: rising + low-dots
    3: (CONTOUR_FALLING, None),           # T3: falling (high)
    4: (CONTOUR_RISING, None),            # T4: rising (high)
    5: (CONTOUR_FALLING, REGISTER_LOW),   # T5: falling + low-dots
    6: (CONTOUR_RISING, UNDERBAR),        # T6: rising + under-bar (rusheng)
}

# === BETA 5.0 TO TENGWAR MAPPING ===

# Initial consonants - Beta 5.0 romanization
# Note: aspiration is marked with 'h' suffix unlike Pinyin
INITIALS = {
    # Labials
    'p': 'parma',           # /p/ unaspirated
    'ph': 'umbar',          # /pʰ/ aspirated
    'm': 'malta',           # /m/
    'f': 'formen',          # /f/

    # Alveolars
    't': 'tinco',           # /t/ unaspirated
    'th': 'ando',           # /tʰ/ aspirated
    'n': 'nuumen',          # /n/
    'l': 'lambe',           # /l/

    # Velars
    'k': 'calma',           # /k/ unaspirated
    'kh': 'anga',           # /kʰ/ aspirated
    'ng': 'noldo',          # /ŋ/ - unlike Mandarin, can be initial
    'h': 'hwesta',          # /x/

    # Alveolar affricates
    'c': 'tinco_ext',       # /ts/ unaspirated
    'ch': 'ando_ext',       # /tsʰ/ aspirated
    's': 'thuule',          # /s/

    # Palatals (velar tengwar + palatal mark)
    'q': ('calma', True),   # /tɕ/ + palatal
    'qh': ('anga', True),   # /tɕʰ/ + palatal
    'x': ('hwesta', True),  # /ɕ/ + palatal

    # Retroflexes (marginal - for older/conservative speakers)
    'zr': 'quesse',         # /tʂ/
    'chr': 'ungwe',         # /tʂʰ/
    'sr': 'harma',          # /ʂ/
    'r': 'oore',            # /ɻ/
}

# Two-letter initials to check first (order matters for parsing)
TWO_LETTER_INITIALS = ['ph', 'th', 'kh', 'ng', 'ch', 'qh', 'zr', 'sr']
THREE_LETTER_INITIALS = ['chr']


def beta_to_tengwar(syllable, tone=None):
    """
    Convert a single Beta 5.0 syllable to Tengwar.

    Args:
        syllable: Beta 5.0 syllable (e.g., 'ma', 'kho', 'qhi', 'kon')
        tone: Tone number 1-6 (None = no tone mark)

    Returns:
        Tengwar Unicode string
    """
    result = []
    syllable = syllable.lower()
    pos = 0

    # === Parse initial ===
    initial = None
    palatal = False

    # Check three-letter initials first
    if len(syllable) >= 3 and syllable[pos:pos+3] in THREE_LETTER_INITIALS:
        initial = INITIALS[syllable[pos:pos+3]]
        pos += 3
    # Check two-letter initials
    elif len(syllable) >= 2 and syllable[pos:pos+2] in TWO_LETTER_INITIALS:
        init_data = INITIALS[syllable[pos:pos+2]]
        if isinstance(init_data, tuple):
            initial, palatal = init_data
        else:
            initial = init_data
        pos += 2
    # Check single-letter initials
    elif syllable[pos:pos+1] in INITIALS:
        init_data = INITIALS[syllable[pos]]
        if isinstance(init_data, tuple):
            initial, palatal = init_data
        else:
            initial = init_data
        pos += 1

    # Add initial tengwa
    if initial:
        result.append(TENGWAR[initial])
        if palatal:
            result.append(PALATAL_MARK)
    else:
        # Zero initial - use carrier
        result.append(TENGWAR['carrier_short'])

    # === Parse final (medials, vowels, codas) ===
    final = syllable[pos:]
    has_nasal_vowel = False

    # Handle medial glides (rising diphthongs)
    if final.startswith('i') and len(final) > 1 and final[1] in 'aeou':
        # Medial /j/: ia, ie, io, iu → anna + vowel
        result.append(TENGWAR['anna'])
        final = final[1:]
    elif final.startswith('u') and len(final) > 1 and final[1] in 'aeio':
        # Medial /w/: ua, uo, ui, ue → vala + vowel
        result.append(TENGWAR['vala'])
        final = final[1:]
    elif final.startswith('y') and len(final) > 1:
        # Medial /ɥ/: ye → anna + palatal + vowel
        result.append(TENGWAR['anna'])
        result.append(PALATAL_MARK)
        final = final[1:]

    # Handle main vowel
    vowel_char = None
    if final:
        if final[0] == 'y':
            # Front rounded vowel /y/ - use both u-tehta and i-tehta
            result.append(TEHTAR['u'])
            result.append(TEHTAR['i'])
            final = final[1:]
        elif final[0] in TEHTAR:
            vowel_char = final[0]
            result.append(TEHTAR[vowel_char])
            final = final[1:]

    # Check for nasalized vowels (on, en as nasalized when no nasal coda follows)
    # In Beta 5.0, 'on' and 'en' at end of syllable indicate nasalized vowels
    # But -n and -ng as codas are actual nasal codas
    # The distinction: nasalized vowels don't co-occur with nasal codas
    #
    # Pattern: if we have 'n' at end but vowel was 'o' or 'e', it's nasalized
    # But if we have 'ng' or 'n' after other vowels, it's a coda
    if final == 'n' and vowel_char in ('o', 'e'):
        # Nasalized vowel - add tilde marker
        result.append(NASAL_VOWEL)
        has_nasal_vowel = True
        final = ''

    # Handle diphthong glides (falling diphthongs - just consume, tehta already placed)
    # ai→a, ao→a, ei→e, ou→o
    if final.startswith(('i', 'u', 'o')) and vowel_char:
        final = final[1:]

    # Handle nasal codas
    if final == 'n' and not has_nasal_vowel:
        result.append(TENGWAR['nuumen'])
    elif final == 'ng':
        result.append(TENGWAR['noldo'])

    # === Add tone mark ===
    if tone and tone in TONE_MARKS:
        contour, register = TONE_MARKS[tone]
        result.append(contour)
        if register:
            result.append(register)

    return ''.join(result)


def parse_numbered_beta(text):
    """
    Parse Beta 5.0 with tone numbers (e.g., 'nga1 tha1 li3') into syllables.

    Returns list of (syllable, tone) tuples.
    """
    import re
    syllables = []
    # Match syllable + optional tone number (1-6)
    pattern = r"([a-zA-Z]+)([1-6])?"
    for match in re.finditer(pattern, text):
        syl = match.group(1).lower()
        tone = int(match.group(2)) if match.group(2) else None
        syllables.append((syl, tone))
    return syllables


def convert_text(beta_text):
    """
    Convert a full Beta 5.0 text (with tone numbers) to Tengwar.

    Args:
        beta_text: String of Beta 5.0 romanization with tone numbers

    Returns:
        Tengwar Unicode string
    """
    syllables = parse_numbered_beta(beta_text)
    return ''.join(beta_to_tengwar(syl, tone) for syl, tone in syllables)


# === SAMPLE TEXTS ===

SAMPLES = {
    'basic_syllables': {
        'title': 'Basic Syllables (from spec)',
        'items': [
            ('nga1', 'I (colloquial)', 'noldo + a-tehta + T1'),
            ('tha1', 'he/she', 'ando + a-tehta + T1'),
            ('li3', 'inside', 'lambe + i-tehta + T3'),
            ('kho4', 'go', 'anga + o-tehta + T4'),
            ('fan5', 'rice', 'formen + a-tehta + numen + T5'),
        ],
    },

    'palatals': {
        'title': 'Syllables with Palatals',
        'items': [
            ('qhi4', 'to eat', 'anga+pal. + i-tehta + T4'),
            ('xi3', 'to wash', 'hwesta+pal. + i-tehta + T3'),
            ('qiu2', 'ball', 'calma+pal. + anna + u-tehta + T2'),
        ],
    },

    'nasal_vowels': {
        'title': 'Syllables with Nasalized Vowels',
        'items': [
            ('kon3', 'dog', 'calma + o-tehta + tilde + T3'),
            ('sen1', 'to live', 'thule + e-tehta + tilde + T1'),
        ],
    },

    'tone_6_rusheng': {
        'title': 'Tone 6 (Entering Tone) Syllables',
        'items': [
            ('pa6', 'hundred (historical *pak)', 'parma + a-tehta + T6'),
            ('se6', 'color (historical *sek)', 'thule + e-tehta + T6'),
            ('qi6', 'seven (historical *tsit)', 'calma+pal. + i-tehta + T6'),
            ('mo6', 'ink (historical *mok)', 'malta + o-tehta + T6'),
            ('fu6', 'fortune (historical *fuk)', 'formen + u-tehta + T6'),
        ],
    },

    'nasal_codas': {
        'title': 'Syllables with Nasal Codas',
        'items': [
            ('san1', 'three', 'thule + a-tehta + numen + T1'),
            ('tang2', 'sugar', 'tinco + a-tehta + noldo + T2'),
            ('ming4', 'bright', 'malta + i-tehta + noldo + T4'),
            ('pen3', 'book', 'parma + e-tehta + numen + T3'),
        ],
    },

    'tone_contrasts': {
        'title': 'Tone Contrasts on "ma"',
        'items': [
            ('ma1', 'mother', 'malta + a-tehta + T1'),
            ('ma2', 'hemp', 'malta + a-tehta + T2'),
            ('ma3', 'horse', 'malta + a-tehta + T3'),
            ('ma4', 'scold', 'malta + a-tehta + T4'),
            ('ma5', '(varies)', 'malta + a-tehta + T5'),
            ('ma6', '(rusheng)', 'malta + a-tehta + T6'),
        ],
    },
}


def demo():
    """Demonstrate the Tengwar Xiang converter."""
    print("=== Tengwar Xiang (Changsha) Converter Demo ===\n")

    # Test all 6 tones on 'ma'
    print("Six tones of 'ma':")
    for i in range(1, 7):
        syl = f"ma{i}"
        tengwar = convert_text(syl)
        print(f"  {syl}: {tengwar}")

    print()

    # Test sample categories
    for category, data in SAMPLES.items():
        print(f"{data['title']}:")
        for beta, meaning, structure in data['items']:
            tengwar = convert_text(beta)
            print(f"  {beta:8} ({meaning:20}) -> {tengwar}")
        print()

    # Test a phrase
    print("Sample phrase (approximate):")
    phrase = "nga1 qhi4 fan5"  # "I eat rice"
    tengwar = convert_text(phrase)
    print(f"  '{phrase}' -> {tengwar}")
    print()

    # Test nasalized vowels
    print("Nasalized vowel examples:")
    for syl in ['kon3', 'sen1', 'on2']:
        tengwar = convert_text(syl)
        print(f"  {syl}: {tengwar}")
    print()

    # Test entering tone (T6) without coda
    print("Tone 6 (rusheng/entering tone) - no stop coda:")
    for syl in ['pa6', 'se6', 'qi6', 'mo6']:
        tengwar = convert_text(syl)
        print(f"  {syl}: {tengwar}")


if __name__ == '__main__':
    demo()
