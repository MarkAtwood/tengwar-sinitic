# Shared Sinitic Tengwar Infrastructure

This document describes the common patterns and shared components across all Sinitic Tengwar modes.

---

## 1. Mode Overview

| Mode | Status | Spec File | Reference Romanization | Tones |
|------|--------|-----------|------------------------|-------|
| Mandarin | Complete | `tengwar-mandarin.md` | Pinyin | 4 (+neutral) |
| Cantonese | Complete | `tengwar-cantonese.md` | Jyutping | 6 |
| Hakka | Complete | `tengwar-hakka.md` | Taiwan MOE Hakka | 6 |
| Min | Complete | `tengwar-min.md` | Tai-lo / POJ | 7 |
| Wu | Complete | `tengwar-wu.md` | Qian Nairong / Wugniu | 5 |

### Compatibility Groups

**Group A: Mandarin/Cantonese/Hakka**
- Grade 1 = voiceless unaspirated
- Grade 2 = voiceless aspirated
- No voiced obstruents in these languages

**Group B: Min/Wu (Classical Voicing)**
- Grade 1 = voiceless unaspirated
- Grade 2 = voiced
- Aspiration marked with diacritic (U+E0B0)
- **Incompatible with Group A** due to different grade semantics
- Phonetically correct: matches Tolkien's original Tengwar design

---

## 2. Shared Consonant Patterns

### 2.1 Aspiration Contrast

**Group A (Mandarin/Cantonese/Hakka):** Uses doubled bow for aspiration

| Grade | Articulation | Example (Mandarin) |
|-------|--------------|-------------------|
| 1 (single bow) | voiceless unaspirated | parma /p/ = Pinyin "b" |
| 2 (doubled bow) | voiceless aspirated | umbar /pʰ/ = Pinyin "p" |

**Group B (Min/Wu):** Uses diacritic for aspiration, doubled bow for voicing

| Grade | Articulation | Example (Min) |
|-------|--------------|---------------|
| 1 (single bow) | voiceless unaspirated | parma /p/ = Tai-lo "p" |
| 1 + asp mark | voiceless aspirated | parma+asp /pʰ/ = Tai-lo "ph" |
| 2 (doubled bow) | voiced | umbar /b/ = Tai-lo "b" |

### 2.2 Extended Stems for Affricates

**Group A (Mandarin/Cantonese/Hakka):**

| Phoneme | Tengwa | Usage |
|---------|--------|-------|
| /ts/ | tinco-ext (U+E009) | z (Pinyin/Jyutping) |
| /tsʰ/ | ando-ext (U+E00A) | c (Pinyin/Jyutping) |

**Group B (Min/Wu):** Same tengwar, different semantics

| Phoneme | Tengwa | Usage |
|---------|--------|-------|
| /ts/ | tinco-ext (U+E009) | ts (Tai-lo), z (Wu) |
| /tsʰ/ | tinco-ext + asp | tsh (Tai-lo), c (Wu) |
| /dz/ | ando-ext (U+E00A) | j (Tai-lo), zz (Wu) |

### 2.3 Palatal Diacritic for Alveolo-Palatals

Mandarin and Hakka have alveolo-palatal consonants /tc, tch, c/ that use Column III tengwar with a below-tengwa palatal diacritic:

| Phoneme | Tengwa | Romanization |
|---------|--------|--------------|
| /tc/ | calma + palatal mark | j (Pinyin/Hakka) |
| /tch/ | anga + palatal mark | q (Pinyin/Hakka) |
| /c/ | hwesta + palatal mark | x (Pinyin/Hakka) |

Cantonese and Min lack these phonemes. Wu uses the same convention.

### 2.4 Glottal Stop (Halla) for Checked Syllables

Cantonese, Hakka, Min, and Wu preserve final stop consonants (checked syllables). The glottal stop coda uses halla:

| Mode | Final Stops | Glottal Coda |
|------|-------------|--------------|
| Mandarin | None | N/A |
| Cantonese | -p, -t, -k | N/A (stops preserved) |
| Hakka | -p, -t, -k | N/A (stops preserved) |
| Min | -p, -t, -k, -h | halla (U+E029) for -h |
| Wu | -q (merged) | halla (U+E028) for merged /-?/ |

### 2.5 Syllabic Nasals

Cantonese, Min, and Wu have syllabic nasals that function as complete syllables:

| Syllabic | Tengwa | Representation |
|----------|--------|----------------|
| /m/ | malta | bare nasal + tone mark |
| /ng/ | noldo | bare nasal + tone mark |

A bare nasal tengwa with no vowel tehta plus a tone mark signals a syllabic nasal.

---

## 3. Shared Vowel Patterns

### 3.1 Basic Tehtar

All modes share these five core vowel tehtar:

| Vowel | IPA | Tehta | Codepoint |
|-------|-----|-------|-----------|
| a | /a/ | three dots above | U+E040 |
| e | /e~E/ | acute stroke | U+E046 |
| i | /i/ | single dot above | U+E044 |
| o | /o~O/ | left curl | U+E04C |
| u | /u/ | right curl | U+E04A |

### 3.2 Combined Tehtar

The front rounded vowel /y/ (Pinyin u, Cantonese yu) combines two tehtar:

| Vowel | IPA | Composition | Usage |
|-------|-----|-------------|-------|
| u/yu | /y/ | u-tehta + i-tehta | Mandarin, Cantonese |

### 3.3 Quenya-Style Placement

All Sinitic modes place tehtar on the **preceding consonant**, following Quenya mode conventions. This works well because Sinitic syllables predominantly end in vowels or nasals.

```
  [vowel tehta]
  [  tengwa   ]
  [tone mark  ]
```

### 3.4 Mode-Specific Vowels

| Mode | Additional Vowels |
|------|-------------------|
| Cantonese | short /6/ (underdot), /9:/ (oe: o+i tehta), /8/ (eo: u+underdot) |
| Hakka | apical vowel /1/ (unutixe mark) |
| Min | nasal vowels (tilde-below diacritic) |
| Wu | schwa /e/ (underdot) |

---

## 4. Tone System

### 4.1 Design Principle: Contour + Register

The extended tone system uses two orthogonal components:

1. **Contour shape**: flat bar (level), rising stroke (rising), falling stroke (falling)
2. **Register modifier**: none (high), single dot (mid), double dot (low)

This produces a systematic inventory where shape shows pitch movement and dots show register height.

### 4.2 Contour Marks

| Contour | Shape | Codepoint | Glyph Name |
|---------|-------|-----------|------------|
| Level | horizontal bar | U+E050 | macron-teng |
| Rising | acute stroke | U+E046 | acute-teng |
| Falling | grave stroke | U+E054 | grave-teng |
| Dipping | chevron | U+E055 | caron-teng (Mandarin T3 only) |

### 4.3 Register Modifiers

| Modifier | Meaning | Codepoint | Glyph Name |
|----------|---------|-----------|------------|
| (none) | high register | -- | -- |
| single dot | mid register | U+E045 | dotbelow-teng |
| double dot | low register | U+E043 | dotdblbelow-teng |

### 4.4 Below-Tengwa Placement

All modes place tone marks **below the tengwa** bearing the nuclear vowel:

```
  [vowel tehta]
  [  tengwa   ]
  [contour mark]
  [register dot(s)]
```

### 4.5 Checked Tones

Syllables ending in stop codas (-p, -t, -k, -h) use the same tone marks as their open counterparts. The final stop consonant implies checked quality.

---

## 5. Mode-Specific Features

### 5.1 Mandarin

| Feature | Description |
|---------|-------------|
| Retroflex initials | Column IV: zh /ts`/, ch /ts`h/, sh /s`/, r /r`/ |
| 4 tones | T1 flat, T2 rising, T3 dipping (chevron), T4 falling |
| Apical vowels | Bare consonant with tone (after z/c/s/zh/ch/sh/r) |
| No final stops | Only -n, -ng codas |

### 5.2 Cantonese

| Feature | Description |
|---------|-------------|
| Long/short vowels | /a:/ (a-tehta) vs /6/ (underdot) |
| 6 tones | Using contour + register system |
| Final stops | -p, -t, -k preserved from Middle Chinese |
| Labiovelar initials | gw, kw with w-curl diacritic |
| Syllabic nasals | m, ng |

### 5.3 Hakka

| Feature | Description |
|---------|-------------|
| /v/ initial | Uses ampa (Grade 4 labial) |
| Apical vowel | ii /1/ uses unutixe mark |
| 6 tones | Same system as Cantonese, different contour values |
| Palatals | j, q, x use Mandarin convention |

### 5.4 Min

| Feature | Description |
|---------|-------------|
| Nasal vowels | Tilde-below diacritic on vowel tehta |
| Three-way laryngeal | Voiced consonants via Grade 3 reassignment |
| 7 tones | Extended contour + register system |
| Tone sandhi | Write surface (post-sandhi) tones |
| Glottal stop coda | -h uses halla |

### 5.5 Wu

| Feature | Description |
|---------|-------------|
| Classical voicing | Grade 2 = voiced (not aspirated) |
| Aspiration diacritic | Rightward curl at upper-right (U+E0B0) |
| 5 tones | Contour + register system |
| Left-dominant sandhi | First syllable determines phrase tone |
| Merged final stops | Historical *-p/*-t/*-k merged to glottal /-?/ |

---

## 6. Incompatibility Notes

### Wu Mode Incompatibility

Wu mode uses **different grade semantics** from the other four modes:

| Feature | Mandarin/Cantonese/Hakka/Min | Wu |
|---------|------------------------------|-----|
| Grade 1 | voiceless unaspirated | voiceless unaspirated |
| Grade 2 | voiceless aspirated | **voiced** |
| Grade 3 | fricative (or voiced hack) | voiceless fricative |
| Aspiration | grade distinction | **diacritic** |

**A document must declare which mode applies.** Mixed-mode text is not supported.

### Why Incompatibility is Acceptable

1. **Phonological honesty**: Each mode represents its language's contrasts faithfully
2. **Visual clarity**: No ambiguity about grade semantics within a document
3. **Classical fidelity**: Wu mode aligns with Tolkien's original Tengwar design
4. **Practical isolation**: Wu speakers read Wu texts; Mandarin speakers read Mandarin texts

---

## 7. Font Requirements

### 7.1 Glyphs in Alcarin Extended (Available)

All modes work with the extended Alcarin Tengwar font. Existing glyphs include:

| Category | Glyphs |
|----------|--------|
| Base tengwar | All Grade 1-6 in Columns I-IV |
| Extended stems | tinco-ext, ando-ext, thule-ext |
| Vowel tehtar | a, e, i, o, u tehtar |
| Underdot | U+E045 (short vowel, mid register) |
| Double-dot below | U+E043 (low register) |
| Tone contours | flat, rising, falling, dipping |
| Glottal stop | halla (U+E028/U+E029) |
| Palatal diacritic | below-tengwa double-dot |
| Labialization | w-curl below (U+E04B) |

### 7.2 New Glyphs Required

| Glyph | Codepoint | Purpose | Mode |
|-------|-----------|---------|------|
| aspiration-teng | U+E0B0 | Marks aspiration in Wu | Wu |
| tilde-below | (TBD) | Nasal vowel marker | Min |

### 7.3 Aspiration Mark Details (Wu)

- **Shape**: Rightward-opening curl (miniature halla)
- **Size**: ~1/3 height of vowel tehta
- **Position**: Upper-right of tengwa, below tehta zone
- **Anchor**: New `topright` / `_topright` anchor pair

### 7.4 Tilde-Below Details (Min)

- **Shape**: Tilde (~) curve
- **Position**: Below tengwa, above register dots
- **Purpose**: Marks vowel as nasalized
- **Combines with**: Any vowel tehta

---

## 8. References

### Specification Files

- `/Volumes/Attic/Desktop/Projects/Tengwar-Mandarin/tengwar-mandarin.md`
- `/Volumes/Attic/Desktop/Projects/Tengwar-Mandarin/tengwar-cantonese.md`
- `/Volumes/Attic/Desktop/Projects/Tengwar-Mandarin/tengwar-hakka.md`
- `/Volumes/Attic/Desktop/Projects/Tengwar-Mandarin/tengwar-min.md`
- `/Volumes/Attic/Desktop/Projects/Tengwar-Mandarin/tengwar-wu.md`

### Design Documents

- `/Volumes/Attic/Desktop/Projects/Tengwar-Mandarin/docs/design-tones-extended.md`
- `/Volumes/Attic/Desktop/Projects/Tengwar-Mandarin/docs/design-final-stops.md`
- `/Volumes/Attic/Desktop/Projects/Tengwar-Mandarin/docs/font-extension-cantonese.md`
- `/Volumes/Attic/Desktop/Projects/Tengwar-Mandarin/docs/font-extension-wu.md`

### Font Resources

- `/Volumes/Attic/Desktop/Projects/Tengwar-Mandarin/fonts/Alcarin-Tengwar/`
