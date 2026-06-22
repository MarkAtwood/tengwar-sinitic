#!/usr/bin/env python3
"""
Tengwar Wu (Shanghainese) Converter

Converts Qian Nairong romanization (with tone numbers) to Tengwar Unicode
for the Wu (Shanghainese) mode.

Uses Alcarin Tengwar codepoints (PUA U+E000-E0FF).

CRITICAL: Wu mode uses DIFFERENT grade semantics than Mandarin/Cantonese:

    | Grade | Mandarin/Cantonese | Wu (this mode)      |
    |-------|-------------------|---------------------|
    | 1     | voiceless unasp.  | voiceless unasp.    |
    | 2     | voiceless ASP.    | VOICED              |
    | 3     | fricative         | voiceless fricative |
    | asp   | (uses Grade 2)    | DIACRITIC U+E070    |

This mode uses CLASSICAL Tengwar voicing semantics:
- Grade 1: voiceless unaspirated (b/d/g/z/j = /p, t, k, ts, tc/)
- Grade 2: voiced (bb/dd/gg/zz/jj = /b, d, g, dz, dz/)
- Aspiration = diacritic U+E070 (p/t/k/c/q = /ph, th, kh, tsh, tch/)

This mode is INCOMPATIBLE with Mandarin/Cantonese modes.
A document must declare which mode applies.

Qian Nairong romanization:
- bb, dd, gg = voiced stops
- b, d, g = voiceless unaspirated stops
- p, t, k = voiceless aspirated stops
- Tones: 1-5 after syllable
"""

# === TENGWAR CODEPOINTS (Alcarin Tengwar) ===

TENGWAR = {
    # Column I - Alveolar
    # Grade 1 = voiceless unaspirated, Grade 2 = VOICED (not aspirated!)
    'tinco': '\ue001',      # Grade 1: d /t/ voiceless unaspirated
    'ando': '\ue002',       # Grade 2: dd /d/ VOICED
    'thule': '\ue003',      # Grade 3: s /s/ voiceless fricative
    'anto': '\ue004',       # Grade 4: ss /z/ voiced fricative
    'numen': '\ue005',      # Grade 5: n /n/ nasal
    'lambe': '\ue006',      # Grade 6: l /l/ lateral (spec: U+E006)

    # Column II - Labial
    'parma': '\ue011',      # Grade 1: b /p/ voiceless unaspirated
    'umbar': '\ue012',      # Grade 2: bb /b/ VOICED
    'formen': '\ue013',     # Grade 3: f /f/ voiceless fricative
    'ampa': '\ue014',       # Grade 4: v /v/ voiced fricative
    'malta': '\ue015',      # Grade 5: m /m/ nasal
    'vala': '\ue016',       # Glide /w/ (spec: U+E016)

    # Column III - Velar/Glottal
    'calma': '\ue021',      # Grade 1: g /k/ voiceless unaspirated
    'anga': '\ue022',       # Grade 2: gg /g/ VOICED
    'hwesta': '\ue023',     # Grade 3: h /h~x/ voiceless fricative
    'unque': '\ue024',      # Grade 4: gh /H/ voiced glottal fricative
    'noldo': '\ue025',      # Grade 5: ng /N/ velar nasal (initial in Wu!)

    # Extended stem - Alveolar affricates (spec: U+E061/U+E062)
    'tinco_ext': '\ue061',  # z /ts/ voiceless unaspirated affricate
    'ando_ext': '\ue062',   # zz /dz/ voiced affricate

    # Approximants/glides (spec: U+E036)
    'anna': '\ue036',       # Glide /j/ (initial y, medial i-)

    # Carriers and special (spec: U+E030)
    'telco': '\ue030',      # Zero initial carrier

    # Glottal stop coda (spec: U+E028)
    'halla': '\ue028',      # -q /-P/ glottal stop (from historical *-p, *-t, *-k)
}

# Aspiration diacritic (new for Wu mode)
ASPIRATION_MARK = '\ue070'

# Palatal diacritic (below tengwa)
PALATAL_MARK = '\ue06b'

# Tehtar (vowel marks) - spec codepoints
VOWELS = {
    'a': '\ue040',      # three dots (a-tehta) /a/
    'o': '\ue04c',      # left curl (o-tehta) /o/ (spec: U+E04C)
    'e': '\ue046',      # acute stroke (e-tehta) /e/
    'i': '\ue044',      # single dot (i-tehta) /i/
    'u': '\ue04a',      # right curl (u-tehta) /u/ (spec: U+E04A)
    'oe': '\ue045',     # underdot /ə/ (schwa)
}

# Combined vowels
# y /y/ (front rounded high) = u-tehta + i-tehta

# Alias for backward compatibility
TEHTAR = VOWELS.copy()
TEHTAR['aa'] = VOWELS['a']   # long a same glyph
TEHTAR['ee'] = VOWELS['e']   # long e same glyph
TEHTAR['eu'] = VOWELS['o']   # eu diphthong uses o-tehta
TEHTAR['y'] = VOWELS['u'] + VOWELS['i']  # u+i for /y/

# Tone marks - contour shapes (below-tengwa position)
TONE_CONTOUR = {
    'level': '\ue050',      # flat bar
    'rising': '\ue046',     # acute stroke
    'falling': '\ue054',    # grave stroke
}

# Register modifiers (below the contour mark)
REGISTER_MOD = {
    'high': None,           # no modifier (implicit)
    'mid': '\ue045',        # single dot
    'low': '\ue043',        # double dot
}


def get_tone_marks(tone):
    """
    Return the tone mark sequence for a Shanghainese tone (1-5).

    Shanghainese tones:
    - T1 (53, high falling): falling stroke
    - T2 (31, low falling): falling stroke + double-dot
    - T3 (55, high level): flat bar
    - T4 (34, mid rising): rising stroke + single-dot
    - T5 (13, low rising): rising stroke + double-dot
    """
    if tone == 1:
        return TONE_CONTOUR['falling']
    elif tone == 2:
        return TONE_CONTOUR['falling'] + REGISTER_MOD['low']
    elif tone == 3:
        return TONE_CONTOUR['level']
    elif tone == 4:
        return TONE_CONTOUR['rising'] + REGISTER_MOD['mid']
    elif tone == 5:
        return TONE_CONTOUR['rising'] + REGISTER_MOD['low']
    else:
        return ''


# === WU ROMANIZATION TO TENGWAR MAPPING ===

# Initial consonants using Qian Nairong romanization
# Note: bb/dd/gg = voiced, b/d/g = voiceless unasp, p/t/k = voiceless asp
INITIALS = {
    # Labials
    'b': ('parma', False, False),       # /p/ voiceless unasp
    'p': ('parma', False, True),        # /ph/ voiceless asp
    'bb': ('umbar', False, False),      # /b/ voiced
    'm': ('malta', False, False),       # /m/
    'f': ('formen', False, False),      # /f/
    'v': ('ampa', False, False),        # /v/

    # Alveolars
    'd': ('tinco', False, False),       # /t/ voiceless unasp
    't': ('tinco', False, True),        # /th/ voiceless asp
    'dd': ('ando', False, False),       # /d/ voiced
    'n': ('numen', False, False),       # /n/
    'l': ('lambe', False, False),       # /l/

    # Velars
    'g': ('calma', False, False),       # /k/ voiceless unasp
    'k': ('calma', False, True),        # /kh/ voiceless asp
    'gg': ('anga', False, False),       # /g/ voiced
    'ng': ('noldo', False, False),      # /N/
    'h': ('hwesta', False, False),      # /h~x/
    'gh': ('unque', False, False),      # /G/ voiced velar fricative

    # Alveolar sibilants
    's': ('thule', False, False),       # /s/
    'ss': ('anto', False, False),       # /z/ voiced
    'z': ('tinco_ext', False, False),   # /ts/ voiceless unasp
    'c': ('tinco_ext', False, True),    # /tsh/ voiceless asp
    'zz': ('ando_ext', False, False),   # /dz/ voiced

    # Alveolo-palatals (velar + palatal mark)
    'j': ('calma', True, False),        # /tc/ voiceless unasp
    'q': ('calma', True, True),         # /tch/ voiceless asp
    'jj': ('anga', True, False),        # /dz/ voiced affricate
    'x': ('hwesta', True, False),       # /c/ voiceless fricative
    'xx': ('unque', True, False),       # /z/ voiced fricative
    'zzy': ('ando_ext', True, False),   # alternate spelling for voiced pal
    'gn': ('noldo', True, False),       # /n/ palatal nasal

    # Glides
    'y': ('anna', False, False),        # /j/
    'w': ('vala', False, False),        # /w/
}

# Final consonants (codas)
FINALS = {
    # Nasal coda (only one in Wu, realized as [n]~[N])
    'n': 'numen',
    'ng': 'noldo',

    # Glottal stop coda
    'q': 'halla',
}


def get_vowel_tehtar(vowel):
    """Return the tehtar sequence for a Wu vowel."""
    if vowel in TEHTAR:
        return TEHTAR[vowel]
    return ''


def parse_wu_syllable(syllable):
    """
    Parse a Qian Nairong Wu syllable into components.

    Returns: (initial_tengwa, is_palatal, is_aspirated, medial, vowel, coda)
    """
    syllable = syllable.lower()
    pos = 0
    initial = None
    is_palatal = False
    is_aspirated = False

    # Check multi-letter initials first (longest match)
    for length in [3, 2, 1]:
        candidate = syllable[pos:pos+length]
        if candidate in INITIALS:
            initial, is_palatal, is_aspirated = INITIALS[candidate]
            pos += length
            break

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
    elif rime.startswith('y') and len(rime) > 1 and rime[1] in 'ae':
        medial = 'y'
        rime = rime[1:]

    # Parse vowel and coda
    vowel = None
    coda = None

    # Check for vowel sequences (longest match first)
    # oe = schwa, aa/ee = long vowels, eu = diphthong
    if rime.startswith('oe'):
        vowel = 'oe'
        coda_part = rime[2:]
    elif rime.startswith('aa'):
        vowel = 'aa'
        coda_part = rime[2:]
    elif rime.startswith('ee'):
        vowel = 'ee'
        coda_part = rime[2:]
    elif rime.startswith('eu'):
        vowel = 'eu'
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
    elif rime.startswith('y'):
        vowel = 'y'  # /y/ rounded front vowel
        coda_part = rime[1:]
    else:
        coda_part = rime

    # Consume diphthong offglides
    if coda_part.startswith('i') or coda_part.startswith('u'):
        if len(coda_part) == 1:
            coda_part = ''
        elif coda_part[1:] in ('n', 'ng', 'q'):
            coda_part = coda_part[1:]

    # Parse coda
    if coda_part == 'ng':
        coda = 'ng'
    elif coda_part in ('n', 'q'):
        coda = coda_part

    return (initial, is_palatal, is_aspirated, medial, vowel, coda)


def convert_syllable(syllable, tone=None):
    """
    Convert a single Wu syllable to Tengwar.

    Args:
        syllable: Wu romanization (e.g., 'zaanghe', 'bba', 'pa')
        tone: Tone number 1-5 (None = no tone mark)

    Returns:
        Tengwar Unicode string
    """
    result = []

    initial, is_palatal, is_aspirated, medial, vowel, coda = parse_wu_syllable(syllable)

    # === Add initial tengwa ===
    if initial:
        result.append(TENGWAR[initial])
        if is_palatal:
            result.append(PALATAL_MARK)
        if is_aspirated:
            result.append(ASPIRATION_MARK)
    else:
        # Zero initial - use carrier
        result.append(TENGWAR['telco'])

    # === Add medial glide ===
    if medial == 'i':
        result.append(TENGWAR['anna'])
    elif medial == 'u':
        result.append(TENGWAR['vala'])
    elif medial == 'y':
        # Rounded front glide - use anna with u-tehta?
        result.append(TENGWAR['anna'])

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


def parse_numbered_wu(text):
    """
    Parse Wu romanization with tone numbers (e.g., 'zaanghe3 nong2').

    Returns list of (syllable, tone) tuples.
    """
    import re
    syllables = []
    pattern = r"([a-zA-Z]+)([1-5])?"
    for match in re.finditer(pattern, text):
        syl = match.group(1).lower()
        tone = int(match.group(2)) if match.group(2) else None
        syllables.append((syl, tone))
    return syllables


def convert_text(wu_text):
    """
    Convert full Wu text (with tone numbers) to Tengwar.
    """
    syllables = parse_numbered_wu(wu_text)
    return ''.join(convert_syllable(syl, tone) for syl, tone in syllables)


# === REVERSE LOOKUP FOR DEBUGGING ===

# Build reverse lookup - note: some codepoints are shared
# (e-tehta U+E046 and rising tone U+E046 use same glyph)
_CODEPOINT_NAMES = {v: k for k, v in TENGWAR.items()}
_CODEPOINT_NAMES.update({
    VOWELS['a']: '[a]',
    VOWELS['e']: '[e/rise]',   # e-tehta shares glyph with rising tone
    VOWELS['i']: '[i]',
    VOWELS['o']: '[o]',
    VOWELS['u']: '[u]',
    VOWELS['oe']: '[oe/.]',    # schwa shares glyph with mid register dot
    PALATAL_MARK: '+pal',
    ASPIRATION_MARK: '+asp',
    TONE_CONTOUR['level']: '_',        # flat bar = T3
    TONE_CONTOUR['falling']: '\\',     # falling = T1 or T2
    REGISTER_MOD['low']: '..',         # low register (double dot)
})


def tengwar_to_names(tengwar_str):
    """Convert tengwar unicode to descriptive names for debugging."""
    result = []
    for c in tengwar_str:
        name = _CODEPOINT_NAMES.get(c)
        if name:
            if name.startswith('[') or name.startswith('+'):
                result.append(name)
            elif name in ('_', '\\', '/', '..', '.'):
                result.append(name)
            else:
                result.append('{' + name + '}')
        else:
            result.append(f'?{ord(c):04X}')
    return ''.join(result)


# === SAMPLE DATA ===

# Demonstrating Wu's three-way laryngeal contrast
VOICING_CONTRAST = {
    'title': 'Three-Way Laryngeal Contrast (Minimal Triads)',
    'note': 'Wu preserves voiced stops/affricates that Mandarin lost',
    'items': [
        # Labial triad: /p/ vs /ph/ vs /b/
        ('ba3', '/pa/', 'eight (voiceless unaspirated)'),
        ('pa3', '/pha/', 'afraid (voiceless aspirated)'),
        ('bba2', '/ba/', 'to pull (voiced)'),
        # Alveolar triad: /t/ vs /th/ vs /d/
        ('da3', '/ta/', 'to hit (voiceless unaspirated)'),
        ('ta3', '/tha/', 'he/she (voiceless aspirated)'),
        ('dda2', '/da/', 'big (voiced)'),
        # Velar triad: /k/ vs /kh/ vs /g/
        ('ga3', '/ka/', 'family (voiceless unaspirated)'),
        ('ka3', '/kha/', 'card (voiceless aspirated)'),
        ('gga2', '/ga/', 'price (voiced)'),
    ],
}

# Voiced fricatives - distinctive Wu feature (Grade 4)
VOICED_FRICATIVES = {
    'title': 'Voiced Fricatives (Grade 4)',
    'note': 'Wu has a complete voiced fricative series - rare among Sinitic',
    'items': [
        ('va1', '/va/', 'flower (ampa)'),
        ('ssi2', '/zi/', 'word (anto)'),
        ('gha2', '/Ha/', 'below (unque - voiced glottal)'),
        ('xxi2', '/zji/', 'two (unque+palatal)'),
    ],
}

# Affricate contrasts - three-way with aspiration diacritic
AFFRICATES = {
    'title': 'Affricate Contrasts (Three-way + Aspiration)',
    'note': 'Affricates: Grade 1 unasp, Grade 2 voiced, asp=diacritic',
    'items': [
        # Alveolar affricates: /ts/ vs /tsh/ vs /dz/
        ('za3', '/tsa/', 'to fry (tinco-ext)'),
        ('ca3', '/tsha/', 'fork (tinco-ext + asp)'),
        ('zza2', '/dza/', 'to sit (ando-ext)'),
        # Alveolo-palatal affricates: /tc/ vs /tch/ vs /dz/
        ('ji3', '/tci/', 'self (calma + pal)'),
        ('qi3', '/tchi/', 'seven (calma + pal + asp)'),
        ('jji2', '/dzi/', 'extreme (anga + pal)'),
    ],
}

# Five tones of Shanghainese
FIVE_TONES = {
    'title': 'Five Tones of Shanghainese',
    'note': 'Yin/yang register split with 5 citation tones',
    'items': [
        ('si1', '/si53/', 'T1: high falling = falling stroke'),
        ('zi2', '/zi31/', 'T2: low falling = falling + double-dot'),
        ('si3', '/si55/', 'T3: high level = flat bar'),
        ('si4', '/si34/', 'T4: mid rising = rising + single-dot'),
        ('zi5', '/zi13/', 'T5: low rising = rising + double-dot'),
    ],
}

# Glottal stop coda (checked syllables)
GLOTTAL_CODA = {
    'title': 'Glottal Stop Coda (Checked Syllables)',
    'note': 'Historical *-p, *-t, *-k merged to glottal stop /-q/ (halla)',
    'items': [
        ('baq', '/baP/', 'white (from *bak)'),
        ('seq', '/seP/', 'color (from *sek)'),
        ('goq', '/geP/', 'country (from *kok)'),
        ('siq', '/siP/', 'eat (from *dzik)'),
    ],
}

# The key Wu innovation: aspiration as diacritic
ASPIRATION_DEMO = {
    'title': 'Aspiration vs Voicing - Key Wu Distinction',
    'note': 'Grade 2 = voiced (NOT aspirated). Aspiration = diacritic U+E070',
    'items': [
        ('ba3', 'parma (Grade 1)', '/p/ voiceless unaspirated'),
        ('pa3', 'parma + asp', '/ph/ voiceless aspirated'),
        ('bba2', 'umbar (Grade 2)', '/b/ voiced'),
    ],
}

# Sample greetings
GREETINGS = {
    'title': 'Common Shanghainese Greetings',
    'items': [
        ('nong2 hau3', 'Hello (polite)'),
        ('za3 hau3', 'Good morning'),
        ('xia4 xia4', 'Thank you'),
        ('m2 sa2 se4', "You're welcome"),
        ('ze3 ve1', 'Goodbye'),
    ],
}

# Numbers 1-10
NUMBERS = {
    'title': 'Numbers 1-10',
    'items': [
        ('iq3', '1', 'one'),
        ('ni4', '2', 'two'),
        ('se1', '3', 'three'),
        ('si3', '4', 'four'),
        ('ng3', '5', 'five'),
        ('loq5', '6', 'six'),
        ('ciq3', '7', 'seven'),
        ('baq3', '8', 'eight'),
        ('jieu3', '9', 'nine'),
        ('seq5', '10', 'ten'),
    ],
}


def demo():
    """Comprehensive demonstration of the Wu Tengwar converter."""
    print("=" * 70)
    print("TENGWAR WU (SHANGHAINESE) CONVERTER DEMO")
    print("=" * 70)
    print()
    print("CRITICAL: Wu mode uses DIFFERENT grade semantics than other modes:")
    print()
    print("    | Grade | Mandarin/Cantonese | Wu (this mode)      |")
    print("    |-------|-------------------|---------------------|")
    print("    | 1     | voiceless unasp.  | voiceless unasp.    |")
    print("    | 2     | voiceless ASP.    | VOICED              |")
    print("    | 3     | fricative         | voiceless fricative |")
    print("    | asp   | (uses Grade 2)    | DIACRITIC U+E070    |")
    print()

    # 1. Three-way laryngeal contrast
    print("-" * 70)
    print(f"1. {VOICING_CONTRAST['title']}")
    print(f"   ({VOICING_CONTRAST['note']})")
    print("-" * 70)
    for rom, ipa, meaning in VOICING_CONTRAST['items']:
        tengwar = convert_text(rom)
        names = tengwar_to_names(tengwar)
        print(f"  {rom:8} {ipa:10} {meaning:35} -> {tengwar}  ({names})")
    print()

    # 2. Voiced fricatives (Grade 4)
    print("-" * 70)
    print(f"2. {VOICED_FRICATIVES['title']}")
    print(f"   ({VOICED_FRICATIVES['note']})")
    print("-" * 70)
    for rom, ipa, meaning in VOICED_FRICATIVES['items']:
        tengwar = convert_text(rom)
        names = tengwar_to_names(tengwar)
        print(f"  {rom:8} {ipa:10} {meaning:35} -> {tengwar}  ({names})")
    print()

    # 3. Affricates with aspiration
    print("-" * 70)
    print(f"3. {AFFRICATES['title']}")
    print(f"   ({AFFRICATES['note']})")
    print("-" * 70)
    for rom, ipa, meaning in AFFRICATES['items']:
        tengwar = convert_text(rom)
        names = tengwar_to_names(tengwar)
        print(f"  {rom:8} {ipa:10} {meaning:35} -> {tengwar}  ({names})")
    print()

    # 4. Five tones
    print("-" * 70)
    print(f"4. {FIVE_TONES['title']}")
    print(f"   ({FIVE_TONES['note']})")
    print("-" * 70)
    for rom, ipa, meaning in FIVE_TONES['items']:
        tengwar = convert_text(rom)
        names = tengwar_to_names(tengwar)
        print(f"  {rom:8} {ipa:10} {meaning}")
        print(f"           -> {tengwar}  ({names})")
    print()

    # 5. Glottal stop coda
    print("-" * 70)
    print(f"5. {GLOTTAL_CODA['title']}")
    print(f"   ({GLOTTAL_CODA['note']})")
    print("-" * 70)
    for rom, ipa, meaning in GLOTTAL_CODA['items']:
        tengwar = convert_text(rom)
        names = tengwar_to_names(tengwar)
        print(f"  {rom:8} {ipa:10} {meaning:35} -> {tengwar}  ({names})")
    print()

    # 6. Aspiration vs Voicing demo
    print("-" * 70)
    print(f"6. {ASPIRATION_DEMO['title']}")
    print(f"   ({ASPIRATION_DEMO['note']})")
    print("-" * 70)
    for rom, tengwa_desc, meaning in ASPIRATION_DEMO['items']:
        tengwar = convert_text(rom)
        names = tengwar_to_names(tengwar)
        print(f"  {rom:8} {tengwa_desc:20} {meaning}")
        print(f"           -> {tengwar}  ({names})")
    print()

    # 7. Greetings
    print("-" * 70)
    print(f"7. {GREETINGS['title']}")
    print("-" * 70)
    for rom, meaning in GREETINGS['items']:
        tengwar = convert_text(rom)
        print(f"  {rom:20} {meaning:20} -> {tengwar}")
    print()

    # 8. Numbers
    print("-" * 70)
    print(f"8. {NUMBERS['title']}")
    print("-" * 70)
    for rom, digit, meaning in NUMBERS['items']:
        tengwar = convert_text(rom)
        names = tengwar_to_names(tengwar)
        print(f"  {rom:8} {digit} {meaning:10} -> {tengwar}  ({names})")
    print()

    # Mode incompatibility notice
    print("=" * 70)
    print("MODE INCOMPATIBILITY NOTICE")
    print("=" * 70)
    print()
    print("This mode is NOT compatible with Mandarin/Cantonese modes.")
    print("A document must declare which mode applies.")
    print()
    print("Grade semantics comparison:")
    print("  | Grade | Mandarin/Cantonese | Wu (this mode) |")
    print("  |-------|-------------------|----------------|")
    print("  | 1     | voiceless unasp.  | voiceless unasp.|")
    print("  | 2     | voiceless ASP.    | VOICED          |")
    print("  | 3     | fricative         | voiceless fric. |")
    print("  | asp   | (uses Grade 2)    | DIACRITIC U+E070|")
    print()


if __name__ == '__main__':
    demo()
