# Min (Southern Min) Phonology for Tengwar Mode

This document describes the phonological inventory of Southern Min, focusing on **Taiwanese Hokkien** as the primary variety, with notes on Teochew variations. It serves as the foundation for a Tengwar-Min mode.

## Overview

Southern Min (Minnan/Hokkien) is spoken by approximately 50 million people across Taiwan, Fujian province, Southeast Asia, and diaspora communities worldwide. Unlike Mandarin, Hokkien preserves many archaic Chinese features including:

- **Voiced obstruents** (Mandarin has none)
- **Final stop consonants** (-p, -t, -k, -ʔ)
- **Nasal vowels** (a distinctive feature)
- **7-8 tones** with extensive tone sandhi

The two main dialect bases are **Quanzhou** (泉州) and **Zhangzhou** (漳州). Taiwanese Hokkien blends both, with regional variation.

---

## 1. Consonant Inventory

### Initials

Taiwanese Hokkien has **18 consonant phonemes** that can appear as syllable onsets. The system differs markedly from Mandarin in having a three-way laryngeal contrast: **voiceless unaspirated**, **voiceless aspirated**, and **voiced**.

| Place | Unasp. | Asp. | Voiced | Nasal | Fricative | Approx. |
|-------|--------|------|--------|-------|-----------|---------|
| Bilabial | p /p/ | ph /pʰ/ | b /b/ | m /m/ | | |
| Alveolar | t /t/ | th /tʰ/ | | n /n/ | s /s/ | l /l/ |
| Alveolar Affr. | ts /ts/ | tsh /tsʰ/ | j /dz~z/ | | | |
| Velar | k /k/ | kh /kʰ/ | g /g/ | ng /ŋ/ | h /h/ | |
| Glottal | | | | | | |

**IPA Consonant Chart:**

| Tâi-lô | POJ | IPA | Description |
|--------|-----|-----|-------------|
| p | p | /p/ | voiceless bilabial stop |
| ph | ph | /pʰ/ | aspirated bilabial stop |
| b | b | /b/ | voiced bilabial stop |
| m | m | /m/ | bilabial nasal |
| t | t | /t/ | voiceless alveolar stop |
| th | th | /tʰ/ | aspirated alveolar stop |
| n | n | /n/ | alveolar nasal |
| l | l | /l/ ~ /ɾ/ | alveolar lateral/tap |
| ts | ch | /ts/ | voiceless alveolar affricate |
| tsh | chh | /tsʰ/ | aspirated alveolar affricate |
| j | j | /dz/ ~ /z/ | voiced alveolar affricate/fricative |
| s | s | /s/ | voiceless alveolar fricative |
| k | k | /k/ | voiceless velar stop |
| kh | kh | /kʰ/ | aspirated velar stop |
| g | g | /g/ | voiced velar stop |
| ng | ng | /ŋ/ | velar nasal (also syllabic) |
| h | h | /h/ | glottal fricative |
| (zero) | (zero) | ∅ | null initial |

**Notes:**
- /l/ is often realized as an alveolar tap [ɾ] in rapid speech.
- /b/ and /g/ may have prenasalized allophones [ᵐb] and [ᵑg] in some environments.
- /ts, tsʰ, s/ become palatalized [tɕ, tɕʰ, ɕ] before /i/ and /iⁿ/.
- Syllabic /m/ and /ŋ/ can serve as syllable nuclei (e.g., m̄ "not").

### Tengwar Mapping Implications

The voiced series /b, g, dz/ presents a key difference from Mandarin. The Mandarin mode uses Grade 1/2 for aspiration contrast. Min requires a three-way distinction:

| Contrast | Example | Tengwar consideration |
|----------|---------|----------------------|
| /p/ vs /pʰ/ vs /b/ | pa vs pha vs ba | Need Grade 1, 2, and 3? |
| /k/ vs /kʰ/ vs /g/ | ka vs kha vs ga | Or use separate series? |
| /ts/ vs /tsʰ/ vs /dz/ | tsa vs tsha vs ja | |

**Design decision required:** See issue `Tengwar-Mandarin-xxx` for three-way laryngeal contrast.

---

## 2. Vowel Inventory

### Oral Vowels

Taiwanese Hokkien has **5-6 basic oral vowels**, with some dialect variation:

| Tâi-lô | POJ | IPA | Description |
|--------|-----|-----|-------------|
| a | a | /a/ | open central |
| e | e | /e/ | close-mid front |
| i | i | /i/ | close front |
| o | o | /o/ | close-mid back rounded |
| oo | o͘ | /ɔ/ | open-mid back rounded |
| u | u | /u/ | close back rounded |

**Dialect variations:**
- Quanzhou varieties add central vowels /ɨ/ and /ə/.
- Zhangzhou varieties have /ɛ/ in some positions.
- The "mixed" Taiwanese standard tends toward the Quanzhou core.

### Nasal Vowels (Critical for Tengwar Design)

**This is the most distinctive feature of Min phonology.** Hokkien has a full set of **nasalized vowel phonemes**, written with `nn` in Tâi-lô or superscript `ⁿ` in POJ:

| Tâi-lô | POJ | IPA | Example |
|--------|-----|-----|---------|
| ann | aⁿ | /ã/ | sann /sã/ "three (colloquial)" |
| enn | eⁿ | /ẽ/ | khenn /kʰẽ/ "pit" |
| inn | iⁿ | /ĩ/ | phinn /pʰĩ/ "nose" |
| onn | oⁿ | /ɔ̃/ | honn /hɔ̃/ "yes?" |
| unn | uⁿ | /ũ/ | (rare in isolation) |

**Nasal vowel phonology:**
- Nasalization is **phonemic**, not allophonic. Minimal pairs exist: /a/ vs /ã/.
- Nasal vowels occur primarily in **colloquial (白讀) readings**, not literary (文讀).
- Nasal vowels cannot co-occur with nasal coda consonants (-m, -n, -ng). They are mutually exclusive.
- Nasal diphthongs and triphthongs exist: /ãĩ/, /ũãĩ/, etc.

### Tengwar Design Challenge: Nasal Vowel Tehtar

**This requires new tehtar.** Options:

1. **Tilde-below modifier:** Add a tilde below existing vowel tehtar (cf. Mandarin tone marks below)
2. **Doubled tehtar:** Double the vowel tehta to indicate nasalization
3. **Superscript nasal:** Add a small númen-like mark after the vowel tehta
4. **Combined tehta:** Design new compound tehtar for each nasal vowel

**Recommendation:** Tilde-below is most consistent with the below-mark pattern used for tones. Requires font extension.

See issue `Tengwar-Mandarin-poa` for nasal vowel tehtar design.

### Diphthongs and Triphthongs

| Tâi-lô | IPA | Notes |
|--------|-----|-------|
| ai | /ai/ | falling diphthong |
| au | /au/ | falling diphthong |
| ia | /ia/ | rising diphthong |
| io | /io/ | |
| iu | /iu/ | |
| ua | /ua/ | |
| ue | /ue/ | |
| ui | /ui/ | |
| iau | /iau/ | triphthong |
| uai | /uai/ | triphthong |

Nasalized versions also occur: /ãĩ/, /ãũ/, /ĩã/, /ũãĩ/, etc.

---

## 3. Final Consonants (Codas)

Hokkien preserves the Middle Chinese final consonants that Mandarin has lost. This is crucial for the entering tones (tones 4 and 8).

### Nasal Finals

| Tâi-lô | IPA | Example |
|--------|-----|---------|
| -m | /m/ | lâm /lam/ "south" |
| -n | /n/ | hún /hun/ "powder" |
| -ng | /ŋ/ | tang /taŋ/ "east" |

### Stop Finals (Checked Syllables)

These create the "entering tone" (入聲) syllables that carry tones 4 and 8:

| Tâi-lô | IPA | Example |
|--------|-----|---------|
| -p | /p̚/ | ta̍p /tap̚/ "answer" |
| -t | /t̚/ | pu̍t /put̚/ "Buddha" |
| -k | /k̚/ | ho̍k /hɔk̚/ "blessing" |
| -h | /ʔ/ | o̍h /ɔʔ/ "learn" |

**Notes:**
- Stop finals are **unreleased** [p̚, t̚, k̚].
- The glottal stop /-ʔ/ is written `-h` in Tâi-lô (or `-ʔ` in linguistic notation).
- Checked syllables are inherently short; they can only carry tones 4 or 8.
- **Stop finals and nasal vowels are mutually exclusive** with nasal finals.

### Teochew Variation

Teochew has **lost the -t final**. Where Hokkien has /-t/, Teochew has /-k/:
- Hokkien "huat" 發 → Teochew "huak"
- Hokkien "pu̍t" 佛 → Teochew "puk"

---

## 4. Tone System

### Taiwanese Hokkien: Seven Tones

Taiwanese has **seven phonemic tones**, traditionally numbered 1-5 and 7-8 (tone 6 merged with tone 2 historically). Tones 4 and 8 only occur on checked syllables.

| Tone # | Name | Chao Value | Contour | Syllable Type |
|--------|------|------------|---------|---------------|
| 1 | 陰平 (dark level) | 55 or 44 | high level | smooth |
| 2 | 陰上 (dark rising) | 51 or 53 | high falling | smooth |
| 3 | 陰去 (dark departing) | 31 or 21 | low falling | smooth |
| 4 | 陰入 (dark entering) | 32 or 3 | mid/low short | checked (-p/-t/-k/-h) |
| 5 | 陽平 (light level) | 24 or 13 | rising | smooth |
| 7 | 陽去 (light departing) | 33 or 22 | mid level | smooth |
| 8 | 陽入 (light entering) | 4 or 5 | high short | checked (-p/-t/-k/-h) |

**Dialect variation in tone values:**
- Northern (Quanzhou-influenced): Tone 1 may be 33-44; Tone 5 sandhi → 33
- Southern (Zhangzhou-influenced): Tone 1 may be 55; Tone 5 sandhi → 21

### Neutral Tone (Tone 0)

A **neutral/light tone** exists for grammatical particles and certain suffixes:
- Written with `--` prefix in Tâi-lô: `--a`, `--lah`, `--honnh`
- Realized as low [21] or low-falling [31]
- The preceding syllable retains its **citation tone** (no sandhi)

### Teochew: Eight Tones

Teochew preserves the eighth tone that Taiwanese merged:

| Tone # | Name | Chao Value | Contour |
|--------|------|------------|---------|
| 1 | 陰平 | 33 | mid level |
| 2 | 陰上 | 53 | high falling |
| 3 | 陰去 | 213 | dipping |
| 4 | 陰入 | 2 | low short |
| 5 | 陽平 | 55 | high level |
| 6 | 陽上 | 35 | mid rising |
| 7 | 陽去 | 11 | low level |
| 8 | 陽入 | 5 | high short |

---

## 5. Tone Sandhi Rules

**Policy decision: Write surface (post-sandhi) tones, not citation tones.**

Tone sandhi in Taiwanese Hokkien is **obligatory, pervasive, and predictable**. In any phonological phrase, all syllables except the final one undergo sandhi. The rules are right-dominant: only the rightmost syllable keeps its citation tone.

### Basic Sandhi Circle (Smooth Tones)

The five smooth tones transform in a circular pattern:

```
Citation → Sandhi

   1 (55)  →  7 (33)
     ↑           ↓
   2 (51)  ←  3 (21)
     ↑
   5 (24)  →  7 (33)  [or → 3 in some dialects]
```

**Simplified rules:**
- **Tone 1 → Tone 7** (high level → mid level)
- **Tone 7 → Tone 3** (mid level → low falling)
- **Tone 3 → Tone 2** (low falling → high falling)
- **Tone 2 → Tone 1** (high falling → high level)
- **Tone 5 → Tone 7** (rising → mid level) [Quanzhou]
- **Tone 5 → Tone 3** (rising → low falling) [Zhangzhou]

### Checked Tone Sandhi

Tones 4 and 8 simply swap:

- **Tone 4 (low short) ↔ Tone 8 (high short)**

### Complete Sandhi Mapping Table

| Citation | Chao | Sandhi | Chao | Example |
|----------|------|--------|------|---------|
| 1 | 55 | 7 | 33 | tang-si (東西) |
| 2 | 51 | 1 | 55 | hó-lâng (好人) |
| 3 | 21 | 2 | 51 | sì-kang (四工) |
| 5 | 24 | 7 (or 3) | 33 | lâng-kheh (人客) |
| 7 | 33 | 3 | 21 | tōa-lâng (大人) |
| 4 | 32 | 8 | 4 | la̍t-thâu (力頭) |
| 8 | 4 | 4 | 32 | pe̍h-hún (白粉) |

### Sandhi Domain

Sandhi applies within **phonological phrases**, which roughly correspond to:
- Compound words
- Verb + object combinations
- Modifier + head noun
- Numbers + classifiers + nouns

**Exceptions where citation tone is preserved:**
- Phrase-final position
- Before neutral tone syllables (`--a`, `--lah`, etc.)
- Some emphatic or contrastive contexts
- Certain frozen expressions

### Converter Implementation

Since we write **surface tones**, the converter must:
1. Parse input with citation tones (if provided)
2. Identify phrase boundaries
3. Apply sandhi to all non-final syllables
4. Output surface tone marks

Alternatively, input could already be in surface tones (how the word is actually pronounced).

See issue `Tengwar-Mandarin-0gl` for tone sandhi representation design.

---

## 6. Romanization Systems

### Tâi-lô (台灣閩南語羅馬字拼音方案)

The **official romanization** for Taiwanese, promoted by Taiwan's Ministry of Education since 2006. Derived from POJ with modernizations.

**Key features:**
- Uses `ts`, `tsh` instead of POJ `ch`, `chh`
- Uses `oo` instead of `o͘` (no dot-above)
- Uses `nn` instead of superscript `ⁿ`
- Tone marks: á (2), à (3), â (5), ā (7), a̍ (8), a (1/4 unmarked)

### POJ (Pe̍h-ōe-jī)

The **traditional romanization**, developed by Presbyterian missionaries in the 19th century. Still widely used, especially in religious and older texts.

**Key features:**
- Uses `ch`, `chh` for affricates
- Uses `o͘` (o with dot above) for /ɔ/
- Uses superscript `ⁿ` for nasalization
- Same tone diacritics as Tâi-lô

### Comparison Table

| Feature | Tâi-lô | POJ |
|---------|--------|-----|
| /ts/ | ts | ch |
| /tsʰ/ | tsh | chh |
| /ɔ/ | oo | o͘ |
| nasal | ann, enn | aⁿ, eⁿ |
| /ua/ | ua | oa |
| /ue/ | ue | oe |

**Recommendation for Tengwar converter:** Support both input formats, normalize to Tâi-lô internally.

---

## 7. Key Challenges for Tengwar-Min Mode

### Challenge 1: Nasal Vowels

**Problem:** Min has phonemic nasal vowels requiring distinct representation. Mandarin mode has no provision for this.

**Options:**
1. Below-tilde on vowel tehta (consistent with below-mark pattern)
2. Superscript nasal mark following vowel tehta
3. Dedicated nasal vowel tehtar

**Tracked in:** `Tengwar-Mandarin-poa`

### Challenge 2: Three-Way Laryngeal Contrast

**Problem:** Min distinguishes /p/ : /pʰ/ : /b/, but Tengwar traditionally uses Grade 1 : Grade 2 for voiceless : voiced.

**Options:**
1. Grade 1 = unaspirated, Grade 2 = aspirated, Grade 3 = voiced (if available)
2. Use aspiration mark (h-tehta?) on Grade 1 for aspirates
3. Separate tengwar series for voiced stops

### Challenge 3: Seven/Eight Tones

**Problem:** Min has 7-8 tones vs. Mandarin's 4. The iconographic marks need extension.

**Options:**
1. Extend contour mark system (more complex shapes)
2. Use two-tier marking (register + contour)
3. Number-based marks

**Tracked in:** `Tengwar-Mandarin-i26`

### Challenge 4: Glottal Stop Final

**Problem:** The glottal stop /-ʔ/ is a coda consonant with no Mandarin equivalent.

**Options:**
1. Use a dedicated tengwa (tecco? or modified ora?)
2. Use a below-mark
3. Implicit from checked tone context

### Challenge 5: Tone Sandhi Complexity

**Problem:** Nearly every syllable changes tone in connected speech. We write surface tones.

**Solution:** The converter applies sandhi rules. Output is post-sandhi. Documentation needed on phrase boundary detection.

**Tracked in:** `Tengwar-Mandarin-0gl`

---

## References

- Wikipedia: [Hokkien phonology](https://en.wikipedia.org/wiki/Hokkien_phonology)
- Wikipedia: [Taiwanese Hokkien](https://en.wikipedia.org/wiki/Taiwanese_Hokkien)
- Wikipedia: [Teochew Min](https://en.wikipedia.org/wiki/Teochew_Min)
- [Tâi-lô romanization](https://en.wikipedia.org/wiki/T%C3%A2i-u%C3%A2n_L%C3%B4-m%C3%A1-j%C4%AB_Phing-im_Hong-%C3%A0n)
- [Pe̍h-ōe-jī](https://en.wikipedia.org/wiki/Pe%CC%8Dh-%C5%8De-j%C4%AB)
- Cambridge: [The Phonetics of Taiwanese](https://www.cambridge.org/core/elements/phonetics-of-taiwanese/8F27DDDD1CD389740378237A6FD4E838)
- [Learn Teochew pronunciation guide](https://learnteochew.com/pages/pronunciation.html)
- [Taioaan Wiki: Tone sandhi](https://taioaan.org/wiki/index.php/Tone_sandhi)
