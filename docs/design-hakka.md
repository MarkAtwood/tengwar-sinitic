# Hakka Tengwar Mode Design

This document specifies adaptations for Hakka (primarily Sixian dialect) building on the Cantonese mode infrastructure. Most mappings inherit directly; only differences are documented here.

## Scope

Primary dialect: **Sixian (四縣)**, the most widely spoken Taiwanese Hakka variety.

Optional extension: Hailu (海陸), which adds postalveolar consonants and a 7th tone.

## What Inherits Unchanged from Cantonese

### Consonants (15 of 18 Sixian initials)

These mappings carry over directly:

| Hakka | IPA | Tengwa | Grid |
|-------|-----|--------|------|
| b | /p/ | parma | II-1 |
| p | /pʰ/ | umbar | II-2 |
| m | /m/ | malta | II-5 |
| f | /f/ | formen | II-3 |
| d | /t/ | tinco | I-1 |
| t | /tʰ/ | ando | I-2 |
| n | /n/ | numen | I-5 |
| l | /l/ | lambe | I-6 |
| g | /k/ | calma | III-1 |
| k | /kʰ/ | anga | III-2 |
| ng | /ŋ/ | noldo | III-5 |
| h | /h/ | hwesta | III-3 |
| z | /ts/ | ext. tinco | I-1 ext. |
| c | /tsʰ/ | ext. ando | I-2 ext. |
| s | /s/ | thule | I-3 |

### Final consonants

All six finals use identical Cantonese mappings:

| Final | IPA | Tengwa |
|-------|-----|--------|
| -m | /m/ | malta |
| -n | /n/ | numen |
| -ng | /ŋ/ | noldo |
| -p | /p̚/ | parma |
| -t | /t̚/ | tinco |
| -k | /k̚/ | calma |

See `design-final-stops.md` for rationale.

### Vowels (5 of 6 monophthongs)

| Hakka | IPA | Tehta | Same as |
|-------|-----|-------|---------|
| a | /a/ | a-tehta (three dots) | Cantonese aa |
| e | /ɛ/ | e-tehta (acute) | Cantonese e |
| i | /i/ | i-tehta (single dot) | Cantonese i |
| o | /ɔ/ | o-tehta (left curl) | Cantonese o |
| u | /u/ | u-tehta (right curl) | Cantonese u |

### Diphthongs

All Hakka diphthongs use the same tehta-for-nucleus pattern as Cantonese:

| Hakka | IPA | Tehta |
|-------|-----|-------|
| ai | /ai/ | a-tehta |
| au | /au/ | a-tehta |
| eu | /ɛu/ | e-tehta |
| oi | /ɔi/ | o-tehta |
| ia | /ia/ | a-tehta (with anna glide) |
| ie | /ie/ | e-tehta (with anna glide) |
| io | /iɔ/ | o-tehta (with anna glide) |
| iu | /iu/ | u-tehta (with anna glide) |
| ui | /ui/ | i-tehta (with vala glide) |
| iau | /iau/ | a-tehta (with anna glide) |

## Hakka-Specific Mappings

### 1. Initial /v/ (voiced labiodental)

Hakka has /v/ ~ /ʋ/ from Middle Chinese *m- before certain rimes. Cantonese lacks this phoneme.

| Hakka | IPA | Tengwa | Grid |
|-------|-----|--------|------|
| v | /v/ | ampa | II-4 |

**Rationale:** Ampa is the Grade 4 (voiced fricative) position in the labial series. This follows the Tengwar phonetic grid: formen (/f/) is Grade 3 (voiceless fricative), ampa is its voiced counterpart. The phonetic relationship /f/ : /v/ mirrors the grid relationship formen : ampa.

**Examples:**
- 武 "vu" (martial)
- 屋 "vuk" (house)
- 文 "vun" (writing)

### 2. Palatal affricates and fricative (j, q, x)

Sixian has distinct palatals /tɕ, tɕʰ, ɕ/ that Cantonese lacks but Mandarin has.

| Hakka | IPA | Tengwa | Source |
|-------|-----|--------|--------|
| j | /tɕ/ | calma + palatal mark | from Mandarin mode |
| q | /tɕʰ/ | anga + palatal mark | from Mandarin mode |
| x | /ɕ/ | hwesta + palatal mark | from Mandarin mode |

These use the same convention as Mandarin: velar tengwar plus the below-tengwa palatal diacritic.

### 3. Apical vowel /ɨ/ (ii)

The syllabic alveolar approximant [ɹ̩], romanized "ii", occurs only after alveolars (z, c, s). This is the same phoneme as Mandarin's apical vowel in "zi, ci, si".

| Hakka | IPA | Tehta | Context |
|-------|-----|-------|---------|
| ii | /ɨ/ ~ /ɹ̩/ | unutixe (syllabic mark) | after z, c, s only |

**Rationale:** The unutixe mark (syllabic indicator) already exists in Tengwar for consonants functioning as syllable nuclei. The apical vowel is phonetically a syllabic consonant-like sound. Using unutixe parallels its traditional function.

**Alternative considered:** Context-dependent null marking (the vowel is predictable after z/c/s). Rejected because explicit marking aids readability and aligns with the Taiwan MOE romanization choice to mark it distinctly as "ii".

## Sixian Tone Mapping

Sixian has 6 tones, using the extended tone system from `design-tones-extended.md`.

| Tone | Category | Chao | Description | Mark |
|------|----------|------|-------------|------|
| 1 | 陰平 | 24 | mid-rising | rising stroke |
| 2 | 陽平 | 11 | low level | flat bar + double-dot |
| 3 | 上聲 | 31 | mid-falling | falling stroke + dot |
| 4 | 去聲 | 55 | high level | flat bar |
| 5 | 陰入 | 2 | low checked | flat bar + double-dot |
| 6 | 陽入 | 5 | high checked | flat bar |

### Rationale for tone assignments

The extended system maps contour shape (flat/rising/falling) and register (high/mid/low) independently:

- **Tone 1 (24, mid-rising):** Rising stroke alone. The "mid" starting point is implicit; rising is the salient feature.
- **Tone 2 (11, low level):** Flat bar + double-dot. Level contour at low register.
- **Tone 3 (31, mid-falling):** Falling stroke + single dot. Falling contour at mid register.
- **Tone 4 (55, high level):** Flat bar alone. Level contour at high register.
- **Tones 5/6 (checked):** Final stop implies checked quality; pitch mark follows the same logic as corresponding open-syllable tones.

### Checked tone simplification

Tones 5 and 6 occur only on syllables ending in -p, -t, -k. The final stop consonant distinguishes them from open-syllable tones with the same pitch. No additional marking needed beyond the standard tone mark.

## Hailu Dialect Extension (Optional)

Hailu differs from Sixian in two ways:

### Additional consonants (postalveolars)

| Hailu | IPA | Tengwa | Notes |
|-------|-----|--------|-------|
| zh | /tʃ/ | quesse | reuse Mandarin retroflex position |
| ch | /tʃʰ/ | ungwe | reuse Mandarin retroflex position |
| sh | /ʃ/ | harma | reuse Mandarin retroflex position |
| rh | /ʒ/ | ore | voiced counterpart |

**Note:** Sixian merges these as alveolar z, c, s. The Hailu extensions use the same tengwar as Mandarin retroflexes since these occupy similar phonological space (post-alveolar articulation).

### Seventh tone

Hailu splits the Qu category into Yin and Yang, yielding 7 tones. The 7th tone (Yang Qu, Chao 33) uses:

| Tone | Category | Chao | Mark |
|------|----------|------|------|
| 5 | 陽去 | 33 | flat bar + dot |

This is mid-level, using the same mark as Cantonese tone 3.

## Differences from Cantonese Summary

| Feature | Cantonese | Hakka | Impact |
|---------|-----------|-------|--------|
| /v/ initial | absent | present | +1 tengwa (ampa) |
| Palatals j/q/x | absent | present | reuse Mandarin marks |
| Apical vowel /ɨ/ | absent | present | +1 tehta (unutixe) |
| Labialized gw/kw | present | absent | not needed |
| Short /ɐ/, /ɵ/, /œ/ | present | absent | not needed |
| Tone values | different | different | same system, different assignments |

## Font Requirements

Hakka requires no new glyphs beyond what Cantonese and Mandarin modes already need:

- **ampa** (for /v/): Standard tengwa, already in Alcarin
- **palatal mark**: From Mandarin mode
- **unutixe**: Standard syllabic marker, already in Alcarin
- **extended tone marks**: From Cantonese mode

## Examples

| Hakka | IPA | Gloss | Tengwar structure |
|-------|-----|-------|-------------------|
| ngai | /ŋai²⁴/ | I/me | noldo + a-tehta + rising |
| vuk | /vuk̚⁵/ | house | ampa + u-tehta + calma + flat |
| sii | /sɨ⁵⁵/ | four | thule + unutixe + flat |
| jam | /tɕam²⁴/ | needle | calma+pal. + a-tehta + malta + rising |

---

*Hakka mode design complete. Inherits ~90% from Cantonese; deltas are minimal.*
