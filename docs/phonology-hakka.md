# Hakka Phonology for Tengwar Mode Design

This document describes Hakka phonology with focus on the Sixian (四縣) dialect as the primary reference, noting Hailu (海陸) variations where relevant. The goal is to inform future Tengwar-Hakka mode design by identifying what can be reused from the Cantonese mode versus what requires adaptation.

## Consonant Inventory

### Sixian Initials (18 consonants)

| Romanization | IPA | Description |
|--------------|-----|-------------|
| b | /p/ | voiceless unaspirated bilabial stop |
| p | /pʰ/ | voiceless aspirated bilabial stop |
| m | /m/ | bilabial nasal |
| f | /f/ | voiceless labiodental fricative |
| v | /v/ ~ /ʋ/ | voiced labiodental fricative/approximant |
| d | /t/ | voiceless unaspirated alveolar stop |
| t | /tʰ/ | voiceless aspirated alveolar stop |
| n | /n/ | alveolar nasal |
| l | /l/ | alveolar lateral |
| g | /k/ | voiceless unaspirated velar stop |
| k | /kʰ/ | voiceless aspirated velar stop |
| ng | /ŋ/ | velar nasal |
| h | /h/ | voiceless glottal fricative |
| z | /ts/ | voiceless unaspirated alveolar affricate |
| c | /tsʰ/ | voiceless aspirated alveolar affricate |
| s | /s/ | voiceless alveolar fricative |
| j | /tɕ/ | voiceless unaspirated alveolo-palatal affricate |
| q | /tɕʰ/ | voiceless aspirated alveolo-palatal affricate |
| x | /ɕ/ | voiceless alveolo-palatal fricative |
| (zero) | ∅ | null initial |

**Note on palatalization:** When /k/, /kʰ/, /h/, /ŋ/ precede palatal medial /j/, they become palatalized: [c], [cʰ], [ç], [ɲ] respectively.

### Hailu Additions (22 consonants)

Hailu preserves postalveolar consonants that Sixian lacks:

| Romanization | IPA | Description |
|--------------|-----|-------------|
| zh | /tʃ/ | voiceless unaspirated postalveolar affricate |
| ch | /tʃʰ/ | voiceless aspirated postalveolar affricate |
| sh | /ʃ/ | voiceless postalveolar fricative |
| rh | /ʒ/ | voiced postalveolar fricative |

**Design implication:** Sixian merges these as alveolar /ts/, /tsʰ/, /s/. The Tengwar mode may need additional symbols if supporting Hailu.

## Vowel Inventory

### Monophthongs (6-7 vowels)

| Romanization | IPA | Description |
|--------------|-----|-------------|
| a | /a/ | open central |
| e | /ɛ/ ~ /ə/ | mid (context-dependent) |
| i | /i/ | close front |
| ii | /ɨ/ ~ /ɪ/ | close central (apical vowel) |
| o | /ɔ/ | open-mid back rounded |
| u | /u/ | close back rounded |

**Note:** The syllabic alveolar approximant [ɹ̩], romanized as "ii", occurs after alveolar consonants (z, c, s). This is the "apical vowel" common in Chinese varieties.

### Diphthongs (9 diphthongs)

| Romanization | IPA |
|--------------|-----|
| ai | /ai/ |
| au | /au/ |
| eu | /ɛu/ |
| oi | /ɔi/ |
| ia | /ia/ |
| ie | /ie/ |
| io | /iɔ/ |
| iu | /iu/ |
| ui | /ui/ |

### Triphthongs

| Romanization | IPA |
|--------------|-----|
| iau | /iau/ |

## Final Consonants

Hakka preserves all six Middle Chinese final consonants, identical to Cantonese:

### Nasal finals

| Romanization | IPA |
|--------------|-----|
| -m | /m/ |
| -n | /n/ |
| -ng | /ŋ/ |

### Stop finals (unreleased)

| Romanization | IPA |
|--------------|-----|
| -p | /p̚/ |
| -t | /t̚/ |
| -k | /k̚/ |

**Design implication:** The entering-tone (ru) syllables end in stop finals. The Tengwar mode can reuse the Cantonese final consonant design unchanged.

## Tones

### Sixian Tones (6 tones)

| Number | Category | Chao Contour | Description |
|--------|----------|--------------|-------------|
| 1 | Yin Ping 陰平 | 24 | mid-rising |
| 2 | Yang Ping 陽平 | 11 | low level |
| 3 | Shang Sheng 上聲 | 31 | mid-falling |
| 4 | Qu Sheng 去聲 | 55 | high level |
| 5 | Yin Ru 陰入 | 2 | low checked (short) |
| 6 | Yang Ru 陽入 | 5 | high checked (short) |

**Tone sandhi:** Tone 1 changes from [24] to [35] before lower tones. Tone 4 changes from [55] to [55] (stable) or shows minor variation.

### Hailu Tones (7 tones)

Hailu has an additional tone split in the Qu category:

| Number | Category | Chao Contour |
|--------|----------|--------------|
| 1 | Yin Ping 陰平 | 53 |
| 2 | Yang Ping 陽平 | 55 |
| 3 | Shang Sheng 上聲 | 24 |
| 4 | Yin Qu 陰去 | 11 |
| 5 | Yang Qu 陽去 | 33 |
| 6 | Yin Ru 陰入 | 5 |
| 7 | Yang Ru 陽入 | 2 |

**Key difference:** Sixian and Hailu have opposite pitch patterns. When Sixian is high, Hailu is low, and vice versa. This is a striking feature of inter-dialect variation.

## Romanization Systems

### Taiwanese Hakka Romanization System (臺灣客家語拼音方案)

Published by Taiwan Ministry of Education (2012). Official standard for Taiwanese Hakka.

**Key features:**
- Tone numbers written as superscript diacritics
- Aspirated consonants: p, t, k, c (vs. unaspirated b, d, g, z)
- Special symbol "ii" for apical vowel /ɨ/
- Dialect-specific adaptations for Sixian, Hailu, Dabu, Raoping, Zhao'an

### Pha̍k-fa-sṳ (白話字)

Missionary romanization from 19th century, modeled on Hokkien Pe̍h-ōe-jī. Still used in some communities and publications.

**Key differences from Taiwan MOE:**
- Uses "ch" for aspirated /tsʰ/ (vs. MOE "c")
- Uses "ts" for unaspirated /ts/ (vs. MOE "z")
- Tone marks use diacritics over vowels

**Recommendation:** Use Taiwan MOE romanization for consistency with official materials and computational resources.

## Comparison with Cantonese

### What's the Same (Reusable from Cantonese Mode)

| Feature | Status |
|---------|--------|
| Final stops -p, -t, -k | Identical |
| Final nasals -m, -n, -ng | Identical |
| 6 tones (Sixian) | Same count as Cantonese |
| Voiceless unaspirated/aspirated distinction | Identical pattern |
| Syllable structure CV(C) | Identical |

### What Differs (Requires Adaptation)

| Feature | Cantonese | Hakka | Design Impact |
|---------|-----------|-------|---------------|
| /v/ initial | Absent | Present | Need new tengwa |
| Apical vowel /ɨ/ | Absent | Present ("ii") | Need tehta or tengwa |
| -ik vs -it pattern | -ik | -it | Orthographic, no glyph change |
| Palatal initials | /tɕ, tɕʰ, ɕ/ merged/absent | Distinct /tɕ, tɕʰ, ɕ/ | May need separate tengwar |
| Postalveolars (Hailu) | Absent | /tʃ, tʃʰ, ʃ, ʒ/ | Hailu-specific tengwar |
| Tone contours | Different values | Different values | Tehta redesign needed |

### Detailed Phoneme Differences

**Initial /v/:** Hakka has /v/ (or /ʋ/) from Middle Chinese *m- before certain rimes. Examples: 武 "vu" (martial), 屋 "vuk" (house). Cantonese has /m/ or /w/ in these contexts.

**Rime differences:**
- Hakka often has /ia/ where Cantonese has /i/ or /ɛ/: 惜 Hakka "siak" vs Cantonese "sek"
- Hakka has -it where Cantonese has -ik: 力 Hakka "lit" vs Cantonese "lik"
- Hakka collapsed some nasal codas: -ing often becomes -in

**Tone contour values:** Though both have 6 tones, the Chao numbers differ significantly:

| Category | Cantonese | Sixian Hakka |
|----------|-----------|--------------|
| Yin Ping | 55 (high level) | 24 (mid-rising) |
| Yang Ping | 21 (low falling) | 11 (low level) |
| Yin Shang | 35 (high rising) | - |
| Yang Shang | 23 (mid rising) | 31 (mid-falling) |
| Yin Qu | 33 (mid level) | 55 (high level) |
| Yang Qu | 22 (low level) | - |
| Yin Ru | 5 (high) | 2 (low) |
| Yang Ru | 2 (low) | 5 (high) |

**Note:** Hakka merged the Shang tones (no yin-yang split), while Cantonese merged the Qu tones. The Ru tones have opposite pitch relationships.

## Hakka-Specific Challenges for Tengwar Mode

1. **The /v/ initial:** Needs a new tengwa. Could use an extended Telerin tengwa or derive from the labial series with modification.

2. **Apical vowel /ɨ/:** Distinct from /i/. Options:
   - Separate tehta
   - Modified short carrier with special mark
   - Context-dependent: only after z/c/s, so could be implicit

3. **Hailu postalveolars:** If supporting Hailu dialect, need tengwar for /tʃ, tʃʰ, ʃ, ʒ/. Consider whether to support only Sixian initially.

4. **Seven tones (Hailu):** The 6-tone tehta system from Cantonese would need extension for Hailu's 7th tone.

5. **Tone contour differences:** Even with same tone count, the tehta shapes may need redesign to reflect different pitch patterns (level vs rising vs falling).

6. **Dialect selection:** Major variation between Sixian and Hailu suggests either:
   - Pick one primary dialect (recommend Sixian as most spoken)
   - Design extensible system supporting both

## Syllable Structure

Hakka follows the standard Chinese CV(C) pattern:

```
(C)(G)V(C)
```

Where:
- C = initial consonant (optional)
- G = glide/medial (i, u)
- V = main vowel (required)
- C = final consonant (-p, -t, -k, -m, -n, -ng)

Maximum complexity: CGVC (e.g., "kiang" /kiaŋ/)

This is identical to Cantonese structure and compatible with existing Tengwar mode design patterns.

## Sources

Research compiled from:

- [Sixian dialect - Wikipedia](https://en.wikipedia.org/wiki/Sixian_dialect)
- [Taiwanese Hakka Romanization System - Wikipedia](https://en.wikipedia.org/wiki/Taiwanese_Hakka_Romanization_System)
- [Taiwanese Hakka - Wikipedia](https://en.wikipedia.org/wiki/Taiwanese_Hakka)
- [Meixian dialect - Wikipedia](https://en.wikipedia.org/wiki/Meixian_dialect)
- [Hakka Chinese - Journal of IPA (Lee & Zee)](https://www.cambridge.org/core/journals/journal-of-the-international-phonetic-association/article/hakka-chinese/2C4B6E6EB3F5DED1E739EB8C188D80ED)
- [Sixian vs Hailu comparison (wpchen.net)](https://www.wpchen.net/en/posts/hakka-taiwan-sixian-hailu-difference)
- [Hakka Language overview (sachinese.wordpress.com)](https://sachinese.wordpress.com/2013/03/05/the-hakka-language/)
- [Cantonese phonology - Wikipedia](https://en.wikipedia.org/wiki/Cantonese_phonology)
- [Hakka's relation to Cantonese and Mandarin (dylansung)](https://dylansung.tripod.com/sapienti/langintr.htm)

---

*Document prepared for Tengwar-Mandarin project. Hakka mode design depends on completion of Cantonese mode first.*
