# Font Extension Requirements for Cantonese

This document analyzes the Alcarin Extended font's capability to support
Cantonese Tengwar, based on the vowel tehtar and extended tone mark designs.

## Summary

**No new glyphs are required.** All marks needed for Cantonese support already
exist in Alcarin Tengwar (upstream or extended). The Cantonese mode uses:

1. Existing tehtar for most vowels
2. Existing combining marks in new combinations for /oe/ and /eo/
3. Existing below-marks (underdot, double-dot) for register modifiers
4. Existing contour marks (flat, rising, falling) for tone shapes

Optional enhancement: precomposed ligature glyphs for combined tehtar could
improve optical quality but are not required for correct rendering.

---

## 1. Existing Glyphs in Alcarin Extended

### Vowel Tehtar (above-tengwa combining marks)

| Glyph Name | Codepoint | Purpose in Cantonese |
|------------|-----------|----------------------|
| dottripleabove-teng | U+E040 | a-tehta for /aː/ (aa) |
| dotabove-teng | U+E044 | i-tehta for /iː/ (i) |
| acute-teng | U+E046 | e-tehta for /ɛː/ (e) |
| leftcurl-teng | U+E04C | o-tehta for /ɔː/ (o) |
| rightcurl-teng | U+E04A | u-tehta for /uː/ (u) |

### Register Modifier Marks (below-tengwa combining marks)

| Glyph Name | Codepoint | Purpose in Cantonese |
|------------|-----------|----------------------|
| dotbelow-teng | U+E045 | short/central vowel marker (for /ɐ/, /ɵ/) and mid-register tone |
| dotdblelow-teng | U+E043 | low-register tone modifier |
| dottriplebelow-teng | U+E041 | extra-low register (Min extension) |

### Tone Contour Marks (below-tengwa combining marks)

| Glyph Name | Codepoint | Purpose in Cantonese |
|------------|-----------|----------------------|
| macronbelow-teng | U+E051 | flat bar (level tones: T1, T3, T6) |
| acutebelow-teng | U+E047 | rising stroke (rising tones: T2, T5) |
| gravebelow-teng | U+E097 | falling stroke (falling tone: T4) |

### Additional Marks Used

| Glyph Name | Codepoint | Purpose |
|------------|-----------|---------|
| macron-teng | U+E050 | flat bar above (also called nasalizer/andaith) |
| grave-teng | U+E054 | falling stroke above |
| caron-teng | U+E055 | yanta/chevron above (Mandarin T3) |

---

## 2. New Glyphs Analysis

### Cantonese Vowel Tehtar

The Cantonese vowel design specifies three phonemes not in Mandarin:

| Jyutping | IPA | Design Decision | Font Status |
|----------|-----|-----------------|-------------|
| a (short) | /ɐ/ | underdot (dotbelow-teng) | **EXISTS** at U+E045 |
| oe | /œː/ | o-tehta + i-tehta combination | **EXISTS** (both components) |
| eo | /ɵ/ | u-tehta + underdot combination | **EXISTS** (both components) |

**Conclusion:** No new vowel tehtar glyphs needed.

The underdot (dotbelow-teng, U+E045) already exists in the upstream Alcarin
font. It is described as "TENGWAR COMBINING MARK UNUTIXE (DOT BELOW)" and has
proper `_bottom` anchor positioning for below-tengwa placement.

### Combined Tehtar for /oe/ and /eo/

The /oe/ vowel uses o-tehta (leftcurl-teng) + i-tehta (dotabove-teng) placed
adjacently above the tengwa. Both glyphs exist; proper stacking depends on:

1. The font's `top` anchor on leftcurl-teng allowing dotabove-teng to attach
2. OpenType `mark` feature positioning both marks above the base

The /eo/ vowel uses u-tehta (rightcurl-teng) above + underdot (dotbelow-teng)
below. This is a simpler case: separate anchor positions (`top` vs `bottom`).

### Extended Tone Marks

| Cantonese Tone | Contour | Register | Composition | Font Status |
|----------------|---------|----------|-------------|-------------|
| T1 (55) high level | flat | high | U+E051 | EXISTS |
| T2 (25) high rising | rising | high | U+E047 | EXISTS |
| T3 (33) mid level | flat | mid | U+E051 + U+E045 | EXISTS |
| T4 (21) low falling | falling | low | U+E097 + U+E043 | EXISTS |
| T5 (23) low rising | rising | low | U+E047 + U+E043 | EXISTS |
| T6 (22) low level | flat | low | U+E051 + U+E043 | EXISTS |

**Conclusion:** No new tone glyphs needed.

The design document confirms: "For Cantonese and Hakka (6 tones): All required
glyphs exist in Alcarin Extended. No new font work needed."

---

## 3. Proposed Codepoint Assignments

**None required.** All needed glyphs have codepoints in the existing scheme:

| Codepoint | Name | Description |
|-----------|------|-------------|
| U+E040 | dottripleabove-teng | a-tehta (three dots above) |
| U+E041 | dottriplebelow-teng | three dots below (Min extension) |
| U+E043 | dotdblelow-teng | double dot below (low register) |
| U+E044 | dotabove-teng | i-tehta (single dot above) |
| U+E045 | dotbelow-teng | underdot / unutixe (short vowel / mid register) |
| U+E046 | acute-teng | e-tehta / rising stroke above |
| U+E047 | acutebelow-teng | rising stroke below (T2/T5 contour) |
| U+E04A | rightcurl-teng | u-tehta (right curl above) |
| U+E04C | leftcurl-teng | o-tehta (left curl above) |
| U+E050 | macron-teng | flat bar above (nasalizer/andaith) |
| U+E051 | macronbelow-teng | flat bar below (level tone contour) |
| U+E054 | grave-teng | falling stroke above |
| U+E097 | gravebelow-teng | falling stroke below (T4 contour) |

---

## 4. Precomposed Ligatures

### Current Situation

The font already includes two dot-inside ligatures added in the Extended build:

- rightcurl_dotinside-teng (U+E098): right curl + interior dot
- leftcurl_dotinside-teng (U+E09E): left curl + interior dot

These are implemented via `ccmp` substitution rules, not as atomic character
input.

### Potential Cantonese Ligatures

Combined tehtar may benefit from precomposed ligature glyphs for optical
refinement:

| Combination | Cantonese Use | Ligature Name | Priority |
|-------------|---------------|---------------|----------|
| leftcurl + dotabove | /oe/ vowel | leftcurl_dotabove-teng | optional |
| rightcurl + dotabove | /y/ (yu) vowel | rightcurl_dotabove-teng | optional |

### Recommendation

**Defer ligature work.** The current mark-based rendering should work correctly
with HarfBuzz shaping. If visual testing reveals awkward spacing or overlap,
file a separate issue to add ligature glyphs.

Note: The existing yu (/y/) tehta in Mandarin mode already uses this approach
(u-tehta + i-tehta as separate marks), so rendering precedent exists.

---

## 5. Technical Verification

### Anchor-Based Stacking

The GlyphData.xml shows proper anchor definitions:

- Above tehtar have `_top` (attach to base) and `top` (chain another mark)
- Below marks have `_bottom` (attach to base) and `bottom` (chain another mark)

This allows:
- Vowel tehta above: attaches to base tengwa via `_top` anchor
- Tone contour below: attaches to base tengwa via `_bottom` anchor
- Register dot below: chains to tone contour via `bottom` anchor

### Mark-to-Mark Positioning

For combined tehtar like /oe/ (o + i above), the font needs:
1. leftcurl-teng attaches to base via `_top`
2. dotabove-teng chains to leftcurl-teng via its `_top` to leftcurl's `top`

The GlyphData.xml confirms leftcurl-teng has both `_top` and `top` anchors,
supporting this stacking.

---

## 6. Conclusion

The Alcarin Extended font fully supports Cantonese Tengwar without modifications:

| Requirement | Status | Notes |
|-------------|--------|-------|
| Vowel tehtar | Complete | All 9 Cantonese vowels covered |
| Short vowel marker | Complete | U+E045 dotbelow-teng exists |
| Tone contours | Complete | All 6 tones representable |
| Register modifiers | Complete | dot and double-dot exist |
| Combined tehtar | Complete | Mark stacking via anchors |

**Action: Close font extension issue with no work required.**

If visual testing reveals spacing or collision issues with combined marks,
file a separate bead for kerning/ligature refinement. This is an enhancement,
not a blocker.

---

## References

- Design source: `/Volumes/Attic/Desktop/Projects/Tengwar-Mandarin-wt-research/docs/design-vowels-cantonese.md`
- Design source: `/Volumes/Attic/Desktop/Projects/Tengwar-Mandarin-wt-research/docs/design-tones-extended.md`
- Font build guide: `/Volumes/Attic/Desktop/Projects/Tengwar-Mandarin/fonts/Alcarin-Tengwar/Font source/BUILD_GUIDE.md`
- Glyph metadata: `/Volumes/Attic/Desktop/Projects/Tengwar-Mandarin/fonts/Alcarin-Tengwar/Font source/GlyphData.xml`
