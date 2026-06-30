#!/usr/bin/env python3
"""
Tengwar Southern Min (Hokkien) Converter

Converts Tai-lo or POJ romanization (with tone numbers) to Tengwar Unicode.
Uses Alcarin Tengwar codepoints (PUA U+E000-E0FF).

CRITICAL: Min mode uses CLASSICAL Tengwar voicing semantics (same as Wu):

    | Grade | Mandarin/Cantonese | Min (this mode)     |
    |-------|-------------------|---------------------|
    | 1     | voiceless unasp.  | voiceless unasp.    |
    | 2     | voiceless ASP.    | VOICED              |
    | 3     | fricative         | voiceless fricative |
    | asp   | (uses Grade 2)    | DIACRITIC U+E070    |

Based on the Min mode specification:
- Grade 1 (single bow) = voiceless unaspirated (p, t, k, ts)
- Grade 2 (double bow) = VOICED (b, g, j)
- Grade 3 = voiceless fricatives only (s, h)
- Aspiration = diacritic U+E070 (ph, th, kh, tsh)
- Extended stems for alveolar affricates ts/tsh/j
- Nasal vowels marked with tilde-below diacritic
- 7-tone system with register modifiers
- Glottal stop final (-h) using halla

This mode is INCOMPATIBLE with Mandarin/Cantonese modes.
A document must declare which mode applies.
"""

import re

# === TENGWAR CODEPOINTS (Alcarin Tengwar) ===

TENGWAR = {
    # Column I - Alveolar
    # Grade 1 = voiceless unaspirated, Grade 2 = VOICED (classical semantics)
    'tinco': '\ue001',      # Grade 1: t /t/ voiceless unaspirated
    'ando': '\ue002',       # Grade 2: (not used for stops in Min)
    'thule': '\ue003',      # Grade 3: s /s/ voiceless fricative
    'numen': '\ue005',      # Grade 5: n /n/ nasal
    'lambe': '\ue026',      # Grade 6: l /l/ lateral

    # Column II - Labial
    'parma': '\ue011',      # Grade 1: p /p/ voiceless unaspirated
    'umbar': '\ue012',      # Grade 2: b /b/ VOICED
    'formen': '\ue013',     # Grade 3: (not used for stops)
    'malta': '\ue015',      # Grade 5: m /m/ nasal

    # Column III - Velar
    'calma': '\ue021',      # Grade 1: k /k/ voiceless unaspirated
    'anga': '\ue022',       # Grade 2: g /g/ VOICED
    'hwesta': '\ue023',     # Grade 3: h /h/ voiceless fricative
    'noldo': '\ue025',      # Grade 5: ng /ŋ/ nasal

    # Extended stem - Alveolar affricates
    # Grade 1 = voiceless unaspirated, Grade 2 = VOICED
    'tinco_ext': '\ue009',  # Grade 1: ts /ts/ voiceless unaspirated
    'ando_ext': '\ue00a',   # Grade 2: j /dz~z/ VOICED

    # Glottal and glides
    'halla': '\ue029',      # h /h/ initial, also /-ʔ/ final (glottal stop)
    'anna': '\ue027',       # Glide /j/
    'vala': '\ue02d',       # Glide /w/

    # Carrier
    'telco': '\ue02e',      # Zero initial carrier
}

# Tehtar (vowel marks)
TEHTAR = {
    'a': '\ue040',      # three dots above /a/
    'e': '\ue046',      # acute stroke above /e/
    'i': '\ue044',      # single dot above /i/
    'o': '\ue048',      # left curl above /o/
    'oo': '\ue048\ue045',  # o-tehta + underdot for /ɔ/ (open-mid back)
    'u': '\ue049',      # right curl above /u/
}

# Nasal vowel marker (tilde-below)
# Note: Using U+E051 as placeholder since U+E044 conflicts with i-tehta
# This should be the dedicated tilde-below glyph in the font
NASAL_MARK = '\ue051'

# Aspiration diacritic (classical voicing mode)
# Used for aspirated stops: ph, th, kh, tsh (not for voiced)
ASPIRATION_MARK = '\ue070'

# Tone contour marks (below-tengwa position)
TONE_CONTOUR = {
    'level': '\ue050',      # flat bar
    'rising': '\ue046',     # acute stroke
    'falling': '\ue054',    # grave stroke
}

# Register modifiers (below the contour mark)
REGISTER_MOD = {
    'high': '',             # no modifier
    'mid': '\ue045',        # single dot
    'low': '\ue043',        # double dot
}

# Complete tone mark compositions for Min's 7 tones
# T1 (44~55, high level): flat bar
# T2 (51~53, high falling): falling stroke
# T3 (21~31, low falling): falling stroke + double-dot
# T4 (32, low checked): unmarked (implied by final stop)
# T5 (24~13, rising): rising stroke
# T7 (33~22, mid level): flat bar + single dot
# T8 (4~5, high checked): flat bar (distinguishes from unmarked T4)

def get_tone_marks(tone, is_checked=False):
    """
    Return the tone mark sequence for a given tone number (1-8).

    For checked syllables (T4/T8), the final stop implies checked quality.
    T4 is unmarked, T8 gets flat bar to indicate high pitch.
    """
    if tone == 1:
        return TONE_CONTOUR['level']
    elif tone == 2:
        return TONE_CONTOUR['falling']
    elif tone == 3:
        return TONE_CONTOUR['falling'] + REGISTER_MOD['low']
    elif tone == 4:
        # Low checked - unmarked (final stop implies checked)
        return ''
    elif tone == 5:
        return TONE_CONTOUR['rising']
    elif tone == 7:
        return TONE_CONTOUR['level'] + REGISTER_MOD['mid']
    elif tone == 8:
        # High checked - flat bar to distinguish from T4
        return TONE_CONTOUR['level']
    else:
        return ''


# === TAI-LO / POJ MAPPING ===

# Initial consonants (Tai-lo romanization)
# Format: 'romanization': (tengwa_name, is_aspirated)
# Classical voicing: Grade 1 = voiceless unasp, Grade 2 = voiced, asp = diacritic
INITIALS = {
    # Labials - three-way contrast
    'p': ('parma', False),      # voiceless unaspirated (Grade 1)
    'ph': ('parma', True),      # voiceless aspirated (Grade 1 + asp)
    'b': ('umbar', False),      # voiced (Grade 2)
    'm': ('malta', False),      # nasal

    # Alveolars - three-way contrast
    't': ('tinco', False),      # voiceless unaspirated (Grade 1)
    'th': ('tinco', True),      # voiceless aspirated (Grade 1 + asp)
    'n': ('numen', False),      # nasal
    'l': ('lambe', False),      # lateral

    # Velars - three-way contrast
    'k': ('calma', False),      # voiceless unaspirated (Grade 1)
    'kh': ('calma', True),      # voiceless aspirated (Grade 1 + asp)
    'g': ('anga', False),       # voiced (Grade 2)
    'ng': ('noldo', False),     # nasal

    # Alveolar affricates - three-way contrast
    'ts': ('tinco_ext', False), # voiceless unaspirated (Grade 1)
    'tsh': ('tinco_ext', True), # voiceless aspirated (Grade 1 + asp)
    'j': ('ando_ext', False),   # voiced (Grade 2)
    's': ('thule', False),      # voiceless fricative (Grade 3)

    # Glottal
    'h': ('halla', False),      # voiceless fricative
}

# POJ to Tai-lo consonant conversions
POJ_TO_TAILO_INITIALS = {
    'ch': 'ts',
    'chh': 'tsh',
}

# Final consonants (codas)
FINALS = {
    # Nasal codas
    'm': 'malta',
    'n': 'numen',
    'ng': 'noldo',

    # Stop codas (unreleased)
    'p': 'parma',
    't': 'tinco',
    'k': 'calma',

    # Glottal stop coda (written -h in Tai-lo)
    'h': 'halla',
}

# Checked syllable finals (trigger T4/T8)
CHECKED_FINALS = {'p', 't', 'k', 'h'}


def normalize_to_tailo(syllable):
    """
    Normalize POJ romanization to Tai-lo.

    POJ differences:
    - ch -> ts, chh -> tsh
    - o (dotted) -> oo (we accept both as 'oo')
    - superscript n -> nn
    - oa -> ua, oe -> ue
    """
    s = syllable.lower()

    # Consonant conversions
    s = re.sub(r'^chh', 'tsh', s)
    s = re.sub(r'^ch', 'ts', s)

    # Vowel conversions (POJ -> Tai-lo)
    s = s.replace('oa', 'ua')
    s = s.replace('oe', 'ue')

    # Handle superscript nasal (POJ uses Unicode superscript n or trailing 'n' for nasalization)
    # Convert to Tai-lo 'nn' doubling
    s = s.replace('\u207f', 'nn')  # Unicode superscript n

    return s


def parse_syllable(syllable):
    """
    Parse a Tai-lo syllable into components.

    Returns: {
        'initial': tengwa name or None,
        'is_aspirated': True if aspirated consonant,
        'medial': 'i' or 'u' or None (for glides before main vowel),
        'vowel': vowel string,
        'nasal_vowel': True if nasalized,
        'coda': coda consonant or None,
        'is_checked': True if ends in stop,
        'is_syllabic_nasal': True if syllabic m/ng
    }
    """
    s = normalize_to_tailo(syllable)
    result = {
        'initial': None,
        'is_aspirated': False,
        'medial': None,
        'vowel': None,
        'nasal_vowel': False,
        'coda': None,
        'is_checked': False,
        'is_syllabic_nasal': False,
    }

    pos = 0

    # Check for syllabic nasals (bare m or ng with no vowel)
    if s in ('m', 'ng'):
        tengwa, is_asp = INITIALS[s]
        result['initial'] = tengwa
        result['is_aspirated'] = is_asp
        result['is_syllabic_nasal'] = True
        return result

    # Parse initial consonant (longest match first)
    for init in ['tsh', 'ts', 'th', 'ph', 'kh', 'ng', 'ch', 'chh',
                 'p', 'b', 'm', 't', 'n', 'l', 'k', 'g', 's', 'h', 'j']:
        if s.startswith(init):
            if init in INITIALS:
                tengwa, is_asp = INITIALS[init]
                result['initial'] = tengwa
                result['is_aspirated'] = is_asp
            pos = len(init)
            break

    remainder = s[pos:]

    # Check for medial glide (i or u before another vowel)
    # Rising diphthongs: ia, io, iu, ua, ue, ui
    if len(remainder) >= 2:
        if remainder[0] == 'i' and remainder[1] in 'aou':
            result['medial'] = 'i'
            remainder = remainder[1:]
        elif remainder[0] == 'u' and remainder[1] in 'aei':
            result['medial'] = 'u'
            remainder = remainder[1:]

    # Parse vowel and check for nasalization (nn suffix)
    # Vowels: a, e, i, o, oo, u
    # Nasal vowels: ann, enn, inn, onn, unn (or with tilde in input)

    vowel = ''
    nasal = False

    # Check for 'oo' first
    if remainder.startswith('oo'):
        vowel = 'oo'
        remainder = remainder[2:]
    elif remainder and remainder[0] in 'aeiou':
        vowel = remainder[0]
        remainder = remainder[1:]

    # Check for nasalization marker (nn)
    if remainder.startswith('nn'):
        nasal = True
        remainder = remainder[2:]
    # Also check for single 'n' followed by another 'n' (POJ style)

    result['vowel'] = vowel
    result['nasal_vowel'] = nasal

    # Handle falling diphthong offglides (ai, au, etc.)
    # These are implied in the vowel tehta, not written separately
    if remainder and remainder[0] in 'iu':
        # Check if this is an offglide (followed by nothing or nasal marker or coda)
        if len(remainder) == 1:
            remainder = ''  # Just an offglide
        elif remainder[1:].startswith('nn'):
            nasal = True
            result['nasal_vowel'] = True
            remainder = remainder[1:]  # Remove offglide, keep nn
            remainder = remainder[2:]  # Remove nn
        elif remainder[1:] and remainder[1] in 'mnptkh':
            remainder = remainder[1:]  # Remove offglide, keep coda

    # Parse coda
    if remainder.startswith('ng'):
        result['coda'] = 'ng'
        remainder = remainder[2:]
    elif remainder and remainder[0] in 'mnptkh':
        result['coda'] = remainder[0]
        remainder = remainder[1:]

    # Check if checked syllable
    if result['coda'] in CHECKED_FINALS:
        result['is_checked'] = True

    return result


def convert_syllable(syllable, tone=None):
    """
    Convert a single Tai-lo/POJ syllable to Tengwar.

    Args:
        syllable: Romanized syllable (e.g., 'lang', 'sann', 'tshit')
        tone: Tone number 1-8 (None = no tone mark)

    Returns:
        Tengwar Unicode string
    """
    parsed = parse_syllable(syllable)
    result = []

    # Handle syllabic nasals
    if parsed['is_syllabic_nasal']:
        result.append(TENGWAR[parsed['initial']])
        if parsed['is_aspirated']:
            result.append(ASPIRATION_MARK)
        if tone:
            result.append(get_tone_marks(tone))
        return ''.join(result)

    # Add initial tengwa
    if parsed['initial']:
        result.append(TENGWAR[parsed['initial']])
        # Add aspiration diacritic if aspirated (classical voicing mode)
        if parsed['is_aspirated']:
            result.append(ASPIRATION_MARK)
    else:
        # Zero initial - use carrier
        result.append(TENGWAR['telco'])

    # Add medial glide tengwa
    if parsed['medial'] == 'i':
        result.append(TENGWAR['anna'])
    elif parsed['medial'] == 'u':
        result.append(TENGWAR['vala'])

    # Add vowel tehta
    if parsed['vowel']:
        if parsed['vowel'] in TEHTAR:
            result.append(TEHTAR[parsed['vowel']])
        elif parsed['vowel'] == 'oo':
            result.append(TEHTAR['oo'])

    # Add nasal vowel marker (tilde-below)
    if parsed['nasal_vowel']:
        result.append(NASAL_MARK)

    # Add coda consonant
    if parsed['coda']:
        result.append(TENGWAR[FINALS[parsed['coda']]])

    # Add tone mark
    if tone:
        result.append(get_tone_marks(tone, parsed['is_checked']))

    return ''.join(result)


def parse_numbered_tailo(text):
    """
    Parse Tai-lo with tone numbers (e.g., 'gua2 si7 lang5').

    Returns list of (syllable, tone) tuples.
    """
    syllables = []
    # Match syllable + optional tone number (1-8)
    pattern = r"([a-zA-Zⁿ]+)([1-8])?"
    for match in re.finditer(pattern, text):
        syl = match.group(1)
        tone = int(match.group(2)) if match.group(2) else None
        syllables.append((syl, tone))
    return syllables


def convert_text(text):
    """
    Convert Tai-lo text (with tone numbers) to Tengwar.
    """
    syllables = parse_numbered_tailo(text)
    return ''.join(convert_syllable(syl, tone) for syl, tone in syllables)


# === DEBUG UTILITIES ===

_CODEPOINT_NAMES = {v: k for k, v in TENGWAR.items()}
# Note: U+E046 serves dual purpose as both e-tehta and rising tone mark.
# In the debug output, it will show as [e/rise] to indicate this ambiguity.
_CODEPOINT_NAMES.update({
    TEHTAR['a']: '[a]',
    TEHTAR['e']: '[e/rise]',  # dual purpose: e-tehta AND rising tone
    TEHTAR['i']: '[i]',
    TEHTAR['o']: '[o]',
    TEHTAR['u']: '[u]',
    '\ue045': '[./mid]',     # underdot (also mid register)
    NASAL_MARK: '[~]',       # nasal mark
    ASPIRATION_MARK: '+asp', # aspiration diacritic (classical voicing mode)
    TONE_CONTOUR['level']: '_',
    TONE_CONTOUR['falling']: '\\',
    REGISTER_MOD['low']: '..',
})


def tengwar_to_names(tengwar_str):
    """Convert Tengwar unicode to descriptive names for debugging."""
    result = []
    i = 0
    while i < len(tengwar_str):
        c = tengwar_str[i]
        # Check for oo-tehta (two-char sequence)
        if i + 1 < len(tengwar_str) and tengwar_str[i:i+2] == TEHTAR['oo']:
            result.append('[oo]')
            i += 2
            continue

        name = _CODEPOINT_NAMES.get(c)
        if name:
            if name.startswith('[') or name.startswith('+'):
                result.append(name)
            elif name in ('_', '\\', '..'):
                result.append(name)
            else:
                result.append('{' + name + '}')
        else:
            result.append(f'?{ord(c):04X}')
        i += 1
    return ''.join(result)


# === SAMPLE DATA ===

TONE_DEMO = {
    'title': 'Seven Tones of Hokkien (su)',
    'items': [
        ('su1', '書', 'book (T1 high level)'),
        ('su2', '輸', 'lose (T2 high falling)'),
        ('su3', '四', 'four (T3 low falling)'),
        ('su5', '樹', 'tree (T5 rising)'),
        ('su7', '數', 'count (T7 mid level)'),
        # Checked tones require final stop
        ('sut4', '術', 'skill (T4 low checked)'),
        ('sut8', '實', 'real (T8 high checked)'),
    ],
}

NASAL_VOWEL_DEMO = {
    'title': 'Nasal Vowels',
    'items': [
        ('sann1', '三', 'three (nasal a)'),
        ('phinn7', '鼻', 'nose (nasal i)'),
        ('tinn1', '甜', 'sweet (nasal i)'),
        ('kinn3', '見', 'see (nasal i)'),
        ('hinn7', '耳', 'ear (nasal i)'),
        ('honn2', '好?', 'yes? (nasal o)'),
    ],
}

THREE_WAY_CONTRAST = {
    'title': 'Three-Way Laryngeal Contrast (Classical Voicing)',
    'note': 'Grade 1 = voiceless unasp, Grade 2 = VOICED, asp = diacritic',
    'items': [
        # Labial triad: /p/ vs /ph/ vs /b/
        ('pa1', '巴', '/p/ voiceless unasp (parma)'),
        ('pha1', '帕', '/ph/ aspirated (parma+asp)'),
        ('ba2', '馬', '/b/ voiced (umbar)'),
        # Velar triad: /k/ vs /kh/ vs /g/
        ('ka1', '家', '/k/ voiceless unasp (calma)'),
        ('kha1', '腳', '/kh/ aspirated (calma+asp)'),
        ('ga5', '牙', '/g/ voiced (anga)'),
        # Affricate triad: /ts/ vs /tsh/ vs /dz/
        ('tsa1', '查', '/ts/ voiceless unasp (tinco-ext)'),
        ('tsha1', '叉', '/tsh/ aspirated (tinco-ext+asp)'),
        ('ja5', '蛇', '/dz/ voiced (ando-ext)'),
    ],
}

GLOTTAL_STOP = {
    'title': 'Glottal Stop Final (-h)',
    'items': [
        ('oh4', '學', 'learn'),
        ('tah4', '踏', 'step on'),
        ('peh8', '白', 'white'),
        ('koh4', '閣', 'more'),
        ('tsiah8', '食', 'eat'),
    ],
}

STOP_CODAS = {
    'title': 'Stop Codas (-p, -t, -k)',
    'items': [
        ('tap4', '答', 'answer (-p)'),
        ('pat4', '八', 'eight (-t)'),
        ('pak4', '北', 'north (-k)'),
        ('sit8', '實', 'real (-t)'),
        ('hok8', '福', 'blessing (-k)'),
    ],
}

GREETINGS = {
    'title': 'Common Expressions',
    'items': [
        ('li2 ho2', '你好', 'Hello'),
        ('gua2 si7 lang5', '我是人', 'I am a person'),
        ('tsia1 pn7', '食飯', 'eat rice'),
        ('to1 sia7', '多謝', 'thank you'),
        ('bo5 tai7 tsi3', '無代誌', 'no problem'),
    ],
}

PLACES = {
    'title': 'Place Names',
    'items': [
        ('tai5 uan5', '台灣', 'Taiwan'),
        ('tai5 pak4', '台北', 'Taipei'),
        ('tai5 lam5', '台南', 'Tainan'),
        ('ko1 hiong5', '高雄', 'Kaohsiung'),
        ('hok4 kian3', '福建', 'Fujian'),
    ],
}


def demo():
    """Run demonstration of the converter."""
    print("=" * 70)
    print("TENGWAR SOUTHERN MIN (HOKKIEN) CONVERTER DEMO")
    print("=" * 70)
    print()
    print("CRITICAL: Min mode uses CLASSICAL Tengwar voicing semantics:")
    print()
    print("    | Grade | Mandarin/Cantonese | Min (this mode)     |")
    print("    |-------|-------------------|---------------------|")
    print("    | 1     | voiceless unasp.  | voiceless unasp.    |")
    print("    | 2     | voiceless ASP.    | VOICED              |")
    print("    | 3     | fricative         | voiceless fricative |")
    print("    | asp   | (uses Grade 2)    | DIACRITIC U+E070    |")
    print()

    # Three-way laryngeal contrast (most important demo)
    print("-" * 70)
    print(f"1. {THREE_WAY_CONTRAST['title']}")
    print(f"   ({THREE_WAY_CONTRAST['note']})")
    print("-" * 70)
    for tailo, zh, meaning in THREE_WAY_CONTRAST['items']:
        tengwar = convert_text(tailo)
        names = tengwar_to_names(tengwar)
        print(f"  {tailo:8} {zh} {meaning:35} -> {tengwar}  ({names})")
    print()

    # Tone demonstration
    print("-" * 70)
    print(f"2. {TONE_DEMO['title']}")
    print("-" * 70)
    for tailo, zh, meaning in TONE_DEMO['items']:
        tengwar = convert_text(tailo)
        names = tengwar_to_names(tengwar)
        print(f"  {tailo:8} {zh} {meaning:30} -> {tengwar}  ({names})")
    print()

    # Nasal vowels
    print("-" * 70)
    print(f"3. {NASAL_VOWEL_DEMO['title']}")
    print("-" * 70)
    for tailo, zh, meaning in NASAL_VOWEL_DEMO['items']:
        tengwar = convert_text(tailo)
        names = tengwar_to_names(tengwar)
        print(f"  {tailo:10} {zh} {meaning:25} -> {tengwar}  ({names})")
    print()

    # Glottal stop
    print("-" * 70)
    print(f"4. {GLOTTAL_STOP['title']}")
    print("-" * 70)
    for tailo, zh, meaning in GLOTTAL_STOP['items']:
        tengwar = convert_text(tailo)
        names = tengwar_to_names(tengwar)
        print(f"  {tailo:10} {zh} {meaning:15} -> {tengwar}  ({names})")
    print()

    # Stop codas
    print("-" * 70)
    print(f"5. {STOP_CODAS['title']}")
    print("-" * 70)
    for tailo, zh, meaning in STOP_CODAS['items']:
        tengwar = convert_text(tailo)
        names = tengwar_to_names(tengwar)
        print(f"  {tailo:8} {zh} {meaning:20} -> {tengwar}  ({names})")
    print()

    # Greetings
    print("-" * 70)
    print(f"6. {GREETINGS['title']}")
    print("-" * 70)
    for tailo, zh, meaning in GREETINGS['items']:
        tengwar = convert_text(tailo)
        print(f"  {tailo:20} {zh:10} {meaning:15} -> {tengwar}")
    print()

    # Places
    print("-" * 70)
    print(f"7. {PLACES['title']}")
    print("-" * 70)
    for tailo, zh, meaning in PLACES['items']:
        tengwar = convert_text(tailo)
        print(f"  {tailo:15} {zh:4} {meaning:15} -> {tengwar}")
    print()

    # Syllabic nasals
    print("-" * 70)
    print("8. Syllabic Nasals")
    print("-" * 70)
    syllabic = [
        ('m7', '唔', 'not'),
        ('ng5', '黃', 'yellow'),
    ]
    for tailo, zh, meaning in syllabic:
        tengwar = convert_text(tailo)
        names = tengwar_to_names(tengwar)
        print(f"  {tailo:8} {zh} {meaning:15} -> {tengwar}  ({names})")
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
    print("  | Grade | Mandarin/Cantonese | Min (this mode) |")
    print("  |-------|-------------------|-----------------|")
    print("  | 1     | voiceless unasp.  | voiceless unasp.|")
    print("  | 2     | voiceless ASP.    | VOICED          |")
    print("  | 3     | fricative         | voiceless fric. |")
    print("  | asp   | (uses Grade 2)    | DIACRITIC U+E070|")
    print()


if __name__ == '__main__':
    demo()
