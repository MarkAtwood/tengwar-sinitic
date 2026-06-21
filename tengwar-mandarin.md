# Tengwar Mode for Mandarin Chinese

## Why this mode exists

Nobody has published a Tengwar mode for any Chinese language. There are modes for Kurdish, Lingala, and High Valyrian, but not for the language spoken by more humans than any other. The only Tengwar mode for a tonal language at all is Laicasaane's Vietnamese mode from 2016.

Mandarin is a good fit for Tengwar. Its phonology is small and regular: 21 initial consonants, a handful of vowels, only two possible coda consonants, and a strict syllable template. The difficulty is tones. Every syllable carries one of four contrastive tones (plus a neutral tone), and without them the language is unintelligible. The script has to encode them.

This is a phonemic tehtar mode. It transcribes the sounds of Standard Mandarin as analyzed through the Pinyin system. It does not represent Chinese characters, etymologies, or meaning. It is a way of writing what you hear.

## Consonants

Mandarin's consonants fall into four places of articulation that map onto the four Tengwar series: alveolar, labial, velar, and retroflex.

The retroflex assignment needs justification. Column IV is the labiovelar (quessetéma) series in Quenya. Mandarin has no labiovelars. It does have a complete retroflex series (four members: unaspirated affricate, aspirated affricate, fricative, approximant) that fills the column naturally. Tolkien was explicit in Appendix E that series assignments shift between modes to fit the target language. The General Use mode already reassigns Column III from velar to /tʃ/. Retroflex is the most retracted articulation in Mandarin, which parallels how Column IV sits at the "back" of the grid.

The rows handle manner of articulation. Here's where Mandarin forces the first real design choice.

Mandarin has no voiced obstruents. Its stops and affricates contrast by aspiration: /p/ vs. /pʰ/, /t/ vs. /tʰ/, etc. In Elvish modes, Grade 1 (single bow) is voiceless and Grade 2 (doubled bow) is voiced. I map Grade 1 to unaspirated and Grade 2 to aspirated. The doubled bow means "more energy at the same place," which is what aspiration is. Tolkien's note in Appendix E that extended stems "usually represented aspirated consonants (e.g. t+h, p+h, k+h), but might represent other consonantal variations required" gave me the precedent, but I use the doubled bow rather than extended stems because I need extended stems for the alveolar affricates (below), and because the doubled bow fills the grid cleanly.

| Grade | I: Alveolar | II: Labial | III: Velar | IV: Retroflex |
|---|---|---|---|---|
| 1 (unasp.) | tinco /t/ **d** | parma /p/ **b** | calma /k/ **g** | quessë /tʂ/ **zh** |
| 2 (asp.) | ando /tʰ/ **t** | umbar /pʰ/ **p** | anga /kʰ/ **k** | ungwë /tʂʰ/ **ch** |
| 3 (fric.) | thúlë /s/ **s** | formen /f/ **f** | hwesta /x/ **h** | harma /ʂ/ **sh** |
| 5 (nasal) | númen /n/ **n** | malta /m/ **m** | ñoldo /ŋ/ **(ng)** | — |
| 6 (approx.) | lambe /l/ **l** | — | — | órë /ɻ/ **r** |

Bold = Pinyin letter. Parenthesized (ng) is coda-only.

The tengwar names (tinco, ando, etc.) are Quenya words. Their original phonetic values differ from what's assigned here. That's normal. Every non-Elvish mode reassigns phonetic values; the names are labels, not definitions.

### Alveolar affricates: z, c

Mandarin has a plain alveolar affricate pair /ts/ and /tsʰ/ (Pinyin z and c) distinct from both the alveolar stops and the retroflexes. Same place of articulation as /t/ and /tʰ/, different manner.

I write them with extended-stem Column I tengwar: extended tinco for /ts/, extended ando for /tsʰ/. This follows the German phonemic mode at tengwar.info, which uses extended tinco for /ts/ and extended parma for /pf/, citing the same Appendix E passage about extended stems representing "other consonantal variations required." The German affricates are the closest precedent for Mandarin's.

### Palatals: j, q, x

The palatal series /tɕ, tɕʰ, ɕ/ (Pinyin j, q, x) are in complementary distribution with the velars. They appear only before /i/ and /y/. Following Tolkien's tyelpetéma convention, I write them as Column III (velar) tengwar with a double-dot palatal diacritic below:

- /tɕ/ (j): calma + palatal mark
- /tɕʰ/ (q): anga + palatal mark
- /ɕ/ (x): hwesta + palatal mark

This is phonologically honest. The palatals derive historically from velars before front vowels, and the notation makes the relationship visible.

### Zero initial

Syllables starting with a vowel (like ài, ér, ān) use the short vowel carrier (telco).

## Vowels

Tehtar on the preceding consonant (Quenya-style placement). Mandarin syllables end in vowels or nasals far more often than in consonants, which makes this the natural choice.

| Vowel | IPA | Tehta |
|---|---|---|
| a | /a/ | three dots (circumflex shape) |
| o | /o/ | left curl |
| e | /ɤ~ə/ | acute stroke |
| i | /i/ | single dot |
| u | /u/ | right curl |
| ü | /y/ | see below |

Pinyin uses the same letter for different phonemes depending on context (the letter "e" covers /ɤ/, /ɛ/, and /ə/; the letter "a" covers /a/ and /ɑ/). These are allophonic. The mode collapses them to one tehta each. A Mandarin reader will pronounce correctly from syllable context, the same way an English reader handles the letter "a" in "cat" versus "call."

### The ü vowel

The vowel /y/ (Pinyin ü) appears only after certain initials, and its representation depends on context:

**After j, q, x:** Write the regular u-tehta (right curl). No ambiguity exists because /u/ never occurs after palatals. Pinyin itself drops the umlaut here (writing ju, qu, xu rather than jü, qü, xü).

**After l, n:** The contrast between /y/ and /u/ is meaningful (lǜ vs. lù, nǚ vs. nǔ). Write both the u-tehta and i-tehta together, side by side. This represents the phonetic reality: /y/ is a front rounded vowel, combining the tongue position of /i/ with the lip rounding of /u/.

This approach uses only existing tehtar and requires no font modification.

### Diphthongs

Mandarin has several diphthongs: ao, ou, ai, ei, ia, ie, ua, uo, üe. Write only the primary (nuclear) vowel tehta; the glide is implied.

| Pinyin | Tehta | Notes |
|--------|-------|-------|
| ao | a-tehta | /au/ — glide to /u/ implied |
| ou | o-tehta | /ou/ — glide to /u/ implied |
| ai | a-tehta | /ai/ — glide to /i/ implied |
| ei | e-tehta | /ei/ — glide to /i/ implied |

For rising diphthongs (ia, ie, ua, uo, üe), the medial glide is written as a separate tengwa (see Medial glides below), and the nuclear vowel takes the tehta.

This keeps each syllable visually clean with one vowel mark above and one tone mark below. Mandarin readers will pronounce correctly from context, just as Pinyin readers do.

### The apical vowels

After z, c, s and zh, ch, sh, r, the Pinyin letter "i" is not the vowel /i/. It's a syllabic continuant (/z̩/ or /ʐ̩/), essentially the consonant itself sustaining through the syllable with no real vowel segment. Some phonological analyses treat these syllables as having no vowel at all.

This mode follows that analysis. A bare consonant tengwa with a tone mark and no vowel tehta is a syllabic consonant. This is unambiguous: every other syllable starting with zh, ch, sh, r, z, c, s requires a vowel tehta, so its absence can only mean one thing.

## Medial glides

When /j/, /w/, or /ɥ/ appear between the initial and the nuclear vowel (as in jiā, guó, xué), they are written as tengwar between the initial and the vowel:

| Glide | Tengwa |
|---|---|
| /j/ | anna |
| /w/ | vala |
| /ɥ/ | anna + palatal mark |

When the high vowel is the nuclear vowel itself (no following vowel), it's a tehta on the consonant, not a separate tengwa. So jī (机) is calma+palatal with i-tehta. But jiā (家) is calma+palatal, then anna with a-tehta.

## Codas

Mandarin allows exactly two coda consonants: /n/ and /ŋ/.

I write -n by appending númen after the vowel. I write -ng by appending ñoldo. Straightforward and unambiguous.

I did not use the overbar convention. In standard Tengwar usage, an overbar on a consonant means a nasal *preceding* that consonant (so overbar+tinco = /nt/). Using it for a *following* nasal would invert the established meaning. Appending the nasal tengwa costs one glyph of width per syllable, but it avoids confusing anyone who knows Tengwar.

Erhua (the -r suffix common in Beijing Mandarin) appends órë to the syllable.

## Tones

Every toned syllable carries one of four marks. The marks are iconographic, tracing pitch contour:

| Tone | Contour | Mark |
|---|---|---|
| 1 (high level) | ˥ | horizontal bar |
| 2 (rising) | ˧˥ | stroke rising left to right |
| 3 (dipping) | ˨˩˦ | chevron (v-shape) |
| 4 (falling) | ˥˩ | stroke falling left to right |
| 5 (neutral) | — | no mark |

The marks trace the pitch contour, following the same design principle as Pinyin's own diacritics and the Chao tone letters.

### Placement strategies

This mode defines two placement strategies. A document should use one consistently throughout.

**Below-tengwa placement (preferred):**

The tone mark sits below the tengwa or carrier bearing the nuclear vowel. This is the canonical form, preferred for handwriting and for typefaces that support below-glyph diacritics.

```
  [vowel tehta]
  [  tengwa   ]
  [tone mark  ]
```

For syllabic consonants (the apical vowels), the tone mark sits below the bare consonant tengwa.

**Carrier placement (fallback):**

When rendering with a typeface that lacks below-tengwa diacritics, append a short carrier (telco) after the syllable. The tone mark appears above the carrier as a tehta, using existing glyphs:

| Tone | Tehta on carrier |
|------|------------------|
| 1 (high level) | overbar (andaith) |
| 2 (rising) | acute stroke |
| 3 (dipping) | three-dot circumflex |
| 4 (falling) | grave stroke |

```
  [vowel tehta]       [tone tehta]
  [  tengwa   ]       [  telco   ]
```

Neutral tone takes no mark. In carrier placement, it also takes no carrier.

### Choosing a strategy

- **Handwriting:** Use below-tengwa placement. The four marks are simple strokes that fit naturally beneath the letter body.
- **Digital, custom font:** Use below-tengwa placement. Requires extending the font with four below-glyph marks.
- **Digital, stock font:** Use carrier placement. Works with unmodified Tengwar Annatar, Tengwar Eldamar, Tengwar Parmaite, and other standard fonts.

### Tone sandhi

Tone sandhi is not written. Citation tones only, matching Pinyin convention (你好 is written nǐhǎo even though it's pronounced níhǎo).

## Rendering and compatibility

This mode is designed to work at two levels:

**Full compatibility (carrier placement):** Works immediately with any existing Tengwar font. The tone carrier adds horizontal width but requires no font modification. All tehtar and tengwar used are standard.

**Native rendering (below-tengwa placement):** Requires a font extended with below-glyph marks. The below-tengwa position is used in some existing modes (underposed dot for silent-e in English, unutixe for syllabic consonants in German), so the position itself is not unprecedented.

An extended font is available: [Alcarin Tengwar Extended](https://github.com/MarkAtwood/Alcarin-Tengwar) adds the required below-marks (gravebelow for Tone 4, plus symmetry glyphs completing the above/below inventory). Build instructions in `fonts/Alcarin-Tengwar/Font source/BUILD_GUIDE.md`. PRs submitted upstream.

For handwriting, below-tengwa placement is natural and requires no special tools.

## Sample text

UDHR Article 1 in Mandarin:

人人生而自由，在尊严和权利上一律平等。他们赋有理性和良心，并应以兄弟关系的精神相互对待。

Rénrén shēng ér zìyóu, zài zūnyán hé quánlì shàng yīlǜ píngděng. Tāmen fùyǒu lǐxìng hé liángxīn, bìng yīng yǐ xiōngdì guānxi de jīngshén xiānghù duìdài.

### Syllable breakdown (carrier placement)

| Pinyin | Structure |
|--------|-----------|
| rén | órë + e-tehta, númen, telco + acute |
| shēng | harma + e-tehta, ñoldo, telco + overbar |
| ér | telco + e-tehta, órë, telco + acute |
| zì | ext. tinco, telco + grave |
| yóu | anna + o-tehta, vala, telco + acute |
| ... | |

*Full Tengwar rendering in preparation.*

## Complete initial mapping

| Pinyin | IPA | Tengwa | Grid |
|---|---|---|---|
| b | /p/ | parma | II-1 |
| p | /pʰ/ | umbar | II-2 |
| m | /m/ | malta | II-5 |
| f | /f/ | formen | II-3 |
| d | /t/ | tinco | I-1 |
| t | /tʰ/ | ando | I-2 |
| n | /n/ | númen | I-5 |
| l | /l/ | lambe | I-6 |
| g | /k/ | calma | III-1 |
| k | /kʰ/ | anga | III-2 |
| h | /x/ | hwesta | III-3 |
| j | /tɕ/ | calma + pal. | III-1+pal. |
| q | /tɕʰ/ | anga + pal. | III-2+pal. |
| x | /ɕ/ | hwesta + pal. | III-3+pal. |
| zh | /tʂ/ | quessë | IV-1 |
| ch | /tʂʰ/ | ungwë | IV-2 |
| sh | /ʂ/ | harma | IV-3 |
| r | /ɻ/ | órë | IV-6 |
| z | /ts/ | ext. tinco | I-1 ext. |
| c | /tsʰ/ | ext. ando | I-2 ext. |
| s | /s/ | thúlë | I-3 |
| ∅ | — | telco | (carrier) |
