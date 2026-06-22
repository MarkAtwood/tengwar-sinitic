# Font Extension Requirements for Wu Chinese

This document specifies the glyph additions and anchor modifications required
to support the Wu Chinese (Shanghainese) Tengwar mode in Alcarin Tengwar.

## Summary

**One new glyph is required:** the aspiration mark (U+E0B0).

All other marks needed for Wu support already exist in Alcarin Tengwar Extended:

- Grade 1-4 tengwar (all exist)
- Extended-stem affricates (exist)
- Palatal diacritic (exists)
- Tone contour marks (exist from Cantonese mode)
- Register modifier dots (exist)
- Glottal stop halla (exists)

The new glyph requires a new anchor type (`topright` / `_topright`) for proper
positioning at the upper-right corner of base tengwar.

---

## 1. New Glyph: Aspiration Mark

### Specifications

| Property | Value |
|----------|-------|
| Codepoint | U+E0B0 |
| Glyph name | aspiration-teng |
| Category | Mark |
| Subcategory | Nonspacing |
| Script | tengwar |
| Production name | uniE0B0 |
| Description | TENGWAR COMBINING MARK ASPIRATION |

**Note on codepoint:** The design documents originally proposed U+E070, but that
codepoint is already assigned to `zero-teng` (Tengwar digit zero). U+E0B0 is in
the extended PUA range used for Sinitic mode additions.

### Design Requirements

#### Shape

A **rightward-opening curl**, resembling a miniature halla (the glottal stop
tengwa). The shape evokes the puff of breath associated with aspiration.

```
    ╭─
    │
    ╰
```

The curl opens to the right, with:
- An upward stem beginning at the attachment point
- A rightward curve at the top
- A small downward terminal

This is essentially the upper portion of halla, scaled down.

#### Size

Approximately **1/3 the height of a standard vowel tehta**.

| Reference | Approximate height |
|-----------|-------------------|
| Vowel tehta (e.g., dotabove-teng) | 100% |
| Aspiration mark | 30-35% |

The mark should be visually lightweight---present but not dominant.

#### Position

**Upper-right corner of the tengwa**, in a dedicated zone:

```
  [vowel tehta]     <- _top anchor (standard tehtar zone)
  [  tengwa   ][asp] <- aspiration at topright
  [ tone mark ]     <- _bottom anchor (standard tone zone)
```

The aspiration mark occupies a position that:
1. Is to the right of the tengwa stem
2. Is below the vowel tehta zone (does not overlap with tehtar)
3. Is above the baseline and any below-tengwa marks
4. Aligns horizontally with the rightmost extent of the tengwa bow

#### Anchoring

The aspiration mark requires a new anchor pair:

| Anchor | On glyph | Purpose |
|--------|----------|---------|
| `topright` | Base tengwar | Attachment point for aspiration mark |
| `_topright` | aspiration-teng | Connects to base tengwa's `topright` |

**Anchor position on base tengwar:**

The `topright` anchor should be placed at:
- X: Right edge of the tengwa bow (or stem for single-bow tengwar)
- Y: Approximately 2/3 up the tengwa height, below the tehta zone

**Anchor position on aspiration mark:**

The `_topright` anchor should be at the bottom-left of the curl, where it
attaches to the base tengwa.

### Stacking Considerations

The aspiration mark must stack correctly with the palatal diacritic. For
palatalized aspirates like /tɕʰ/ (Pinyin "q"), the stacking order is:

```
  [vowel tehta]           <- _top on base
  [  calma   ][pal][asp]  <- palatal closer to stem, aspiration outside
  [ tone mark ]           <- _bottom on base
```

**Stacking rule:** Palatal mark sits closer to the tengwa stem; aspiration mark
sits further right (outside the palatal).

This requires:
1. The palatal diacritic to have a `topright` anchor (for chaining aspiration)
2. The aspiration mark's `_topright` to attach to either:
   - The base tengwa's `topright` (for non-palatalized aspirates), or
   - The palatal mark's `topright` (for palatalized aspirates)

### Visual Reference: Existing Analogues

For design consistency, reference these existing marks in Alcarin:

| Glyph | Relevant feature |
|-------|------------------|
| halla (U+E028) | The curl shape to miniaturize |
| w-curl / rightcurlbelow-teng (U+E04B) | Below-tengwa positioning logic |
| palatal diacritic | Stacking companion; similar size class |

The w-curl (labialization mark) demonstrates how a small curl-shaped diacritic
attaches to a base tengwa. The aspiration mark follows similar positioning
logic, but at the upper-right rather than below.

---

## 2. Anchor Modifications

### New Anchor Pair: `topright` / `_topright`

All base tengwar that can take aspiration need a `topright` anchor:

**Grade 1 tengwar (voiceless unaspirated -> aspirated with diacritic):**
- tinco (U+E001)
- parma (U+E011)
- calma (U+E021)
- extended-tinco (U+E061)
- extended-parma (U+E062)
- extended-calma (U+E063)

**Palatal diacritic:**
- The palatal mark also needs `topright` to allow aspiration chaining

### Anchor Positioning Guidelines

For a standard-width tengwa (e.g., parma):

```
                    topright anchor
                         |
                         v
    +-----------------+
    |   tehta zone    |  <- top anchor here
    |                 |
    |    ┌──────┐     |•  <- topright anchor (~2/3 height)
    |    │      │     |
    |    │      │     |
    |    │      │     |
    +----┴──────┴-----+
         |
         v
      bottom anchor
```

The `topright` anchor X-coordinate should align with the rightmost curve of the
tengwa bow. For double-bow tengwar (Grade 2), it aligns with the outer bow.

---

## 3. GlyphData.xml Entry

```xml
<glyph unicode="E0B0"
       name="aspiration-teng"
       sortName="teng400"
       category="Mark"
       subCategory="Nonspacing"
       script="tengwar"
       production="uniE0B0"
       direction="BIDI"
       description="TENGWAR COMBINING MARK ASPIRATION"
       anchors="_topright, topright"
       marks="aspiration-teng" />
```

The `marks` attribute lists itself to allow theoretical double-marking (though
this is not used in Wu phonology).

---

## 4. OpenType Feature Considerations

### Mark Positioning (GPOS)

The `mark` feature must include rules for:

1. **Aspiration on base tengwar:**
   ```
   mark aspiration-teng <anchor _topright>
     on tinco-teng <anchor topright>
     on parma-teng <anchor topright>
     on calma-teng <anchor topright>
     ... (all Grade 1 tengwar)
   ```

2. **Aspiration chained to palatal:**
   ```
   mark aspiration-teng <anchor _topright>
     on palatal-teng <anchor topright>
   ```

### Mark-to-Mark Stacking (mkmk)

For palatalized aspirates, the mark-to-mark feature chains:
1. Palatal attaches to base via `_bottom` (existing)
2. Aspiration attaches to palatal via `_topright` -> `topright`

This may require the palatal diacritic to gain a `topright` anchor.

### No GSUB Rules Required

The aspiration mark does not participate in any substitution rules. It is a
pure combining mark with no ligature behavior.

---

## 5. Existing Glyphs Confirmed

The following glyphs already exist and require no modification for Wu support:

### Base Tengwar

| Usage | Glyphs |
|-------|--------|
| Grade 1 stops | tinco, parma, calma |
| Grade 2 stops | ando, umbar, anga |
| Grade 3 fricatives | thule, formen, hwesta |
| Grade 4 fricatives | anto, ampa, unque |
| Grade 5 nasals | numen, malta, noldo |
| Grade 6 approximants | lambe, vala, anna |
| Extended affricates | ext-tinco, ext-ando |
| Carriers | telco, ara |
| Glottal stop | halla |

### Diacritics

| Usage | Glyph | Codepoint |
|-------|-------|-----------|
| Vowel tehtar | dottripleabove-teng, dotabove-teng, acute-teng, leftcurl-teng, rightcurl-teng | U+E040, U+E044, U+E046, U+E04C, U+E04A |
| Palatal mark | (existing below-tengwa double-dot) | -- |
| Tone contours | macronbelow-teng, acutebelow-teng, gravebelow-teng | U+E051, U+E047, U+E097 |
| Register dots | dotbelow-teng, dotdblelow-teng | U+E045, U+E043 |
| Schwa marker | dotbelow-teng | U+E045 |

---

## 6. Implementation Checklist

- [ ] Create aspiration-teng glyph (U+E0B0)
  - [ ] Design rightward-opening curl shape
  - [ ] Scale to 1/3 vowel tehta height
  - [ ] Add `_topright` anchor at attachment point
  - [ ] Add `topright` anchor for theoretical chaining

- [ ] Add `topright` anchors to base tengwar
  - [ ] tinco, parma, calma (Grade 1)
  - [ ] extended-tinco, extended-parma, extended-calma
  - [ ] All other tengwar that could theoretically take aspiration

- [ ] Add `topright` anchor to palatal diacritic
  - [ ] Enables aspiration stacking on palatalized consonants

- [ ] Update GPOS mark feature
  - [ ] Add aspiration-teng positioning rules
  - [ ] Add mark-to-mark rules for palatal + aspiration stacking

- [ ] Add GlyphData.xml entry

- [ ] Test rendering
  - [ ] Simple aspirates: /pʰ, tʰ, kʰ/ (parma+asp, tinco+asp, calma+asp)
  - [ ] Affricate aspirates: /tsʰ, tɕʰ/ (ext-tinco+asp, calma+pal+asp)
  - [ ] Palatalized aspirates: /tɕʰ/ (calma + palatal + aspiration)
  - [ ] With vowel tehtar: verify no collision
  - [ ] With tone marks: verify proper stacking

---

## 7. Visual Examples

### Simple Aspirate: /pʰa/ (Pinyin "pa")

```
    · · ·        <- a-tehta (dottripleabove-teng)
   ┌─────┐
   │     │  ╭─   <- aspiration mark at topright
   │     │  │
   │     │  ╰
   └─────┘
     ───         <- tone mark (macronbelow-teng)
```

### Palatalized Aspirate: /tɕʰi/ (Pinyin "qi")

```
      ·          <- i-tehta (dotabove-teng)
   ┌─────┐
   │     │  ··╭─ <- palatal (··) then aspiration (╭─)
   │     │    │
   │     │    ╰
   └──┬──┘
     ───         <- tone mark
```

### Comparison with Non-Aspirate: /pa/ vs /pʰa/ vs /ba/

```
/pa/ (voiceless unaspirated)    /pʰa/ (voiceless aspirated)    /ba/ (voiced)
        · · ·                           · · ·                       · · ·
       ┌─────┐                         ┌─────┐                    ┌──────┐
       │     │                         │     │  ╭─                │ ┌──┐ │
       │     │                         │     │  │                 │ │  │ │
       │     │                         │     │  ╰                 │ │  │ │
       └─────┘                         └─────┘                    └─┴──┴─┘
         ───                             ───                        ───
       parma                     parma + aspiration                umbar
```

---

## 8. Conclusion

Wu mode requires exactly one new glyph: the aspiration mark at U+E0B0.

All other required glyphs exist in the current Alcarin Tengwar Extended font.
The primary implementation work is:

1. Designing the aspiration-teng glyph
2. Adding the `topright` / `_topright` anchor infrastructure
3. Updating GPOS mark positioning rules

This is a modest font extension that enables the phonologically principled Wu
mode without disrupting existing Sinitic modes.

---

## References

- Design source: `docs/design-wu.md`
- Mode specification: `tengwar-wu.md`
- Font build guide: `fonts/Alcarin-Tengwar/Font source/BUILD_GUIDE.md`
- Existing extension: `docs/font-extension-cantonese.md`
