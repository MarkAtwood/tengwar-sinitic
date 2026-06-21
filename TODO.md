# TODO

## Mandarin mode

Current status: draft, awaiting community review and sample renderings.

## Font work

- [x] Search `../AI` and GitHub for previous work forking Tengwar typefaces
- [x] Evaluate which font to extend (Annatar, Eldamar, Parmaite) → Alcarin Tengwar (OFL)
- [x] Add below-tengwa tone marks and symmetry glyphs to chosen font

**Completed:** Extended [Alcarin Tengwar](https://github.com/MarkAtwood/Alcarin-Tengwar) with 9 new glyphs:
- 7 below-marks completing above/below symmetry (caronbelow, gravebelow, brevebelow, tildebelow, wavebelow, ringbelow, dottripleturnedbelow)
- 2 dot-inside tehta variants (rightcurl_dotinside, leftcurl_dotinside)

Upstream PRs filed: [#19](https://github.com/Tosche/Alcarin-Tengwar/pull/19), [#20](https://github.com/Tosche/Alcarin-Tengwar/pull/20), [#21](https://github.com/Tosche/Alcarin-Tengwar/pull/21), [#22](https://github.com/Tosche/Alcarin-Tengwar/pull/22)

## Sample renderings

- [ ] UDHR Article 1 (carrier placement, stock font)
- [ ] UDHR Article 1 (below-tengwa placement, handwritten or custom font)

Classical poems — the ones every student learns:
- [ ] 静夜思 (Quiet Night Thought) — Li Bai, 5-char quatrain
- [ ] 春晓 (Spring Dawn) — Meng Haoran
- [ ] 悯农 (Pitying the Farmers) — Li Shen
- [ ] 咏鹅 (Ode to the Goose) — Luo Binwang, often the first poem children memorize
- [ ] 登鹳雀楼 (Climbing Stork Tower) — Wang Zhihuan

These are short, universally known, and cover a good range of syllable types.

## Submission

- [ ] Finalize sample images
- [ ] Submit to Amanye Tenceli
- [ ] Post to r/Tengwar for community feedback

## Future modes

Design goal: a family of Sinitic modes sharing core conventions, adapted per language.

### Cantonese (next priority)
- [ ] Research phoneme inventory (Jyutping as reference romanization)
- [ ] Map 6 tones (or 9 with checked tones) to extended tone mark system
- [ ] Handle final stops -p, -t, -k (Grade 1 codas? New convention?)
- [ ] Draft spec

### Hokkien (Southern Min)
- [ ] Research phoneme inventory (Pe̍h-ōe-jī or Tâi-lô as reference)
- [ ] Handle nasal vowels (nasalization tehta?)
- [ ] Handle tone sandhi (write citation tones only, matching Mandarin convention?)
- [ ] Draft spec

### Shanghainese (Wu)
- [ ] Search archive.org / HathiTrust for Joseph Edkins' 19th-century Shanghainese grammar and dictionary
- [ ] Review other missionary romanizations (T.P. Crawford 1885, John A. Silsby)
- [ ] Compare with Qian Nairong's modern Shanghainese Pinyin (钱拼, 2006)
- [ ] Research phoneme inventory from these sources
- [ ] Handle voiced obstruents — reconsider Grade 1/2 mapping (aspiration vs voicing)
- [ ] Handle register tone system
- [ ] Draft spec

### Hakka
- [ ] Research phoneme inventory (Pha̍k-fa-sṳ as reference)
- [ ] Handle final stops
- [ ] Draft spec

### Cross-cutting design questions
- [ ] Standardize tone mark inventory across modes (4 marks? 6? 9?)
- [ ] Document shared conventions in a "Sinitic mode family" design doc
- [ ] Decide on canonical romanization references for each language
