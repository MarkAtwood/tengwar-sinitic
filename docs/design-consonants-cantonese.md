# Cantonese Consonant Mappings

Design document for mapping Cantonese initials to Tengwar.

## Overview

Cantonese has 19 initials in the Jyutping romanization system. The phonological system differs from Mandarin in several key ways:

- **Shared:** Aspiration-based stop/affricate contrast (same as Mandarin)
- **Added:** Initial /ŋ/ (ng), labialized velars /kʷ/ and /kʷʰ/
- **Absent:** Retroflex series (zh, ch, sh, r), alveolar affricates (z, c), palatals (j, q, x)

Most Cantonese initials map directly to Mandarin equivalents. Only the labialized velars and initial /ŋ/ require new design decisions.

## Jyutping Initials

| Jyutping | IPA | Description |
|----------|-----|-------------|
| b | /p/ | unaspirated bilabial stop |
| p | /pʰ/ | aspirated bilabial stop |
| m | /m/ | bilabial nasal |
| f | /f/ | labiodental fricative |
| d | /t/ | unaspirated alveolar stop |
| t | /tʰ/ | aspirated alveolar stop |
| n | /n/ | alveolar nasal |
| l | /l/ | alveolar lateral |
| g | /k/ | unaspirated velar stop |
| k | /kʰ/ | aspirated velar stop |
| ng | /ŋ/ | velar nasal |
| h | /h/ | glottal fricative |
| gw | /kʷ/ | unaspirated labialized velar stop |
| kw | /kʷʰ/ | aspirated labialized velar stop |
| w | /w/ | labiovelar approximant |
| z | /ts/ | unaspirated alveolar affricate |
| c | /tsʰ/ | aspirated alveolar affricate |
| s | /s/ | alveolar fricative |
| j | /j/ | palatal approximant |

## Consonant Grid

Cantonese initials map to four Tengwar series:

| Grade | I: Alveolar | II: Labial | III: Velar | III+lab: Labiovelar |
|-------|-------------|------------|------------|---------------------|
| 1 (unasp.) | tinco /t/ **d** | parma /p/ **b** | calma /k/ **g** | calma+w /kʷ/ **gw** |
| 2 (asp.) | ando /tʰ/ **t** | umbar /pʰ/ **p** | anga /kʰ/ **k** | anga+w /kʷʰ/ **kw** |
| 3 (fric.) | thule /s/ **s** | formen /f/ **f** | hwesta /h/ **h** | — |
| 5 (nasal) | numen /n/ **n** | malta /m/ **m** | noldo /ŋ/ **ng** | — |
| 6 (approx.) | lambe /l/ **l** | — | — | vala /w/ **w** |

Plus two alveolar affricates using extended stems:

| Grade | I: Alveolar (ext.) |
|-------|-------------------|
| 1 (unasp.) | ext. tinco /ts/ **z** |
| 2 (asp.) | ext. ando /tsʰ/ **c** |

Plus the palatal approximant:

| Glide | Tengwa |
|-------|--------|
| j /j/ | anna |

## Mappings Inherited from Mandarin

These 14 initials use identical tengwar assignments:

| Jyutping | IPA | Tengwa | Grid | Notes |
|----------|-----|--------|------|-------|
| b | /p/ | parma | II-1 | |
| p | /pʰ/ | umbar | II-2 | |
| m | /m/ | malta | II-5 | |
| f | /f/ | formen | II-3 | |
| d | /t/ | tinco | I-1 | |
| t | /tʰ/ | ando | I-2 | |
| n | /n/ | numen | I-5 | |
| l | /l/ | lambe | I-6 | |
| g | /k/ | calma | III-1 | |
| k | /kʰ/ | anga | III-2 | |
| s | /s/ | thule | I-3 | |
| z | /ts/ | ext. tinco | I-1 ext. | Mandarin uses same |
| c | /tsʰ/ | ext. ando | I-2 ext. | Mandarin uses same |
| j | /j/ | anna | — | Same as Mandarin medial glide |

## Cantonese-Specific Mappings

Three initials require design decisions:

### Initial /ŋ/ (ng)

**Analysis:** Mandarin has /ŋ/ only as a coda, written with noldo. Cantonese has it as both initial and coda.

**Decision:** Use noldo for initial /ŋ/, same as coda /ŋ/.

**Rationale:** No ambiguity arises. Initial position is unambiguous in Tengwar (syllable-initial vs syllable-final). Using the same tengwa maintains the principle that one phoneme = one tengwa.

| Jyutping | IPA | Tengwa | Grid |
|----------|-----|--------|------|
| ng | /ŋ/ | noldo | III-5 |

### Cantonese /h/ vs Mandarin /x/

**Analysis:** Mandarin has /x/ (velar fricative), written with hwesta. Cantonese has /h/ (glottal fricative), a different phoneme.

**Decision:** Use hwesta for Cantonese /h/.

**Rationale:**
1. Both occupy the same functional slot in their respective phonologies (the "h-sound")
2. Hwesta historically represents aspirate/fricative sounds across modes
3. Using a different tengwa would complicate cross-language consistency
4. The phonetic difference (/x/ vs /h/) is predictable from knowing which language is being read

| Jyutping | IPA | Tengwa | Grid | Notes |
|----------|-----|--------|------|-------|
| h | /h/ | hwesta | III-3 | Different phoneme, same slot |

### Labialized Velars /kʷ/ (gw) and /kʷʰ/ (kw)

**Analysis:** These are the most significant Cantonese-specific consonants. Mandarin lacks them entirely. Two design options:

**Option 1: Velar tengwa + labialization diacritic**
- Use calma + w-curl (labialization mark) for /kʷ/
- Use anga + w-curl for /kʷʰ/
- Follows Tolkien's quessetema convention for labiovelars
- Compositional: readers understand these as "velar + lip rounding"

**Option 2: Dedicated tengwar**
- Assign quesse (Grade 1) and ungwe (Grade 2) directly
- These are the traditional labiovelar tengwar
- Simple, but abandons the compositional principle
- Problem: These slots are used for retroflexes in Mandarin mode

**Decision:** Option 1 (velar + labialization diacritic).

**Rationale:**
1. **Consistency with Tengwar tradition:** Tolkien's own quessetema uses labiovelars as modified velars. The w-curl diacritic (used in some modes for labialization) follows this principle.
2. **Compositionality:** Readers can parse gw/kw as "g/k with lip rounding" rather than memorizing unrelated symbols.
3. **Cross-mode clarity:** The Mandarin mode uses Column IV for retroflexes. Reusing those positions for different sounds in Cantonese would create confusion for readers switching between modes.
4. **Phonetic accuracy:** /kʷ/ and /kʷʰ/ are genuinely velar stops with secondary labialization, not a separate place of articulation.

| Jyutping | IPA | Tengwa | Notes |
|----------|-----|--------|-------|
| gw | /kʷ/ | calma + w-curl | velar + labialization |
| kw | /kʷʰ/ | anga + w-curl | aspirated velar + labialization |

**Diacritic placement:** The w-curl appears below the tengwa, in the same position as the palatal mark in Mandarin mode. This is consistent: both marks modify place of articulation.

### Labiovelar Approximant /w/

**Analysis:** Mandarin uses vala for the medial glide /w/. Cantonese has /w/ as an initial.

**Decision:** Use vala for initial /w/.

**Rationale:** Same phoneme, same tengwa. Position (initial vs medial) is clear from syllable structure.

| Jyutping | IPA | Tengwa |
|----------|-----|--------|
| w | /w/ | vala |

## Complete Cantonese Initial Table

| Jyutping | IPA | Tengwa | Grid | Source |
|----------|-----|--------|------|--------|
| b | /p/ | parma | II-1 | inherited |
| p | /pʰ/ | umbar | II-2 | inherited |
| m | /m/ | malta | II-5 | inherited |
| f | /f/ | formen | II-3 | inherited |
| d | /t/ | tinco | I-1 | inherited |
| t | /tʰ/ | ando | I-2 | inherited |
| n | /n/ | numen | I-5 | inherited |
| l | /l/ | lambe | I-6 | inherited |
| g | /k/ | calma | III-1 | inherited |
| k | /kʰ/ | anga | III-2 | inherited |
| ng | /ŋ/ | noldo | III-5 | **Cantonese-specific** |
| h | /h/ | hwesta | III-3 | inherited (different phoneme) |
| gw | /kʷ/ | calma + w-curl | III-1+lab | **Cantonese-specific** |
| kw | /kʷʰ/ | anga + w-curl | III-2+lab | **Cantonese-specific** |
| w | /w/ | vala | — | inherited |
| z | /ts/ | ext. tinco | I-1 ext. | inherited |
| c | /tsʰ/ | ext. ando | I-2 ext. | inherited |
| s | /s/ | thule | I-3 | inherited |
| j | /j/ | anna | — | inherited |

## What Cantonese Lacks

Cantonese does not use these Mandarin mappings:

| Mandarin | IPA | Tengwa | Why absent |
|----------|-----|--------|------------|
| zh | /tʂ/ | quesse | No retroflexes |
| ch | /tʂʰ/ | ungwe | No retroflexes |
| sh | /ʂ/ | harma | No retroflexes |
| r | /ɻ/ | ore | No retroflexes |
| j | /tɕ/ | calma + pal. | No palatal affricates |
| q | /tɕʰ/ | anga + pal. | No palatal affricates |
| x | /ɕ/ | hwesta + pal. | No palatal fricative |

Note: Jyutping "j" is /j/ (palatal approximant), same as Mandarin "y", not the palatal affricate.

## Font Requirements

The labialization diacritic (w-curl) requires:

1. **Glyph:** A below-tengwa diacritic indicating labialization
2. **Positioning:** Same vertical zone as the palatal mark (below tengwa body)
3. **Options:**
   - Use existing Tengwar fonts that include w-modification marks
   - Extend Alcarin Tengwar with a w-curl below glyph
   - In handwriting, a small curved hook or "w" shape below the tengwa

**Note:** Some Tengwar fonts include a "tehta w" or labialization mark. Compatibility varies; the extended Alcarin font may need this glyph added.

## Open Questions

1. **Font glyph:** Does Alcarin Tengwar Extended include a suitable labialization diacritic? If not, one needs to be added.

2. **Alternative notation:** Some modes write labiovelars as tengwa + vala (as a cluster). This is more verbose but requires no new diacritics. Should this be offered as a fallback?

## Summary

- 14 of 19 Cantonese initials inherit directly from Mandarin
- 1 initial (ng) uses the same tengwa as Mandarin coda ng, now also in initial position
- 1 initial (h) uses the same tengwa as Mandarin h, despite different phonemes
- 2 initials (gw, kw) require a labialization diacritic on velar tengwar
- 1 initial (w) uses the same tengwa as Mandarin medial w, now also as initial

The design maintains maximum consistency with the Mandarin mode while accurately representing Cantonese phonology.
