# Cantonese Phonology Reference

This document provides a comprehensive phonological inventory of Cantonese (Standard Hong Kong/Guangzhou Cantonese) as the foundation for designing a Tengwar mode. It uses Jyutping romanization as the primary reference system.

## Sources

- Bauer, R. S., & Benedict, P. K. (1997). *Modern Cantonese Phonology*. Mouton de Gruyter.
- Matthews, S., & Yip, V. (2011). *Cantonese: A Comprehensive Grammar* (2nd ed.). Routledge.
- Zee, E. (1999). Chinese (Hong Kong Cantonese). *Handbook of the International Phonetic Association*, 58-60. Cambridge University Press.
- The Linguistic Society of Hong Kong (LSHK). (1993). *Jyutping romanisation scheme*.

## Syllable Structure

Cantonese syllables follow the template:

```
(C) V (C)
```

More precisely:

```
(Initial) (Medial) Nucleus (Coda) Tone
```

Where:
- **Initial**: One of 19 consonants, or zero (null initial)
- **Medial**: /w/ only (limited distribution, occurs in /kw/ and /kwʰ/)
- **Nucleus**: A vowel (short or long) or syllabic nasal
- **Coda**: One of {-p, -t, -k, -m, -n, -ng} or zero
- **Tone**: One of 6 contrastive tones (9 in some analyses)

Unlike Mandarin, Cantonese permits stop codas (-p, -t, -k), which are unreleased.

---

## Consonant Inventory

### Initials (19 consonants + null)

Cantonese has 19 initial consonants organized by place and manner of articulation.

| Jyutping | IPA | Description | Example |
|----------|-----|-------------|---------|
| **Labials** ||||
| b | /p/ | voiceless unaspirated bilabial stop | 巴 baa1 "eight" |
| p | /pʰ/ | voiceless aspirated bilabial stop | 怕 paa3 "fear" |
| m | /m/ | bilabial nasal | 媽 maa1 "mother" |
| f | /f/ | voiceless labiodental fricative | 花 faa1 "flower" |
| **Alveolars** ||||
| d | /t/ | voiceless unaspirated alveolar stop | 打 daa2 "hit" |
| t | /tʰ/ | voiceless aspirated alveolar stop | 他 taa1 "he" |
| n | /n/ | alveolar nasal | 那 naa5 "that" |
| l | /l/ | alveolar lateral | 啦 laa1 (particle) |
| **Alveolar Affricates** ||||
| z | /ts/ | voiceless unaspirated alveolar affricate | 左 zo2 "left" |
| c | /tsʰ/ | voiceless aspirated alveolar affricate | 坐 co5 "sit" |
| s | /s/ | voiceless alveolar fricative | 沙 saa1 "sand" |
| **Velars** ||||
| g | /k/ | voiceless unaspirated velar stop | 家 gaa1 "home" |
| k | /kʰ/ | voiceless aspirated velar stop | 卡 kaa1 "card" |
| ng | /ŋ/ | velar nasal | 我 ngo5 "I" |
| h | /h/ | voiceless glottal fricative | 蝦 haa1 "shrimp" |
| **Labiovelars** ||||
| gw | /kʷ/ | voiceless unaspirated labiovelar stop | 瓜 gwaa1 "melon" |
| kw | /kʷʰ/ | voiceless aspirated labiovelar stop | 誇 kwaa1 "boast" |
| **Glides** ||||
| w | /w/ | labial-velar approximant | 華 waa4 "splendid" |
| j | /j/ | palatal approximant | 也 jaa5 "also" |
| **Null Initial** ||||
| ∅ | /ʔ/ or zero | glottal stop or zero | 阿 aa3 (prefix) |

Notes:
1. The velar nasal /ŋ/ can appear both as an initial and as a coda, unlike Mandarin where it is coda-only.
2. The null initial may have a slight glottal onset [ʔ] but this is not phonemic.
3. Unlike Mandarin, Cantonese has **no retroflex** consonants and **no palatal** series.

### Final Consonants (Codas)

Cantonese permits six coda consonants: three nasals and three unreleased stops.

| Jyutping | IPA | Description | Example |
|----------|-----|-------------|---------|
| **Nasals** ||||
| -m | /m/ | bilabial nasal | 三 saam1 "three" |
| -n | /n/ | alveolar nasal | 山 saan1 "mountain" |
| -ng | /ŋ/ | velar nasal | 生 saang1 "born" |
| **Stops** (unreleased) ||||
| -p | /p̚/ | unreleased bilabial stop | 十 sap6 "ten" |
| -t | /t̚/ | unreleased alveolar stop | 八 baat3 "eight" |
| -k | /k̚/ | unreleased velar stop | 百 baak3 "hundred" |

The stop codas are **always unreleased** in Cantonese. They close the syllable with no audible burst. These are the "entering tone" (入聲 jap6sing1) syllables that historically preserve Middle Chinese finals lost in Mandarin.

The coda nasals and stops form symmetrical pairs at each place of articulation:
- Labial: -m / -p
- Alveolar: -n / -t
- Velar: -ng / -k

---

## Vowel Inventory

Cantonese has a rich vowel system with both short and long vowels. Length is phonemic.

### Basic Vowels

| Jyutping | IPA | Length | Description | Example |
|----------|-----|--------|-------------|---------|
| aa | /aː/ | long | open front unrounded | 沙 saa1 |
| a | /ɐ/ | short | near-open central unrounded | 心 sam1 |
| e | /ɛː/ | long | open-mid front unrounded | 些 se1 |
| i | /iː/ | long | close front unrounded | 詩 si1 |
| o | /ɔː/ | long | open-mid back rounded | 蘇 so1 |
| u | /uː/ | long | close back rounded | 夫 fu1 |
| oe | /œː/ | long | open-mid front rounded | 靴 hoe1 |
| eo | /ɵ/ | short | close-mid central rounded | 春 ceon1 |
| yu | /yː/ | long | close front rounded | 書 syu1 |

### Vowel Distribution Notes

1. **Short /ɐ/ vs. long /aː/**: These are phonemically distinct. Compare:
   - 心 sam1 /sɐm˥/ "heart" vs. 三 saam1 /saːm˥/ "three"

2. **The /ɵ/ vowel** (Jyutping "eo"): A short, centralized rounded vowel. Only appears before -n and -t codas. Compare:
   - 春 ceon1 /tsʰɵn˥/ "spring" vs. 村 cyun1 /tsʰyːn˥/ "village"

3. **The /œː/ vowel** (Jyutping "oe"): A long open-mid front rounded vowel. Rarer than other vowels.

4. **The /yː/ vowel** (Jyutping "yu"): Front rounded, like German ü or French u. Unlike Mandarin, it is written distinctly in Jyutping rather than being conflated with u.

### Diphthongs and Triphthongs

| Jyutping | IPA | Example |
|----------|-----|---------|
| aai | /aːi/ | 大 daai6 "big" |
| aau | /aːu/ | 交 gaau1 "teach" |
| ai | /ɐi/ | 四 sei3 "four" |
| au | /ɐu/ | 九 gau2 "nine" |
| ei | /ei/ | 你 nei5 "you" |
| ou | /ou/ | 都 dou1 "all" |
| eoi | /ɵy/ | 需 seoi1 "need" |
| iu | /iːu/ | 小 siu2 "small" |
| ui | /uːi/ | 回 wui4 "return" |
| oi | /ɔːi/ | 愛 oi3 "love" |
| ou | /ou/ | 好 hou2 "good" |

### Syllabic Nasals

Cantonese has syllabic nasals that function as complete syllables:

| Jyutping | IPA | Example |
|----------|-----|---------|
| m | /m̩/ | 唔 m4 "not" |
| ng | /ŋ̩/ | 五 ng5 "five" |

These carry tone and require no additional vowel.

---

## Tone System

### The Six Tones

Cantonese has **six contrastive tones** in the traditional Hong Kong/Guangzhou analysis. Each tone is characterized by pitch contour and/or pitch height.

| Tone | Name | Chao Number | Contour | Description | Example |
|------|------|-------------|---------|-------------|---------|
| 1 | 陰平 jam1ping4 | 55 or 53 | ˥ or ˥˧ | high level (or high falling) | 詩 si1 "poem" |
| 2 | 陰上 jam1soeng5 | 35 | ˧˥ | high rising | 史 si2 "history" |
| 3 | 陰去 jam1heoi3 | 33 | ˧ | mid level | 試 si3 "try" |
| 4 | 陽平 joeng4ping4 | 21 or 11 | ˨˩ or ˩ | low falling (or low level) | 時 si4 "time" |
| 5 | 陽上 joeng4soeng5 | 23 | ˨˧ | low rising | 市 si5 "market" |
| 6 | 陽去 joeng4heoi3 | 22 | ˨ | low level | 是 si6 "be" |

### Tone Number Conventions

Jyutping uses the numbers 1-6 to mark tones. The Chao tone letters use a 5-point scale where 5 is the highest pitch and 1 is the lowest.

Tone contour summary:
- **High register** (陰 jam): Tones 1, 2, 3
- **Low register** (陽 joeng): Tones 4, 5, 6

| Tone | Pitch Pattern |
|------|---------------|
| 1 | ˥ (high level 55) or ˥˧ (high falling 53) |
| 2 | ˧˥ (mid-to-high rising 35) |
| 3 | ˧ (mid level 33) |
| 4 | ˨˩ (low falling 21) or ˩ (low level 11) |
| 5 | ˨˧ (low rising 23) |
| 6 | ˨ (low level 22) |

### Entering Tones (Checked Syllables)

Syllables ending in -p, -t, or -k (the "entering tones" 入聲 jap6sing1) can carry three of the six tones:

| Jyutping Tone | Traditional Name | Chao | Example |
|---------------|------------------|------|---------|
| 1 | 陰入 jam1jap6 (upper entering) | 5 | 北 bak1 "north" |
| 3 | 中入 zung1jap6 (middle entering) | 3 | 百 baak3 "hundred" |
| 6 | 陽入 joeng4jap6 (lower entering) | 2 | 白 baak6 "white" |

In the traditional 9-tone analysis, these are counted as separate tones (7, 8, 9). The LSHK Jyutping system uses 1, 3, 6 for these syllables since the pitch contour matches the corresponding open-syllable tones.

### Tone Variation and Allophony

1. **Tone 1 variation**: Some speakers realize Tone 1 as high falling [53] rather than high level [55]. Both are acceptable.

2. **Tone 4 variation**: Similarly varies between low falling [21] and low level [11].

3. **Changed tone (變調 bin3diu6)**: High-frequency words and affective speech can trigger tone changes, but these are not written in standard orthography.

---

## Comparison: Cantonese vs. Mandarin

### Consonant Comparison

| Feature | Mandarin | Cantonese | Design Implication |
|---------|----------|-----------|-------------------|
| Retroflex series | /tʂ tʂʰ ʂ ɻ/ | Absent | No Column IV retroflexes needed |
| Palatal series | /tɕ tɕʰ ɕ/ | Absent | No palatal marks needed |
| Velar nasal initial | Coda only | Initial and coda | /ŋ/ initial needs a tengwa |
| Labiovelar stops | Absent | /kʷ kʷʰ/ | Need gw/kw representation |
| Stop codas | Absent | /p̚ t̚ k̚/ | Need final stop representation |
| Bilabial coda | Absent | /-m/ | Need -m representation |

### Consonants in Cantonese but not Mandarin

| Sound | Jyutping | Notes |
|-------|----------|-------|
| /ŋ/ initial | ng- | 我 ngo5, 牙 ngaa4 |
| /kʷ/ | gw- | 瓜 gwaa1, 國 gwok3 |
| /kʷʰ/ | kw- | 誇 kwaa1, 狂 kwong4 |
| /-m/ coda | -m | 三 saam1, 心 sam1 |
| /-p̚/ coda | -p | 十 sap6, 答 daap3 |
| /-t̚/ coda | -t | 八 baat3, 筆 bat1 |
| /-k̚/ coda | -k | 百 baak3, 北 bak1 |

### Consonants in Mandarin but not Cantonese

| Sound | Pinyin | Notes |
|-------|--------|-------|
| /tʂ/ | zh | Retroflex series absent |
| /tʂʰ/ | ch | |
| /ʂ/ | sh | |
| /ɻ/ | r | |
| /tɕ/ | j | Palatal series absent |
| /tɕʰ/ | q | |
| /ɕ/ | x | |

### Vowel Comparison

| Feature | Mandarin | Cantonese |
|---------|----------|-----------|
| Vowel length | Not phonemic | Phonemic (a vs. aa) |
| Front rounded /y/ | Present (ü) | Present (yu) |
| /œ/ | Absent | Present (oe) |
| /ɵ/ | Absent | Present (eo) |
| Syllabic consonants | /ʐ̩ z̩/ after sibilants | Syllabic /m̩ ŋ̩/ |

### Tone Comparison

| Feature | Mandarin | Cantonese |
|---------|----------|-----------|
| Number of tones | 4 (+neutral) | 6 (or 9) |
| Contour types | Level, rising, dipping, falling | Level (3), rising (2), falling (1) |
| Tone 3 dip | Present | Absent |
| Checked syllables | Absent | Present (with stop codas) |

### Shared Features (Design Carryover)

The following Mandarin mode decisions can potentially carry over:

1. **Aspiration contrast**: Both languages contrast unaspirated/aspirated pairs. The doubled-bow convention for aspiration works.

2. **Nasal codas -n and -ng**: Both languages have these. Númen and ñoldo can be reused.

3. **High front rounded vowel**: /y/ exists in both (Mandarin ü, Cantonese yu). Same tehta approach applies.

4. **Tone iconography principle**: Pitch contour marks can extend to more tones.

---

## Allophones Relevant to Orthography

### Vowel Allophones

1. **Long /aː/ has allophone [ɑː] before velars**:
   - 講 gong2 /kɔːŋ/ vs. 江 gong1 /kɑːŋ/
   - Written the same in Jyutping (both "ong"); orthography can collapse.

2. **Short /ɐ/ centralizes further in closed syllables**:
   - Not written distinctly; predictable from environment.

3. **The vowel in Jyutping "e" vs "i"**:
   - Before -k and -ng: "e" represents /ɛ/ (色 sik1 [sɛːk̚])
   - This is the same grapheme as long /ɛː/ elsewhere

### Consonant Allophones

1. **Labiovelar stops only before /a/ and /ɔ/**:
   - gw and kw have limited distribution
   - No contrast with plain velars in other environments

2. **Stop codas are unreleased**:
   - [p̚ t̚ k̚] — no audible release burst
   - This affects nothing orthographically but is phonetically distinct from Mandarin (which lacks these entirely)

3. **Null initial may have [ʔ]**:
   - Slight glottal stop onset before vowel-initial syllables
   - Not phonemic; same carrier can be used

---

## Summary for Tengwar Design

### What Carries Over from Mandarin Mode

1. **Aspiration via doubled bow** — same principle
2. **Alveolar affricates z/c** — same phonemes, same tengwar
3. **Fricative s** — same phoneme
4. **Labials b/p/m/f** — same phonemes
5. **Alveolar d/t/n/l** — same phonemes
6. **Velars g/k** — same phonemes
7. **Nasal codas -n/-ng** — same, with addition of -m
8. **Vowel tehtar concept** — extends with more vowels

### What Needs New Design

1. **Velar nasal /ŋ/ as initial** — needs distinct representation since ñoldo is used for coda
2. **Labiovelar stops gw/kw** — need labialization marker or dedicated tengwar
3. **Stop codas -p/-t/-k** — need representation (shared concern with other Sinitic languages)
4. **Extended vowel system** — oe /œ/, eo /ɵ/, length distinction a/aa
5. **Six tones** — more marks than Mandarin's four
6. **Syllabic nasals m/ng** — standalone syllables

### Phoneme Count Summary

| Category | Count | Details |
|----------|-------|---------|
| Initial consonants | 19 | +null initial |
| Coda consonants | 6 | 3 nasals + 3 stops |
| Basic vowels | 9 | Including length contrasts |
| Diphthongs | ~11 | Various combinations |
| Tones | 6 | (9 in traditional analysis) |
| Syllabic nasals | 2 | m, ng |

---

## Open Questions for Further Research

1. **Tone mark design**: How to extend the 4-tone iconographic system to 6 tones? The three level tones (1, 3, 6) at different heights are a challenge.

2. **Vowel length marking**: Should length be marked explicitly (new tehta modifier) or rely on syllable structure?

3. **Front rounded vowels oe/eo**: These don't exist in Mandarin. Need new tehta or tehta combination.

4. **Stop coda representation**: Should final stops be written as full tengwar, as diacritics, or abbreviated? This decision affects Hakka, Min, and Middle Chinese reconstruction modes as well.

5. **Initial ng-**: Coda uses ñoldo. Should initial use the same? Different? Need to avoid ambiguity in syllable boundaries.

6. **Labiovelar representation**: Options include:
   - Dedicated tengwar (ungwë repurposed?)
   - Velar + labialization mark
   - Velar + vala ligature
