# Cantonese Vowel Tehtar Design

This document maps the Cantonese vowel inventory (as analyzed through Jyutping romanization) to Tengwar tehtar. The design extends the existing Mandarin mode while maintaining consistency and phonetic logic.

## Cantonese Vowel Inventory

Cantonese has a richer vowel system than Mandarin, with nine distinct vowel phonemes:

| Jyutping | IPA | Description | Distribution |
|----------|-----|-------------|--------------|
| aa | /aː/ | long open front-central | open and closed syllables |
| a | /ɐ/ | short near-open central | closed syllables only |
| e | /ɛː/ | open-mid front unrounded | open and closed syllables |
| i | /iː/ | close front unrounded | open and closed syllables |
| o | /ɔː/ | open-mid back rounded | open and closed syllables |
| u | /uː/ | close back rounded | open and closed syllables |
| oe | /œː/ | open-mid front rounded | open and closed syllables |
| eo | /ɵ/ | close-mid central rounded | closed syllables only |
| yu | /yː/ | close front rounded | open and closed syllables |

Note: The short vowel /ɐ/ (Jyutping "a") only appears before codas (-i, -u, -m, -n, -ng, -p, -t, -k). The vowel /ɵ/ (Jyutping "eo") similarly appears only before -n and -t.

## Comparison with Mandarin

| Vowel quality | Mandarin | Cantonese | Status |
|---------------|----------|-----------|--------|
| /a/ open | a | aa | reuse tehta |
| /ɐ/ central | — | a | **new** |
| /ɛ/ open-mid front | — | e | **different from Mandarin e** |
| /ɤ~ə/ mid back | e | — | Mandarin only |
| /i/ close front | i | i | reuse tehta |
| /o~ɔ/ back rounded | o | o | reuse tehta |
| /u/ close back | u | u | reuse tehta |
| /y/ close front rounded | ü | yu | reuse tehta |
| /œ/ open-mid front rounded | — | oe | **new** |
| /ɵ/ close-mid central rounded | — | eo | **new** |

**Critical observation:** Mandarin "e" represents /ɤ~ə/ (a mid back unrounded vowel), while Cantonese "e" represents /ɛ/ (an open-mid front unrounded vowel). These are phonetically distinct. However, since this is a Cantonese-specific mode (not a pan-Sinitic mode), we can safely assign the e-tehta (acute stroke) to Cantonese /ɛ/. A reader of Cantonese Tengwar will pronounce it correctly.

## Tehtar Assignments

### Vowels reused from Mandarin

| Jyutping | IPA | Tehta | Notes |
|----------|-----|-------|-------|
| aa | /aː/ | three dots (a-tehta) | identical to Mandarin a |
| i | /iː/ | single dot (i-tehta) | identical to Mandarin i |
| o | /ɔː/ | left curl (o-tehta) | close enough to Mandarin o |
| u | /uː/ | right curl (u-tehta) | identical to Mandarin u |
| yu | /yː/ | i-tehta + u-tehta | same as Mandarin ü after l/n |
| e | /ɛː/ | acute stroke (e-tehta) | different phoneme, same glyph |

### New tehtar required

| Jyutping | IPA | Proposed tehta | Rationale |
|----------|-----|----------------|-----------|
| a | /ɐ/ | single dot below | "reduced" or "lowered" variant of /a/ |
| oe | /œː/ | left curl + i-tehta | front rounded = /o/ rounding + /i/ frontness |
| eo | /ɵ/ | right curl + single dot below | central rounded, related to /u/ |

## Design Rationale for New Tehtar

### Short /ɐ/ (Jyutping "a")

The short central vowel /ɐ/ contrasts with long /aː/ only in closed syllables. Examples:
- saam /saːm/ 三 "three" vs. sam /sɐm/ 心 "heart"

**Design:** Single dot below the tengwa (underdot).

**Rationale:** The underdot suggests a "reduced" or "centralized" vowel, paralleling how reduced vowels are sometimes marked in other orthographies. Placing it below distinguishes it visually from the three-dot a-tehta above. The position is also practical: Cantonese tehtar go above, tones go below, and /ɐ/ only occurs in closed syllables where syllable structure is unambiguous.

**Alternative considered:** A smaller or modified three-dot mark. Rejected because it would be hard to distinguish at small sizes.

### Open-mid front rounded /œ/ (Jyutping "oe")

This vowel combines the frontness of /e/ with the rounding of /o/. It does not exist in Mandarin. Examples:
- soeng /sœːŋ/ 想 "want/think"
- goek /kœːk/ 腳 "foot"

**Design:** Left curl (o-tehta) combined with single dot (i-tehta), placed side by side.

**Rationale:** /œ/ is phonetically "front rounded"—it has the lip rounding of /o/ and the tongue position approaching /i/. Combining o-tehta and i-tehta represents this compound quality visually. This parallels the Mandarin mode's treatment of /y/ (ü) as u-tehta + i-tehta.

**Alternative considered:** A modified curl or new glyph. Rejected because combining existing tehtar is more learnable and follows established precedent.

### Close-mid central rounded /ɵ/ (Jyutping "eo")

This short vowel appears only before -n and -t. It is central (between front and back) and rounded. Examples:
- seon /sɵn/ 信 "letter/trust"
- ceot /tsʰɵt/ 出 "exit"

**Design:** Right curl (u-tehta) combined with single dot below (underdot).

**Rationale:** /ɵ/ is a centralized rounded vowel, related to /u/ but more central and shorter. The u-tehta captures the rounding; the underdot (same as short /ɐ/) signals "reduced/centralized." This creates a systematic relationship: underdot marks centralization.

**Alternative considered:** A new dedicated glyph. Deferred because the combination approach maintains consistency with the /ɐ/ solution and avoids font proliferation.

## Complete Tehtar Table

| Jyutping | IPA | Tehta | Glyph description | Font status |
|----------|-----|-------|-------------------|-------------|
| aa | /aː/ | a-tehta | three dots above | existing |
| a | /ɐ/ | underdot | single dot below | **new glyph** |
| e | /ɛː/ | e-tehta | acute stroke above | existing |
| i | /iː/ | i-tehta | single dot above | existing |
| o | /ɔː/ | o-tehta | left curl above | existing |
| u | /uː/ | u-tehta | right curl above | existing |
| oe | /œː/ | o+i tehta | left curl + dot above | existing (combination) |
| eo | /ɵ/ | u-tehta + underdot | right curl above + dot below | **new combination** |
| yu | /yː/ | u+i tehta | right curl + dot above | existing (combination) |

## Diphthongs

Cantonese has more diphthongs than Mandarin, including some with the short /ɐ/ nucleus.

### Falling diphthongs (nucleus + offglide)

| Jyutping | IPA | Tehta | Notes |
|----------|-----|-------|-------|
| aai | /aːi/ | a-tehta | glide to /i/ implied |
| aau | /aːu/ | a-tehta | glide to /u/ implied |
| ai | /ɐi/ | underdot | short nucleus, glide implied |
| au | /ɐu/ | underdot | short nucleus, glide implied |
| ei | /ei/ | e-tehta | glide to /i/ implied |
| eoi | /ɵy/ | u-tehta + underdot | glide to /y/ implied |
| iu | /iːu/ | i-tehta | glide to /u/ implied |
| oi | /ɔːi/ | o-tehta | glide to /i/ implied |
| ou | /ou/ | o-tehta | glide to /u/ implied |
| ui | /uːi/ | u-tehta | glide to /i/ implied |

Following the Mandarin mode's approach, falling diphthongs write only the nuclear vowel tehta. The offglide is predictable from the final.

### Rising diphthongs (onglide + nucleus)

Rising diphthongs use medial glide tengwar, as in the Mandarin mode:

| Jyutping | Structure | Tengwar |
|----------|-----------|---------|
| gwaa | /kʷaː/ | velar + vala + a-tehta |
| gwaai | /kʷaːi/ | velar + vala + a-tehta |
| gwok | /kʷɔːk/ | velar + vala + o-tehta + final |

The labiovelar initials gw- and kw- use vala as a glide marker between the initial and nuclear vowel.

## Vowel-only syllables (null initial)

Syllables beginning with a vowel use the short carrier (telco), as in the Mandarin mode:

- aa /aː/ → telco + a-tehta
- ai /ɐi/ → telco + underdot
- ou /ou/ → telco + o-tehta

## Font Requirements

### New glyphs needed

1. **Underdot (single dot below tengwa)**
   - Unicode position: combining below
   - Purpose: marks short central /ɐ/ and centralized /ɵ/
   - Similar to: Tengwar unutixe (syllabic marker) but semantically distinct

### Existing glyphs in new combinations

The following require no new font work but may benefit from kerning adjustments:

- **o+i tehta combination** for /œ/: left curl and single dot placed adjacently above
- **u+i tehta combination** for /y/: right curl and single dot placed adjacently above (already used in Mandarin mode)

## Open Questions

1. **Underdot vs. unutixe:** The underdot for /ɐ/ resembles the unutixe mark used for syllabic consonants in some modes. In Cantonese, syllabic consonants do not occur, so there is no collision. However, a pan-Sinitic mode would need to distinguish these uses. Consider: should the underdot be identical to unutixe, or a distinct glyph (e.g., smaller, different position)?

2. **Combination tehtar rendering:** Should o+i and u+i be treated as atomic glyphs, or always rendered as two separate marks? For handwriting, side-by-side is natural. For fonts, a ligature might improve appearance.

3. **Long/short marking convention:** This design marks the short vowel /ɐ/ with a distinct tehta (underdot) rather than using a length diacritic on the /a/ tehta. This is the cleaner solution because the phonetic quality also differs (open /aː/ vs. central /ɐ/). But should a general "short" marker be available for other contexts?

## Summary

The Cantonese vowel tehtar system requires one genuinely new glyph (the underdot for /ɐ/ and the centralization component of /ɵ/) and two combination tehtar (/œ/ as o+i, /ɵ/ as u+underdot). All other vowels reuse Mandarin tehtar directly.

This design:
- Maintains visual consistency with the Mandarin mode
- Uses phonetic logic (combining tehtar represent combined articulatory features)
- Minimizes new font work
- Remains extensible for other Sinitic languages

## References

- Jyutping romanization scheme: https://jyutping.org/en/jyutping/
- Bauer, Robert S. and Paul K. Benedict. 1997. *Modern Cantonese Phonology*. Berlin: Mouton de Gruyter.
- Matthews, Stephen and Virginia Yip. 2011. *Cantonese: A Comprehensive Grammar*. 2nd ed. London: Routledge.
