# Tengwar Mode for Wu Chinese (Shanghainese)

## Why this mode exists

Wu Chinese is spoken by approximately 80 million people in the Yangtze River Delta region, centered on Shanghai. It is the second-largest Chinese language group after Mandarin. Wu preserves a **three-way laryngeal contrast**---voiceless unaspirated, voiceless aspirated, and voiced---that Mandarin has lost. This phonological feature aligns Wu more closely with Middle Chinese and with the classical Tengwar voicing system than any other major Sinitic language.

This mode takes a principled approach: instead of hacking aspiration into the Tengwar grade system (as the Mandarin and Cantonese modes do), it returns to **classical Tengwar voicing semantics** and marks aspiration with a diacritic. The result is a mode that is phonologically honest, internally consistent, and closer to Tolkien's original design.

**This mode is incompatible with the Mandarin and Cantonese modes.** They cannot be mixed in a single document. A reader must know which mode applies. This is an acceptable cost for a principled design.

## The case for classical voicing semantics

### The problem with existing Sinitic modes

The Mandarin and Cantonese modes repurpose the Tengwar grade system:
- Grade 1 (single bow) = voiceless unaspirated
- Grade 2 (doubled bow) = voiceless aspirated

This works for languages with a two-way contrast, but the semantics are strained. The doubled bow in classical Tengwar means "voiced counterpart," not "aspirated counterpart." Using it for aspiration is a functional hack, not a principled assignment.

The Min mode faces a three-way contrast and hacks further: it uses Grade 3 (the fricative grade) for voiced stops. Formen becomes /b/ instead of /f/; hwesta becomes /g/ instead of /x/. The grade system loses its articulatory coherence entirely.

### The Wu solution: return to source

Wu Chinese has the same three-way contrast as Min, but Wu offers an opportunity to design correctly from the start. The classical Tengwar grades map naturally:

| Grade | Classical (Sindarin) | Wu (this mode) |
|-------|---------------------|----------------|
| 1 | voiceless stops | voiceless unaspirated |
| 2 | voiced stops | voiced stops |
| 3 | voiceless fricatives | voiceless fricatives |
| 4 | voiced fricatives | voiced fricatives |

The mapping is phonetically honest. Voiceless stays voiceless; voiced stays voiced. Aspiration---which is a secondary articulation, not a voicing distinction---is marked with a diacritic.

### Why aspiration should be a diacritic

Aspiration is a laryngeal gesture superimposed on an oral articulation. It does not change place or manner of articulation. In IPA, it is written as a superscript: /ph/, not a separate phoneme. A diacritic representation is phonologically appropriate.

Classical Tengwar already uses diacritics for secondary articulations:
- The palatal mark modifies velars to palatals
- The labialization mark modifies velars to labiovelars
- The nasalization tilde (in the Min mode) modifies oral vowels to nasal

Aspiration fits this pattern. An aspirated /ph/ is "p with aspiration," just as /kw/ is "k with labialization."

## Consonants

### The three-way laryngeal contrast

Wu has the following stop and affricate inventory:

| Place | Voiceless unasp. | Voiceless asp. | Voiced |
|-------|------------------|----------------|--------|
| Bilabial | /p/ | /ph/ | /b/ |
| Alveolar | /t/ | /th/ | /d/ |
| Velar | /k/ | /kh/ | /g/ |
| Alv. affricate | /ts/ | /tsh/ | /dz/ |
| Alv-pal. affricate | /tc/ | /tch/ | /dz/ |

### Grade assignments

| Grade | Articulation | Examples |
|-------|--------------|----------|
| 1 | voiceless unaspirated stops/affricates | /p, t, k, ts, tc/ |
| 2 | voiced stops/affricates | /b, d, g, dz, dz/ |
| 3 | voiceless fricatives | /f, s, c, x, h/ |
| 4 | voiced fricatives | /v, z, z, G/ |
| 5 | nasals | /m, n, N, n/ |
| 6 | approximants/laterals | /l, j, w/ |

### The aspiration diacritic

**Proposed mark: a rightward-opening hook or curl above the tengwa.**

Design rationale:
1. It should be visually distinct from vowel tehtar (which sit above)
2. It should suggest "breath" or "puff of air"
3. It should be small enough not to crowd the vowel tehta
4. It should have no existing Tengwar meaning that would cause confusion

**Candidate glyphs:**

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| Small h-curl | Miniature version of halla | Iconic (h = aspiration) | May crowd tehtar |
| Superscript dot-cluster | Two small dots horizontally | Simple | Ambiguous with i-tehta |
| Rightward hook | Like a small acute with curve | Distinctive | Novel glyph |
| Doubled tehta carrier | Double the vowel tehta | Uses existing shapes | May be confusing |

**Recommendation: A small rightward-opening curl (like a tiny halla) positioned at the upper-right corner of the tengwa, below and to the right of the vowel tehta zone.**

This mark:
- Evokes the breath of aspiration
- Does not conflict with existing diacritics
- Is visually lightweight
- Can be implemented as a combining mark in the PUA

**Codepoint assignment:** U+E070 (proposed), named `aspiration-mark`.

### Consonant grid

| Grade | I: Alveolar | II: Labial | III: Velar |
|-------|-------------|------------|------------|
| 1 (vl. unasp.) | tinco /t/ | parma /p/ | calma /k/ |
| 1 + asp. | tinco+asp /th/ | parma+asp /ph/ | calma+asp /kh/ |
| 2 (voiced) | ando /d/ | umbar /b/ | anga /g/ |
| 3 (fric.) | thule /s/ | formen /f/ | hwesta /x~h/ |
| 4 (vd. fric.) | anto /z/ | ampa /v/ | unque /G/ |
| 5 (nasal) | numen /n/ | malta /m/ | noldo /N/ |
| 6 (approx.) | lambe /l/ | vala /w/ | -- |

Note: The voiced velar fricative /G/ is allophonic with /g/ in many Wu varieties. It appears intervocalically and may be written as Grade 2 anga in casual notation.

### Affricate series

| Grade | Alveolar (ext.) | Alveolo-palatal |
|-------|-----------------|-----------------|
| 1 (vl. unasp.) | ext. tinco /ts/ | calma+pal /tc/ |
| 1 + asp. | ext. tinco+asp /tsh/ | calma+pal+asp /tch/ |
| 2 (voiced) | ext. ando /dz/ | anga+pal /dz/ |
| 3 (fric.) | thule /s/ | hwesta+pal /c/ |
| 4 (vd. fric.) | anto /z/ | unque+pal /z/ |

The alveolo-palatal series uses Column III tengwar with the palatal diacritic, following the Mandarin mode convention.

### Complete initial mapping

| IPA | Wu Pinyin | Tengwa | Diacritics | Grid |
|-----|-----------|--------|------------|------|
| /p/ | b | parma | -- | II-1 |
| /ph/ | p | parma | aspiration | II-1+asp |
| /b/ | bb | umbar | -- | II-2 |
| /m/ | m | malta | -- | II-5 |
| /f/ | f | formen | -- | II-3 |
| /v/ | v | ampa | -- | II-4 |
| /t/ | d | tinco | -- | I-1 |
| /th/ | t | tinco | aspiration | I-1+asp |
| /d/ | dd | ando | -- | I-2 |
| /n/ | n | numen | -- | I-5 |
| /l/ | l | lambe | -- | I-6 |
| /k/ | g | calma | -- | III-1 |
| /kh/ | k | calma | aspiration | III-1+asp |
| /g/ | gg | anga | -- | III-2 |
| /N/ | ng | noldo | -- | III-5 |
| /x~h/ | h | hwesta | -- | III-3 |
| /ts/ | z | ext. tinco | -- | I-1 ext. |
| /tsh/ | c | ext. tinco | aspiration | I-1 ext.+asp |
| /dz/ | zz | ext. ando | -- | I-2 ext. |
| /s/ | s | thule | -- | I-3 |
| /z/ | ss | anto | -- | I-4 |
| /tc/ | j | calma | palatal | III-1+pal |
| /tch/ | q | calma | palatal + asp | III-1+pal+asp |
| /dz/ | jj | anga | palatal | III-2+pal |
| /c/ | x | hwesta | palatal | III-3+pal |
| /z/ | xx | unque | palatal | III-4+pal |
| /n/ | gn | noldo | palatal | III-5+pal |
| /j/ | y | anna | -- | -- |
| /w/ | w | vala | -- | -- |
| null | -- | telco | -- | (carrier) |

### Phonological notes

1. **Voiced obstruent devoicing:** In younger Shanghainese speakers, voiced stops /b, d, g/ are increasingly realized as "slack-voiced" or "breathy-voiced" rather than fully voiced. The Tengwar representation preserves the phonemic distinction regardless of phonetic realization.

2. **Glottal stop:** Some Wu dialects have a phonemic glottal stop /P/. Use halla if needed.

3. **Velar nasal initial:** /N/ occurs syllable-initially in Wu (as in Cantonese), unlike Mandarin where it is coda-only.

4. **The "voiced h":** The phoneme sometimes transcribed as /H/ or breathy /h/ in Wu phonology is here written as hwesta (Grade 3, voiceless). Its voiced character comes from co-articulation with voiced vowels, not from an inherent voicing specification.

## Vowels

Tehtar on the preceding consonant (Quenya-style placement), consistent with all Sinitic modes.

### Basic vowel tehtar

| Wu Pinyin | IPA | Tehta | Codepoint |
|-----------|-----|-------|-----------|
| a | /a/ | three dots (a-tehta) | U+E040 |
| o | /o/ | left curl (o-tehta) | U+E048 |
| e | /E/ or /e/ | acute stroke (e-tehta) | U+E046 |
| i | /i/ | single dot (i-tehta) | U+E044 |
| u | /u/ | right curl (u-tehta) | U+E049 |
| y | /y/ | u+i tehta combined | U+E049 + U+E044 |

### The schwa vowel

Wu has a central vowel /e/ (schwa) that contrasts with /e/. Following the Cantonese precedent:

| Wu Pinyin | IPA | Tehta |
|-----------|-----|-------|
| oe | /e/ | underdot |

The underdot (U+E045) signals centralized quality, as in the Cantonese short /a/.

### Diphthongs

Wu has several diphthongs. Following the established convention, falling diphthongs write only the nuclear vowel:

| Wu Pinyin | IPA | Tehta |
|-----------|-----|-------|
| au | /Au/ | a-tehta |
| ou | /eu/ | o-tehta |
| ai | /E/ | a-tehta |
| ei | /e/ | e-tehta |

Rising diphthongs use medial glide tengwar (anna for /j/, vala for /w/).

### Syllabic consonants

Wu has syllabic nasals and possibly syllabic fricatives in some analyses:

| Wu Pinyin | IPA | Tengwa |
|-----------|-----|--------|
| m | /m/ | malta (no vowel tehta) |
| n | /n/ | numen (no vowel tehta) |
| ng | /N/ | noldo (no vowel tehta) |

A bare nasal tengwa with a tone mark signals a syllabic nasal.

## Tones

Shanghainese has a **five-tone system** with a yin/yang register split. The system differs from Mandarin's four tones and from Cantonese's six.

### The five citation tones

| Tone | Traditional name | Chao value | Contour |
|------|------------------|------------|---------|
| 1 | yin-ping (T1) | 53 | high falling |
| 2 | yang-ping (T2) | 31 | low falling |
| 3 | yin-shang (T3) | 55 | high level |
| 4 | yin-qu (T4) | 34 | mid rising |
| 5 | yang-qu (T5) | 13 | low rising |

Checked syllables (ending in glottal stop /P/):
- Yin-ru: high short (5)
- Yang-ru: low short (2)

### Tone marks

Following the contour + register system from the Cantonese mode:

| Tone | Contour | Register | Mark |
|------|---------|----------|------|
| T1 (53) | falling | high | falling stroke |
| T2 (31) | falling | low | falling stroke + double-dot |
| T3 (55) | level | high | flat bar |
| T4 (34) | rising | mid | rising stroke + single-dot |
| T5 (13) | rising | low | rising stroke + double-dot |

### Checked tones

For checked syllables (those ending in /-P/ or derived from historical *-p, *-t, *-k):

| Checked tone | Corresponds to | Mark |
|--------------|----------------|------|
| Yin-ru (high) | T3 | flat bar |
| Yang-ru (low) | T2 | falling + double-dot |

The glottal stop coda implies checked quality; the tone mark shows register.

### Tone mark placement

Below the tengwa bearing the nuclear vowel:

```
  [vowel tehta]
  [  tengwa   ]
  [aspiration mark (if aspirated)]
  [contour mark]
  [register dot(s)]
```

For aspirated consonants, the aspiration mark sits between the tengwa body and the tone mark zone.

## Tone sandhi

Wu Chinese has **left-dominant tone sandhi**, unlike Min's right-dominant pattern. In a polysyllabic word, the first syllable's tone spreads or determines the pattern for the entire word.

### Sandhi rule (Shanghainese)

In connected speech within a prosodic phrase:
1. The first syllable retains its citation tone contour
2. Subsequent syllables lose their lexical tone
3. The entire phrase takes a unified pitch pattern determined by the first syllable's register

| First syllable register | Pattern |
|-------------------------|---------|
| Yin (high) | High-falling spread: 55-31 or 55-33-31 |
| Yang (low) | Low-rising spread: 13-44 or 22-33-44 |

### Policy: Citation tones in isolation, surface tones in phrases

**Design decision:** Write citation tones for isolated words, surface tones for connected phrases.

This differs from the Min mode (surface tones always) and from the Mandarin mode (citation tones always). The hybrid approach reflects Wu sandhi realities:

1. Wu sandhi is **domain-based**: it applies within prosodic phrases, not across phrase boundaries.
2. For isolated words or phrase-final position, citation tones are correct.
3. For running text, the converter applies sandhi within phrases.

A romanization-to-Tengwar converter must:
1. Parse phrase boundaries (spaces, punctuation, or explicit markers)
2. Within each phrase, determine the sandhi domain
3. Retain the first syllable's citation tone
4. Reduce subsequent syllables to neutral (unmarked) or apply spread pattern

**Simplified notation:** For running text, mark only the first syllable of each sandhi domain; leave subsequent syllables unmarked. This captures the functional reality that non-initial syllables lose distinctive tone.

## Final consonants

Modern Shanghainese has limited coda inventory compared to Middle Chinese:

| Coda | IPA | Tengwa |
|------|-----|--------|
| -n | /n/ | numen |
| -ng | /N/ | noldo |
| -P | /P/ | halla |

The historical *-m coda has merged with *-n in most Wu dialects. The stop codas *-p, *-t, *-k have merged to glottal stop /-P/.

### Examples with codas

| Wu Pinyin | IPA | Tengwar structure |
|-----------|-----|-------------------|
| san | /sE/ | thule + a-tehta + numen |
| zang | /zAN/ | ext.ando + a-tehta + noldo |
| baq | /baP/ | umbar + a-tehta + halla |
| seq | /seP/ | thule + e-tehta + halla |

## Syllable structure

Wu syllables follow the template:

```
(Initial) (Medial) Nucleus (Coda) Tone
```

Where:
- **Initial:** One of 29 consonants (including aspirated variants), or null
- **Medial:** /j/ or /w/ (limited distribution)
- **Nucleus:** A vowel tehta or syllabic nasal
- **Coda:** -n, -ng, or -P (glottal stop)
- **Tone:** One of 5 marks (or unmarked in sandhi)

### Visual structure

**Aspirated initial, open syllable:**
```
  [vowel tehta]
  [  tengwa   ] [asp mark]
  [ tone mark ]
```

**Voiced initial with coda:**
```
  [vowel tehta]
  [  tengwa   ] [coda]
  [ tone mark ]
```

## Sample syllables

### Voicing contrast (minimal triad)

| Wu Pinyin | IPA | Meaning | Structure |
|-----------|-----|---------|-----------|
| ba | /pa/ | eight | parma + a-tehta + T4 |
| pa | /pha/ | afraid | parma + asp + a-tehta + T4 |
| bba | /ba/ | to pull | umbar + a-tehta + T2 |

### Aspiration diacritic examples

| Wu Pinyin | IPA | Structure |
|-----------|-----|-----------|
| ti | /thi/ | tinco + asp + i-tehta |
| qi | /tchi/ | calma + pal + asp + i-tehta |
| cu | /tshu/ | ext.tinco + asp + u-tehta |

### Voiced fricative examples

| Wu Pinyin | IPA | Meaning | Structure |
|-----------|-----|---------|-----------|
| va | /va/ | flower | ampa + a-tehta |
| zi | /zi/ | word | anto + i-tehta |

### Syllables with glottal stop coda

| Wu Pinyin | IPA | Meaning | Structure |
|-----------|-----|---------|-----------|
| baq | /baP/ | white | umbar + a-tehta + halla |
| seq | /seP/ | color | thule + e-tehta + halla |
| goq | /geP/ | country | anga + o-tehta + halla |

## Comparison with other modes

### Incompatibility notice

**This mode is not compatible with the Mandarin, Cantonese, or Min modes.**

| Feature | Mandarin/Cantonese | Min | Wu (this mode) |
|---------|-------------------|-----|----------------|
| Grade 1 | voiceless unasp. | voiceless unasp. | voiceless unasp. |
| Grade 2 | voiceless asp. | voiceless asp. | **voiced** |
| Grade 3 | fricative | **voiced** (hack) | fricative |
| Aspiration | doubled bow | doubled bow | **diacritic** |

A document must declare which mode it uses. Mixed-mode documents are not supported.

### Why mode-specific is better than "universal Sinitic"

A universal mode for all Sinitic languages would require:
1. Grade slots for three laryngeal series (unasp/asp/voiced)
2. Diacritics or extensions for retroflexes, palatals, labiovelars
3. Nasal vowel marking (Min)
4. Phonemic length marking (Cantonese)
5. 8+ tone distinctions with register and contour

Such a mode would be:
- Cluttered: Every syllable would carry multiple diacritics
- Ambiguous: Readers couldn't predict which features apply
- Unfaithful: No language uses all features simultaneously

Dialect-specific modes are cleaner. Each mode uses the minimal notation needed for its phonology. A reader knowing "this is Wu mode" has complete, unambiguous information.

### Shared features with other modes

These elements carry over unchanged:

1. **Extended stems for affricates** (ext. tinco, ext. ando)
2. **Palatal diacritic** for alveolo-palatal series
3. **Quenya-style tehtar placement** (vowel on preceding consonant)
4. **Below-tengwa tone marks** with contour + register system
5. **Nasal codas** (numen, noldo)
6. **Glottal stop coda** (halla)
7. **Null initial** (telco carrier)
8. **Medial glides** (anna, vala)

## Font requirements

### New glyph

| Glyph | Purpose | Codepoint | Description |
|-------|---------|-----------|-------------|
| Aspiration mark | marks voiceless aspirated consonants | U+E070 (proposed) | Small rightward curl, upper-right of tengwa |

### Implementation notes

The aspiration mark should:
- Be positioned at the upper-right corner of the tengwa, below and right of the vowel tehta zone
- Be small (approximately 1/3 the height of a vowel tehta)
- Curve rightward, evoking breath
- Combine with both base tengwar and extended-stem tengwar
- Stack correctly with the palatal diacritic (aspiration outside palatal)

### Existing glyphs

All other glyphs are standard Tengwar or already present in the Alcarin Tengwar Extended font:
- Grade 1-4 tengwar in all columns
- Extended-stem alveolar series
- Palatal diacritic
- Tone contour marks
- Register dots

## Summary

The Wu Tengwar mode:

1. **Returns to classical Tengwar semantics**: Grade 1 voiceless, Grade 2 voiced
2. **Marks aspiration with a diacritic**: Phonologically honest, visually minimal
3. **Represents the three-way laryngeal contrast**: /p/ vs. /ph/ vs. /b/ distinguished cleanly
4. **Uses 29 initial consonants**: All grades populated according to Wu phonology
5. **Marks 5 tones**: Using the contour + register system
6. **Handles left-dominant sandhi**: Citation tones phrase-initially, neutral elsewhere
7. **Is incompatible with other Sinitic modes**: By design, for clarity

The mode demonstrates that a principled design---one that respects both the target language's phonology and the source script's semantics---produces a cleaner result than hacking existing conventions.

## Romanization systems

This mode accepts input in **Qian Nairong's Shanghainese Pinyin** or **Wugniu romanization**, normalizing to a consistent internal representation.

### Key correspondences

| Feature | This document | Qian Nairong | Wugniu |
|---------|---------------|--------------|--------|
| Voiced stops | bb, dd, gg | b, d, g | b, d, g |
| Voiceless unasp. | b, d, g | p, t, k | p, t, k |
| Voiceless asp. | p, t, k | ph, th, kh | ph, th, kh |
| Glottal stop coda | -q | -q or -h | -k |

The converter normalizes input romanization to the internal representation before mapping to Tengwar.

## References

- Qian, Nairong. (2007). *Shanghai Dialect: An Introduction to Speaking and Understanding*. Hippocrene Books.
- Chen, Yiya, & Gussenhoven, Carlos. (2015). Shanghai Chinese. *Journal of the International Phonetic Association*, 45(3), 321-337.
- Zee, Eric. (2003). Shanghai Phonology. In G. Thurgood & R. J. LaPolla (Eds.), *The Sino-Tibetan Languages* (pp. 131-138). Routledge.
- Sherard, Michael. (1972). *Shanghai Phonology*. PhD dissertation, Cornell University.
- Wikipedia: [Shanghainese](https://en.wikipedia.org/wiki/Shanghainese)
- Wikipedia: [Wu Chinese](https://en.wikipedia.org/wiki/Wu_Chinese)
