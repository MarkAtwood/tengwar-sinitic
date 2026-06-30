#!/usr/bin/env python3
"""
Tengwar Mandarin Converter

Converts Pinyin (with tone numbers) to Tengwar Unicode for the Mandarin mode.
Uses Alcarin Tengwar codepoints (PUA U+E000-E0FF).

Based on the mapping in tengwar-mandarin.md:
- Grade 1 (single bow) = unaspirated
- Grade 2 (double bow) = aspirated
- Column I = alveolar, II = labial, III = retroflex, IV = velar
"""

# === TENGWAR CODEPOINTS (Alcarin Tengwar) ===

# Base consonants
TENGWAR = {
    # Column I - Alveolar
    'tinco': '\ue000',      # Grade 1: Pinyin d /t/
    'ando': '\ue004',       # Grade 2: Pinyin t /tʰ/
    'thuule': '\ue008',     # Grade 3: Pinyin s /s/
    'nuumen': '\ue010',     # Grade 5: Pinyin n /n/
    'lambe': '\ue022',      # Grade 6: Pinyin l /l/

    # Column II - Labial
    'parma': '\ue001',      # Grade 1: Pinyin b /p/
    'umbar': '\ue005',      # Grade 2: Pinyin p /pʰ/
    'formen': '\ue009',     # Grade 3: Pinyin f /f/
    'malta': '\ue011',      # Grade 5: Pinyin m /m/

    # Column III - Retroflex
    'calma': '\ue002',      # Grade 1: Pinyin zh /tʂ/
    'anga': '\ue006',       # Grade 2: Pinyin ch /tʂʰ/
    'hwesta': '\ue00b',     # Grade 3: Pinyin sh /ʂ/
    'oore': '\ue021',       # Grade 6: Pinyin r /ɻ/

    # Column IV - Velar
    'quesse': '\ue003',     # Grade 1: Pinyin g /k/
    'ungwe': '\ue007',      # Grade 2: Pinyin k /kʰ/
    'harma': '\ue00a',      # Grade 3: Pinyin h /x/
    'noldo': '\ue012',      # Grade 5: coda -ng /ŋ/

    # Extended stem - Alveolar affricates
    'tinco_ext': '\ue030',  # Pinyin z /ts/
    'ando_ext': '\ue031',   # Pinyin c /tsʰ/

    # Approximants/glides
    'anna': '\ue023',       # Glide /j/ (y-)
    'vala': '\ue025',       # Glide /w/ (w-)

    # Carriers
    'carrier_short': '\ue02e',  # telco - zero initial
    'carrier_long': '\ue02c',   # ára - for carrier-placement tones
}

# Tehtar (vowel marks) - placed above preceding consonant
TEHTAR = {
    'a': '\ue040',      # three dots (amatixe)
    'o': '\ue04a',      # right curl
    'e': '\ue046',      # acute stroke
    'i': '\ue044',      # single dot
    'u': '\ue04c',      # left curl
}

# Tone marks for below-tengwa placement
TONE_BELOW = {
    1: '\ue051',        # macronbelow-teng (high level) - upstream U+E051
    2: '\ue047',        # acutebelow-teng (rising) - upstream U+E047
    3: '\ue096',        # caronbelow-teng (dipping) - extended U+E096
    4: '\ue097',        # gravebelow-teng (falling) - extended U+E097
    # 5 (neutral): no mark
}

# Tone marks for carrier placement (tehta on telco)
TONE_CARRIER = {
    1: '\ue050',        # overbar (macron)
    2: '\ue046',        # acute
    3: '\ue040',        # three-dot (amatixe) for v-shape
    4: '\ue054',        # grave
}

# Palatal diacritic (double dot below)
PALATAL_MARK = '\ue043'  # dotdblbelow

# Reverse lookup: codepoint → name (for romanization output)
_CODEPOINT_NAMES = {v: k for k, v in TENGWAR.items()}
_CODEPOINT_NAMES.update({v: f'[{k}]' for k, v in TEHTAR.items()})  # vowels in brackets
_CODEPOINT_NAMES.update({
    TONE_BELOW[1]: '¹', TONE_BELOW[2]: '²', TONE_BELOW[3]: '³', TONE_BELOW[4]: '⁴',
    PALATAL_MARK: '+pal',
})

def tengwar_to_names(tengwar_str):
    """Convert tengwar unicode to romanized names like {malta}[a]´"""
    result = []
    for c in tengwar_str:
        name = _CODEPOINT_NAMES.get(c)
        if name:
            if name.startswith('['):  # vowel tehta
                result.append(name)
            elif len(name) <= 3:  # tone/modifier mark
                result.append(name)
            else:  # consonant
                result.append('{' + name + '}')
        else:
            result.append(f'?{ord(c):04X}')
    return ''.join(result)

# === PINYIN TO TENGWAR MAPPING ===

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
    'n': 'nuumen',
    'l': 'lambe',

    # Retroflexes (Column III)
    'zh': 'calma',
    'ch': 'anga',
    'sh': 'hwesta',
    'r': 'oore',

    # Velars (Column IV)
    'g': 'quesse',
    'k': 'ungwe',
    'h': 'harma',

    # Palatals (velar + palatal mark)
    'j': ('quesse', True),   # + palatal
    'q': ('ungwe', True),    # + palatal
    'x': ('harma', True),    # + palatal

    # Alveolar affricates (extended stem)
    'z': 'tinco_ext',
    'c': 'ando_ext',
    's': 'thuule',

    # Glides (when initial)
    'y': 'anna',
    'w': 'vala',
}

def pinyin_to_tengwar(syllable, tone=None, use_carrier_tones=False):
    """
    Convert a single Pinyin syllable to Tengwar.

    Args:
        syllable: Pinyin syllable (e.g., 'ma', 'zhong', 'nü')
        tone: Tone number 1-5 (5 or None = neutral)
        use_carrier_tones: If True, use carrier placement; else below-tengwa

    Returns:
        Tengwar Unicode string
    """
    result = []
    syllable = syllable.lower()
    pos = 0

    # === Parse initial ===
    initial = None
    palatal = False

    # Check two-letter initials first
    if syllable[pos:pos+2] in ('zh', 'ch', 'sh'):
        initial = INITIALS[syllable[pos:pos+2]]
        pos += 2
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

    # === Parse final (vowels + codas) ===
    final = syllable[pos:]

    # Handle medial glides
    if final.startswith('i') and len(final) > 1 and final[1] in 'aeo':
        # Medial /j/: ia, ie, io → anna + vowel
        result.append(TENGWAR['anna'])
        final = final[1:]
    elif final.startswith('u') and len(final) > 1 and final[1] in 'aeiïo':
        # Medial /w/: ua, uo, ui, uï, ue → vala + vowel
        result.append(TENGWAR['vala'])
        final = final[1:]
    elif final.startswith('ü') and len(final) > 1:
        # Medial /ɥ/: üe, üan → anna + palatal + vowel
        result.append(TENGWAR['anna'])
        result.append(PALATAL_MARK)
        final = final[1:]

    # Handle main vowel
    vowel_char = None
    if final:
        # Check for ü (written as v or ü)
        if final[0] in 'üv':
            # ü after l/n: write u + i tehtar
            result.append(TEHTAR['u'])
            result.append(TEHTAR['i'])
            final = final[1:]
        elif final[0] in TEHTAR:
            vowel_char = final[0]
            result.append(TEHTAR[vowel_char])
            final = final[1:]
        # Handle apical vowels (zi, ci, si, zhi, chi, shi, ri) - no vowel tehta
        # These are handled by having no vowel after sibilant/retroflex

    # Handle diphthongs - write only primary vowel, glide is implied
    # ao→a, ou→o, ai→a, ei→e (see spec: Diphthongs section)
    # This keeps one vowel mark above + one tone mark below per syllable
    if final.startswith(('i', 'u', 'o')) and vowel_char:
        final = final[1:]  # consume but don't write secondary vowel

    # Handle codas
    if final == 'n':
        result.append(TENGWAR['nuumen'])
    elif final == 'ng':
        result.append(TENGWAR['noldo'])
    elif final == 'r':
        # Erhua
        result.append(TENGWAR['oore'])

    # === Add tone mark ===
    if tone and tone != 5:
        if use_carrier_tones:
            # Append carrier with tone tehta
            result.append(TENGWAR['carrier_short'])
            result.append(TONE_CARRIER[tone])
        else:
            # Below-tengwa placement
            result.append(TONE_BELOW[tone])

    return ''.join(result)


def parse_numbered_pinyin(text):
    """
    Parse Pinyin with tone numbers (e.g., 'ni3 hao3') into syllables.

    Returns list of (syllable, tone) tuples.
    """
    import re
    syllables = []
    # Match syllable + optional tone number
    pattern = r"([a-züïA-ZÜÏ]+)([1-5])?"
    for match in re.finditer(pattern, text):
        syl = match.group(1).lower()
        tone = int(match.group(2)) if match.group(2) else 5
        syllables.append((syl, tone))
    return syllables


def convert_text(pinyin_text, use_carrier_tones=False):
    """
    Convert a full Pinyin text (with tone numbers) to Tengwar.
    """
    syllables = parse_numbered_pinyin(pinyin_text)
    return ''.join(pinyin_to_tengwar(syl, tone, use_carrier_tones)
                   for syl, tone in syllables)


# === SAMPLE TEXTS ===

SAMPLES = {
    'jing_ye_si': {
        'title_zh': '静夜思',
        'title_en': 'Quiet Night Thought',
        'author': '李白 (Li Bai, 701-762)',
        'pinyin': [
            'chuang2 qian2 ming2 yue4 guang1',
            'yi2 shi4 di4 shang4 shuang1',
            'ju3 tou2 wang4 ming2 yue4',
            'di1 tou2 si1 gu4 xiang1',
        ],
        'chinese': [
            '床前明月光',
            '疑是地上霜',
            '举头望明月',
            '低头思故乡',
        ],
        'translation': [
            'Before my bed, bright moonlight',
            'I thought it was frost on the ground',
            'Raising my head, I gaze at the bright moon',
            'Lowering my head, I think of my homeland',
        ],
    },

    'chun_xiao': {
        'title_zh': '春晓',
        'title_en': 'Spring Dawn',
        'author': '孟浩然 (Meng Haoran, 689-740)',
        'pinyin': [
            'chun1 mian2 bu4 jue2 xiao3',
            'chu4 chu4 wen2 ti2 niao3',
            'ye4 lai2 feng1 yu3 sheng1',
            'hua1 luo4 zhi1 duo1 shao3',
        ],
        'chinese': [
            '春眠不觉晓',
            '处处闻啼鸟',
            '夜来风雨声',
            '花落知多少',
        ],
        'translation': [
            'Spring slumber, unaware of dawn',
            'Everywhere, I hear birds singing',
            'Last night came sounds of wind and rain',
            'How many blossoms have fallen?',
        ],
    },

    'deng_guanque_lou': {
        'title_zh': '登鹳雀楼',
        'title_en': 'Climbing Stork Tower',
        'author': '王之涣 (Wang Zhihuan, 688-742)',
        'pinyin': [
            'bai2 ri4 yi1 shan1 jin4',
            'huang2 he2 ru4 hai3 liu2',
            'yu4 qiong2 qian1 li3 mu4',
            'geng4 shang4 yi1 ceng2 lou2',
        ],
        'chinese': [
            '白日依山尽',
            '黄河入海流',
            '欲穷千里目',
            '更上一层楼',
        ],
        'translation': [
            'The white sun sets behind the mountains',
            'The Yellow River flows into the sea',
            'To see a thousand miles further',
            'Climb one more floor',
        ],
    },

    'min_nong': {
        'title_zh': '悯农',
        'title_en': 'Pitying the Farmers',
        'author': '李绅 (Li Shen, 772-846)',
        'pinyin': [
            'chu2 he2 ri4 dang1 wu3',
            'han4 di1 he2 xia4 tu3',
            'shui2 zhi1 pan2 zhong1 can1',
            'li4 li4 jie1 xin1 ku3',
        ],
        'chinese': [
            '锄禾日当午',
            '汗滴禾下土',
            '谁知盘中餐',
            '粒粒皆辛苦',
        ],
        'translation': [
            'Hoeing grain under the midday sun',
            'Sweat drips onto the soil beneath',
            'Who knows that the meal in the bowl',
            'Every grain comes from bitter toil',
        ],
    },

    'yong_e': {
        'title_zh': '咏鹅',
        'title_en': 'Ode to the Goose',
        'author': '骆宾王 (Luo Binwang, 619-687)',
        'pinyin': [
            'e2 e2 e2',
            'qu1 xiang4 xiang4 tian1 ge1',
            'bai2 mao2 fu2 lü4 shui3',
            'hong2 zhang3 bo1 qing1 bo1',
        ],
        'chinese': [
            '鹅鹅鹅',
            '曲项向天歌',
            '白毛浮绿水',
            '红掌拨清波',
        ],
        'translation': [
            'Goose, goose, goose',
            'Curved neck singing to the sky',
            'White feathers floating on green water',
            'Red feet paddling the clear waves',
        ],
    },

    'xiang_si': {
        'title_zh': '相思',
        'title_en': 'Longing',
        'author': '王维 (Wang Wei, 699-759)',
        'pinyin': [
            'hong2 dou4 sheng1 nan2 guo2',
            'chun1 lai2 fa1 ji3 zhi1',
            'yuan4 jun1 duo1 cai3 xie2',
            'ci3 wu4 zui4 xiang1 si1',
        ],
        'chinese': [
            '红豆生南国',
            '春来发几枝',
            '愿君多采撷',
            '此物最相思',
        ],
        'translation': [
            'Red beans grow in the southern lands',
            'When spring comes, how many branches bloom?',
            'I wish you would gather many',
            'For this thing evokes the deepest longing',
        ],
    },

    'feng_qiao_ye_bo': {
        'title_zh': '枫桥夜泊',
        'title_en': 'Mooring at Night by Maple Bridge',
        'author': '张继 (Zhang Ji, 715-779)',
        'pinyin': [
            'yue4 luo4 wu1 ti2 shuang1 man3 tian1',
            'jiang1 feng1 yu2 huo3 dui4 chou2 mian2',
            'gu1 su1 cheng2 wai4 han2 shan1 si4',
            'ye4 ban4 zhong1 sheng1 dao4 ke4 chuan2',
        ],
        'chinese': [
            '月落乌啼霜满天',
            '江枫渔火对愁眠',
            '姑苏城外寒山寺',
            '夜半钟声到客船',
        ],
        'translation': [
            'Moon sets, crows cry, frost fills the sky',
            'River maples, fishing fires—sleeping in sorrow',
            'Outside Suzhou, Cold Mountain Temple',
            'Midnight bell reaches the traveler\'s boat',
        ],
    },

    'you_zi_yin': {
        'title_zh': '游子吟',
        'title_en': 'Song of the Wandering Son',
        'author': '孟郊 (Meng Jiao, 751-814)',
        'pinyin': [
            'ci2 mu3 shou3 zhong1 xian4',
            'you2 zi3 shen1 shang4 yi1',
            'lin2 xing2 mi4 mi4 feng2',
            'yi4 kong3 chi2 chi2 gui1',
            'shui2 yan2 cun4 cao3 xin1',
            'bao4 de2 san1 chun1 hui1',
        ],
        'chinese': [
            '慈母手中线',
            '游子身上衣',
            '临行密密缝',
            '意恐迟迟归',
            '谁言寸草心',
            '报得三春晖',
        ],
        'translation': [
            'The thread in a loving mother\'s hand',
            'Becomes the clothes on the wanderer\'s back',
            'Before he leaves, stitch after stitch',
            'Fearing his return will be long delayed',
            'Who says the heart of an inch of grass',
            'Can repay the radiance of three springs?',
        ],
    },
}

# Additional practical texts
PRACTICAL = {
    'greetings': {
        'title': 'Common Greetings',
        'items': [
            ('ni3 hao3', '你好', 'Hello'),
            ('zao3 shang4 hao3', '早上好', 'Good morning'),
            ('wan3 an1', '晚安', 'Good night'),
            ('xie4 xie4', '谢谢', 'Thank you'),
            ('bu2 ke4 qi4', '不客气', 'You\'re welcome'),
            ('dui4 bu4 qi3', '对不起', 'Sorry'),
            ('mei2 guan1 xi4', '没关系', 'It\'s okay'),
            ('zai4 jian4', '再见', 'Goodbye'),
        ],
    },

    'numbers': {
        'title': 'Numbers 1-10',
        'items': [
            ('yi1', '一', 'one'),
            ('er4', '二', 'two'),
            ('san1', '三', 'three'),
            ('si4', '四', 'four'),
            ('wu3', '五', 'five'),
            ('liu4', '六', 'six'),
            ('qi1', '七', 'seven'),
            ('ba1', '八', 'eight'),
            ('jiu3', '九', 'nine'),
            ('shi2', '十', 'ten'),
        ],
    },

    'places': {
        'title': 'Place Names',
        'items': [
            ('bei3 jing1', '北京', 'Beijing'),
            ('shang4 hai3', '上海', 'Shanghai'),
            ('guang3 zhou1', '广州', 'Guangzhou'),
            ('xi1 an1', '西安', 'Xi\'an'),
            ('cheng2 du1', '成都', 'Chengdu'),
            ('chang2 jiang1', '长江', 'Yangtze River'),
            ('huang2 he2', '黄河', 'Yellow River'),
            ('tai4 shan1', '泰山', 'Mount Tai'),
            ('zhong1 guo2', '中国', 'China'),
        ],
    },

    'chengyu': {
        'title': 'Four-Character Idioms (Chengyu)',
        'items': [
            ('yi1 xin1 yi1 yi4', '一心一意', 'wholeheartedly'),
            ('wan4 shi4 ru2 yi4', '万事如意', 'may all go as you wish'),
            ('xue2 wu2 zhi3 jing4', '学无止境', 'learning has no limits'),
            ('ren2 shan1 ren2 hai3', '人山人海', 'huge crowds'),
            ('feng1 he2 ri4 li4', '风和日丽', 'gentle breeze, beautiful day'),
            ('long2 fei1 feng4 wu3', '龙飞凤舞', 'lively and vigorous (calligraphy)'),
        ],
    },

    'tongue_twisters': {
        'title': 'Tongue Twisters',
        'items': [
            ('si4 shi4 si4 shi2 shi4 shi2', '四是四十是十', 'Four is four, ten is ten'),
            ('chi1 pu2 tao2 bu4 tu3 pu2 tao2 pi2', '吃葡萄不吐葡萄皮',
             'Eat grapes without spitting grape skins'),
        ],
    },
}


if __name__ == '__main__':
    # Demo output
    print("=== Tengwar Mandarin Converter Demo ===\n")

    # Test basic conversion
    test_syllables = ['ma1', 'ma2', 'ma3', 'ma4', 'ma5']
    print("Tones of 'ma':")
    for syl in test_syllables:
        parsed = parse_numbered_pinyin(syl)
        tengwar = pinyin_to_tengwar(parsed[0][0], parsed[0][1])
        print(f"  {syl}: {tengwar}")

    print("\n静夜思 (Quiet Night Thought):")
    for line in SAMPLES['jing_ye_si']['pinyin']:
        tengwar = convert_text(line)
        print(f"  {tengwar}")
