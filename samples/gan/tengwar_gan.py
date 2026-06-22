#!/usr/bin/env python3
"""
Tengwar Gan Converter

Converts Gan (Nanchang) romanization (with tone numbers) to Tengwar Unicode.

Uses Alcarin Tengwar codepoints (PUA U+E000-E0FF).

Based on tengwar-gan.md spec:
- Inherits ~90% from Hakka mode
- NO /v/ initial (unlike Hakka)
- NO -p coda (-p merged to -t in Gan)
- 7 tones with different contour assignments
- Adds schwa 'oe' and front rounded 'yu'

Known limitation: Complex rimes like 'xue' (/ɕyɛ/) where 'u' represents
front-rounded /y/ rather than a medial glide need special handling.
"""

# === TENGWAR CODEPOINTS (Alcarin Tengwar) ===

TENGWAR = {
    # Column I - Alveolar
    'tinco': '\ue001',      # Grade 1: d /t/
    'ando': '\ue002',       # Grade 2: t /th/
    'thule': '\ue003',      # Grade 3: s /s/
    'numen': '\ue005',      # Grade 5: n /n/
    'lambe': '\ue026',      # Grade 6: l /l/

    # Column II - Labial
    'parma': '\ue011',      # Grade 1: b /p/
    'umbar': '\ue012',      # Grade 2: p /ph/
    'formen': '\ue013',     # Grade 3: f /f/
    'malta': '\ue015',      # Grade 5: m /m/

    # Column III - Velar
    'calma': '\ue021',      # Grade 1: g /k/
    'anga': '\ue022',       # Grade 2: k /kh/
    'hwesta': '\ue023',     # Grade 3: h /h/
    'noldo': '\ue025',      # Grade 5: ng /ng/

    # Extended stem - Alveolar affricates
    'tinco_ext': '\ue009',  # z /ts/
    'ando_ext': '\ue00a',   # c /tsh/

    # Approximants/glides
    'anna': '\ue027',       # Glide /j/ (medial i-)
    'vala': '\ue02d',       # Glide /w/ (medial u-)

    # Carriers
    'telco': '\ue02f',      # Zero initial carrier
}

# Palatal diacritic (below tengwa)
PALATAL_MARK = '\ue06b'

# Tehtar (vowel marks)
TEHTAR = {
    'a': '\ue040',      # three dots above (a-tehta)
    'e': '\ue046',      # acute stroke above (e-tehta)
    'i': '\ue044',      # single dot above (i-tehta)
    'o': '\ue048',      # left curl above (o-tehta)
    'u': '\ue049',      # right curl above (u-tehta)
    'ii': '\ue045',     # unutixe - syllabic/apical vowel mark
    'oe': '\ue04d',     # underdot - schwa
}

# Tone marks - contour shapes (below-tengwa position)
TONE_CONTOUR = {
    'level': '\ue050',      # flat bar (nasalizer-teng)
    'rising': '\ue046',     # acute stroke (acute-teng)
    'falling': '\ue054',    # grave stroke (grave-teng)
    'chevron': '\ue055',    # caron-teng (for dipping tone)
}

# Register modifiers (below the contour mark)
REGISTER_MOD = {
    'high': None,           # no modifier (implicit)
    'mid': '\ue045',        # single dot (unutixe-teng)
    'low': '\ue043',        # double dot (dotdblbelow-teng)
}


def get_tone_marks(tone):
    """
    Return the tone mark sequence for a Nanchang Gan tone (1-7).

    Gan tones:
    - T1 (42, mid-falling): falling stroke
    - T2 (24, low-rising): rising stroke + double-dot
    - T3 (213, dipping): chevron
    - T4 (45, high-rising): rising stroke
    - T5 (11, low-level): flat bar + double-dot
    - T6 (5, high checked): flat bar
    - T7 (21, low-falling checked): falling stroke + double-dot
    """
    if tone == 1:
        return TONE_CONTOUR['falling']
    elif tone == 2:
        return TONE_CONTOUR['rising'] + REGISTER_MOD['low']
    elif tone == 3:
        return TONE_CONTOUR['chevron']
    elif tone == 4:
        return TONE_CONTOUR['rising']
    elif tone == 5:
        return TONE_CONTOUR['level'] + REGISTER_MOD['low']
    elif tone == 6:
        return TONE_CONTOUR['level']
    elif tone == 7:
        return TONE_CONTOUR['falling'] + REGISTER_MOD['low']
    else:
        return ''


# === GAN ROMANIZATION TO TENGWAR MAPPING ===

# Initial consonants (NO /v/ in Gan, unlike Hakka)
INITIALS = {
    # Labials
    'b': 'parma',       # /p/
    'p': 'umbar',       # /ph/
    'm': 'malta',       # /m/
    'f': 'formen',      # /f/

    # Alveolars
    'd': 'tinco',       # /t/
    't': 'ando',        # /th/
    'n': 'numen',       # /n/
    'l': 'lambe',       # /l/

    # Velars
    'g': 'calma',       # /k/
    'k': 'anga',        # /kh/
    'ng': 'noldo',      # /ng/
    'h': 'hwesta',      # /h/

    # Alveolar affricates (extended stem)
    'z': 'tinco_ext',   # /ts/
    'c': 'ando_ext',    # /tsh/
    's': 'thule',       # /s/

    # Palatals (calma/anga/hwesta + palatal mark)
    'j': ('calma', True),   # /tc/
    'q': ('anga', True),    # /tch/
    'x': ('hwesta', True),  # /c/ (palatal fricative)
}

# Final consonants (codas) - NO -p in Gan (merged to -t)
FINALS = {
    # Nasal codas
    'n': 'numen',
    'ng': 'noldo',

    # Stop codas (only -t and -k in Gan; NO -p)
    't': 'tinco',
    'k': 'calma',
}


def get_vowel_tehtar(vowel):
    """
    Return the tehtar sequence for a Gan vowel.

    Gan vowels:
    - a: /a/ -> a-tehta (three dots)
    - e: /ɛ/ -> e-tehta (acute)
    - i: /i/ -> i-tehta (dot)
    - o: /o/ -> o-tehta (left curl)
    - u: /u/ -> u-tehta (right curl)
    - ii: /ɨ/ apical vowel -> unutixe (syllabic mark)
    - oe: /ə/ schwa -> underdot
    - yu: /y/ front rounded -> u-tehta + i-tehta
    """
    if vowel == 'yu':
        return TEHTAR['u'] + TEHTAR['i']
    elif vowel in TEHTAR:
        return TEHTAR[vowel]
    return ''


def parse_gan_syllable(syllable):
    """
    Parse a Gan syllable into components.

    Returns: (initial_tengwa, is_palatal, medial, vowel, coda)

    Where:
    - initial_tengwa: tengwa name for initial (or None for zero initial)
    - is_palatal: True if j/q/x (needs palatal mark)
    - medial: 'i' or 'u' glide, or None
    - vowel: vowel string (a, e, i, o, u, ii, oe, yu)
    - coda: coda consonant (n, ng, t, k) or None
    """
    syllable = syllable.lower()
    pos = 0
    initial = None
    is_palatal = False

    # Parse initial consonant
    # Check two-letter initials first
    if syllable[pos:pos+2] == 'ng':
        initial = INITIALS['ng']
        pos += 2
    elif syllable[pos:pos+1] in INITIALS:
        init_data = INITIALS[syllable[pos]]
        if isinstance(init_data, tuple):
            initial, is_palatal = init_data
        else:
            initial = init_data
        pos += 1
    # else: null initial

    # Remaining is the rime (medial + vowel + coda)
    rime = syllable[pos:]

    # Parse medial glide
    medial = None
    if rime.startswith('i') and len(rime) > 1 and rime[1] in 'aeou':
        medial = 'i'
        rime = rime[1:]
    elif rime.startswith('u') and len(rime) > 1 and rime[1] in 'aei':
        medial = 'u'
        rime = rime[1:]

    # Parse vowel and coda
    vowel = None
    coda = None

    # Check for special vowels first
    if rime.startswith('ii'):
        vowel = 'ii'
        coda_part = rime[2:]
    elif rime.startswith('oe'):
        vowel = 'oe'
        coda_part = rime[2:]
    elif rime.startswith('yu'):
        vowel = 'yu'
        coda_part = rime[2:]
    elif rime.startswith('a'):
        vowel = 'a'
        coda_part = rime[1:]
    elif rime.startswith('e'):
        vowel = 'e'
        coda_part = rime[1:]
    elif rime.startswith('i'):
        vowel = 'i'
        coda_part = rime[1:]
    elif rime.startswith('o'):
        vowel = 'o'
        coda_part = rime[1:]
    elif rime.startswith('u'):
        vowel = 'u'
        coda_part = rime[1:]
    else:
        coda_part = rime

    # Consume diphthong offglides (i, u following nucleus)
    if coda_part.startswith('i') or coda_part.startswith('u'):
        if len(coda_part) == 1:
            coda_part = ''
        elif coda_part[1:].startswith('ng') or coda_part[1:] in ('n', 't', 'k'):
            coda_part = coda_part[1:]

    # Parse coda (only n, ng, t, k in Gan - NO p)
    if coda_part == 'ng':
        coda = 'ng'
    elif coda_part in ('n', 't', 'k'):
        coda = coda_part

    return (initial, is_palatal, medial, vowel, coda)


def convert_syllable(syllable, tone=None):
    """
    Convert a single Gan syllable to Tengwar.

    Args:
        syllable: Gan romanization (e.g., 'gon', 'set', 'sii')
        tone: Tone number 1-7 (None = no tone mark)

    Returns:
        Tengwar Unicode string
    """
    result = []

    initial, is_palatal, medial, vowel, coda = parse_gan_syllable(syllable)

    # === Add initial tengwa ===
    if initial:
        result.append(TENGWAR[initial])
        if is_palatal:
            result.append(PALATAL_MARK)
    else:
        # Zero initial - use carrier
        result.append(TENGWAR['telco'])

    # === Add medial glide ===
    if medial == 'i':
        result.append(TENGWAR['anna'])
    elif medial == 'u':
        result.append(TENGWAR['vala'])

    # === Add vowel tehtar ===
    if vowel:
        result.append(get_vowel_tehtar(vowel))

    # === Add coda consonant ===
    if coda:
        result.append(TENGWAR[FINALS[coda]])

    # === Add tone mark ===
    if tone:
        result.append(get_tone_marks(tone))

    return ''.join(result)


def parse_numbered_gan(text):
    """
    Parse Gan romanization with tone numbers (e.g., 'gon1 nan2').

    Returns list of (syllable, tone) tuples.
    """
    import re
    syllables = []
    pattern = r"([a-zA-Z]+)([1-7])?"
    for match in re.finditer(pattern, text):
        syl = match.group(1).lower()
        tone = int(match.group(2)) if match.group(2) else None
        syllables.append((syl, tone))
    return syllables


def convert_text(gan_text):
    """
    Convert full Gan text (with tone numbers) to Tengwar.
    """
    syllables = parse_numbered_gan(gan_text)
    return ''.join(convert_syllable(syl, tone) for syl, tone in syllables)


# === REVERSE LOOKUP FOR DEBUGGING ===

_CODEPOINT_NAMES = {v: k for k, v in TENGWAR.items()}
_CODEPOINT_NAMES.update({
    TEHTAR['a']: '[a]',
    TEHTAR['e']: '[e/rise]',
    TEHTAR['i']: '[i]',
    TEHTAR['o']: '[o]',
    TEHTAR['u']: '[u]',
    TEHTAR['ii']: '[ii/.]',
    TEHTAR['oe']: '[oe]',
    PALATAL_MARK: '+pal',
    TONE_CONTOUR['level']: '_',
    TONE_CONTOUR['rising']: '/',
    TONE_CONTOUR['falling']: '\\',
    TONE_CONTOUR['chevron']: 'v',
    REGISTER_MOD['low']: '..',
})


def tengwar_to_names(tengwar_str):
    """Convert tengwar unicode to descriptive names for debugging."""
    result = []
    for c in tengwar_str:
        name = _CODEPOINT_NAMES.get(c)
        if name:
            if name.startswith('['):
                result.append(name)
            elif name.startswith('+') or name.startswith('.'):
                result.append(name)
            elif name in ('_', '/', '\\', 'v'):
                result.append(name)
            else:
                result.append('{' + name + '}')
        else:
            result.append(f'?{ord(c):04X}')
    return ''.join(result)


# === SAMPLE DATA ===

TONE_DEMO = {
    'title': 'Nanchang Gan Tones (7 tones)',
    'items': [
        ('gon1', '赣', 'T1 (42 mid-falling)'),
        ('nan2', '南', 'T2 (24 low-rising)'),
        ('song3', '上', 'T3 (213 dipping)'),
        ('qu4', '去', 'T4 (45 high-rising)'),
        ('ma5', '吗', 'T5 (11 low-level)'),
        ('set6', '十', 'T6 (5 high checked)'),
        ('set7', '食', 'T7 (21 low checked)'),
    ],
}

GAN_SPECIFIC = {
    'title': 'Gan-Specific Features',
    'items': [
        # Palatals j/q/x
        ('jin1', '金', 'gold (j-)'),
        ('qin2', '钱', 'money (q-)'),
        ('xin1', '新', 'new (x-)'),
        # Apical vowel ii
        ('sii3', '四', 'four (apical ii)'),
        ('cii2', '词', 'word'),
        ('zii5', '自', 'self'),
        # -p > -t merger examples
        ('set7', '十', 'ten (-t, was *-p)'),
        ('nit6', '入', 'enter (-t, was *-p)'),
        ('dat6', '答', 'answer (-t, was *-p)'),
    ],
}

FINAL_STOPS = {
    'title': 'Final Stops (only -t and -k in Gan)',
    'items': [
        ('it6', '一', 'one (-t)'),
        ('set7', '十', 'ten (-t)'),
        ('bak6', '百', 'hundred (-k)'),
        ('luk7', '六', 'six (-k)'),
    ],
}

NUMBERS = {
    'title': 'Numbers 1-10',
    'items': [
        ('it6', '一', 'one'),
        ('ngi4', '二', 'two'),
        ('san1', '三', 'three'),
        ('sii3', '四', 'four'),
        ('ng3', '五', 'five'),
        ('luk7', '六', 'six'),
        ('qit6', '七', 'seven'),
        ('bat6', '八', 'eight'),
        ('giu3', '九', 'nine'),
        ('set7', '十', 'ten'),
    ],
}

MEDIALS = {
    'title': 'Medial Glides',
    'items': [
        ('gua1', '瓜', 'melon (u-medial)'),
        ('tiau2', '跳', 'jump (i-medial)'),
        ('xue2', '学', 'study (palatal + u-medial)'),
    ],
}


def demo():
    """Demonstrate the converter with sample syllables."""
    print("=== Tengwar Gan Converter Demo (Nanchang) ===\n")

    # Test tones
    print(f"--- {TONE_DEMO['title']} ---")
    for gan, zh, meaning in TONE_DEMO['items']:
        tengwar = convert_text(gan)
        names = tengwar_to_names(tengwar)
        print(f"  {gan:8} {zh} {meaning:25} -> {tengwar}  ({names})")

    print()

    # Test Gan-specific features
    print(f"--- {GAN_SPECIFIC['title']} ---")
    for gan, zh, meaning in GAN_SPECIFIC['items']:
        tengwar = convert_text(gan)
        names = tengwar_to_names(tengwar)
        print(f"  {gan:8} {zh} {meaning:25} -> {tengwar}  ({names})")

    print()

    # Test final stops
    print(f"--- {FINAL_STOPS['title']} ---")
    for gan, zh, meaning in FINAL_STOPS['items']:
        tengwar = convert_text(gan)
        names = tengwar_to_names(tengwar)
        print(f"  {gan:8} {zh} {meaning:20} -> {tengwar}  ({names})")

    print()

    # Test numbers
    print(f"--- {NUMBERS['title']} ---")
    for gan, zh, meaning in NUMBERS['items']:
        tengwar = convert_text(gan)
        names = tengwar_to_names(tengwar)
        print(f"  {gan:8} {zh} {meaning:6} -> {tengwar}  ({names})")

    print()

    # Test medials
    print(f"--- {MEDIALS['title']} ---")
    for gan, zh, meaning in MEDIALS['items']:
        tengwar = convert_text(gan)
        names = tengwar_to_names(tengwar)
        print(f"  {gan:8} {zh} {meaning:25} -> {tengwar}  ({names})")

    print()

    # Comparison with Hakka (demonstrating -p > -t merger)
    print("--- Comparison: Gan -t vs Hakka -p (historical merger) ---")
    comparison = [
        ('set7', 'sip', '十 ten'),
        ('nit6', 'ngip', '入 enter'),
        ('dat6', 'dap', '答 answer'),
    ]
    for gan, hakka, meaning in comparison:
        tengwar = convert_text(gan)
        names = tengwar_to_names(tengwar)
        print(f"  Gan {gan:6} (vs Hakka {hakka:5}) {meaning:12} -> {tengwar}  ({names})")


if __name__ == '__main__':
    demo()
