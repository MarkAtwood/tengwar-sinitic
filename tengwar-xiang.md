# Tengwar Mode for Xiang Chinese (Changsha)

## Why this mode exists

Xiang is one of the major Chinese language groups, spoken by approximately 38 million people primarily in Hunan province. This mode targets the **Changsha dialect**, the prestige variety of New Xiang and the basis for the community-standard romanization.

Xiang occupies a phonologically intermediate position among Sinitic languages:

- Like Mandarin, it has **lost all final stop consonants** (-p, -t, -k merged to open syllables)
- Like Mandarin, it has a **two-way laryngeal contrast** (aspirated vs. unaspirated, no voiced obstruents)
- Unlike Mandarin, it preserves **six tones** including a distinct "entering tone" (rusheng)
- Unlike Mandarin, it has **nasalized vowels** /o, e/ as phonemes

The distinctive feature of Changsha Xiang is **Tone 6 (rusheng)**: the historical entering tone survives as a purely tonal category with no stop coda. Where Cantonese preserves -p/-t/-k, and Min preserves -p/-t/-k/-h, Changsha has lost the consonants entirely but retained the tonal distinction. This is a transitional state between conservative and innovative Chinese varieties.

This is a phonemic tehtar mode. It transcribes the sounds of Changsha Xiang as analyzed through the Beta 5.0 romanization system. It does not represent Chinese characters, etymologies, or meaning. It is a way of writing what you hear.

## Romanization reference

This mode uses **Beta 5.0** (changsha-hua pinyin fang'an), a community-developed romanization system. Beta 5.0 is not an official government standard but has become the de facto reference for Changsha dialect documentation.

Key features of Beta 5.0:

- Tone numbers 1-6 (unlike Pinyin's 1-4)
- Aspiration marked with `h` following stops/affricates (p/ph, t/th, k/kh, c/ch, q/qh)
- Nasalized vowels written with final `-n` when no nasal coda follows
- Uses `r` for the retroflex approximant (where present)
- Uses `ng-` for initial velar nasal

Note: Older romanization systems exist (including missionary romanizations from the 19th century), but Beta 5.0 is the current community standard.

## Consonants

Changsha Xiang has **19 initial consonants** plus a null initial. The inventory is similar to Mandarin but with some differences:

- No retroflex affricates /ts, tsh/ (merged with alveolars or palatals)
- Limited retroflex fricative /s/ (in free variation with /s/ for many speakers)
- Velar nasal /ng/ can appear initially (unlike Standard Mandarin)

### Two-way laryngeal contrast

Xiang patterns with **Group A** (Mandarin/Cantonese/Hakka):

| Contrast | Voiceless unaspirated | Voiceless aspirated |
|----------|----------------------|---------------------|
| Bilabial | p /p/ | ph /ph/ |
| Alveolar | t /t/ | th /th/ |
| Velar | k /k/ | kh /kh/ |
| Alveolar affr. | c /ts/ | ch /tsh/ |
| Palatal affr. | q /tc/ | qh /tch/ |

No voiced obstruents. This means Grade 1 = voiceless unaspirated, Grade 2 = voiceless aspirated, following the Mandarin convention.

### Tengwar grade assignment

| Grade | I: Alveolar | II: Labial | III: Velar | IV: (unused) |
|-------|-------------|------------|------------|--------------|
| 1 (vl. unasp.) | tinco /t/ **t** | parma /p/ **p** | calma /k/ **k** | -- |
| 2 (vl. asp.) | ando /th/ **th** | umbar /ph/ **ph** | anga /kh/ **kh** | -- |
| 3 (fric.) | thule /s/ **s** | formen /f/ **f** | hwesta /x/ **h** | -- |
| 5 (nasal) | numen /n/ **n** | malta /m/ **m** | noldo /ng/ **ng** | -- |
| 6 (approx.) | lambe /l/ **l** | -- | -- | -- |

Bold = Beta 5.0 letter.

Column IV (retroflex) is largely unused in Changsha. The retroflex fricative /s/, where it occurs, can be written with harma, but most speakers merge it with /s/.

### Alveolar affricates: c, ch

Following the Mandarin convention, alveolar affricates use extended-stem Column I tengwar:

| Beta 5.0 | IPA | Tengwa | Grid |
|----------|-----|--------|------|
| c | /ts/ | tinco-ext | I-1 ext. |
| ch | /tsh/ | ando-ext | I-2 ext. |

### Palatals: q, qh, x

The palatal series /tc, tch, c/ (Beta 5.0: q, qh, x) follows the Mandarin convention: Column III tengwar with the below-tengwa palatal diacritic.

| Beta 5.0 | IPA | Tengwa | Grid |
|----------|-----|--------|------|
| q | /tc/ | calma + palatal mark | III-1 + pal. |
| qh | /tch/ | anga + palatal mark | III-2 + pal. |
| x | /c/ | hwesta + palatal mark | III-3 + pal. |

### Velar nasal initial

Unlike Standard Mandarin, Changsha permits initial /ng/:

| Beta 5.0 | IPA | Tengwa |
|----------|-----|--------|
| ng- | /ng/ | noldo |

Example: nga "I" (colloquial first person pronoun)

### Complete initial mapping

| Beta 5.0 | IPA | Tengwa | Diacritics | Grid |
|----------|-----|--------|------------|------|
| p | /p/ | parma | -- | II-1 |
| ph | /ph/ | umbar | -- | II-2 |
| m | /m/ | malta | -- | II-5 |
| f | /f/ | formen | -- | II-3 |
| t | /t/ | tinco | -- | I-1 |
| th | /th/ | ando | -- | I-2 |
| n | /n/ | numen | -- | I-5 |
| l | /l/ | lambe | -- | I-6 |
| k | /k/ | calma | -- | III-1 |
| kh | /kh/ | anga | -- | III-2 |
| ng | /ng/ | noldo | -- | III-5 |
| h | /x/ | hwesta | -- | III-3 |
| c | /ts/ | tinco-ext | -- | I-1 ext. |
| ch | /tsh/ | ando-ext | -- | I-2 ext. |
| s | /s/ | thule | -- | I-3 |
| q | /tc/ | calma | + palatal | III-1 + pal. |
| qh | /tch/ | anga | + palatal | III-2 + pal. |
| x | /c/ | hwesta | + palatal | III-3 + pal. |
| (zero) | -- | telco | -- | (carrier) |

### Retroflex notes

Some speakers and older documentation include retroflex consonants (zh, ch, sh, r) parallel to Mandarin. Where these occur:

| Beta 5.0 | IPA | Tengwa | Grid |
|----------|-----|--------|------|
| zr | /ts/ | quesse | IV-1 |
| chr | /tsh/ | ungwe | IV-2 |
| sr | /s/ | harma | IV-3 |
| r | /r/ | ore | IV-6 |

Most modern Changsha speakers merge these with the alveolar or palatal series. This mode supports both analyses.

## Vowels

Tehtar on the preceding consonant (Quenya-style placement), consistent with all Sinitic modes.

### Basic vowels

| Beta 5.0 | IPA | Tehta | Description |
|----------|-----|-------|-------------|
| a | /a/ | a-tehta | three dots above |
| o | /o/ | o-tehta | left curl above |
| e | /e/ | e-tehta | acute stroke above |
| i | /i/ | i-tehta | single dot above |
| u | /u/ | u-tehta | right curl above |
| y | /y/ | u-tehta + i-tehta | combined (front rounded) |

The front rounded vowel /y/ (Beta 5.0: y) uses the Mandarin convention: both u-tehta and i-tehta together.

### Nasalized vowels

Changsha Xiang has two phonemically nasalized vowels:

| Beta 5.0 | IPA | Oral counterpart |
|----------|-----|------------------|
| on | /o/ | /o/ |
| en | /e/ | /e/ |

These are written with `-n` in Beta 5.0 when no nasal coda follows. Minimal pairs exist:

- /ko/ "dog" vs. /ko/ (nasalized, different word)
- /se/ vs. /se/ (nasalized)

**Tengwar representation:** Use the tilde-below diacritic from Min mode:

| Beta 5.0 | IPA | Tengwar |
|----------|-----|---------|
| on | /o/ | o-tehta + tilde-below |
| en | /e/ | e-tehta + tilde-below |

The tilde-below appears below the tengwa, above any tone marks.

### Schwa

Changsha has a schwa /e/ that may be nasalized. Write with e-tehta (context distinguishes from /e/).

### Diphthongs

| Beta 5.0 | IPA | Tehta | Notes |
|----------|-----|-------|-------|
| ai | /ai/ | a-tehta | falling diphthong |
| ao | /au/ | a-tehta | falling diphthong |
| ei | /ei/ | e-tehta | falling diphthong |
| ou | /ou/ | o-tehta | falling diphthong |
| ia | /ia/ | medial anna + a-tehta | rising diphthong |
| ie | /ie/ | medial anna + e-tehta | rising diphthong |
| io | /io/ | medial anna + o-tehta | rising diphthong |
| iu | /iu/ | medial anna + u-tehta | rising diphthong |
| ua | /ua/ | medial vala + a-tehta | rising diphthong |
| uo | /uo/ | medial vala + o-tehta | rising diphthong |
| ui | /ui/ | medial vala + i-tehta | rising diphthong |
| ye | /ye/ | medial anna+pal. + e-tehta | rising diphthong |

Following established conventions:
- Falling diphthongs: write nuclear vowel tehta only
- Rising diphthongs: use medial glide tengwar (anna for /j/, vala for /w/)

### Medial glides

| Glide | Tengwa |
|-------|--------|
| /j/ | anna |
| /w/ | vala |
| /y/ | anna + palatal mark |

## Codas

Changsha Xiang permits only **nasal codas**. All historical stop codas (-p, -t, -k) have been lost.

### Nasal codas

| Beta 5.0 | IPA | Tengwa |
|----------|-----|--------|
| -n | /n/ | numen |
| -ng | /ng/ | noldo |

Unlike Cantonese and Hakka, there is no /-m/ coda in Changsha (merged with /-n/).

### No stop codas

This is a crucial difference from conservative varieties:

| Historical | Cantonese | Min | Changsha |
|------------|-----------|-----|----------|
| *-p | -p | -p | (lost) |
| *-t | -t | -t | (lost) |
| *-k | -k | -k | (lost) |
| *-h | -- | -h | (lost) |

The historical "entering tone" syllables that once had stop codas are now open syllables in Changsha. The tonal distinction survives (as Tone 6), but the consonant is gone.

## Tones

Changsha Xiang has **six tones**:

| Tone | Name | Chao value | Contour | Type |
|------|------|-----------|---------|------|
| 1 | yin-ping | 34 | mid-rising | smooth |
| 2 | yang-ping | 13 / 223 | low-rising | smooth |
| 3 | shang | 42 | falling | smooth |
| 4 | yin-qu | 45 | high-rising | smooth |
| 5 | yang-qu | 21 | low-falling | smooth |
| 6 | ru (entering) | 14 / 24 | rising, short | **rusheng** |

### The Tone 6 problem: rusheng without a coda

Tone 6 is historically the "entering tone" (rusheng). In conservative varieties like Cantonese, entering tone syllables end in stop codas (-p, -t, -k), and the tone is phonetically short because the stop closure cuts off the vowel.

In Changsha, the stop codas have been lost, but Tone 6 remains distinct:
- **Phonetically short** (shorter duration than smooth tones)
- **Distinct pitch contour** (14 or 24, rising)
- **No consonant coda** (the syllable is open)

This is a purely tonal distinction with no segmental reflex.

### Tengwar representation of Tone 6

**Design decision:** Tone 6 uses the same mark system as other tones, with no coda consonant.

The contour is rising (like Tone 1, 2, and 4), but the pitch values differ:
- T1: 34 (mid-high level-ish, slight rise)
- T2: 13/223 (low-rising)
- T4: 45 (high-rising)
- T6: 14/24 (low-to-mid rising, short)

The shortness of T6 is not marked explicitly. In speech, duration distinguishes T6 from T2 and T4. In writing, context (primarily vocabulary) disambiguates.

**Alternative considered:** Marking T6 with a special "short" diacritic or using halla as a null coda. Rejected because:
1. The distinction is purely prosodic, not segmental
2. Adding a "phantom" glottal stop would be phonologically dishonest
3. Duration is not phonemically contrastive in any other Sinitic mode

### Tone marks

Using the contour + register system from the shared infrastructure:

| Tone | Contour | Register | Mark composition |
|------|---------|----------|------------------|
| 1 (34) | rising | mid | rising stroke + single dot |
| 2 (13) | rising | low | rising stroke + double dot |
| 3 (42) | falling | (high) | falling stroke |
| 4 (45) | rising | high | rising stroke |
| 5 (21) | falling | low | falling stroke + double dot |
| 6 (14/24) | rising | low-mid | rising stroke + single dot (same as T1) |

**Tone 1 vs. Tone 6 ambiguity:** Both T1 (34) and T6 (14/24) are rising tones in a similar register range. Visual disambiguation options:

1. **Accept the ambiguity:** Like T4 (unmarked) in Min checked syllables, context resolves it
2. **Use a distinct mark for T6:** A dedicated "short" or "entering" mark

**This mode chooses option 2:** Tone 6 uses a rising stroke with an **under-bar** (short horizontal bar below) to indicate the entering-tone category. This visually signals "this syllable belongs to the rusheng class" without falsely implying a stop coda.

### Complete tone inventory

| Tone | Visual description | Composition |
|------|-------------------|-------------|
| 1 (yin-ping) | rising stroke + dot | mid-rising |
| 2 (yang-ping) | rising stroke + double-dot | low-rising |
| 3 (shang) | falling stroke | high-falling |
| 4 (yin-qu) | rising stroke (bare) | high-rising |
| 5 (yang-qu) | falling stroke + double-dot | low-falling |
| 6 (ru) | rising stroke + under-bar | entering (short rising) |

### Placement

Tone marks appear **below the tengwa** bearing the nuclear vowel:

```
  [vowel tehta]
  [  tengwa   ]
  [contour mark]
  [register modifier]
```

For syllables with nasal codas, the tone mark stays below the nuclear vowel bearer, not the coda:

```
  [vowel tehta]
  [  initial  ] [nasal coda]
  [tone mark  ]
```

## Syllable structure

Changsha syllables follow the template:

```
(Initial) (Medial) Nucleus (Nasal coda) Tone
```

Where:
- **Initial:** One of 19 consonants, or null
- **Medial:** /j/, /w/, or /y/ (limited distribution)
- **Nucleus:** A vowel tehta (oral or nasal)
- **Coda:** -n or -ng, or none
- **Tone:** One of 6 marks

### Key constraints

1. No stop codas (all historical -p, -t, -k lost)
2. No -m coda (merged with -n)
3. Nasalized vowels do not co-occur with nasal codas
4. Tone 6 syllables never have codas (historically they ended in stops; now they're open)

## Sample syllables

### Basic syllables

| Beta 5.0 | Meaning | Tengwar structure |
|----------|---------|-------------------|
| nga1 | I (colloquial) | noldo + a-tehta + T1 |
| tha1 | he/she | ando + a-tehta + T1 |
| li3 | inside | lambe + i-tehta + T3 |
| kho4 | go | anga + o-tehta + T4 |
| fan5 | rice | formen + a-tehta + numen + T5 |

### Syllables with palatals

| Beta 5.0 | Meaning | Tengwar structure |
|----------|---------|-------------------|
| qhi4 | to eat | anga+pal. + i-tehta + T4 |
| xi3 | to wash | hwesta+pal. + i-tehta + T3 |
| qiu2 | ball | calma+pal. + anna + u-tehta + T2 |

### Syllables with nasalized vowels

| Beta 5.0 | Meaning | Tengwar structure |
|----------|---------|-------------------|
| kon3 | dog | calma + o-tehta + tilde-below + T3 |
| sen1 | to live | thule + e-tehta + tilde-below + T1 |

### Tone 6 (entering tone) syllables

These are historically checked syllables, now open:

| Beta 5.0 | Meaning | Tengwar structure | Historical |
|----------|---------|-------------------|------------|
| pa6 | hundred | parma + a-tehta + T6 | *pak |
| se6 | color | thule + e-tehta + T6 | *sek |
| qi6 | seven | calma+pal. + i-tehta + T6 | *tsit |
| mo6 | ink | malta + o-tehta + T6 | *mok |
| fu6 | fortune | formen + u-tehta + T6 | *fuk |

Note: The Tone 6 mark (rising + under-bar) signals the entering-tone category. No coda consonant appears.

### Syllables with nasal codas

| Beta 5.0 | Meaning | Tengwar structure |
|----------|---------|-------------------|
| san1 | three | thule + a-tehta + numen + T1 |
| tang2 | sugar | tinco + a-tehta + noldo + T2 |
| ming4 | bright | malta + i-tehta + noldo + T4 |
| pen3 | book | parma + e-tehta + numen + T3 |

### Tone contrasts

| Beta 5.0 | Tone | Meaning | Tengwar structure |
|----------|------|---------|-------------------|
| ma1 | T1 | mother | malta + a-tehta + T1 |
| ma2 | T2 | hemp | malta + a-tehta + T2 |
| ma3 | T3 | horse | malta + a-tehta + T3 |
| ma4 | T4 | scold | malta + a-tehta + T4 |
| ma5 | T5 | (varies) | malta + a-tehta + T5 |
| ma6 | T6 | (rusheng) | malta + a-tehta + T6 |

## Comparison with Mandarin

| Feature | Mandarin | Changsha Xiang |
|---------|----------|----------------|
| Tones | 4 (+neutral) | 6 |
| Stop codas | None | None |
| Entering tone | Merged into T2/T4 | Preserved as T6 |
| Nasalized vowels | No | Yes (/o/, /e/) |
| Initial ng- | Coda only | Initial and coda |
| Retroflex series | Full set | Marginal/merging |
| Palatals | j, q, x | q, qh, x |
| Aspiration marking | p vs. b | ph vs. p |

The most significant difference is the preservation of the entering tone as a distinct category (T6), even without the stop codas that define it in conservative varieties.

## Compatibility

This mode is **compatible with Group A** (Mandarin/Cantonese/Hakka):
- Grade 1 = voiceless unaspirated
- Grade 2 = voiceless aspirated
- No voiced obstruents

It is **incompatible with Group B** (Min/Wu), which uses Grade 2 for voicing.

Shared components:
- All basic tengwar assignments
- Palatal diacritic convention
- Extended stems for affricates
- Quenya-style tehtar placement
- Below-tengwa tone placement
- Nasal coda tengwar

Xiang-specific components:
- Tone 6 mark (entering tone without coda)
- Nasalized vowel marking (shared with Min)

## Font requirements

### Glyphs from earlier modes

All Mandarin mode glyphs are required. The tilde-below from Min mode is also used for nasalized vowels.

### New glyph for Xiang

| Glyph | Purpose | Description |
|-------|---------|-------------|
| Under-bar | Tone 6 marker | Short horizontal bar below contour mark |

The under-bar appears below the rising stroke, signaling the entering-tone category. It is positioned in the register-modifier zone but is distinct from the register dots.

**Alternative implementation:** If font extension is not possible, Tone 6 can be written with the same mark as Tone 1 (rising + dot), with disambiguation left to context. This is suboptimal but workable.

## Summary

The Xiang (Changsha) Tengwar mode:

1. **Uses Group A grade semantics** (Grade 2 = aspirated), compatible with Mandarin/Cantonese/Hakka
2. **Has 19 initials** including initial ng- but with reduced/merged retroflexes
3. **Has no stop codas** (all historical -p/-t/-k lost)
4. **Marks 6 tones** using contour + register system
5. **Preserves the entering tone (T6)** as a purely tonal category, marked distinctively
6. **Represents nasalized vowels** with tilde-below (as in Min)

The distinctive contribution of this mode is the handling of Tone 6: a historical "entering tone" that has lost its defining consonant but retained its categorical status. The under-bar modifier signals this unique situation without falsely implying a stop coda.

## References

- Beta 5.0 romanization documentation (community standard)
- Bauer, R. S. (2018). "Xiang" in *The Oxford Handbook of Chinese Linguistics*
- Norman, J. (1988). *Chinese*. Cambridge University Press.
- Wikipedia: [Xiang Chinese](https://en.wikipedia.org/wiki/Xiang_Chinese)
- Wikipedia: [Changsha dialect](https://en.wikipedia.org/wiki/Changsha_dialect)
