#!/usr/bin/env python3
"""
Tengwar Hakka Converter

Converts Taiwan MOE Hakka Romanization (with tone numbers) to Tengwar Unicode
for the Hakka mode (Sixian dialect).

Uses Alcarin Tengwar codepoints (PUA U+E000-E0FF).

Based on tengwar-hakka.md spec:
- Inherits ~90% from Cantonese mode
- Adds /v/ initial (ampa), palatals j/q/x, apical vowel ii (unutixe)
- 6 tones with different Chao values than Cantonese
- No labialized velars (gw/kw) or syllabic nasals
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
    'ampa': '\ue014',       # Grade 4: v /v/ (Hakka-specific)
    'malta': '\ue015',      # Grade 5: m /m/

    # Column IV - Velar
    'quesse': '\ue021',     # Grade 1: g /k/
    'ungwe': '\ue022',      # Grade 2: k /kh/
    'harma': '\ue023',      # Grade 3: h /h/
    'noldo': '\ue025',      # Grade 5: ng /ng/

    # Extended stem - Alveolar affricates
    'tinco_ext': '\ue009',  # z /ts/
    'ando_ext': '\ue00a',   # c /tsh/

    # Approximants/glides
    'anna': '\ue027',       # Glide /j/ (medial i-)
    'vala': '\ue02d',       # Glide /w/ (medial u-)

    # Carriers
    'telco': '\ue02e',      # Zero initial carrier
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
}

# Tone marks - contour shapes (below-tengwa position)
TONE_CONTOUR = {
    'level': '\ue050',      # flat bar (nasalizer-teng)
    'rising': '\ue046',     # acute stroke (acute-teng)
    'falling': '\ue054',    # grave stroke (grave-teng)
}

# Register modifiers (below the contour mark)
REGISTER_MOD = {
    'high': None,           # no modifier (implicit)
    'mid': '\ue045',        # single dot (unutixe-teng)
    'low': '\ue043',        # double dot (dotdblbelow-teng)
}


def get_tone_marks(tone):
    """
    Return the tone mark sequence for a Sixian Hakka tone (1-6).

    Sixian tones:
    - T1 (24, mid-rising): rising stroke
    - T2 (11, low level): flat bar + double-dot
    - T3 (31, mid-falling): falling stroke + single dot
    - T4 (55, high level): flat bar
    - T5 (2, low checked): flat bar + double-dot
    - T6 (5, high checked): flat bar
    """
    if tone == 1:
        return TONE_CONTOUR['rising']
    elif tone == 2:
        return TONE_CONTOUR['level'] + REGISTER_MOD['low']
    elif tone == 3:
        return TONE_CONTOUR['falling'] + REGISTER_MOD['mid']
    elif tone == 4:
        return TONE_CONTOUR['level']
    elif tone == 5:
        return TONE_CONTOUR['level'] + REGISTER_MOD['low']
    elif tone == 6:
        return TONE_CONTOUR['level']
    else:
        return ''


# === HAKKA ROMANIZATION TO TENGWAR MAPPING ===

# Initial consonants
INITIALS = {
    # Labials
    'b': 'parma',       # /p/
    'p': 'umbar',       # /ph/
    'm': 'malta',       # /m/
    'f': 'formen',      # /f/
    'v': 'ampa',        # /v/ (Hakka-specific)

    # Alveolars
    'd': 'tinco',       # /t/
    't': 'ando',        # /th/
    'n': 'numen',       # /n/
    'l': 'lambe',       # /l/

    # Velars (Column IV)
    'g': 'quesse',      # /k/
    'k': 'ungwe',       # /kh/
    'ng': 'noldo',      # /ng/
    'h': 'harma',       # /h/

    # Alveolar affricates (extended stem)
    'z': 'tinco_ext',   # /ts/
    'c': 'ando_ext',    # /tsh/
    's': 'thule',       # /s/

    # Palatals (velar tengwar + palatal mark)
    'j': ('quesse', True),  # /tc/
    'q': ('ungwe', True),   # /tch/
    'x': ('harma', True),   # /c/ (palatal fricative)
}

# Final consonants (codas)
FINALS = {
    # Nasal codas
    'm': 'malta',
    'n': 'numen',
    'ng': 'noldo',

    # Stop codas (Grade 1 unaspirated)
    # Note: Taiwan MOE uses 'b', 'd', 'g' for final stops (written as /p/, /t/, /k/)
    'p': 'parma',
    't': 'tinco',
    'k': 'quesse',
    'b': 'parma',   # alternate spelling for -p
    'd': 'tinco',   # alternate spelling for -t
    'g': 'quesse',  # alternate spelling for -k
}


def get_vowel_tehtar(vowel):
    """
    Return the tehtar sequence for a Hakka vowel.

    Hakka vowels:
    - a: /a/ -> a-tehta (three dots)
    - e: /E/ -> e-tehta (acute)
    - i: /i/ -> i-tehta (dot)
    - o: /O/ -> o-tehta (left curl)
    - u: /u/ -> u-tehta (right curl)
    - ii: apical vowel -> unutixe (syllabic mark)
    """
    if vowel in TEHTAR:
        return TEHTAR[vowel]
    return ''


def parse_hakka_syllable(syllable):
    """
    Parse a Taiwan MOE Hakka syllable into components.

    Returns: (initial_tengwa, is_palatal, medial, vowel, coda)

    Where:
    - initial_tengwa: tengwa name for initial (or None for zero initial)
    - is_palatal: True if j/q/x (needs palatal mark)
    - medial: 'i' or 'u' glide, or None
    - vowel: vowel string (a, e, i, o, u, ii)
    - coda: coda consonant (m, n, ng, p, t, k) or None
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

    # Check for apical vowel 'ii' first
    if rime.startswith('ii'):
        vowel = 'ii'
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
        elif coda_part[1:] in ('m', 'n', 'ng', 'p', 't', 'k', 'b', 'd', 'g'):
            coda_part = coda_part[1:]

    # Parse coda
    if coda_part == 'ng':
        coda = 'ng'
    elif coda_part in ('m', 'n', 'p', 't', 'k', 'b', 'd', 'g'):
        coda = coda_part

    return (initial, is_palatal, medial, vowel, coda)


def convert_syllable(syllable, tone=None):
    """
    Convert a single Hakka syllable to Tengwar.

    Args:
        syllable: Hakka romanization (e.g., 'ngai', 'vuk', 'sii')
        tone: Tone number 1-6 (None = no tone mark)

    Returns:
        Tengwar Unicode string
    """
    result = []

    initial, is_palatal, medial, vowel, coda = parse_hakka_syllable(syllable)

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


def parse_numbered_hakka(text):
    """
    Parse Hakka romanization with tone numbers (e.g., 'ngai1 vuk5').

    Returns list of (syllable, tone) tuples.
    """
    import re
    syllables = []
    pattern = r"([a-zA-Z]+)([1-6])?"
    for match in re.finditer(pattern, text):
        syl = match.group(1).lower()
        tone = int(match.group(2)) if match.group(2) else None
        syllables.append((syl, tone))
    return syllables


def convert_text(hakka_text):
    """
    Convert full Hakka text (with tone numbers) to Tengwar.
    """
    syllables = parse_numbered_hakka(hakka_text)
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
    PALATAL_MARK: '+pal',
    TONE_CONTOUR['level']: '_',
    TONE_CONTOUR['falling']: '\\',
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
            elif name in ('_', '/', '\\'):
                result.append(name)
            else:
                result.append('{' + name + '}')
        else:
            result.append(f'?{ord(c):04X}')
    return ''.join(result)


# === SAMPLE DATA ===

TONE_DEMO = {
    'title': 'Sixian Tones',
    'items': [
        ('du1', '', 'T1 (24 mid-rising)'),
        ('du2', '', 'T2 (11 low level)'),
        ('du3', '', 'T3 (31 mid-falling)'),
        ('du4', '', 'T4 (55 high level)'),
        ('duk5', '', 'T5 (2 low checked)'),
        ('duk6', '', 'T6 (5 high checked)'),
    ],
}

HAKKA_SPECIFIC = {
    'title': 'Hakka-Specific Features',
    'items': [
        # /v/ initial
        ('vug5', '屋', 'house (v- initial)'),
        ('vun2', '文', 'writing'),
        ('vu3', '武', 'martial'),
        # Palatals j/q/x
        ('jim1', '針', 'needle (j-)'),
        ('qien2', '錢', 'money (q-)'),
        ('xin1', '新', 'new (x-)'),
        # Apical vowel ii
        ('sii4', '四', 'four (apical ii)'),
        ('cii2', '詞', 'word'),
        ('zii4', '自', 'self'),
    ],
}

GREETINGS = {
    'title': 'Common Greetings',
    'items': [
        ('ngai1', '涯', 'I/me'),
        ('ngi2', '你', 'you'),
        ('ki2', '佢', 'he/she'),
        ('an1 zong3', '安祥', 'good/well'),
        ('do1 xia4', '多謝', 'thank you'),
    ],
}

NUMBERS = {
    'title': 'Numbers 1-10',
    'items': [
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
    ],
}

PLACES = {
    'title': 'Taiwan Hakka Place Names',
    'items': [
        ('meu2 lid5', '苗栗', 'Miaoli'),
        ('sin1 zuk5', '新竹', 'Hsinchu'),
        ('toi2 bak5', '台北', 'Taipei'),
        ('toi2 zung1', '台中', 'Taichung'),
        ('pin2 tung2', '屏東', 'Pingtung'),
    ],
}


def test_conversion():
    """Test the converter with sample syllables."""
    print("=== Tengwar Hakka Converter Demo (Sixian) ===\n")

    # Test Hakka-specific features
    print(f"--- {HAKKA_SPECIFIC['title']} ---")
    for hakka, zh, meaning in HAKKA_SPECIFIC['items']:
        tengwar = convert_text(hakka)
        names = tengwar_to_names(tengwar)
        print(f"  {hakka:10} {zh:2} {meaning:25} -> {tengwar}  ({names})")

    print()

    # Test tones
    print(f"--- {TONE_DEMO['title']} ---")
    for hakka, zh, meaning in TONE_DEMO['items']:
        tengwar = convert_text(hakka)
        names = tengwar_to_names(tengwar)
        print(f"  {hakka:8} {meaning:25} -> {tengwar}  ({names})")

    print()

    # Test greetings
    print(f"--- {GREETINGS['title']} ---")
    for hakka, zh, meaning in GREETINGS['items']:
        tengwar = convert_text(hakka)
        names = tengwar_to_names(tengwar)
        print(f"  {hakka:12} {zh:4} {meaning:15} -> {tengwar}  ({names})")

    print()

    # Test numbers
    print(f"--- {NUMBERS['title']} ---")
    for hakka, zh, meaning in NUMBERS['items']:
        tengwar = convert_text(hakka)
        names = tengwar_to_names(tengwar)
        print(f"  {hakka:8} {zh} {meaning:6} -> {tengwar}  ({names})")

    print()

    # Test places
    print(f"--- {PLACES['title']} ---")
    for hakka, zh, meaning in PLACES['items']:
        tengwar = convert_text(hakka)
        print(f"  {hakka:15} {zh:4} {meaning:15} -> {tengwar}")

    print()

    # Final stops
    print("--- Final Stops (-b/-p, -d/-t, -g/-k) ---")
    stop_tests = [
        ('siib6', '十', 'ten (-b)'),
        ('id5', '一', 'one (-d)'),
        ('vug5', '屋', 'house (-g)'),
        ('liug5', '六', 'six (-g)'),
    ]
    for hakka, zh, meaning in stop_tests:
        tengwar = convert_text(hakka)
        names = tengwar_to_names(tengwar)
        print(f"  {hakka:8} {zh} {meaning:15} -> {tengwar}  ({names})")

    print()

    # Medial glides
    print("--- Medial Glides (ia, iu, ui, etc.) ---")
    glide_tests = [
        ('gia1', '', 'ia glide'),
        ('giu1', '', 'iu glide'),
        ('gui1', '', 'ui glide'),
        ('kiau1', '', 'iau triphthong'),
    ]
    for hakka, zh, meaning in glide_tests:
        tengwar = convert_text(hakka)
        names = tengwar_to_names(tengwar)
        print(f"  {hakka:8} {meaning:20} -> {tengwar}  ({names})")


if __name__ == '__main__':
    test_conversion()
