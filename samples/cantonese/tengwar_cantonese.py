#!/usr/bin/env python3
"""
Tengwar Cantonese Converter

Converts Jyutping (with tone numbers) to Tengwar Unicode for the Cantonese mode.
Uses Alcarin Tengwar codepoints (PUA U+E000-E0FF).

Based on the mapping in tengwar-cantonese.md:
- Grade 1 (single bow) = unaspirated
- Grade 2 (double bow) = aspirated
- Column I = alveolar, II = labial, III = velar
- Extended stems for alveolar affricates z/c
- W-curl diacritic for labialized velars gw/kw
- 6-tone system with register modifiers
"""

# === TENGWAR CODEPOINTS (Alcarin Tengwar) ===

# Base consonants - using codepoints from the spec
TENGWAR = {
    # Column I - Alveolar
    'tinco': '\ue001',      # Grade 1: Jyutping d /t/
    'ando': '\ue002',       # Grade 2: Jyutping t /tʰ/
    'thule': '\ue003',      # Grade 3: Jyutping s /s/
    'numen': '\ue005',      # Grade 5: Jyutping n /n/
    'lambe': '\ue026',      # Grade 6: Jyutping l /l/

    # Column II - Labial
    'parma': '\ue011',      # Grade 1: Jyutping b /p/
    'umbar': '\ue012',      # Grade 2: Jyutping p /pʰ/
    'formen': '\ue013',     # Grade 3: Jyutping f /f/
    'malta': '\ue015',      # Grade 5: Jyutping m /m/

    # Column III - Velar
    'calma': '\ue021',      # Grade 1: Jyutping g /k/
    'anga': '\ue022',       # Grade 2: Jyutping k /kʰ/
    'hwesta': '\ue023',     # Grade 3: Jyutping h /h/
    'noldo': '\ue025',      # Grade 5: Jyutping ng /ŋ/

    # Extended stem - Alveolar affricates
    'tinco_ext': '\ue009',  # Jyutping z /ts/
    'ando_ext': '\ue00a',   # Jyutping c /tsʰ/

    # Approximants/glides
    'anna': '\ue027',       # Glide /j/ (j-)
    'vala': '\ue02d',       # Glide /w/ (w-)

    # Carriers
    'carrier_short': '\ue02f',  # telco - zero initial
}

# Tehtar (vowel marks) - using codepoints from the spec
TEHTAR = {
    'aa': '\ue040',     # three dots above (long /a:/)
    'a': '\ue045',      # underdot (short /ɐ/)
    'e': '\ue046',      # acute stroke above
    'i': '\ue044',      # single dot above
    'o': '\ue048',      # left curl above
    'u': '\ue049',      # right curl above
}

# Combination vowels (will be rendered as multiple tehtar)
# oe /œ:/ = o-tehta + i-tehta
# eo /ɵ/ = u-tehta + underdot
# yu /y:/ = u-tehta + i-tehta

# W-curl diacritic for labialization (below tengwa)
W_CURL = '\ue06a'

# Tone marks - contour shapes (below-tengwa position)
TONE_CONTOUR = {
    'level': '\ue050',      # flat bar (high level, used for T1, T3, T6)
    'rising': '\ue046',     # acute stroke (rising, used for T2, T5)
    'falling': '\ue054',    # grave stroke (falling, used for T4)
}

# Register modifiers (below the contour mark)
REGISTER_MOD = {
    'high': None,           # no modifier
    'mid': '\ue045',        # single dot (unutixe-teng)
    'low': '\ue043',        # double dot (dotdblbelow-teng)
}

# Complete tone compositions
# Tone 1 (high level): flat bar only
# Tone 2 (high rising): rising stroke only
# Tone 3 (mid level): flat bar + single dot
# Tone 4 (low falling): falling stroke + double dot
# Tone 5 (low rising): rising stroke + double dot
# Tone 6 (low level): flat bar + double dot

def get_tone_marks(tone):
    """Return the tone mark sequence for a given tone number (1-6)."""
    if tone == 1:
        return TONE_CONTOUR['level']
    elif tone == 2:
        return TONE_CONTOUR['rising']
    elif tone == 3:
        return TONE_CONTOUR['level'] + REGISTER_MOD['mid']
    elif tone == 4:
        return TONE_CONTOUR['falling'] + REGISTER_MOD['low']
    elif tone == 5:
        return TONE_CONTOUR['rising'] + REGISTER_MOD['low']
    elif tone == 6:
        return TONE_CONTOUR['level'] + REGISTER_MOD['low']
    else:
        return ''  # No tone mark for invalid/missing tone


# === JYUTPING TO TENGWAR MAPPING ===

# Initial consonants
INITIALS = {
    # Labials
    'b': 'parma',
    'p': 'umbar',
    'm': 'malta',
    'f': 'formen',

    # Alveolars
    'd': 'tinco',
    't': 'ando',
    'n': 'numen',
    'l': 'lambe',

    # Velars
    'g': 'calma',
    'k': 'anga',
    'ng': 'noldo',
    'h': 'hwesta',

    # Labialized velars (special handling with w-curl)
    'gw': ('calma', True),   # + w-curl
    'kw': ('anga', True),    # + w-curl

    # Alveolar affricates (extended stem)
    'z': 'tinco_ext',
    'c': 'ando_ext',
    's': 'thule',

    # Glides
    'j': 'anna',
    'w': 'vala',
}

# Final consonants (codas)
FINALS = {
    # Nasal codas
    'm': 'malta',
    'n': 'numen',
    'ng': 'noldo',

    # Stop codas (use Grade 1 unaspirated forms)
    'p': 'parma',
    't': 'tinco',
    'k': 'calma',
}


def get_vowel_tehtar(vowel):
    """
    Return the tehtar sequence for a Cantonese vowel.

    Handles:
    - aa: long /a:/ -> a-tehta (three dots)
    - a: short /ɐ/ -> underdot
    - e: /ɛ:/ -> e-tehta
    - i: /i:/ -> i-tehta
    - o: /ɔ:/ -> o-tehta
    - u: /u:/ -> u-tehta
    - oe: front rounded /œ:/ -> o-tehta + i-tehta
    - eo: central rounded /ɵ/ -> u-tehta + underdot
    - yu: front rounded high /y:/ -> u-tehta + i-tehta
    """
    if vowel == 'aa':
        return TEHTAR['aa']
    elif vowel == 'a':
        return TEHTAR['a']
    elif vowel == 'e':
        return TEHTAR['e']
    elif vowel == 'i':
        return TEHTAR['i']
    elif vowel == 'o':
        return TEHTAR['o']
    elif vowel == 'u':
        return TEHTAR['u']
    elif vowel == 'oe':
        # Front rounded /œ:/ = o-tehta + i-tehta
        return TEHTAR['o'] + TEHTAR['i']
    elif vowel == 'eo':
        # Central rounded /ɵ/ = u-tehta + underdot
        return TEHTAR['u'] + TEHTAR['a']  # underdot is same as short 'a'
    elif vowel == 'yu':
        # Front rounded high /y:/ = u-tehta + i-tehta
        return TEHTAR['u'] + TEHTAR['i']
    else:
        return ''


def parse_jyutping_syllable(syllable):
    """
    Parse a Jyutping syllable into its components.

    Returns: (initial, labialized, vowel, coda, is_syllabic_nasal)

    Where:
    - initial: the initial consonant tengwa name (or None for null initial)
    - labialized: True if gw/kw (needs w-curl)
    - vowel: the vowel string (aa, a, e, i, o, u, oe, eo, yu)
    - coda: the coda consonant (m, n, ng, p, t, k) or None
    - is_syllabic_nasal: True if this is a syllabic nasal (m or ng only)
    """
    syllable = syllable.lower()
    pos = 0
    initial = None
    labialized = False
    is_syllabic_nasal = False

    # Check for syllabic nasals first (bare m or ng with no vowel)
    if syllable in ('m', 'ng'):
        return (INITIALS[syllable], False, None, None, True)

    # Parse initial consonant
    # Check three-letter initials first (none in standard Jyutping)
    # Check two-letter initials
    if syllable[pos:pos+2] in ('ng', 'gw', 'kw'):
        init_key = syllable[pos:pos+2]
        init_data = INITIALS[init_key]
        if isinstance(init_data, tuple):
            initial, labialized = init_data
        else:
            initial = init_data
        pos += 2
    elif syllable[pos:pos+1] in INITIALS:
        init_data = INITIALS[syllable[pos]]
        if isinstance(init_data, tuple):
            initial, labialized = init_data
        else:
            initial = init_data
        pos += 1
    # else: null initial

    # Remaining is the final (vowel + optional coda)
    final = syllable[pos:]

    # Parse vowel and coda
    # Vowel patterns to check (longest first):
    # - Diphthongs: aai, aau, aam, aan, aang, aap, aat, aak
    #               ai, au, ei, eoi, eon, eot, iu, oi, ou, ui
    # - Long vowels with codas: oeng, oek, yun, yut
    # - Simple: aa, oe, eo, yu, a, e, i, o, u

    vowel = None
    coda = None

    # Check for compound vowels first
    if final.startswith('aa'):
        vowel = 'aa'
        coda_part = final[2:]
    elif final.startswith('oe'):
        vowel = 'oe'
        coda_part = final[2:]
    elif final.startswith('eo'):
        vowel = 'eo'
        coda_part = final[2:]
    elif final.startswith('yu'):
        vowel = 'yu'
        coda_part = final[2:]
    elif final.startswith('a'):
        vowel = 'a'
        coda_part = final[1:]
    elif final.startswith('e'):
        vowel = 'e'
        coda_part = final[1:]
    elif final.startswith('i'):
        vowel = 'i'
        coda_part = final[1:]
    elif final.startswith('o'):
        vowel = 'o'
        coda_part = final[1:]
    elif final.startswith('u'):
        vowel = 'u'
        coda_part = final[1:]
    else:
        coda_part = final

    # Parse coda (after consuming diphthong offglides)
    # Diphthong offglides: i, u (these are not written as separate tengwar)
    # Nasal/stop codas: m, n, ng, p, t, k

    # First, consume any diphthong offglide (i or u following the nucleus)
    if coda_part.startswith('i') and len(coda_part) >= 1:
        # Check if this is diphthong offglide or just vowel
        # Offglide if followed by nothing or by a coda
        if len(coda_part) == 1:
            # Just an offglide, no coda
            coda_part = ''
        elif coda_part[1:] in ('m', 'n', 'ng', 'p', 't', 'k'):
            # Offglide followed by coda
            coda_part = coda_part[1:]
    elif coda_part.startswith('u') and len(coda_part) >= 1:
        if len(coda_part) == 1:
            coda_part = ''
        elif coda_part[1:] in ('m', 'n', 'ng', 'p', 't', 'k'):
            coda_part = coda_part[1:]

    # Now parse actual coda
    if coda_part == 'ng':
        coda = 'ng'
    elif coda_part in ('m', 'n', 'p', 't', 'k'):
        coda = coda_part
    # else: no coda or already consumed

    return (initial, labialized, vowel, coda, is_syllabic_nasal)


def jyutping_to_tengwar(syllable, tone=None):
    """
    Convert a single Jyutping syllable to Tengwar.

    Args:
        syllable: Jyutping syllable (e.g., 'gong', 'hoeng', 'sik')
        tone: Tone number 1-6 (None = no tone mark)

    Returns:
        Tengwar Unicode string
    """
    result = []

    initial, labialized, vowel, coda, is_syllabic_nasal = parse_jyutping_syllable(syllable)

    # === Handle syllabic nasals ===
    if is_syllabic_nasal:
        result.append(TENGWAR[initial])
        if tone:
            result.append(get_tone_marks(tone))
        return ''.join(result)

    # === Add initial tengwa ===
    if initial:
        result.append(TENGWAR[initial])
        if labialized:
            result.append(W_CURL)
    else:
        # Zero initial - use carrier
        result.append(TENGWAR['carrier_short'])

    # === Add medial glide for labiovelar initials ===
    # For gw-/kw- syllables, add vala between initial and vowel
    if labialized:
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


def parse_numbered_jyutping(text):
    """
    Parse Jyutping with tone numbers (e.g., 'nei5 hou2') into syllables.

    Returns list of (syllable, tone) tuples.
    """
    import re
    syllables = []
    # Match syllable + optional tone number
    pattern = r"([a-zA-Z]+)([1-6])?"
    for match in re.finditer(pattern, text):
        syl = match.group(1).lower()
        tone = int(match.group(2)) if match.group(2) else None
        syllables.append((syl, tone))
    return syllables


def convert_text(jyutping_text):
    """
    Convert a full Jyutping text (with tone numbers) to Tengwar.
    """
    syllables = parse_numbered_jyutping(jyutping_text)
    return ''.join(jyutping_to_tengwar(syl, tone) for syl, tone in syllables)


# === REVERSE LOOKUP FOR DEBUGGING ===

# Note: Some codepoints serve multiple purposes (e.g., U+E046 is both e-tehta and rising tone)
# The debug output may show the same glyph with different names depending on context
_CODEPOINT_NAMES = {v: k for k, v in TENGWAR.items()}
_CODEPOINT_NAMES.update({
    TEHTAR['aa']: '[aa]',
    TEHTAR['a']: '[a/.]',  # underdot = short a = mid register dot (dual purpose)
    TEHTAR['e']: '[e/rise]',  # acute = e-tehta = rising tone (dual purpose)
    TEHTAR['i']: '[i]',
    TEHTAR['o']: '[o]',
    TEHTAR['u']: '[u]',
    W_CURL: '+w',
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
            if name.startswith('['):  # vowel tehta
                result.append(name)
            elif name.startswith('+') or name.startswith('.'):  # modifier
                result.append(name)
            elif name in ('_', '/', '\\'):  # tone contour
                result.append(name)
            else:  # consonant
                result.append('{' + name + '}')
        else:
            result.append(f'?{ord(c):04X}')
    return ''.join(result)


# === SAMPLE TEXTS ===

SAMPLES = {
    'jyut_gwong_gwong': {
        'title_zh': '月光光',
        'title_en': 'Moonlight Bright',
        'note': 'Traditional Cantonese nursery rhyme',
        'jyutping': [
            'jyut6 gwong1 gwong1',
            'ziu3 dei6 tong4',
            'ha1 zi2 nei5 hok6 haang4',
            'a3 je4 caang1 ceoi4 zaang1',
        ],
        'chinese': [
            '月光光',
            '照地堂',
            '蝦仔你學行',
            '阿爺撐船撐',
        ],
        'translation': [
            'Moonlight bright, bright',
            'Shines on the hall floor',
            'Little shrimp, you learn to walk',
            'Grandpa poles the boat',
        ],
    },

    'dai_neoi_faa': {
        'title_zh': '帝女花',
        'title_en': 'Princess Changping',
        'note': 'From the famous Cantonese opera',
        'jyutping': [
            'lok6 faa1 mun5 tin1 fei1',
            'mung4 ceoi4 jyu5 maan4 maan4',
        ],
        'chinese': [
            '落花滿天飛',
            '夢隨雨漫漫',
        ],
        'translation': [
            'Falling petals fill the sky',
            'Dreams drift with the endless rain',
        ],
    },

    'si1_zi2_saan1_haa6': {
        'title_zh': '獅子山下',
        'title_en': 'Below Lion Rock',
        'note': 'Theme song of classic Hong Kong TV series (1979)',
        'jyutping': [
            'jan4 saang1 zung1 jau5 fun1 hei2',
            'naan4 min5 jik1 soeng4 jau5 ci3',
            'ngaa5 mun4 daai6 gaa1',
            'hai2 si1 zi2 saan1 haa6 seong1 jyu6 seong5 zaap6',
        ],
        'chinese': [
            '人生中有歡喜',
            '難免亦常有淚',
            '我哋大家',
            '喺獅子山下相遇上集',
        ],
        'translation': [
            'In life there is joy',
            'Inevitably there are often tears',
            'All of us together',
            'Meet below Lion Rock',
        ],
    },

    'hoi2_fut3_tin1_hung1': {
        'title_zh': '海闊天空',
        'title_en': 'Boundless Oceans, Vast Skies',
        'note': 'Beyond (band), 1993',
        'jyutping': [
            'gam1 tin1 ngo5',
            'hon6 laang5 jyu5 piu1 gwo3',
            'jyun4 loeng6 zi6 jau4',
            'jing4 jyun5 paau3 hoi1 sai3 cuk1',
        ],
        'chinese': [
            '今天我',
            '寒冷雨飄過',
            '原諒自由',
            '仍願拋開世俗',
        ],
        'translation': [
            'Today I',
            'Cold rain drifts by',
            'Forgive freedom',
            'Still willing to cast off worldly conventions',
        ],
    },
}

GREETINGS = {
    'title': 'Common Greetings',
    'items': [
        ('nei5 hou2', '你好', 'Hello'),
        ('zou2 san4', '早晨', 'Good morning'),
        ('ng5 on1', '午安', 'Good afternoon'),
        ('maan5 on1', '晚安', 'Good night'),
        ('baai1 baai3', '拜拜', 'Bye bye'),
        ('zoi3 gin3', '再見', 'Goodbye'),
        ('do1 ze6', '多謝', 'Thank you (for gifts)'),
        ('m4 goi1', '唔該', 'Thank you (for service)'),
        ('deoi3 m4 zyu6', '對唔住', 'Sorry'),
        ('mou5 man6 tai4', '冇問題', 'No problem'),
    ],
}

NUMBERS = {
    'title': 'Numbers 1-10',
    'items': [
        ('jat1', '一', 'one'),
        ('ji6', '二', 'two'),
        ('saam1', '三', 'three'),
        ('sei3', '四', 'four'),
        ('ng5', '五', 'five'),
        ('luk6', '六', 'six'),
        ('cat1', '七', 'seven'),
        ('baat3', '八', 'eight'),
        ('gau2', '九', 'nine'),
        ('sap6', '十', 'ten'),
    ],
}

PLACES = {
    'title': 'Hong Kong Place Names',
    'items': [
        ('hoeng1 gong2', '香港', 'Hong Kong'),
        ('gau2 lung4', '九龍', 'Kowloon'),
        ('san1 gaai3', '新界', 'New Territories'),
        ('zung1 waan4', '中環', 'Central'),
        ('gam1 zung1', '金鐘', 'Admiralty'),
        ('waan1 zai2', '灣仔', 'Wan Chai'),
        ('zim1 saa1 zeoi2', '尖沙咀', 'Tsim Sha Tsui'),
        ('wong4 gok3', '旺角', 'Mong Kok'),
        ('gwong2 zau1', '廣州', 'Guangzhou (Canton)'),
        ('ou3 mun4', '澳門', 'Macau'),
    ],
}

TONE_DEMO = {
    'title': 'Six Tones of Cantonese (si)',
    'items': [
        ('si1', '詩', 'poem (high level)'),
        ('si2', '史', 'history (high rising)'),
        ('si3', '試', 'try (mid level)'),
        ('si4', '時', 'time (low falling)'),
        ('si5', '市', 'market (low rising)'),
        ('si6', '事', 'matter (low level)'),
    ],
}

FOOD = {
    'title': 'Food and Dim Sum',
    'items': [
        ('dim2 sam1', '點心', 'dim sum'),
        ('haa1 gaau2', '蝦餃', 'shrimp dumpling'),
        ('siu1 maai6', '燒賣', 'siu mai'),
        ('caa4 siu1 baau1', '叉燒包', 'BBQ pork bun'),
        ('caang4 fan2', '腸粉', 'rice noodle roll'),
        ('zuk1', '粥', 'congee'),
        ('naai5 caa4', '奶茶', 'milk tea'),
    ],
}


def test_conversion():
    """Test the converter with sample syllables and texts."""
    print("=== Tengwar Cantonese Converter Demo ===\n")

    # Test basic tones
    print("Six tones of 'si' (showing tengwar + debug names):")
    for jyut, zh, meaning in TONE_DEMO['items']:
        tengwar = convert_text(jyut)
        names = tengwar_to_names(tengwar)
        print(f"  {jyut:5} {zh} {meaning:25} -> {tengwar}  ({names})")

    print()

    # Test vowel contrasts
    print("Vowel contrasts:")
    vowel_tests = [
        ('saam1', '三', 'three (long aa)'),
        ('sam1', '心', 'heart (short a)'),
        ('soeng2', '想', 'think (oe vowel)'),
        ('seon3', '信', 'letter (eo vowel)'),
        ('syu1', '書', 'book (yu vowel)'),
    ]
    for jyut, zh, meaning in vowel_tests:
        tengwar = convert_text(jyut)
        names = tengwar_to_names(tengwar)
        print(f"  {jyut:8} {zh} {meaning:25} -> {tengwar}  ({names})")

    print()

    # Test final stops
    print("Final stops (entering tones):")
    stop_tests = [
        ('sap6', '十', 'ten (-p)'),
        ('baat3', '八', 'eight (-t)'),
        ('baak3', '百', 'hundred (-k)'),
        ('sik6', '食', 'eat (-k)'),
    ]
    for jyut, zh, meaning in stop_tests:
        tengwar = convert_text(jyut)
        names = tengwar_to_names(tengwar)
        print(f"  {jyut:8} {zh} {meaning:25} -> {tengwar}  ({names})")

    print()

    # Test labialized velars
    print("Labialized velars (gw-, kw-):")
    labvel_tests = [
        ('gwaa1', '瓜', 'melon'),
        ('kwaa1', '誇', 'boast'),
        ('gwok3', '國', 'country'),
        ('gwan1', '君', 'lord'),
    ]
    for jyut, zh, meaning in labvel_tests:
        tengwar = convert_text(jyut)
        names = tengwar_to_names(tengwar)
        print(f"  {jyut:8} {zh} {meaning:15} -> {tengwar}  ({names})")

    print()

    # Test syllabic nasals
    print("Syllabic nasals:")
    nasal_tests = [
        ('m4', '唔', 'not'),
        ('ng5', '五', 'five'),
    ]
    for jyut, zh, meaning in nasal_tests:
        tengwar = convert_text(jyut)
        names = tengwar_to_names(tengwar)
        print(f"  {jyut:8} {zh} {meaning:15} -> {tengwar}  ({names})")

    print()

    # Test greetings
    print(f"--- {GREETINGS['title']} ---")
    for jyut, zh, meaning in GREETINGS['items'][:5]:
        tengwar = convert_text(jyut)
        print(f"  {jyut:20} {zh:8} {meaning:20} -> {tengwar}")

    print()

    # Test numbers
    print(f"--- {NUMBERS['title']} ---")
    for jyut, zh, meaning in NUMBERS['items']:
        tengwar = convert_text(jyut)
        print(f"  {jyut:8} {zh} {meaning:6} -> {tengwar}")

    print()

    # Test places
    print(f"--- {PLACES['title']} ---")
    for jyut, zh, meaning in PLACES['items'][:5]:
        tengwar = convert_text(jyut)
        print(f"  {jyut:20} {zh:4} {meaning:20} -> {tengwar}")

    print()

    # Test a full poem
    print("--- 月光光 (Moonlight Bright) ---")
    sample = SAMPLES['jyut_gwong_gwong']
    for i, line in enumerate(sample['jyutping']):
        tengwar = convert_text(line)
        print(f"  {sample['chinese'][i]}")
        print(f"  {line}")
        print(f"  {tengwar}")
        print()


if __name__ == '__main__':
    test_conversion()
