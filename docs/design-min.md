# Min (Southern Min) Tengwar Mode Design

This document specifies the Tengwar mode for Southern Min languages, focusing on **Taiwanese Hokkien** as the primary variety. It extends the Mandarin and Cantonese modes with features specific to Min phonology.

## Design Summary

Min requires three new features beyond the Mandarin/Cantonese modes:

1. **Nasal vowel marking** - phonemic nasalization on vowels
2. **Extended tone inventory** - 7-8 tones instead of 4-6
3. **Glottal stop final** - the /-ʔ/ coda consonant

Additionally, Min has a **three-way laryngeal contrast** in stops (voiceless unaspirated / voiceless aspirated / voiced), unlike Mandarin's two-way contrast.

---

## 1. Nasal Vowels

This is the most significant new feature for Min. Nasal vowels are **phonemic**, not allophonic. Minimal pairs exist:

| Oral | Nasal | Meaning contrast |
|------|-------|------------------|
| /a/ sa | /ã/ sann | "sand" vs. "three" |
| /i/ si | /ĩ/ sinn | "silk" vs. "fresh" |

### Design Decision: Nasalization Diacritic

**Use a nasalization tehta (tilde-below) that combines with any vowel tehta.**

The nasalization mark appears **below the tengwa**, in the same vertical zone as register modifiers. It does not conflict with tone marks because:
- Tone contour marks go below the vowel position
- The nasalization mark attaches to the vowel tehta above
- Visually: tehta (above) + tengwa + nasal mark (below, upper) + tone mark (below, lower)

### Glyph Specification

| Mark | Shape | Codepoint | Glyph Name | Purpose |
|------|-------|-----------|------------|---------|
| Nasalization | tilde (~) | U+E044 | tilde-below-teng | Marks vowel as nasalized |

**Placement:** Below the tengwa, above any register dots (if present). For Min, the nasalization mark is the primary below-tengwa diacritic; tone marks use contour shapes rather than position.

### Nasal Vowel Tehtar Table

Each oral vowel tehta can combine with the nasalization mark:

| Tâi-lô | IPA | Tehta | Composed Form |
|--------|-----|-------|---------------|
| ann | /ã/ | a-tehta + nasal | three-dots-above + tilde-below |
| enn | /ẽ/ | e-tehta + nasal | acute-above + tilde-below |
| inn | /ĩ/ | i-tehta + nasal | dot-above + tilde-below |
| onn | /ɔ̃/ | o-tehta + nasal | left-curl + tilde-below |
| unn | /ũ/ | u-tehta + nasal | right-curl + tilde-below |

### Nasal Diphthongs and Triphthongs

Nasalization spreads across the entire nucleus. Write the nasalization mark once, on the nuclear vowel:

| Tâi-lô | IPA | Tengwar representation |
|--------|-----|------------------------|
| ainn | /ãĩ/ | telco + a-tehta + nasal + anna |
| iunn | /ĩũ/ | anna + i-tehta + nasal + vala |
| uainn | /ũãĩ/ | vala + a-tehta + nasal + anna |

For falling diphthongs, place the nasal mark on the nuclear vowel (first element). For triphthongs, place it on the central vowel.

### Mutual Exclusivity Rule

**Nasal vowels cannot co-occur with nasal codas (-m, -n, -ng).**

This is a phonotactic constraint of Min. If a syllable has a nasal vowel, it cannot end in a nasal consonant, and vice versa. The Tengwar representation naturally reflects this: either the nasalization diacritic appears (nasal vowel), or a nasal tengwa appears in coda position (nasal coda), never both.

### Font Requirements

**New glyph needed:** Tilde-below (U+E044)

This is the only new glyph required for Min nasal vowels. The mark should be:
- Positioned in the below-tengwa zone
- Sized to be visually balanced with register dots
- Curved like a tilde (~), not angular

**Alternative considered:** A superscript nasal mark (small ng-shape) after the vowel tehta. Rejected because:
1. It breaks the above/below spatial logic (vowels above, modifiers below)
2. It would interfere with tone mark placement
3. The tilde is internationally recognized for nasalization

---

## 2. Tone System (7-8 Tones)

Min has 7 phonemic tones in Taiwanese Hokkien (8 in Teochew, which preserves Tone 6). The extended tone system from the Cantonese design handles this.

### Tone Inventory

**Taiwanese Hokkien (7 tones):**

| Tone | Name | Chao | Contour | Syllable Type | Tengwar Mark |
|------|------|------|---------|---------------|--------------|
| 1 | yin-ping | 44~55 | high level | smooth | flat bar |
| 2 | yin-shang | 51~53 | high falling | smooth | falling stroke |
| 3 | yin-qu | 21~31 | low falling | smooth | falling stroke + double-dot |
| 4 | yin-ru | 32 | low short | checked | (implied by final stop) |
| 5 | yang-ping | 24~13 | rising | smooth | rising stroke |
| 7 | yang-qu | 33~22 | mid level | smooth | flat bar + dot |
| 8 | yang-ru | 4~5 | high short | checked | (implied by final stop) |

**Note:** Tone 6 merged with Tone 7 historically in most Min varieties. Teochew preserves Tone 6 as a distinct mid-rising tone.

### Checked Tone Handling

Tones 4 and 8 occur only on **checked syllables** (those ending in /-p/, /-t/, /-k/, or /-ʔ/). The presence of a final stop consonant implies the checked quality; **no separate tone mark is needed for checked tones**.

This follows the Cantonese precedent: the final stop tengwa serves double duty as both coda marker and checked-tone indicator.

| Tone | Final | Tengwar representation |
|------|-------|------------------------|
| Tone 4 (low checked) | -p, -t, -k, -h | final stop tengwa, no tone mark |
| Tone 8 (high checked) | -p, -t, -k, -h | final stop tengwa, no tone mark |

**Ambiguity resolution:** Tones 4 and 8 differ in pitch height (low vs. high). Options:

1. **Mark neither:** Readers infer from context and lexical knowledge
2. **Mark T8 only:** Use flat bar (high level shape) for T8; unmarked = T4
3. **Mark both:** T4 = double-dot, T8 = no dot (high register)

**Recommendation:** Option 2 (mark T8 only). Rationale:
- T8 is the marked case (high pitch on a checked syllable)
- Unmarked checked syllables default to T4 (low)
- This parallels how Cantonese marks high vs. low checked tones

### Teochew Extension (8 tones)

Teochew preserves Tone 6 (陽上, yang-shang), which is mid-rising:

| Tone | Chao | Contour | Tengwar Mark |
|------|------|---------|--------------|
| 6 | 35 | mid rising | rising stroke + dot |

This fits naturally into the contour + register system: rising contour + mid register.

### Neutral Tone

Grammatical particles and suffixes carry a **neutral tone** (輕聲), written with `--` prefix in Tâi-lô:
- Realized as low [21] or low-falling [31]
- The preceding syllable retains its citation tone (no sandhi)

**Tengwar representation:** Use the low-level mark (flat bar + double-dot) or leave unmarked. The neutral tone is predictable from grammatical context.

### Tone Mark Codepoints

| Mark | Shape | Codepoint | Used for |
|------|-------|-----------|----------|
| Flat bar | — | U+E050 | T1 (high level), T8 (high checked) |
| Flat bar + dot | —̣ | U+E050 + U+E045 | T7 (mid level) |
| Flat bar + double-dot | —̤ | U+E050 + U+E043 | (neutral/extra-low if needed) |
| Rising stroke | ´ | U+E046 | T5 (rising) |
| Rising stroke + dot | ´̣ | U+E046 + U+E045 | T6 Teochew (mid rising) |
| Falling stroke | ` | U+E054 | T2 (high falling) |
| Falling stroke + double-dot | `̤ | U+E054 + U+E043 | T3 (low falling) |

### Font Status

All tone marks exist in Alcarin Extended. No new glyphs needed for Min tones.

---

## 3. Tone Sandhi Representation

**Policy: Write surface tones (post-sandhi).**

This is a fundamental design decision. Min tone sandhi is:
- **Obligatory:** Applies in virtually all multi-syllable contexts
- **Pervasive:** All non-final syllables change
- **Predictable:** Rules are regular (with exceptions for particles)

Writing surface tones means the Tengwar representation matches pronunciation. A reader does not need to apply sandhi rules mentally.

### Converter Responsibility

The romanization-to-Tengwar converter must:

1. Accept input in **citation tones** (standard Tâi-lô/POJ notation)
2. Identify **phrase boundaries** (compound words, verb-object, modifier-head)
3. Apply **sandhi rules** to all non-final syllables
4. Output Tengwar with **surface tone marks**

### Sandhi Rules Summary

**Smooth tones (1, 2, 3, 5, 7):**

```
Citation  →  Sandhi
   1 (55)  →  7 (33)
   7 (33)  →  3 (21)
   3 (21)  →  2 (51)
   2 (51)  →  1 (55)
   5 (24)  →  7 (33)  [Quanzhou]
   5 (24)  →  3 (21)  [Zhangzhou]
```

**Checked tones (4, 8):**

```
   4 (32)  ↔  8 (4)
```

### Exceptions

Sandhi does **not** apply:
- Phrase-finally (the final syllable keeps citation tone)
- Before neutral-tone particles (`--a`, `--lah`)
- In emphatic or contrastive speech
- Certain frozen expressions

### Example

| Tâi-lô (citation) | Tengwar tones | Pronunciation |
|-------------------|---------------|---------------|
| Tâi-uân (臺灣) | T5 → T7, T1 unchanged | [tai³³ uan⁴⁴] |
| hó-lâng (好人) | T2 → T1, T5 unchanged | [ho⁵⁵ laŋ²⁴] |

The Tengwar output shows the surface (sandhi-applied) tones, not the underlying citation tones.

---

## 4. Final Stop Consonants

Min preserves Middle Chinese final stops, as in Cantonese and Hakka.

### Oral Stops

Per the final-stops design document, use the same tengwar as initials:

| Final | IPA | Tengwa | Same as initial |
|-------|-----|--------|-----------------|
| -p | /p̚/ | parma | p- |
| -t | /t̚/ | tinco | t- |
| -k | /k̚/ | calma | k- |

Position (after the vowel) distinguishes finals from initials.

### Glottal Stop Final

Min has a final glottal stop /-ʔ/, written `-h` in Tâi-lô. This has no equivalent in Mandarin or Cantonese.

**Decision:** Use **halla** for final /-ʔ/.

| Final | IPA | Tengwa | Codepoint |
|-------|-----|--------|-----------|
| -h | /ʔ/ | halla | U+E029 |

**Rationale:**
1. Halla represents /h/ in many modes; /h/ and /ʔ/ are both glottal
2. The glottal stop historically derives from earlier *-p, *-t, *-k
3. Using a distinct glyph prevents ambiguity with oral stops
4. Halla is not used for any other purpose in the Min mode

### Examples

| Tâi-lô | IPA | Tengwar structure |
|--------|-----|-------------------|
| o̍h (learn) | /ɔʔ/ | telco + o-tehta + halla |
| ta̍h (step on) | /taʔ/ | tinco + a-tehta + halla |
| si̍t (real) | /sit̚/ | thule + i-tehta + tinco |
| la̍t (strength) | /lat̚/ | lambe + a-tehta + tinco |

---

## 5. Consonant Inventory

Min has a **three-way laryngeal contrast** in stops and affricates:

| Contrast | Voiceless unasp. | Voiceless asp. | Voiced |
|----------|------------------|----------------|--------|
| Bilabial | p /p/ | ph /pʰ/ | b /b/ |
| Velar | k /k/ | kh /kʰ/ | g /g/ |
| Alveolar affr. | ts /ts/ | tsh /tsʰ/ | j /dz~z/ |

This differs from Mandarin (two-way) and Cantonese (two-way, different romanization).

### Tengwar Grade Assignment

The Mandarin mode uses:
- Grade 1 = voiceless unaspirated
- Grade 2 = voiceless aspirated

For Min, extend to Grade 3 for voiced:

| Contrast | Grade | Example |
|----------|-------|---------|
| Voiceless unaspirated | 1 | parma /p/, tinco /t/, calma /k/ |
| Voiceless aspirated | 2 | umbar /pʰ/, ando /tʰ/, anga /kʰ/ |
| Voiced | 3 | formen /b/?, .... ??? |

**Problem:** Tengwar Grade 3 traditionally represents fricatives, not voiced stops.

### Design Options for Voiced Stops

**Option A: Use Grade 3 (Fricative row)**
- parma (Gr.1) /p/, umbar (Gr.2) /pʰ/, formen (Gr.3) /b/
- Problem: formen is /f/ in other modes; /b/ is not a fricative

**Option B: Use Grade 4 (if available)**
- Some Tengwar charts have Grade 4 for voiced
- anca, unque, etc.
- Problem: These are not in all fonts

**Option C: Diacritic for voicing**
- Use parma + voicing mark for /b/
- Keeps Grade 1/2 semantics intact
- Problem: Adds complexity, new diacritic needed

**Option D: Accept functional slot mapping**
- Mandarin: Grade 1 = unasp, Grade 2 = asp (no voiced)
- Cantonese: Same (no voiced initials)
- Min: Grade 1 = unasp, Grade 2 = asp, **Grade 3 = voiced**
- Even though Grade 3 is traditionally "fricative," assign voiced stops there
- The reader knows the mode and interprets accordingly

**Decision:** Option D (functional slot mapping)

This is phonologically defensible: the three-way contrast fills three slots, regardless of original Tengwar phonetic associations. The Min mode documents this clearly.

### Complete Min Initial Table

| Tâi-lô | IPA | Tengwa | Grade | Notes |
|--------|-----|--------|-------|-------|
| p | /p/ | parma | II-1 | voiceless unaspirated |
| ph | /pʰ/ | umbar | II-2 | voiceless aspirated |
| b | /b/ | formen | II-3 | voiced (slot reuse) |
| m | /m/ | malta | II-5 | nasal |
| t | /t/ | tinco | I-1 | voiceless unaspirated |
| th | /tʰ/ | ando | I-2 | voiceless aspirated |
| n | /n/ | numen | I-5 | nasal |
| l | /l/ | lambe | I-6 | lateral |
| ts | /ts/ | ext. tinco | I-1 ext. | affricate |
| tsh | /tsʰ/ | ext. ando | I-2 ext. | aspirated affricate |
| j | /dz~z/ | ext. thule | I-3 ext. | voiced affricate (slot reuse) |
| s | /s/ | thule | I-3 | fricative |
| k | /k/ | calma | III-1 | voiceless unaspirated |
| kh | /kʰ/ | anga | III-2 | voiceless aspirated |
| g | /g/ | hwesta | III-3 | voiced (slot reuse) |
| ng | /ŋ/ | noldo | III-5 | nasal (also syllabic) |
| h | /h/ | halla | — | glottal fricative |
| (zero) | ∅ | — | — | null initial |

**Note on voiced consonant mapping:** The Grade 3 reuse means:
- formen = /b/ in Min (vs. /f/ in Mandarin/Cantonese)
- hwesta = /g/ in Min (vs. /h/ or /x/ in other modes)
- ext. thule = /dz/ in Min

This is mode-specific. Readers must know which mode applies.

**Alternative:** A later revision could introduce a voicing diacritic to keep Grade 3 for fricatives. This would require font work but produce a more universal solution.

---

## 6. Vowel Inventory

Min vowels largely parallel Mandarin and Cantonese. The main additions are:
- Nasal vowels (covered above)
- /ɔ/ (written `oo` in Tâi-lô) as distinct from /o/

### Oral Vowels

| Tâi-lô | IPA | Tehta | Notes |
|--------|-----|-------|-------|
| a | /a/ | a-tehta (three dots) | same as Mandarin |
| e | /e/ | e-tehta (acute) | same as Mandarin |
| i | /i/ | i-tehta (dot) | same as Mandarin |
| o | /o/ | o-tehta (left curl) | close-mid back |
| oo | /ɔ/ | o-tehta + underdot | open-mid back (Cantonese pattern) |
| u | /u/ | u-tehta (right curl) | same as Mandarin |

**Note:** The /o/ vs. /ɔ/ distinction uses the Cantonese pattern: underdot for the more open variant.

### Diphthongs and Triphthongs

Follow Mandarin/Cantonese conventions:
- Falling diphthongs: write nuclear vowel only
- Rising diphthongs: use medial glide tengwar (anna, vala)
- Triphthongs: medial + nuclear + implied final glide

---

## 7. Mappings Carried Over from Cantonese

The following elements transfer unchanged:

### From Cantonese

| Feature | Cantonese Design | Min Status |
|---------|------------------|------------|
| Final -p, -t, -k | parma, tinco, calma | **same** |
| Initial ng /ŋ/ | noldo | **same** |
| Syllabic m /m̩/ | malta + syllabic mark | **same** |
| Syllabic ng /ŋ̍/ | noldo + syllabic mark | **same** |
| Tone contour marks | flat, rising, falling | **same** |
| Register modifiers | dot (mid), double-dot (low) | **same** |
| Underdot for /ɔ/ | o-tehta + underdot | **same** |

### From Mandarin

| Feature | Mandarin Design | Min Status |
|---------|-----------------|------------|
| Aspiration contrast | Grade 1 vs. Grade 2 | **same** |
| Medial glides | anna /j/, vala /w/ | **same** |
| Vowel tehtar | a, e, i, o, u | **same** |
| Below-tengwa tone marks | contour shapes | **same** |
| Null initial carrier | telco | **same** |

---

## 8. Summary of New Design Elements

### New Glyph Required

| Glyph | Codepoint | Purpose |
|-------|-----------|---------|
| Tilde-below | U+E044 | Nasal vowel marker |

### New Semantic Assignments

| Tengwa | Traditional | Min usage |
|--------|-------------|-----------|
| formen | /f/ fricative | /b/ voiced stop |
| hwesta | /h/ or /x/ fricative | /g/ voiced stop |
| ext. thule | (various) | /dz/ voiced affricate |
| halla | /h/ glottal | /-ʔ/ glottal stop final |

### Tone Extensions

| Tone mark | Min tone |
|-----------|----------|
| flat bar | T1 (high level), T8 (high checked) |
| falling stroke | T2 (high falling) |
| falling + double-dot | T3 (low falling) |
| rising stroke | T5 (rising) |
| flat bar + dot | T7 (mid level) |
| rising + dot | T6 Teochew (mid rising) |

---

## 9. Open Questions and Future Work

### Font Work

1. **Tilde-below glyph (U+E044):** Must be added to Alcarin Extended
2. **Voiced consonant glyphs:** Consider alternative if slot-reuse proves confusing
3. **Precomposed nasal vowel glyphs:** Optional optimization for common nasal vowels

### Converter Implementation

1. **Sandhi engine:** Implement citation → surface tone conversion
2. **Phrase boundary detection:** Heuristics for compound words and phrases
3. **Dual input support:** Accept both Tâi-lô and POJ romanizations

### Dialect Variation

1. **Quanzhou vs. Zhangzhou:** Different T5 sandhi targets
2. **Teochew 8-tone system:** Document separately or integrate here
3. **Amoy, Penang, Philippine Hokkien:** Note major divergences

### Cross-Mode Consistency

1. **Voiced consonant solution:** A universal voicing diacritic would be cleaner
2. **Nasal vowel applicability:** Wu also has nasal vowels; design should transfer

---

## References

- phonology-min.md (this project)
- design-tones-extended.md (this project)
- design-final-stops.md (this project)
- design-vowels-cantonese.md (this project)
- design-consonants-cantonese.md (this project)
- Wikipedia: Hokkien phonology
- Wikipedia: Taiwanese Hokkien
- Wikipedia: Teochew Min
- Tâi-lô romanization specification (MOE Taiwan)
- Pe̍h-ōe-jī traditional romanization
