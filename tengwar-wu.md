# Tengwar Mode for Wu Chinese (Shanghainese)

**Version:** 1.0
**Status:** Draft
**Author:** Tengwar-Mandarin Project

## Overview

This document defines a Tengwar writing system for Wu Chinese, specifically the Shanghainese dialect spoken by approximately 80 million people in the Yangtze River Delta region.

**Key design principle:** Wu preserves a three-way laryngeal contrast (voiceless unaspirated / voiceless aspirated / voiced) that aligns with classical Tengwar voicing semantics. Rather than hack aspiration into the grade system, this mode returns to Tolkien's original design:

- **Grade 1** = voiceless (stops and affricates)
- **Grade 2** = voiced (stops and affricates)
- **Grade 3** = voiceless fricatives
- **Grade 4** = voiced fricatives
- **Aspiration** = marked with a diacritic

This mode is **incompatible** with the Mandarin, Cantonese, and Min modes, which use Grade 2 for aspiration. A document must declare which mode applies.

---

## Consonants

### The Three-Way Laryngeal Contrast

Wu Chinese distinguishes three series where Mandarin has two:

| Series | IPA Example | Wu Pinyin | Description |
|--------|-------------|-----------|-------------|
| Voiceless unaspirated | /p, t, k/ | b, d, g | No aspiration, no voicing |
| Voiceless aspirated | /pʰ, tʰ, kʰ/ | p, t, k | Strong aspiration, no voicing |
| Voiced | /b, d, g/ | bb, dd, gg | True vocal fold vibration |

### Grade Assignments

| Grade | Articulation | Wu Examples |
|-------|--------------|-------------|
| 1 | voiceless unaspirated stops/affricates | /p, t, k, ts, tɕ/ |
| 1 + asp | voiceless aspirated (diacritic) | /pʰ, tʰ, kʰ, tsʰ, tɕʰ/ |
| 2 | voiced stops/affricates | /b, d, g, dz, dʑ/ |
| 3 | voiceless fricatives | /f, s, ɕ, x, h/ |
| 4 | voiced fricatives | /v, z, ʑ, ɦ/ |
| 5 | nasals | /m, n, ŋ, ɲ/ |
| 6 | approximants/laterals | /l, j, w/ |

### The Aspiration Diacritic

Aspiration is a secondary articulation—it does not change place or manner. It is marked with a **rightward-opening curl** positioned at the upper-right of the tengwa, below the vowel tehta zone.

| Codepoint | Name | Description |
|-----------|------|-------------|
| U+E070 | aspiration-mark | Small rightward curl, marks /ʰ/ |

This parallels how Tengwar marks other secondary articulations (palatalization, labialization, nasalization) with diacritics rather than consuming grade slots.

### Consonant Grid

#### Stops and Nasals

| Grade | I: Alveolar | II: Labial | III: Velar |
|-------|-------------|------------|------------|
| 1 (vl. unasp.) | tinco /t/ | parma /p/ | calma /k/ |
| 1 + asp | tinco+asp /tʰ/ | parma+asp /pʰ/ | calma+asp /kʰ/ |
| 2 (voiced) | ando /d/ | umbar /b/ | anga /g/ |
| 5 (nasal) | númen /n/ | malta /m/ | noldo /ŋ/ |
| 6 (lateral) | lambe /l/ | — | — |

#### Fricatives

| Grade | I: Alveolar | II: Labial | III: Velar/Glottal |
|-------|-------------|------------|-------------------|
| 3 (vl. fric.) | þúle /s/ | formen /f/ | hwesta /x~h/ |
| 4 (vd. fric.) | anto /z/ | ampa /v/ | unque /ɦ/ |

#### Affricates (Extended Stems)

| Grade | Alveolar | Alveolo-palatal |
|-------|----------|-----------------|
| 1 (vl. unasp.) | tinco-ext /ts/ | calma+pal /tɕ/ |
| 1 + asp | tinco-ext+asp /tsʰ/ | calma+pal+asp /tɕʰ/ |
| 2 (voiced) | ando-ext /dz/ | anga+pal /dʑ/ |
| 3 (vl. fric.) | þúle /s/ | hwesta+pal /ɕ/ |
| 4 (vd. fric.) | anto /z/ | unque+pal /ʑ/ |

### Complete Initial Mapping

| IPA | Wu Pinyin | Tengwa | Diacritics | Codepoint |
|-----|-----------|--------|------------|-----------|
| /p/ | b | parma | — | U+E011 |
| /pʰ/ | p | parma | +asp | U+E011 U+E070 |
| /b/ | bb | umbar | — | U+E012 |
| /m/ | m | malta | — | U+E015 |
| /f/ | f | formen | — | U+E013 |
| /v/ | v | ampa | — | U+E014 |
| /t/ | d | tinco | — | U+E001 |
| /tʰ/ | t | tinco | +asp | U+E001 U+E070 |
| /d/ | dd | ando | — | U+E002 |
| /n/ | n | númen | — | U+E005 |
| /l/ | l | lambe | — | U+E006 |
| /k/ | g | calma | — | U+E021 |
| /kʰ/ | k | calma | +asp | U+E021 U+E070 |
| /g/ | gg | anga | — | U+E022 |
| /ŋ/ | ng | noldo | — | U+E025 |
| /x~h/ | h | hwesta | — | U+E023 |
| /ɦ/ | gh | unque | — | U+E024 |
| /ts/ | z | tinco-ext | — | U+E061 |
| /tsʰ/ | c | tinco-ext | +asp | U+E061 U+E070 |
| /dz/ | zz | ando-ext | — | U+E062 |
| /s/ | s | þúle | — | U+E003 |
| /z/ | ss | anto | — | U+E004 |
| /tɕ/ | j | calma | +pal | U+E021 U+E06B |
| /tɕʰ/ | q | calma | +pal +asp | U+E021 U+E06B U+E070 |
| /dʑ/ | jj | anga | +pal | U+E022 U+E06B |
| /ɕ/ | x | hwesta | +pal | U+E023 U+E06B |
| /ʑ/ | xx | unque | +pal | U+E024 U+E06B |
| /ɲ/ | gn | noldo | +pal | U+E025 U+E06B |
| /j/ | y | anna | — | U+E036 |
| /w/ | w | vala | — | U+E016 |
| ∅ | — | telco | — | U+E030 |

---

## Vowels

Tehtar placed on the preceding consonant (Quenya-style), consistent with other Sinitic modes.

### Basic Vowels

| Wu Pinyin | IPA | Tehta | Codepoint |
|-----------|-----|-------|-----------|
| a | /a/ | three dots (a-tehta) | U+E040 |
| o | /o/ | left curl (o-tehta) | U+E04C |
| e | /e/ | acute stroke (e-tehta) | U+E046 |
| i | /i/ | single dot (i-tehta) | U+E044 |
| u | /u/ | right curl (u-tehta) | U+E04A |
| y | /y/ | u-tehta + i-tehta | U+E04A U+E044 |
| oe | /ə/ | underdot | U+E045 |

### Diphthongs

Falling diphthongs write only the nuclear vowel; the offglide is implied:

| Wu Pinyin | IPA | Tehta |
|-----------|-----|-------|
| au | /aʊ/ | a-tehta |
| ou | /əʊ/ | o-tehta |
| ai | /ɛ/ | a-tehta |
| ei | /e/ | e-tehta |

Rising diphthongs use medial glide tengwar (anna for /j/, vala for /w/).

### Syllabic Consonants

A bare nasal tengwa with a tone mark signals a syllabic nasal:

| Wu Pinyin | IPA | Tengwa |
|-----------|-----|--------|
| m | /m̩/ | malta (no vowel tehta) |
| n | /n̩/ | númen (no vowel tehta) |
| ng | /ŋ̩/ | noldo (no vowel tehta) |

---

## Tones

Shanghainese has **five citation tones** with a yin/yang register split.

### Citation Tones

| Tone | Name | Chao | Contour | Register |
|------|------|------|---------|----------|
| T1 | yin-ping | 53 | falling | high |
| T2 | yang-ping | 31 | falling | low |
| T3 | yin-shang | 55 | level | high |
| T4 | yin-qu | 34 | rising | mid |
| T5 | yang-qu | 13 | rising | low |

### Checked Tones

Syllables ending in glottal stop (from historical *-p, *-t, *-k):

| Checked | Register | Mark |
|---------|----------|------|
| Yin-ru | high | flat bar |
| Yang-ru | low | falling + double-dot |

### Tone Marks

Using the contour + register system:

| Tone | Contour Mark | Register Mark | Combined |
|------|--------------|---------------|----------|
| T1 (53) | falling stroke U+E054 | — | `\` |
| T2 (31) | falling stroke U+E054 | double-dot U+E043 | `\..` |
| T3 (55) | flat bar U+E050 | — | `_` |
| T4 (34) | rising stroke U+E046 | single-dot U+E045 | `[e/rise].` |
| T5 (13) | rising stroke U+E046 | double-dot U+E043 | `[e/rise]..` |

### Tone Sandhi

Wu has **left-dominant tone sandhi**: the first syllable determines the tonal pattern for the entire phrase.

**Policy:** Write citation tones phrase-initially; leave subsequent syllables unmarked or apply the spread pattern. This reflects the functional reality that non-initial syllables lose distinctive tone in connected speech.

| First syllable | Phrase pattern |
|----------------|----------------|
| Yin register (T1, T3, T4) | High-falling spread |
| Yang register (T2, T5) | Low-rising spread |

---

## Final Consonants

Modern Shanghainese has limited coda inventory:

| Coda | IPA | Tengwa | Codepoint |
|------|-----|--------|-----------|
| -n | /n/ | númen | U+E005 |
| -ng | /ŋ/ | noldo | U+E025 |
| -q | /ʔ/ | halla | U+E028 |

Historical *-m has merged with *-n. Historical *-p, *-t, *-k have merged to glottal stop.

---

## Syllable Structure

```
(Initial)(Medial)Nucleus(Coda)Tone
```

### Visual Layout

**Aspirated initial, open syllable:**
```
  [vowel tehta]
  [  tengwa   ][asp]
  [ tone mark ]
```

**Voiced initial with coda:**
```
  [vowel tehta]
  [  tengwa   ][coda]
  [ tone mark ]
```

---

## Examples

### Voicing Contrast (Minimal Triad)

| Wu Pinyin | IPA | Meaning | Structure |
|-----------|-----|---------|-----------|
| ba | /pa⁵⁵/ | eight | parma + a-tehta + T3 |
| pa | /pʰa⁵⁵/ | afraid | parma + asp + a-tehta + T3 |
| bba | /ba³¹/ | pull | umbar + a-tehta + T2 |

### Aspiration Examples

| Wu Pinyin | IPA | Structure |
|-----------|-----|-----------|
| ti | /tʰi/ | tinco + asp + i-tehta |
| qi | /tɕʰi/ | calma + pal + asp + i-tehta |
| cu | /tsʰu/ | tinco-ext + asp + u-tehta |

### Voiced Fricatives

| Wu Pinyin | IPA | Meaning | Structure |
|-----------|-----|---------|-----------|
| va | /va/ | flower | ampa + a-tehta |
| zi | /zi/ | word | anto + i-tehta |

### Glottal Stop Coda

| Wu Pinyin | IPA | Meaning | Structure |
|-----------|-----|---------|-----------|
| baq | /baʔ/ | white | umbar + a-tehta + halla |
| seq | /səʔ/ | color | þúle + oe-tehta + halla |
| goq | /gəʔ/ | country | anga + o-tehta + halla |

---

## Mode Incompatibility

This mode uses different grade semantics from other Sinitic modes:

| Feature | Mandarin/Cantonese/Min | Wu (this mode) |
|---------|------------------------|----------------|
| Grade 1 | voiceless unaspirated | voiceless unaspirated |
| Grade 2 | voiceless aspirated | **voiced** |
| Grade 3 | fricative (or voiced hack) | voiceless fricative |
| Aspiration | grade distinction | **diacritic** |

A document must declare which mode applies. Mixed-mode text is not supported.

### Why Incompatibility is Acceptable

1. **Phonological honesty:** Each mode faithfully represents its language's contrasts
2. **Visual clarity:** No ambiguity about grade semantics within a document
3. **Minimal notation:** Each mode uses only what its phonology requires
4. **Classical fidelity:** Wu mode aligns with Tolkien's original Tengwar design

---

## Font Requirements

### New Glyph

| Codepoint | Name | Description |
|-----------|------|-------------|
| U+E070 | aspiration-mark | Small rightward curl at upper-right of tengwa |

The aspiration mark should:
- Position at upper-right corner, below vowel tehta zone
- Be approximately 1/3 the height of a vowel tehta
- Curve rightward, evoking breath
- Stack correctly with palatal diacritic (aspiration outside palatal)

### Existing Glyphs

All other glyphs are standard Tengwar or present in Alcarin Tengwar Extended:
- Grade 1-4 tengwar in all columns
- Extended-stem alveolar series
- Palatal diacritic
- Tone contour marks
- Register modifier dots
- Glottal stop (halla)

---

## Romanization

This mode accepts **Qian Nairong's Shanghainese Pinyin** or **Wugniu romanization**.

### Normalization

| Feature | This spec | Qian Nairong | Wugniu |
|---------|-----------|--------------|--------|
| Voiced stops | bb, dd, gg | b, d, g | b, d, g |
| Voiceless unasp. | b, d, g | p, t, k | p, t, k |
| Voiceless asp. | p, t, k | ph, th, kh | ph, th, kh |
| Glottal coda | -q | -q or -h | -k |

The converter normalizes input before mapping to Tengwar.

---

## Summary

The Wu Tengwar mode:

1. **Returns to classical Tengwar semantics:** Grade 1 voiceless, Grade 2 voiced
2. **Marks aspiration with a diacritic:** Phonologically honest, visually minimal
3. **Represents the three-way laryngeal contrast:** /p/ vs. /pʰ/ vs. /b/ distinguished cleanly
4. **Uses 29 initial consonants:** All grades populated according to Wu phonology
5. **Marks 5 tones:** Using contour + register system
6. **Handles left-dominant sandhi:** Citation tones phrase-initially
7. **Is incompatible with other Sinitic modes:** By design, for clarity

This mode demonstrates that a principled design—one respecting both the target language's phonology and the source script's semantics—produces a cleaner result than retrofitting existing conventions.
