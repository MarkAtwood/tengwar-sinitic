# Tengwar Mode for Mandarin Chinese

A phonemic Tengwar mode for Standard Mandarin, transcribing the language as analyzed through the Pinyin romanization system.

## Overview

This is the first published Tengwar mode for any Chinese language. It maps Mandarin's phonology onto the Tengwar consonant grid and provides a system for encoding the four lexical tones.

**Key features:**

- Maps 21 Mandarin initials onto the four Tengwar series (alveolar, labial, velar, retroflex)
- Uses Grade 1/2 distinction for aspiration contrast (not voicing)
- Encodes tones with iconographic marks that trace pitch contour
- Two rendering strategies: below-tengwa marks (preferred) or carrier-based fallback for stock fonts
- Handles palatals, alveolar affricates, medial glides, and syllabic consonants

## Files

- `tengwar-mandarin-v4.md` — Full specification with rationale for all design decisions

## Status

**Draft for community review.** The phonological mapping is complete. Feedback welcome on:

- Edge cases in the syllable inventory
- Legibility of the ü representation (u+i tehtar after l/n)
- Carrier placement tone marks vs. below-tengwa marks
- Sample text renderings (in progress)

## Design principles

1. **Phonemic, not logographic.** This mode writes sounds, not characters or meanings.
2. **Respect Tengwar tradition.** Every assignment cites precedent from Appendix E or established modes.
3. **Respect Mandarin phonology.** Complementary distribution (palatals/velars) and allophony (apical vowels) are handled correctly.
4. **Work with existing fonts.** The fallback rendering strategy requires no font modifications.

## License

CC BY 4.0 — Attribution required, commercial use permitted.

## Contributing

Issues and pull requests welcome. For substantial changes, please open an issue first to discuss.

## References

- Tolkien, J.R.R. "Appendix E: Writing and Spelling." *The Lord of the Rings.*
- Amanye Tenceli (amanye-tenceli.de) — Tengwar mode documentation
- Laicasaane's Vietnamese Tengwar Mode (2016) — precedent for tonal language
- German phonemic mode at tengwar.info — precedent for extended-stem affricates

## Contact

Mark Atwood — via GitHub issues or pull requests
