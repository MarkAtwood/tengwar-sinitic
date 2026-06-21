# Extended Tone System for 6+ Tones

This document specifies the extended tone marking system for Sinitic languages with more than four tones, building on the Mandarin mode's iconographic contour approach.

## Design Principle

Cantonese has six phonemically distinct tones. Rather than inventing six unrelated marks, the system uses **iconographic contours** (same as Mandarin) combined with **register modifiers**:

- **High register** = plain mark (no modifier)
- **Mid register** = mark + single dot below the mark
- **Low register** = mark + double dot below the mark

This produces a systematic, learnable inventory where the contour shape shows pitch movement and the dots show register height.

## Cantonese Tone Inventory

| Tone | Jyutping | Chao | Description | Contour Mark | Register | Full Mark |
|------|----------|------|-------------|--------------|----------|-----------|
| 1 | 1 | 55 | high level | flat bar | high | flat bar |
| 2 | 2 | 25 | high rising | rising stroke | high | rising stroke |
| 3 | 3 | 33 | mid level | flat bar | mid | flat bar + dot |
| 4 | 4 | 21 | low falling | falling stroke | low | falling stroke + double-dot |
| 5 | 5 | 23 | low rising | rising stroke | low | rising stroke + double-dot |
| 6 | 6 | 22 | low level | flat bar | low | flat bar + double-dot |

### Checked Tones (Entering Tones)

Syllables ending in unreleased stops /-p/, /-t/, /-k/ (the "checked" or "entering" tones) use the **same marks** as their non-checked counterparts. The final stop consonant implies the checked quality; no separate mark is needed.

In traditional analysis, Cantonese has nine tones (1-6 plus 7/8/9 for checked variants). In this system:

| Checked Tone | Corresponds To | Mark |
|--------------|----------------|------|
| 7 (high checked) | Tone 1 | flat bar |
| 8 (mid checked) | Tone 3 | flat bar + dot |
| 9 (low checked) | Tone 6 | flat bar + double-dot |

The phonemic analysis supporting this: checked tones in Cantonese have the same pitch contours as their open counterparts, just shorter. The mode's representation is phonemically accurate.

## Mark Inventory with Codepoints

### Contour Marks (above-tengwa position, Mandarin-compatible)

| Mark | Shape | Codepoint | Glyph Name |
|------|-------|-----------|------------|
| Flat bar | horizontal line | U+E050 | nasalizer-teng (overbar/andaith) |
| Rising stroke | acute | U+E046 | acute-teng |
| Falling stroke | grave | U+E054 | grave-teng |

### Register Modifiers (below-tengwa position)

| Modifier | Meaning | Codepoint | Glyph Name |
|----------|---------|-----------|------------|
| (none) | high register | - | - |
| Single dot | mid register | U+E045 | unutixe-teng |
| Double dot | low register | U+E043 | dotdblbelow-teng |

### Composed Marks

The full extended inventory for 6+ tones:

| Visual | Name | Composition | Used For |
|--------|------|-------------|----------|
| flat bar | high level | U+E050 | Cantonese T1 |
| rising | high rising | U+E046 | Cantonese T2 |
| flat bar + dot | mid level | U+E050 + U+E045 | Cantonese T3 |
| falling + double-dot | low falling | U+E054 + U+E043 | Cantonese T4 |
| rising + double-dot | low rising | U+E046 + U+E043 | Cantonese T5 |
| flat bar + double-dot | low level | U+E050 + U+E043 | Cantonese T6 |

## Placement

Tone marks are placed **below the tengwa** bearing the nuclear vowel, same as the Mandarin mode. For composed marks:

```
  [vowel tehta]
  [  tengwa   ]
  [contour mark]
  [register dot(s)]
```

In practice, fonts may implement this as a single combined glyph or as stacked combining marks. The Alcarin Extended font includes the contour marks; register dots use existing below-mark codepoints.

## Extension to Hakka (6 Tones)

Hakka has the same 6-tone structure as Cantonese with minor pitch differences. The same mark system applies directly:

| Tone | Hagfa Pinyim | Chao | Description | Mark |
|------|--------------|------|-------------|------|
| 1 | 1 | 24 | high rising | rising stroke |
| 2 | 2 | 11 | low level | flat bar + double-dot |
| 3 | 3 | 31 | low falling | falling stroke + double-dot |
| 4 | 4 | 55 | high level | flat bar |
| 5 | 5 | 33 | mid level | flat bar + dot |
| 6 | 6 | 55 | high level (variant) | flat bar |

Note: Hakka tone assignments vary by dialect. The exact mapping should be documented per dialect in the Hakka mode specification.

Hakka also has checked tones (syllables ending in /-p/, /-t/, /-k/). As with Cantonese, the final stop implies checked quality.

## Extension to Min (7-8 Tones)

Min languages (Hokkien, Teochew, etc.) have 7-8 tones in their citation forms, exceeding the 6-tone inventory above.

### Proposed Extension: Triple-Dot Modifier

For Min's additional register distinction, add a **triple-dot** modifier:

| Modifier | Meaning | Codepoint | Glyph Name |
|----------|---------|-----------|------------|
| Triple dot | extra-low register | U+E041 | dottriplebelow-teng |

This would give a potential 12-mark inventory (4 contours x 3 registers), more than enough for any Sinitic tone system.

### Min Tone Mapping (Preliminary)

Hokkien (Taiwanese) example (Tainan accent):

| Tone | POJ | Chao | Description | Proposed Mark |
|------|-----|------|-------------|---------------|
| 1 | unmarked | 44 | mid level | flat bar + dot |
| 2 | ` | 53 | high falling | falling stroke |
| 3 | - | 21 | low falling | falling stroke + double-dot |
| 4 | (stop) | 32 | low checked | (final stop implies) |
| 5 | ^ | 24 | rising | rising stroke |
| 7 | = | 33 | mid level | flat bar + dot |
| 8 | (stop) | 4 | high checked | (final stop implies) |

Note: Tone 6 merged with Tone 7 in most Min dialects. Exact mappings require further research per dialect.

### Font Glyph Needs for Min

The triple-dot below mark (U+E041 dottriplebelow-teng) already exists in the Alcarin character map. No new glyphs are needed for Min.

## Relationship to Mandarin Mode

The extended system is a strict superset of the Mandarin tone marks:

| Mandarin | Cantonese Equivalent | Mark |
|----------|----------------------|------|
| Tone 1 (high level) | Tone 1 | flat bar |
| Tone 2 (rising) | Tone 2 | rising stroke |
| Tone 3 (dipping) | - | chevron (unique to Mandarin) |
| Tone 4 (falling) | - | falling stroke (high register) |

Mandarin Tone 3 (dipping, 214) has no direct Cantonese equivalent. The chevron mark (three-dot circumflex, U+E040) remains available for Mandarin and any other language needing a dipping contour.

Mandarin Tone 4 uses the plain falling stroke (no register modifier), representing high-falling. Cantonese Tone 4 uses falling + double-dot, representing low-falling. This is phonetically accurate.

## Summary

The extended tone system uses three orthogonal components:

1. **Contour shape** (flat, rising, falling, dipping)
2. **Register modifier** (none = high, dot = mid, double-dot = low, triple-dot = extra-low)
3. **Checked quality** (implied by final stop consonant /-p/, /-t/, /-k/)

This provides a unified, extensible framework for all major Sinitic tone systems while maintaining backward compatibility with the Mandarin mode and using only existing Alcarin glyphs.

## Font Requirements Summary

For Cantonese and Hakka (6 tones):
- All required glyphs exist in Alcarin Extended
- No new font work needed

For Min (7-8 tones):
- All required glyphs exist in Alcarin Extended (triple-dot at U+E041)
- No new font work needed

Composed marks (contour + register dots) may benefit from precomposed ligature glyphs for optical refinement, but this is an enhancement, not a requirement.
