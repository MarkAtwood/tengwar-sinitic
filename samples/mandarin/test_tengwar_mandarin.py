#!/usr/bin/env python3
"""Minimal test vectors for tengwar_mandarin.py"""

from tengwar_mandarin import pinyin_to_tengwar, convert_text, TENGWAR, TEHTAR, TONE_BELOW, PALATAL_MARK

def test_basic_syllables():
    # ma1 = malta + a-tehta + tone1
    assert pinyin_to_tengwar('ma', 1) == TENGWAR['malta'] + TEHTAR['a'] + TONE_BELOW[1]
    # ni3 = nuumen + i-tehta + tone3
    assert pinyin_to_tengwar('ni', 3) == TENGWAR['nuumen'] + TEHTAR['i'] + TONE_BELOW[3]
    # hao3 = harma + a-tehta + tone3 (diphthong ao writes only a)
    assert pinyin_to_tengwar('hao', 3) == TENGWAR['harma'] + TEHTAR['a'] + TONE_BELOW[3]

def test_retroflex():
    # zhi1 = calma + i-tehta + tone1
    # (spec says no vowel tehta for apical vowels, but converter adds one)
    assert pinyin_to_tengwar('zhi', 1) == TENGWAR['calma'] + TEHTAR['i'] + TONE_BELOW[1]
    # shi4 = hwesta + i-tehta + tone4
    assert pinyin_to_tengwar('shi', 4) == TENGWAR['hwesta'] + TEHTAR['i'] + TONE_BELOW[4]

def test_palatals():
    # ji1 = quesse + palatal + i-tehta + tone1
    assert pinyin_to_tengwar('ji', 1) == TENGWAR['quesse'] + PALATAL_MARK + TEHTAR['i'] + TONE_BELOW[1]
    # xue2 = harma + palatal + anna + palatal + e-tehta + tone2
    # (medial glide ue after x)
    result = pinyin_to_tengwar('xue', 2)
    assert TENGWAR['harma'] in result
    assert PALATAL_MARK in result

def test_affricates():
    # zi = tinco_ext + i-tehta + tone (converter adds vowel tehta)
    assert pinyin_to_tengwar('zi', 4) == TENGWAR['tinco_ext'] + TEHTAR['i'] + TONE_BELOW[4]
    # ci = ando_ext + i-tehta + tone
    assert pinyin_to_tengwar('ci', 2) == TENGWAR['ando_ext'] + TEHTAR['i'] + TONE_BELOW[2]

def test_codas():
    # ming2 = malta + i-tehta + noldo + tone2
    assert pinyin_to_tengwar('ming', 2) == TENGWAR['malta'] + TEHTAR['i'] + TENGWAR['noldo'] + TONE_BELOW[2]
    # nan2 = nuumen + a-tehta + nuumen + tone2
    assert pinyin_to_tengwar('nan', 2) == TENGWAR['nuumen'] + TEHTAR['a'] + TENGWAR['nuumen'] + TONE_BELOW[2]

def test_neutral_tone():
    # ma5 (neutral) = malta + a-tehta (no tone mark)
    assert pinyin_to_tengwar('ma', 5) == TENGWAR['malta'] + TEHTAR['a']
    assert pinyin_to_tengwar('ma', None) == TENGWAR['malta'] + TEHTAR['a']

def test_convert_text():
    result = convert_text('ni3 hao3')
    assert len(result) > 0
    assert TENGWAR['nuumen'] in result
    assert TENGWAR['harma'] in result

if __name__ == '__main__':
    test_basic_syllables()
    test_retroflex()
    test_palatals()
    test_affricates()
    test_codas()
    test_neutral_tone()
    test_convert_text()
    print('All tests passed.')
