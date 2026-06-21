# Tengwar Mode for Cantonese

## Why this mode exists

Cantonese is the second major Chinese language to receive a Tengwar mode, after Mandarin. While the two languages share most of their written Chinese characters, their phonologies differ substantially: Cantonese preserves final stop consonants, has a richer vowel system with phonemic length contrasts, and distinguishes six tones rather than four.

This mode builds on the Mandarin mode's design framework while extending it to represent Cantonese phonology accurately. It uses Jyutping romanization as the primary reference system, the standard developed by the Linguistic Society of Hong Kong.

Cantonese is a good second test case for Sinitic Tengwar modes because it shares the aspiration-based consonant contrast and tonal nature of Mandarin, but adds challenges the Mandarin mode did not face: final stops, more vowels, and more tones. Solutions developed here will apply to Hakka and Min modes as well.

This is a phonemic tehtar mode. It transcribes the sounds of Standard Hong Kong/Guangzhou Cantonese as analyzed through the Jyutping system. It does not represent Chinese characters, etymologies, or meaning. It is a way of writing what you hear.

## Romanization reference

This mode uses **Jyutping** (粵拼) as its reference romanization. Jyutping was developed by the Linguistic Society of Hong Kong in 1993 and is the de facto standard for linguistic work on Cantonese.

Key features:
- Initial consonants: b, p, m, f, d, t, n, l, g, k, ng, h, gw, kw, w, z, c, s, j
- Vowels: aa, a, e, i, o, u, oe, eo, yu
- Codas: -m, -n, -ng, -p, -t, -k (plus vowel offglides)
- Tones: 1-6 (numbered suffix)

Example: 香港 hoeng1gong2 "Hong Kong"

## Consonants

Cantonese has 19 initial consonants plus a null initial. The system is simpler than Mandarin in some ways (no retroflexes, no palatals) but adds labialized velars and initial /ng/.

### Consonant grid

| Grade | I: Alveolar | II: Labial | III: Velar | III+lab: Labiovelar |
|-------|-------------|------------|------------|---------------------|
| 1 (unasp.) | tinco /t/ **d** | parma /p/ **b** | calma /k/ **g** | calma+w-curl /kw/ **gw** |
| 2 (asp.) | ando /th/ **t** | umbar /ph/ **p** | anga /kh/ **k** | anga+w-curl /kwh/ **kw** |
| 3 (fric.) | thule /s/ **s** | formen /f/ **f** | hwesta /h/ **h** | -- |
| 5 (nasal) | numen /n/ **n** | malta /m/ **m** | noldo /ng/ **ng** | -- |
| 6 (approx.) | lambe /l/ **l** | -- | -- | vala /w/ **w** |

Bold = Jyutping letter.

Plus alveolar affricates using extended stems:

| Grade | I: Alveolar (ext.) |
|-------|-------------------|
| 1 (unasp.) | ext. tinco /ts/ **z** |
| 2 (asp.) | ext. ando /tsh/ **c** |

Plus the palatal approximant:

| Glide | Tengwa |
|-------|--------|
| j /j/ | anna |

### Design rationale

**Aspiration contrast:** Same as Mandarin. Grade 1 (single bow) is unaspirated; Grade 2 (doubled bow) is aspirated. The doubled bow means "more energy at the same place."

**No Column IV:** Cantonese lacks the retroflex series that occupies Column IV in the Mandarin mode. This column is not used.

**Velar nasal initial:** Cantonese has /ng/ as both an initial and a coda, unlike Mandarin where it is coda-only. The same tengwa (noldo) serves both positions. Syllable position is unambiguous: initial precedes the vowel, coda follows it.

**Labialized velars:** Cantonese /kw/ and /kwh/ (Jyutping gw, kw) are velar stops with secondary labialization. Following Tolkien's quessetema convention, these are written as calma/anga with a w-curl diacritic below. This is compositional: readers can parse gw/kw as "g/k with lip rounding."

**Cantonese /h/ vs Mandarin /x/:** Mandarin has /x/ (velar fricative); Cantonese has /h/ (glottal fricative). Both use hwesta. They occupy the same functional slot in their phonologies, and using different tengwar would complicate cross-language consistency.

### Complete initial mapping

| Jyutping | IPA | Tengwa | Codepoint | Grid |
|----------|-----|--------|-----------|------|
| b | /p/ | parma | U+E011 | II-1 |
| p | /ph/ | umbar | U+E012 | II-2 |
| m | /m/ | malta | U+E015 | II-5 |
| f | /f/ | formen | U+E013 | II-3 |
| d | /t/ | tinco | U+E001 | I-1 |
| t | /th/ | ando | U+E002 | I-2 |
| n | /n/ | numen | U+E005 | I-5 |
| l | /l/ | lambe | U+E026 | I-6 |
| g | /k/ | calma | U+E021 | III-1 |
| k | /kh/ | anga | U+E022 | III-2 |
| ng | /ng/ | noldo | U+E025 | III-5 |
| h | /h/ | hwesta | U+E023 | III-3 |
| gw | /kw/ | calma + w-curl | U+E021 + U+E06A | III-1+lab |
| kw | /kwh/ | anga + w-curl | U+E022 + U+E06A | III-2+lab |
| w | /w/ | vala | U+E02D | -- |
| z | /ts/ | ext. tinco | U+E009 | I-1 ext. |
| c | /tsh/ | ext. ando | U+E00A | I-2 ext. |
| s | /s/ | thule | U+E003 | I-3 |
| j | /j/ | anna | U+E027 | -- |
| null | -- | telco | U+E02F | (carrier) |

The w-curl (U+E06A) is a below-tengwa diacritic indicating labialization. It appears in the same vertical zone as the palatal mark in the Mandarin mode.

### What Cantonese lacks

These Mandarin consonants do not appear in Cantonese:

| Mandarin | IPA | Why absent |
|----------|-----|------------|
| zh | /ts`/ | No retroflexes |
| ch | /ts`h/ | No retroflexes |
| sh | /s`/ | No retroflexes |
| r | /r`/ | No retroflexes |
| j | /tc/ | No palatal affricates |
| q | /tch/ | No palatal affricates |
| x | /c/ | No palatal fricative |

Note: Jyutping "j" is /j/ (palatal approximant), the same phoneme as Mandarin "y," not a palatal affricate.

## Vowels

Tehtar on the preceding consonant (Quenya-style placement), same as the Mandarin mode. Cantonese syllables end in vowels, nasals, or unreleased stops, making this placement natural.

### Basic vowel tehtar

| Jyutping | IPA | Tehta | Glyph | Codepoint |
|----------|-----|-------|-------|-----------|
| aa | /a:/ | a-tehta | three dots above | U+E040 |
| a | /6/ | underdot | single dot below | U+E045 |
| e | /E:/ | e-tehta | acute stroke above | U+E046 |
| i | /i:/ | i-tehta | single dot above | U+E044 |
| o | /O:/ | o-tehta | left curl above | U+E048 |
| u | /u:/ | u-tehta | right curl above | U+E049 |
| oe | /9:/ | o+i tehta | left curl + dot above | U+E048 + U+E044 |
| eo | /8/ | u+underdot | right curl above + dot below | U+E049 + U+E045 |
| yu | /y:/ | u+i tehta | right curl + dot above | U+E049 + U+E044 |

### Vowel length distinction

Cantonese has a phonemic length contrast between long /a:/ (Jyutping "aa") and short /6/ (Jyutping "a"). These vowels also differ in quality: long /a:/ is open front-central, while short /6/ is near-open central.

The mode marks this distinction with different tehtar:
- **aa** /a:/: three-dot a-tehta (same as Mandarin)
- **a** /6/: underdot (new tehta)

The underdot suggests a "reduced" or "centralized" vowel. Placing it below the tengwa distinguishes it visually from the above-tengwa vowel tehtar.

Example contrast:
- saam /sa:m/ "three" (three dots above)
- sam /s6m/ "heart" (underdot)

### New vowels

**Short /6/ (Jyutping "a"):** Single dot below the tengwa (underdot). Only appears before codas (-i, -u, -m, -n, -ng, -p, -t, -k). The underdot signals "reduced/centralized" quality.

**Front rounded /9:/ (Jyutping "oe"):** Left curl (o-tehta) combined with single dot (i-tehta), placed side by side above the tengwa. The phoneme /9:/ has the lip rounding of /o/ and the tongue position approaching /i/. This parallels the mode's treatment of /y/ as u+i tehta.

**Central rounded /8/ (Jyutping "eo"):** Right curl (u-tehta) above plus underdot below. This short vowel appears only before -n and -t. It is centralized and rounded, related to /u/ but more central. The u-tehta captures rounding; the underdot signals centralization.

### Diphthongs

Following the Mandarin mode's approach, falling diphthongs write only the nuclear vowel tehta. The offglide is predictable from the syllable structure.

| Jyutping | IPA | Tehta | Notes |
|----------|-----|-------|-------|
| aai | /a:i/ | a-tehta | glide to /i/ implied |
| aau | /a:u/ | a-tehta | glide to /u/ implied |
| ai | /6i/ | underdot | short nucleus |
| au | /6u/ | underdot | short nucleus |
| ei | /ei/ | e-tehta | glide to /i/ implied |
| eoi | /8y/ | u+underdot | glide to /y/ implied |
| iu | /i:u/ | i-tehta | glide to /u/ implied |
| oi | /O:i/ | o-tehta | glide to /i/ implied |
| ou | /ou/ | o-tehta | glide to /u/ implied |
| ui | /u:i/ | u-tehta | glide to /i/ implied |

### Rising diphthongs

Rising diphthongs (onglide + nucleus) use medial glide tengwar between the initial and nuclear vowel:

| Pattern | Structure |
|---------|-----------|
| gwaa | calma + w-curl + vala + a-tehta |
| gwaai | calma + w-curl + vala + a-tehta |
| gwok | calma + w-curl + vala + o-tehta + final |

The labiovelar initials gw- and kw- use vala as a glide marker between the initial and nuclear vowel.

### Syllabic nasals

Cantonese has two syllabic nasals that function as complete syllables:

| Jyutping | IPA | Tengwar |
|----------|-----|---------|
| m | /m=/ | malta (no vowel tehta) + tone |
| ng | /N=/ | noldo (no vowel tehta) + tone |

Examples:
- m4 "not" (malta + low-falling tone mark)
- ng5 "five" (noldo + low-rising tone mark)

These carry tone and require no vowel tehta. A bare nasal tengwa with a tone mark signals a syllabic nasal.

### Vowel-only syllables (null initial)

Syllables beginning with a vowel use the short carrier (telco):

- aa /a:/ -> telco + a-tehta
- ai /6i/ -> telco + underdot
- ou /ou/ -> telco + o-tehta

## Final consonants

Cantonese permits six coda consonants: three nasals and three unreleased stops. This is the major structural difference from Mandarin, which allows only -n and -ng.

### Nasal codas

| Jyutping | IPA | Tengwa | Codepoint |
|----------|-----|--------|-----------|
| -m | /m/ | malta | U+E015 |
| -n | /n/ | numen | U+E005 |
| -ng | /N/ | noldo | U+E025 |

Same tengwar as the corresponding initials. Position after the vowel distinguishes coda from onset.

### Stop codas

| Jyutping | IPA | Tengwa | Codepoint |
|----------|-----|--------|-----------|
| -p | /p-/ | parma | U+E011 |
| -t | /t-/ | tinco | U+E001 |
| -k | /k-/ | calma | U+E021 |

**Design decision:** Final stops use the same tengwar as their corresponding initial stops. Position distinguishes them.

**Rationale:**
1. **Position is sufficient.** Sinitic syllable structure is strictly (C)V(C). The initial consonant precedes the vowel; the final consonant follows it. This distinction is absolute.
2. **Tengwar precedent.** Tolkien's Elvish modes use the same principle: numen represents /n/ in both onset and coda positions.
3. **Phonemic, not phonetic.** Final stops are unreleased [p-, t-, k-] in Cantonese, but this is phonetic detail, not a phonemic contrast. The script is phonemic.
4. **Use Grade 1 (unaspirated).** Final stops are never aspirated. They map to parma, tinco, calma (Grade 1), not to the aspirated forms.

### Examples with final stops

| Jyutping | IPA | Tengwar structure |
|----------|-----|-------------------|
| sap6 | /sa:p-/ | thule + a-tehta + parma + tone |
| jat1 | /j6t-/ | anna + underdot + tinco + tone |
| luk6 | /luk-/ | lambe + u-tehta + calma + tone |
| baak3 | /pa:k-/ | parma + a-tehta + calma + tone |

### The entering tones

Syllables with stop codas correspond to the historical "entering tones" (yap6sing1) that preserve Middle Chinese finals lost in Mandarin. In traditional Cantonese phonology, these are sometimes counted as separate tones (7, 8, 9). In modern analysis, they carry the same pitch contours as open-syllable tones 1, 3, and 6, just shorter.

This mode follows the modern 6-tone analysis. The stop coda implies the "checked" or "entering" quality; no separate tone mark is needed.

## Tones

Cantonese has six phonemically distinct tones. The mode extends the Mandarin tone system by combining **iconographic contours** with **register modifiers**.

### The six tones

| Tone | Jyutping | Chao | Description | Mark |
|------|----------|------|-------------|------|
| 1 | 1 | 55 | high level | flat bar |
| 2 | 2 | 25 | high rising | rising stroke |
| 3 | 3 | 33 | mid level | flat bar + single dot |
| 4 | 4 | 21 | low falling | falling stroke + double dot |
| 5 | 5 | 23 | low rising | rising stroke + double dot |
| 6 | 6 | 22 | low level | flat bar + double dot |

### Design principle

Rather than inventing six unrelated marks, the system uses the Mandarin mode's iconographic contours combined with register modifiers:

- **High register** = plain mark (no modifier)
- **Mid register** = mark + single dot below the mark
- **Low register** = mark + double dot below the mark

The contour shape shows pitch movement. The dots show register height. This is systematic and learnable.

### Tone marks with codepoints

**Contour marks** (below-tengwa position):

| Mark | Shape | Codepoint | Glyph Name |
|------|-------|-----------|------------|
| Flat bar | horizontal line | U+E050 | nasalizer-teng (overbar/andaith) |
| Rising stroke | acute | U+E046 | acute-teng |
| Falling stroke | grave | U+E054 | grave-teng |

**Register modifiers** (below the contour mark):

| Modifier | Meaning | Codepoint | Glyph Name |
|----------|---------|-----------|------------|
| (none) | high register | -- | -- |
| Single dot | mid register | U+E045 | unutixe-teng |
| Double dot | low register | U+E043 | dotdblbelow-teng |

### Complete tone inventory

| Tone | Visual | Composition | Codepoints |
|------|--------|-------------|------------|
| 1 (high level) | flat bar | U+E050 | U+E050 |
| 2 (high rising) | rising stroke | U+E046 | U+E046 |
| 3 (mid level) | flat bar + dot | U+E050 + U+E045 | U+E050 + U+E045 |
| 4 (low falling) | falling + double-dot | U+E054 + U+E043 | U+E054 + U+E043 |
| 5 (low rising) | rising + double-dot | U+E046 + U+E043 | U+E046 + U+E043 |
| 6 (low level) | flat bar + double-dot | U+E050 + U+E043 | U+E050 + U+E043 |

### Placement

Tone marks are placed **below the tengwa** bearing the nuclear vowel:

```
  [vowel tehta]
  [  tengwa   ]
  [contour mark]
  [register dot(s)]
```

For composed marks, fonts may implement this as a single combined glyph or as stacked combining marks.

### Checked tones (entering tones)

Syllables ending in /-p/, /-t/, /-k/ use the **same tone marks** as their open counterparts. The final stop consonant implies the checked quality; no separate mark is needed.

| Traditional Tone | Corresponds To | Mark |
|------------------|----------------|------|
| 7 (high checked) | Tone 1 | flat bar |
| 8 (mid checked) | Tone 3 | flat bar + dot |
| 9 (low checked) | Tone 6 | flat bar + double-dot |

### Carrier placement (fallback)

When rendering with a typeface that lacks below-tengwa diacritics, append a short carrier (telco) after the syllable. The contour mark appears above the carrier as a tehta:

| Tone | Tehta on carrier |
|------|------------------|
| 1 (high level) | overbar (andaith) |
| 2 (high rising) | acute stroke |
| 3 (mid level) | overbar + underdot |
| 4 (low falling) | grave stroke + double-underdot |
| 5 (low rising) | acute stroke + double-underdot |
| 6 (low level) | overbar + double-underdot |

## Syllable structure

Cantonese syllables follow the template:

```
(Initial) (Medial) Nucleus (Coda) Tone
```

Where:
- **Initial:** One of 19 consonants, or null
- **Medial:** /w/ only (limited distribution, in gw-/kw- initials)
- **Nucleus:** A vowel tehta (or syllabic nasal)
- **Coda:** One of -m, -n, -ng, -p, -t, -k, or none
- **Tone:** One of 6 marks

### Composition rules

1. The initial tengwa carries the nuclear vowel tehta.
2. If a medial glide is present, it appears as a separate tengwa between the initial and coda.
3. Coda consonants follow the vowel-bearing tengwa.
4. The tone mark appears below the vowel-bearing tengwa.
5. Null initials use the carrier (telco).

### Visual structure examples

**Open syllable (no coda):**
```
  [vowel tehta]
  [  initial  ]
  [ tone mark ]
```

**Syllable with nasal coda:**
```
  [vowel tehta]
  [  initial  ] [nasal coda]
  [ tone mark ]
```

**Syllable with stop coda:**
```
  [vowel tehta]
  [  initial  ] [stop coda]
  [ tone mark ]
```

**Syllable with medial glide:**
```
  [vowel tehta]
  [  initial  ] [glide] [coda]
  [ tone mark ]
```

## Sample syllables

### Minimal pairs demonstrating vowel contrast

| Jyutping | Meaning | Structure |
|----------|---------|-----------|
| saam1 | three | thule + a-tehta + malta + T1 |
| sam1 | heart | thule + underdot + malta + T1 |

### Minimal pairs demonstrating tone contrast

| Jyutping | Meaning | Structure |
|----------|---------|-----------|
| si1 | poem | thule + i-tehta + T1 (flat bar) |
| si2 | history | thule + i-tehta + T2 (rising) |
| si3 | try | thule + i-tehta + T3 (flat bar + dot) |
| si4 | time | thule + i-tehta + T4 (falling + double-dot) |
| si5 | market | thule + i-tehta + T5 (rising + double-dot) |
| si6 | be | thule + i-tehta + T6 (flat bar + double-dot) |

### Syllables with final stops

| Jyutping | Meaning | Structure |
|----------|---------|-----------|
| sap6 | ten | thule + a-tehta + parma + T6 |
| baat3 | eight | parma + a-tehta + tinco + T3 |
| baak3 | hundred | parma + a-tehta + calma + T3 |
| baak6 | white | parma + a-tehta + calma + T6 |
| bak1 | north | parma + a-tehta + calma + T1 |

### Syllables with labiovelar initials

| Jyutping | Meaning | Structure |
|----------|---------|-----------|
| gwaa1 | melon | calma + w-curl + vala + a-tehta + T1 |
| kwaa1 | boast | anga + w-curl + vala + a-tehta + T1 |
| gwok3 | country | calma + w-curl + vala + o-tehta + calma + T3 |

### Syllables with new Cantonese vowels

| Jyutping | Meaning | Structure |
|----------|---------|-----------|
| soeng2 | think | thule + oe-tehta (o+i) + noldo + T2 |
| goek3 | foot | calma + oe-tehta (o+i) + calma + T3 |
| seon3 | letter | thule + eo-tehta (u+underdot) + numen + T3 |
| ceot1 | exit | ext.ando + eo-tehta + tinco + T1 |

### Syllabic nasals

| Jyutping | Meaning | Structure |
|----------|---------|-----------|
| m4 | not | malta + T4 (falling + double-dot) |
| ng5 | five | noldo + T5 (rising + double-dot) |

### Full syllable: Hong Kong

hoeng1gong2 "Hong Kong"

| Syllable | Structure |
|----------|-----------|
| hoeng1 | hwesta + oe-tehta (o+i) + noldo + T1 |
| gong2 | calma + o-tehta + noldo + T2 |

## Comparison with Mandarin mode

### Consonants

| Feature | Mandarin | Cantonese |
|---------|----------|-----------|
| Retroflex series | Column IV (zh, ch, sh, r) | Absent |
| Palatal affricates | Column III + palatal mark (j, q, x) | Absent |
| Velar nasal initial | Coda only | Initial and coda (ng-) |
| Labiovelar stops | Absent | gw, kw with w-curl |
| Stop codas | Absent | -p, -t, -k |
| Bilabial coda | Absent | -m |

### Vowels

| Feature | Mandarin | Cantonese |
|---------|----------|-----------|
| Phonemic length | No | Yes (aa vs a) |
| Short central /6/ | No | Yes (underdot) |
| Front rounded /9/ | No | Yes (oe, o+i tehta) |
| Central rounded /8/ | No | Yes (eo, u+underdot) |
| Syllabic nasals | No | Yes (m, ng) |
| Apical vowels | Yes (after z, c, s, zh, ch, sh, r) | No |

### Tones

| Feature | Mandarin | Cantonese |
|---------|----------|-----------|
| Number of tones | 4 (+neutral) | 6 |
| Dipping contour | Yes (Tone 3) | No |
| Level tones | 1 (high) | 3 (high, mid, low) |
| Register modifiers | Not needed | Single/double dot |
| Checked syllables | Absent | Present (final stops) |

### Shared features

These design elements carry over unchanged:

1. **Aspiration via doubled bow** (Grade 2 = aspirated)
2. **Alveolar affricates z/c** (extended tinco/ando)
3. **Fricative s** (thule)
4. **Labials b/p/m/f** (parma, umbar, malta, formen)
5. **Alveolars d/t/n/l** (tinco, ando, numen, lambe)
6. **Velars g/k** (calma, anga)
7. **Nasal codas -n/-ng** (numen, noldo)
8. **Palatal glide j** (anna)
9. **Labiovelar glide w** (vala)
10. **Null initial** (telco carrier)
11. **Quenya-style tehtar placement** (vowel on preceding consonant)
12. **Below-tengwa tone placement**

## Font requirements

### Glyphs from Mandarin mode

All Mandarin mode glyphs are used. The extended Alcarin Tengwar font includes them.

### New glyphs for Cantonese

| Glyph | Purpose | Codepoint | Status |
|-------|---------|-----------|--------|
| Underdot | short /6/ and centralized /8/ | U+E045 | Existing (unutixe-teng) |
| W-curl below | labialization mark | U+E06A | Needs verification |
| Double-dot below | low register tone modifier | U+E043 | Existing (dotdblbelow-teng) |

### Combination tehtar

These combinations require no new glyphs but may benefit from kerning adjustments:

- **o+i tehta** for /9:/ (oe)
- **u+i tehta** for /y:/ (yu)
- **u-tehta + underdot** for /8/ (eo)
- **contour + register dots** for composed tones

### Rendering notes

The Alcarin Tengwar Extended font includes all required below-marks. For fonts lacking these marks, the carrier placement fallback provides compatibility with stock Tengwar fonts.

## Summary

The Cantonese Tengwar mode:

1. **Extends the Mandarin framework** with additional vowels, tones, and final consonants
2. **Uses 19 initials** mapped to 17 distinct tengwar (14 inherited, 3 Cantonese-specific)
3. **Represents 9 vowel qualities** using 6 tehtar plus 3 combinations
4. **Marks 6 tones** using 3 contour shapes and 3 register levels
5. **Writes final stops** using the same tengwar as their corresponding initials
6. **Maintains compatibility** with the Mandarin mode where phonemes overlap

The mode is phonemically accurate, visually systematic, and extensible to other Yue dialects.

## References

- The Linguistic Society of Hong Kong. (1993). *Jyutping romanisation scheme*. https://jyutping.org/
- Bauer, R. S., & Benedict, P. K. (1997). *Modern Cantonese Phonology*. Mouton de Gruyter.
- Matthews, S., & Yip, V. (2011). *Cantonese: A Comprehensive Grammar* (2nd ed.). Routledge.
- Zee, E. (1999). Chinese (Hong Kong Cantonese). *Handbook of the International Phonetic Association*, 58-60.
