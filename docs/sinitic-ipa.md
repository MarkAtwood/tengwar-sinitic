# Sinitic IPA Subset

An intermediate phonemic representation for mapping any Sinitic language to Tengwar.

## Purpose

Instead of N separate romanization-to-Tengwar converters, this provides:

```
Pinyin   -> Sinitic IPA -+
Jyutping -> Sinitic IPA -+-> Tengwar
Tai-lo   -> Sinitic IPA -+
(raw IPA)----------------+
```

Languages without standardized romanization (Jin, Huizhou, Pinghua) can input IPA directly.

## Phoneme Inventory

### Consonants

| IPA | Description | Tengwar | Group |
|-----|-------------|---------|-------|
| p | voiceless bilabial stop | parma | A+B |
| pʰ | aspirated bilabial stop | umbar | A |
| b | voiced bilabial stop | umbar | B |
| t | voiceless alveolar stop | tinco | A+B |
| tʰ | aspirated alveolar stop | ando | A |
| d | voiced alveolar stop | ando | B |
| k | voiceless velar stop | calma | A+B |
| kʰ | aspirated velar stop | anga | A |
| g | voiced velar stop | anga | B |
| kʷ | voiceless labiovelar stop | calma + w-curl | A |
| kʷʰ | aspirated labiovelar stop | anga + w-curl | A |
| ʔ | glottal stop | telco | A+B |
| ts | voiceless alveolar affricate | tinco-ext | A+B |
| tsʰ | aspirated alveolar affricate | ando-ext | A |
| dz | voiced alveolar affricate | ando-ext | B |
| tʂ | voiceless retroflex affricate | calma (col III) | A |
| tʂʰ | aspirated retroflex affricate | anga (col III) | A |
| dʐ | voiced retroflex affricate | anga (col III) | B |
| tɕ | voiceless alveolo-palatal affricate | calma + pal | A+B |
| tɕʰ | aspirated alveolo-palatal affricate | anga + pal | A |
| dʑ | voiced alveolo-palatal affricate | anga + pal | B |
| f | voiceless labiodental fricative | formen | A+B |
| v | voiced labiodental fricative | vala (or ampa) | B |
| s | voiceless alveolar fricative | thule | A+B |
| z | voiced alveolar fricative | esse | B |
| ʂ | voiceless retroflex fricative | hwesta (col III) | A |
| ʐ | voiced retroflex fricative | hwesta (col III) | B |
| ɕ | voiceless alveolo-palatal fricative | hwesta + pal | A+B |
| ʑ | voiced alveolo-palatal fricative | hwesta + pal | B |
| x | voiceless velar fricative | harma | A |
| ɣ | voiced velar fricative | harma | B |
| h | voiceless glottal fricative | harma | A+B |
| m | bilabial nasal | malta | A+B |
| n | alveolar nasal | numen | A+B |
| ɲ | palatal nasal | numen + pal | A+B |
| ŋ | velar nasal | noldo | A+B |
| l | alveolar lateral | lambe | A+B |
| ɻ | retroflex approximant | ore | A |
| j | palatal approximant | anna | A+B |
| w | labiovelar approximant | vala | A+B |
| ɥ | labial-palatal approximant | anna + pal | A+B |

### Vowels

| IPA | Description | Tehta |
|-----|-------------|-------|
| a | open front | a-tehta (three dots) |
| ɑ | open back | a-tehta |
| e | close-mid front | e-tehta (acute) |
| ɛ | open-mid front | e-tehta |
| ə | mid central (schwa) | e-tehta or underdot |
| i | close front | i-tehta (single dot) |
| ɨ | close central (apical) | unutixe (syllabic mark) |
| o | close-mid back | o-tehta (left curl) |
| ɔ | open-mid back | o-tehta |
| u | close back | u-tehta (right curl) |
| ʉ | close central rounded | u-tehta |
| y | close front rounded | u-tehta + i-tehta |
| œ | open-mid front rounded | o-tehta + i-tehta |
| ø | close-mid front rounded | o-tehta + i-tehta |

### Modifiers

| Symbol | Meaning | Tengwar |
|--------|---------|---------|
| ̃ | nasalization | nasal bar above |
| ̚ | unreleased (stop coda) | (implicit from position) |
| ː | length | (not typically marked) |

### Tones (Chao tone letters)

| Pitch | Symbol | Mark |
|-------|--------|------|
| extra-high | ˥ (5) | — |
| high | ˦ (4) | — |
| mid | ˧ (3) | — |
| low | ˨ (2) | — |
| extra-low | ˩ (1) | — |

Tone contours are composed: ˥˩ (falling), ˧˥ (rising), ˨˩˦ (dipping), etc.

Tengwar tone marks trace the contour iconographically:
- Level: flat bar
- Rising: rising stroke
- Falling: falling stroke
- Dipping: chevron

Register modifiers:
- High register: plain mark
- Mid register: mark + single dot below
- Low register: mark + double dot below

## Compatibility Groups

**Group A** (aspiration semantics): Mandarin, Cantonese, Hakka, Gan, Xiang
- Grade 1 = voiceless unaspirated
- Grade 2 = voiceless aspirated

**Group B** (voicing semantics): Min, Wu
- Grade 1 = voiceless
- Grade 2 = voiced
- Aspiration marked with diacritic

The IPA → Tengwar converter takes a `group` parameter to select semantics.

## Input Format

IPA strings use standard Unicode IPA characters. Tones are specified either:
1. Inline with Chao letters: `/ma˥˩/` (falling tone on "ma")
2. As suffix number: `/ma51/` (equivalent)

Syllable boundaries use `.` or space.

## Examples

| Language | Input | IPA | Tengwar |
|----------|-------|-----|---------|
| Mandarin | ni3 hao3 | /ni˨˩˦ xau˨˩˦/ | ... |
| Cantonese | nei5 hou2 | /nei˩˧ hou˧˥/ | ... |
| Jin | (direct) | /... / | ... |

## Implementation

See `samples/sinitic_ipa.py` for the reference converter.
