# Tengwar Modes for Sinitic Languages

A family of phonemic Tengwar modes for Chinese languages, covering all major varieties.

## Overview

This is the first published Tengwar mode family for Chinese languages. Each mode maps its language's phonology onto the Tengwar consonant grid with a unified system for encoding lexical tones.

### Language Coverage

| Language | Spec | Romanization | Tones | Stop Codas | Group |
|----------|------|--------------|-------|------------|-------|
| Mandarin | `tengwar-mandarin.md` | Pinyin | 4 | none | A |
| Cantonese | `tengwar-cantonese.md` | Jyutping | 6 | -p -t -k | A |
| Hakka | `tengwar-hakka.md` | Taiwan MOE | 6 | -p -t -k | A |
| Gan | `tengwar-gan.md` | Project-defined* | 7 | -t -k | A |
| Xiang | `tengwar-xiang.md` | Beta 5.0 | 6 | none | A |
| Min | `tengwar-min.md` | Tai-lo/POJ | 7 | -p -t -k -h | B |
| Wu | `tengwar-wu.md` | Wugniu | 5 | -ʔ | B |

*Gan has no standardized romanization; the project defines its own based on Pinfa conventions and IPA.

### Compatibility Groups

**Group A** (Mandarin, Cantonese, Hakka, Gan, Xiang): Grade 2 = aspirated. These modes are mutually compatible.

**Group B** (Min, Wu): Grade 2 = voiced, aspiration marked with diacritic. Uses classical Tengwar voicing semantics. Incompatible with Group A.

See `docs/sinitic-infrastructure.md` for shared patterns and design rationale.

### Beyond Sinitic

This project focuses on Sinitic (Chinese) languages. Other language families of the region — Tibetic, Mongolic, Tungusic (Manchu), Turkic (Uyghur), and historical languages like Tangut or Khitan — would require separate Tengwar modes with different conventions. These are out of scope here but would make natural sister projects.

We welcome proposals for Sinitic conlangs. If your constructed language has a Sinitic phonological basis, these modes should be adaptable to it.

**Key features:**

- Phonemic mapping of initials onto the Tengwar consonant grid
- Iconographic tone marks that trace pitch contour (contour + register system)
- Handles palatals, affricates, retroflex consonants, medial glides, and syllabic nasals
- Nasal vowels (Min), voiced obstruents (Min/Wu), and checked syllables (most modes)
- PDF samples with embedded vector glyphs (work without fonts installed)

### Example: 魔戒 in Tengwar

See [`samples/mandarin/lotr-titles.md`](samples/mandarin/lotr-titles.md) for the Mandarin translations of *The Lord of the Rings* rendered in Tengwar — including all three volume titles from both mainland and Taiwan editions, plus *The Hobbit*, *The Silmarillion*, and *Middle-earth*.

## Files

```
tengwar-mandarin.md      # Mandarin mode spec
tengwar-cantonese.md     # Cantonese mode spec
tengwar-hakka.md         # Hakka mode spec
tengwar-gan.md           # Gan mode spec (with romanization disclaimer)
tengwar-xiang.md         # Xiang mode spec
tengwar-min.md           # Min mode spec
tengwar-wu.md            # Wu mode spec

docs/
  sinitic-infrastructure.md   # Shared patterns across all modes

samples/
  mandarin/              # Mandarin samples (poetry, phrases)
  cantonese/             # Cantonese samples
  hakka/                 # Hakka samples
  gan/                   # Gan samples
  xiang/                 # Xiang samples
  min/                   # Min samples
  wu/                    # Wu samples
  pdf/                   # Vector PDFs (work without fonts)

fonts/Alcarin-Tengwar/   # Extended Tengwar font
```

## Font

This project extends [Alcarin Tengwar](https://github.com/Tosche/Alcarin-Tengwar) (OFL-licensed) with glyphs needed for tonal modes. The fork at [github.com/MarkAtwood/Alcarin-Tengwar](https://github.com/MarkAtwood/Alcarin-Tengwar) adds 9 glyphs:

| Codepoint | Name | Purpose |
|-----------|------|---------|
| U+E096 | caronbelow-teng | Below caron (ˇ) |
| U+E097 | gravebelow-teng | Below grave — Tone 4 mark |
| U+E098 | rightcurl_dotinside-teng | Modified vowel tehta |
| U+E099 | brevebelow-teng | Below breve |
| U+E09A | tildebelow-teng | Below tilde |
| U+E09B | wavebelow-teng | Below wave |
| U+E09C | ringbelow-teng | Below ring |
| U+E09D | dottripleturnedbelow-teng | Below triple-dot-turned |
| U+E09E | leftcurl_dotinside-teng | Modified vowel tehta |

PRs [#19](https://github.com/Tosche/Alcarin-Tengwar/pull/19)–[#22](https://github.com/Tosche/Alcarin-Tengwar/pull/22) submitted upstream. Until merged, use the fork or build from `fonts/Alcarin-Tengwar/Font source/`.

## Status

**Complete.** All seven Sinitic modes are implemented with:
- Full specifications documenting phonological mappings
- Python converters (romanization → Tengwar)
- Sample texts with SVG and PDF renderings

Feedback welcome on edge cases, legibility, and sample texts.

## Design principles

1. **Phonemic, not logographic.** These modes write sounds, not characters or meanings.
2. **Respect Tengwar tradition.** Assignments cite precedent from Appendix E or established modes.
3. **Respect each language's phonology.** Complementary distribution, allophony, and distinctive features are handled correctly per language.
4. **Phonetic honesty.** Group B modes (Min/Wu) use classical Tengwar voicing semantics for languages with voiced obstruents, even though this creates incompatibility with Group A.

## License

CC BY-SA 4.0 — Attribution required, share-alike required, commercial use permitted.

## Contributing

Issues and pull requests welcome. For substantial changes, please open an issue first to discuss.

## Acknowledgments

Thanks to Måns Berg (boktypografen.se) for feedback on the Mandarin mode's grade assignments, leading to the swap of Column III (now retroflex) and Column IV (now velar) to align with cross-mode conventions.

## References

- Tolkien, J.R.R. "Appendix E: Writing and Spelling." *The Lord of the Rings.*
- Amanye Tenceli (amanye-tenceli.de) — Tengwar mode documentation
- Laicasaane's Vietnamese Tengwar Mode (2016) — precedent for tonal language
- German phonemic mode at tengwar.info — precedent for extended-stem affricates

## Contact

Mark Atwood — via GitHub issues or pull requests
