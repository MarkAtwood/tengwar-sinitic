# Tengwar Mode for Southern Min

## Why this mode exists

Southern Min (Minnan/Hokkien) is the third major Chinese language to receive a Tengwar mode, after Mandarin and Cantonese. It is spoken by approximately 50 million people across Taiwan, Fujian province, Southeast Asia, and diaspora communities worldwide. Min preserves many archaic Chinese features lost in Mandarin:

- **Voiced obstruents** (Mandarin has none)
- **Final stop consonants** (-p, -t, -k, and uniquely, -h as glottal stop)
- **Nasal vowels** (a distinctive Min feature)
- **7-8 tones** with extensive tone sandhi

This mode targets **Taiwanese Hokkien** as the primary variety, with notes on Teochew variations where relevant. Taiwanese blends the Quanzhou and Zhangzhou dialect bases, representing the most widely documented and standardized form of Southern Min.

The three unique challenges for Min that earlier modes did not face are:

1. **Nasal vowels** - phonemic nasalization requiring new notation
2. **Three-way laryngeal contrast** - voiceless unaspirated / voiceless aspirated / voiced
3. **Glottal stop final** - the /-h/ (/-ʔ/) coda consonant

This is a phonemic tehtar mode. It transcribes the sounds of Taiwanese Hokkien as analyzed through the Tai-lo or POJ romanization systems. It does not represent Chinese characters, etymologies, or meaning. It is a way of writing what you hear.

## Romanization reference

This mode accepts input in either **Tai-lo** (officially: Taiwan Minnan Language Romanization System) or **POJ** (Pe-oh-ji), normalizing internally to Tai-lo.

### Tai-lo (official)

The Taiwan Ministry of Education standard since 2006. Key features:

- Uses `ts`, `tsh` for affricates (not `ch`, `chh`)
- Uses `oo` for open-mid back vowel (not dotted `o`)
- Uses `nn` for nasalization (not superscript nasal)
- Tone marks: a (1/4 unmarked), a (2), a (3), a (5), a (7), ah (8)

### POJ (traditional)

The Presbyterian romanization from the 19th century, still widely used. Key differences:

- Uses `ch`, `chh` for affricates
- Uses `o` with dot above for /o/
- Uses superscript `n` for nasalization
- Same tone diacritics as Tai-lo

### Conversion table

| Feature | Tai-lo | POJ |
|---------|--------|-----|
| /ts/ | ts | ch |
| /tsh/ | tsh | chh |
| /o/ | oo | o (dotted) |
| nasal | ann, enn | an, en |
| /ua/ | ua | oa |
| /ue/ | ue | oe |

## Consonants

Taiwanese Hokkien has **18 initial consonants** plus a null initial. The most significant difference from Mandarin is the **three-way laryngeal contrast**: voiceless unaspirated, voiceless aspirated, and voiced.

### The three-way laryngeal contrast

| Contrast | Voiceless unasp. | Voiceless asp. | Voiced |
|----------|------------------|----------------|--------|
| Bilabial | p /p/ | ph /pʰ/ | b /b/ |
| Velar | k /k/ | kh /kʰ/ | g /g/ |
| Alveolar affr. | ts /ts/ | tsh /tsʰ/ | j /dz~z/ |

This differs from Mandarin (two-way: unaspirated/aspirated) and Cantonese (also two-way, different romanization).

### Tengwar grade assignment

This mode uses **classical Tengwar voicing semantics**, aligning with Wu Chinese:

- **Grade 1** (single bow) = voiceless unaspirated
- **Grade 2** (doubled bow) = voiced
- **Aspiration** = marked with a diacritic (not a grade distinction)

This returns to Tolkien's original design where Grade 2 indicates voicing. Aspiration is a secondary articulation marked separately, just as palatalization or labialization would be.

**Mode incompatibility:** This mode is **incompatible** with Mandarin and Cantonese modes, which use Grade 2 for aspiration. Min is **compatible** with Wu mode (same grade semantics). A document must declare which mode applies.

### The aspiration diacritic

Aspiration is a secondary articulation—it does not change place or manner. It is marked with a diacritic positioned at the upper-right of the tengwa, below the vowel tehta zone.

| Codepoint | Name | Description |
|-----------|------|-------------|
| U+E0B0 | aspiration-teng | Small rightward curl, marks /ʰ/ |

This is the same mark used in Wu mode. It parallels how Tengwar marks other secondary articulations (palatalization, labialization, nasalization) with diacritics rather than consuming grade slots.

### Consonant grid

| Grade | I: Alveolar | II: Labial | III: Velar |
|-------|-------------|------------|------------|
| 1 (vl. unasp.) | tinco /t/ **t** | parma /p/ **p** | calma /k/ **k** |
| 1 + asp | tinco+asp /tʰ/ **th** | parma+asp /pʰ/ **ph** | calma+asp /kʰ/ **kh** |
| 2 (voiced) | ando /d/ **–** | umbar /b/ **b** | anga /g/ **g** |
| 5 (nasal) | numen /n/ **n** | malta /m/ **m** | noldo /ng/ **ng** |
| 6 (approx.) | lambe /l/ **l** | -- | -- |

Bold = Tai-lo letter. Note: Min lacks voiced alveolar stop /d/; the ando slot is unused.

Plus alveolar affricates using extended stems:

| Grade | I: Alveolar (ext.) |
|-------|-------------------|
| 1 (vl. unasp.) | tinco-ext /ts/ **ts** |
| 1 + asp | tinco-ext+asp /tsʰ/ **tsh** |
| 2 (voiced) | ando-ext /dz/ **j** |

Plus fricatives and glottal:

| Consonant | Tengwa |
|-----------|--------|
| s /s/ | thule |
| h /h/ | halla |
| (zero) | telco (carrier) |

### Complete initial mapping

| Tai-lo | IPA | Tengwa | Diacritics | Codepoint | Grid |
|--------|-----|--------|------------|-----------|------|
| p | /p/ | parma | — | U+E011 | II-1 |
| ph | /pʰ/ | parma | +asp | U+E011 U+E0B0 | II-1+asp |
| b | /b/ | umbar | — | U+E012 | II-2 |
| m | /m/ | malta | — | U+E015 | II-5 |
| t | /t/ | tinco | — | U+E001 | I-1 |
| th | /tʰ/ | tinco | +asp | U+E001 U+E0B0 | I-1+asp |
| n | /n/ | numen | — | U+E005 | I-5 |
| l | /l/ | lambe | — | U+E026 | I-6 |
| k | /k/ | calma | — | U+E021 | III-1 |
| kh | /kʰ/ | calma | +asp | U+E021 U+E0B0 | III-1+asp |
| g | /g/ | anga | — | U+E022 | III-2 |
| ng | /ŋ/ | noldo | — | U+E025 | III-5 |
| ts | /ts/ | tinco-ext | — | U+E009 | I-1 ext. |
| tsh | /tsʰ/ | tinco-ext | +asp | U+E009 U+E0B0 | I-1 ext.+asp |
| j | /dz~z/ | ando-ext | — | U+E00A | I-2 ext. |
| s | /s/ | thule | — | U+E003 | I-3 |
| h | /h/ | halla | — | U+E029 | -- |
| (zero) | — | telco | — | U+E02F | (carrier) |

### Design notes on voiced consonants

With classical voicing semantics, Grade 2 tengwar carry their original meaning:
- umbar = /b/ (voiced bilabial stop)
- anga = /g/ (voiced velar stop)
- ando-ext = /dz/ (voiced alveolar affricate)

This aligns with Tolkien's Tengwar design and with Wu mode. The aspiration diacritic marks the secondary articulation of aspiration, keeping the grade system clean for the voicing contrast that is phonologically primary in Min.

### Phonological notes

- /l/ is often realized as an alveolar tap [r] in rapid speech.
- /b/ and /g/ may have prenasalized allophones [mb] and [ng] in some environments.
- /ts, tsh, s/ become palatalized [tc, tch, c] before /i/ and /in/.
- Syllabic /m/ and /ng/ can serve as syllable nuclei (e.g., m "not").

## Vowels

Tehtar on the preceding consonant (Quenya-style placement), same as the Mandarin and Cantonese modes. Min syllables end in vowels, nasals, or unreleased stops, making this the natural choice.

### Oral vowels

Taiwanese Hokkien has 5-6 basic oral vowels:

| Tai-lo | IPA | Tehta | Glyph | Codepoint |
|--------|-----|-------|-------|-----------|
| a | /a/ | a-tehta | three dots above | U+E040 |
| e | /e/ | e-tehta | acute stroke above | U+E046 |
| i | /i/ | i-tehta | single dot above | U+E044 |
| o | /o/ | o-tehta | left curl above | U+E048 |
| oo | /o/ | o-tehta + underdot | left curl + dot below | U+E048 + U+E045 |
| u | /u/ | u-tehta | right curl above | U+E049 |

The /o/ vs. /o/ distinction (Tai-lo "o" vs. "oo") uses the Cantonese pattern: underdot for the more open variant.

### Nasal vowels

**This is the most distinctive feature of Min phonology.** Hokkien has a full set of **nasalized vowel phonemes**, requiring new notation.

| Tai-lo | POJ | IPA | Example |
|--------|-----|-----|---------|
| ann | an | /a/ | sann "three (colloquial)" |
| enn | en | /e/ | khenn "pit" |
| inn | in | /i/ | phinn "nose" |
| onn | on | /o/ | honn "yes?" |
| unn | un | /u/ | (rare in isolation) |

**Nasalization is phonemic.** Minimal pairs exist:
- /a/ sa vs. /a/ sann ("sand" vs. "three")
- /i/ si vs. /i/ sinn ("silk" vs. "fresh")

### The nasalization tehta

**Design decision:** Use a tilde-below diacritic that combines with any vowel tehta.

The nasalization mark appears **below the tengwa**, in the same vertical zone as register modifiers. It does not conflict with tone marks because the nasalization mark attaches to the vowel position, while tone marks use separate contour shapes.

| Mark | Shape | Codepoint | Glyph Name | Purpose |
|------|-------|-----------|------------|---------|
| Nasalization | tilde (~) | U+E044 | tilde-below-teng | Marks vowel as nasalized |

**Placement:** Below the tengwa, above any register dots (if present).

### Nasal vowel tehtar table

Each oral vowel tehta can combine with the nasalization mark:

| Tai-lo | IPA | Oral Tehta | Nasal Composed Form |
|--------|-----|------------|---------------------|
| ann | /a/ | a-tehta | three-dots-above + tilde-below |
| enn | /e/ | e-tehta | acute-above + tilde-below |
| inn | /i/ | i-tehta | dot-above + tilde-below |
| onn | /o/ | o-tehta | left-curl + tilde-below |
| unn | /u/ | u-tehta | right-curl + tilde-below |

### Nasal diphthongs and triphthongs

Nasalization spreads across the entire nucleus. Write the nasalization mark once, on the nuclear vowel carrier:

| Tai-lo | IPA | Tengwar representation |
|--------|-----|------------------------|
| ainn | /ai/ | telco + a-tehta + nasal + anna |
| iunn | /iu/ | anna + i-tehta + nasal + vala |
| uainn | /uai/ | vala + a-tehta + nasal + anna |

For falling diphthongs, place the nasal mark on the nuclear vowel (first element). For triphthongs, place it on the central vowel.

### Mutual exclusivity rule

**Nasal vowels cannot co-occur with nasal codas (-m, -n, -ng).**

This is a phonotactic constraint of Min. If a syllable has a nasal vowel, it cannot end in a nasal consonant, and vice versa. The Tengwar representation naturally reflects this: either the nasalization diacritic appears (nasal vowel), or a nasal tengwa appears in coda position (nasal coda), never both.

### Diphthongs and triphthongs

Following the Mandarin/Cantonese conventions:

| Tai-lo | IPA | Notes |
|--------|-----|-------|
| ai | /ai/ | falling diphthong |
| au | /au/ | falling diphthong |
| ia | /ia/ | rising diphthong |
| io | /io/ | rising diphthong |
| iu | /iu/ | rising diphthong |
| ua | /ua/ | rising diphthong |
| ue | /ue/ | rising diphthong |
| ui | /ui/ | rising diphthong |
| iau | /iau/ | triphthong |
| uai | /uai/ | triphthong |

- Falling diphthongs: write nuclear vowel tehta only
- Rising diphthongs: use medial glide tengwar (anna, vala)
- Triphthongs: medial + nuclear + implied final glide

Nasalized versions also occur: /ai/, /au/, /ia/, /uai/, etc.

### Syllabic nasals

Min has two syllabic nasals that function as complete syllables:

| Tai-lo | IPA | Tengwar |
|--------|-----|---------|
| m | /m/ | malta (no vowel tehta) + tone |
| ng | /ng/ | noldo (no vowel tehta) + tone |

Examples:
- m "not" (malta + low-falling tone mark)
- ng "yellow" (noldo + tone)

A bare nasal tengwa with a tone mark signals a syllabic nasal.

## Final consonants

Min preserves the Middle Chinese final consonants that Mandarin has lost. This includes both nasal and stop codas.

### Nasal codas

| Tai-lo | IPA | Tengwa | Codepoint |
|--------|-----|--------|-----------|
| -m | /m/ | malta | U+E015 |
| -n | /n/ | numen | U+E005 |
| -ng | /ng/ | noldo | U+E025 |

Same tengwar as the corresponding initials. Position after the vowel distinguishes coda from onset.

### Stop codas

Per the final-stops design, use the same tengwar as initials:

| Tai-lo | IPA | Tengwa | Codepoint |
|--------|-----|--------|-----------|
| -p | /p/ | parma | U+E011 |
| -t | /t/ | tinco | U+E001 |
| -k | /k/ | calma | U+E021 |

Position (after the vowel) distinguishes finals from initials. No diacritics or modifications are required.

### Glottal stop final

Min has a final glottal stop /-h/ (IPA /ʔ/), written `-h` in Tai-lo. This has no equivalent in Mandarin or Cantonese.

**Design decision:** Use **halla** for final /-h/.

| Tai-lo | IPA | Tengwa | Codepoint |
|--------|-----|--------|-----------|
| -h | /ʔ/ | halla | U+E029 |

**Rationale:**
1. Halla represents /h/ in many modes; /h/ and /ʔ/ are both glottal consonants
2. The glottal stop historically derives from earlier *-p, *-t, *-k
3. Using a distinct glyph prevents ambiguity with oral stops
4. Halla is already used for initial /h/ in this mode; position distinguishes

### Examples with finals

| Tai-lo | IPA | Tengwar structure |
|--------|-----|-------------------|
| lam (south) | /lam/ | lambe + a-tehta + malta |
| hun (powder) | /hun/ | halla + u-tehta + numen |
| tang (east) | /tang/ | tinco + a-tehta + noldo |
| tap (answer) | /tap/ | tinco + a-tehta + parma |
| put (Buddha) | /put/ | parma + u-tehta + tinco |
| hok (blessing) | /hok/ | halla + o-tehta + calma |
| oh (learn) | /oh/ | telco + o-tehta + halla |
| tah (step on) | /tah/ | tinco + a-tehta + halla |

### Checked syllables

Syllables ending in stop codas (-p, -t, -k, -h) are called **checked syllables** (entering tones). They can only carry Tones 4 or 8. The presence of a final stop implies the checked quality.

## Tones

Taiwanese Hokkien has **seven phonemic tones**, traditionally numbered 1-5 and 7-8 (Tone 6 merged with Tone 2 historically). The extended tone system from the Cantonese design handles this inventory.

### The seven tones

| Tone | Name | Chao | Contour | Syllable Type | Mark |
|------|------|------|---------|---------------|------|
| 1 | yin-ping | 44~55 | high level | smooth | flat bar |
| 2 | yin-shang | 51~53 | high falling | smooth | falling stroke |
| 3 | yin-qu | 21~31 | low falling | smooth | falling stroke + double-dot |
| 5 | yang-ping | 24~13 | rising | smooth | rising stroke |
| 7 | yang-qu | 33~22 | mid level | smooth | flat bar + dot |
| 4 | yin-ru | 32 | low short | checked | (unmarked) |
| 8 | yang-ru | 4~5 | high short | checked | flat bar |

### Checked tone handling

Tones 4 and 8 occur only on **checked syllables** (those ending in /-p/, /-t/, /-k/, or /-h/). The presence of a final stop consonant implies the checked quality.

**Tone 4/8 disambiguation:**
- Unmarked checked syllable = Tone 4 (low)
- Checked syllable with flat bar = Tone 8 (high)

This follows the principle that the unmarked case (T4, low) needs no mark, while the marked case (T8, high) uses the high-level flat bar.

### Teochew extension (8 tones)

Teochew preserves Tone 6 (yang-shang), which merged into Tone 7 in Taiwanese:

| Tone | Name | Chao | Contour | Mark |
|------|------|------|---------|------|
| 6 | yang-shang | 35 | mid rising | rising stroke + dot |

This fits the contour + register system: rising contour + mid register.

### Neutral tone

Grammatical particles and suffixes carry a **neutral tone** (written with `--` prefix in Tai-lo):
- Realized as low [21] or low-falling [31]
- The preceding syllable retains its citation tone (no sandhi)

**Tengwar representation:** Use the low-level mark (flat bar + double-dot) or leave unmarked. The neutral tone is predictable from grammatical context.

### Tone marks with codepoints

**Contour marks** (below-tengwa position):

| Mark | Shape | Codepoint | Glyph Name |
|------|-------|-----------|------------|
| Flat bar | horizontal line | U+E050 | nasalizer-teng |
| Rising stroke | acute | U+E046 | acute-teng |
| Falling stroke | grave | U+E054 | grave-teng |

**Register modifiers** (below the contour mark):

| Modifier | Meaning | Codepoint | Glyph Name |
|----------|---------|-----------|------------|
| (none) | high register | -- | -- |
| Single dot | mid register | U+E045 | unutixe-teng |
| Double dot | low register | U+E043 | dotdblbelow-teng |

### Complete tone inventory

| Tone | Visual | Composition | Codepoints |
|------|--------|-------------|------------|
| 1 (high level) | flat bar | U+E050 | U+E050 |
| 2 (high falling) | falling stroke | U+E054 | U+E054 |
| 3 (low falling) | falling + double-dot | U+E054 + U+E043 | U+E054 + U+E043 |
| 5 (rising) | rising stroke | U+E046 | U+E046 |
| 7 (mid level) | flat bar + dot | U+E050 + U+E045 | U+E050 + U+E045 |
| 4 (low checked) | (unmarked) | -- | -- |
| 8 (high checked) | flat bar | U+E050 | U+E050 |

### Placement

Tone marks are placed **below the tengwa** bearing the nuclear vowel:

```
  [vowel tehta]
  [  tengwa   ]
  [contour mark]
  [register dot(s)]
```

For syllabic nasals, the tone mark sits below the bare nasal tengwa.

## Tone sandhi

**Policy: Write surface tones (post-sandhi), not citation tones.**

This is a fundamental design decision. Min tone sandhi is:
- **Obligatory:** Applies in virtually all multi-syllable contexts
- **Pervasive:** All non-final syllables change
- **Predictable:** Rules are regular (with exceptions for particles)

Writing surface tones means the Tengwar representation matches pronunciation. A reader does not need to apply sandhi rules mentally.

### Converter responsibility

The romanization-to-Tengwar converter must:

1. Accept input in **citation tones** (standard Tai-lo/POJ notation)
2. Identify **phrase boundaries** (compound words, verb-object, modifier-head)
3. Apply **sandhi rules** to all non-final syllables
4. Output Tengwar with **surface tone marks**

Alternatively, input may already be in surface tones (how the word is actually pronounced).

### Sandhi rules summary

**Smooth tones (1, 2, 3, 5, 7):**

| Citation | Chao | Sandhi | Chao |
|----------|------|--------|------|
| 1 | 55 | 7 | 33 |
| 7 | 33 | 3 | 21 |
| 3 | 21 | 2 | 51 |
| 2 | 51 | 1 | 55 |
| 5 | 24 | 7 (or 3) | 33 |

Note: Tone 5 sandhi differs by dialect. Quanzhou-influenced varieties go to Tone 7; Zhangzhou-influenced go to Tone 3.

**Checked tones (4, 8):**

| Citation | Sandhi |
|----------|--------|
| 4 | 8 |
| 8 | 4 |

Checked tones simply swap.

### Sandhi domain

Sandhi applies within **phonological phrases**, which roughly correspond to:
- Compound words
- Verb + object combinations
- Modifier + head noun
- Numbers + classifiers + nouns

### Exceptions

Sandhi does **not** apply:
- Phrase-finally (the final syllable keeps citation tone)
- Before neutral-tone particles (`--a`, `--lah`, `--honnh`)
- In emphatic or contrastive speech
- Certain frozen expressions

### Example

| Tai-lo (citation) | Surface pronunciation | Tengwar tones |
|-------------------|----------------------|---------------|
| Tai-uan (Taiwan) | [tai33 uan44] | T7 + T1 |
| ho-lang (good person) | [ho55 lang24] | T1 + T5 |
| toa-lang (adult) | [tua21 lang24] | T3 + T5 |

The Tengwar output shows the surface (sandhi-applied) tones, not the underlying citation tones.

## Syllable structure

Min syllables follow the template:

```
(Initial) (Medial) Nucleus (Coda) Tone
```

Where:
- **Initial:** One of 18 consonants, or null
- **Medial:** /j/ or /w/ (limited distribution)
- **Nucleus:** A vowel tehta (oral or nasal) or syllabic nasal
- **Coda:** One of -m, -n, -ng, -p, -t, -k, -h, or none
- **Tone:** One of 7 marks (or unmarked for T4)

### Composition rules

1. The initial tengwa carries the nuclear vowel tehta.
2. If a medial glide is present, it appears as a separate tengwa between the initial and coda.
3. Coda consonants follow the vowel-bearing tengwa.
4. The tone mark appears below the vowel-bearing tengwa.
5. Null initials use the carrier (telco).
6. Nasal vowels add the tilde-below to the vowel-bearing tengwa.

### Visual structure examples

**Open syllable (no coda):**
```
  [vowel tehta]
  [  initial  ]
  [ tone mark ]
```

**Syllable with nasal vowel:**
```
  [vowel tehta]
  [  initial  ]
  [tilde-below]
  [ tone mark ]
```

**Syllable with nasal coda:**
```
  [vowel tehta]
  [  initial  ] [nasal coda]
  [ tone mark ]
```

**Syllable with stop coda:**
```
  [vowel tehta]
  [  initial  ] [stop coda]
  [ tone mark ]
```

**Syllable with glottal stop coda:**
```
  [vowel tehta]
  [  initial  ] [halla]
  [ tone mark ]
```

## Sample syllables

### Basic syllables

| Tai-lo | Meaning | Structure |
|--------|---------|-----------|
| lang | person | lambe + a-tehta + noldo + T5 |
| tsit | one | tinco-ext + i-tehta + tinco (T4 unmarked) |
| gua | I/me | anga + a-tehta + T2 |
| li | you | lambe + i-tehta + T2 |
| tai | big | tinco + a-tehta + T7 |
| sio | small | thule + i-tehta + anna + o-tehta + T2 |

### Nasal vowel syllables

| Tai-lo | Meaning | Structure |
|--------|---------|-----------|
| sann | three | thule + a-tehta + tilde-below + T1 |
| phinn | nose | parma + asp + i-tehta + tilde-below + T7 |
| tinn | sweet | tinco + i-tehta + tilde-below + T1 |
| kinn | to see | calma + i-tehta + tilde-below + T3 |
| hinn | ear | halla + i-tehta + tilde-below + T7 |

### Syllables with final stops

| Tai-lo | Meaning | Structure |
|--------|---------|-----------|
| tap | to answer | tinco + a-tehta + parma (T4 unmarked) |
| pat | eight | parma + a-tehta + tinco (T4 unmarked) |
| pak | north | parma + a-tehta + calma (T4 unmarked) |
| sit | real | thule + i-tehta + tinco + T8 (flat bar) |
| peh | white | parma + e-tehta + halla + T8 (flat bar) |
| oh | to learn | telco + o-tehta + halla (T4 unmarked) |

### Syllables with glottal stop

| Tai-lo | Meaning | Structure |
|--------|---------|-----------|
| oh | learn | telco + oo-tehta + halla |
| tah | step on | tinco + a-tehta + halla |
| iah | wing | telco + i-tehta + anna + a-tehta + halla |
| koh | more | calma + o-tehta + halla |

### Tone contrasts

| Tai-lo | Tone | Meaning | Structure |
|--------|------|---------|-----------|
| su | T1 | book | thule + u-tehta + flat bar |
| su | T2 | lose | thule + u-tehta + falling stroke |
| su | T3 | four | thule + u-tehta + falling + double-dot |
| su | T5 | tree | thule + u-tehta + rising stroke |
| su | T7 | count | thule + u-tehta + flat bar + dot |

### Syllabic nasals

| Tai-lo | Meaning | Structure |
|--------|---------|-----------|
| m | not | malta + T7 (flat bar + dot) |
| ng | yellow | noldo + tone |

### Nasal diphthongs

| Tai-lo | Meaning | Structure |
|--------|---------|-----------|
| ainn | to weigh | telco + a-tehta + tilde-below + anna |
| uainn | (nasalized uai) | vala + a-tehta + tilde-below + anna |

### Multi-syllable examples with sandhi

| Tai-lo (citation) | Surface | Meaning | Structure |
|-------------------|---------|---------|-----------|
| Tai-uan | [tai33 uan44] | Taiwan | tinco + a-tehta + T7, vala + a-tehta + T1 |
| ho-lang | [ho55 lang24] | good person | halla + o-tehta + T1, lambe + a-tehta + noldo + T5 |

## Comparison with other modes

### Consonants

| Feature | Mandarin | Cantonese | Min |
|---------|----------|-----------|-----|
| Laryngeal contrast | 2-way | 2-way | 3-way |
| Voiced stops | Absent | Absent | /b/, /g/, /dz/ |
| Retroflex series | Present | Absent | Absent |
| Palatal affricates | Present | Absent | Absent |
| Velar nasal initial | Coda only | Initial and coda | Initial and coda |
| Stop codas | Absent | -p, -t, -k | -p, -t, -k, -h |
| Glottal stop coda | Absent | Absent | Present (-h) |
| Bilabial coda | Absent | -m | -m |

### Vowels

| Feature | Mandarin | Cantonese | Min |
|---------|----------|-----------|-----|
| Nasal vowels | No | No | Yes (phonemic) |
| Phonemic length | No | Yes (aa vs a) | No |
| Front rounded /y/ | Yes | Yes | No |
| Apical vowels | Yes | No | No |
| Syllabic nasals | No | Yes | Yes |

### Tones

| Feature | Mandarin | Cantonese | Min |
|---------|----------|-----------|-----|
| Number of tones | 4 (+neutral) | 6 | 7 |
| Checked tones | Absent | Present | Present |
| Tone sandhi scope | Third tone only | Limited | Pervasive |
| Output tones | Citation | Citation | Surface |

### Grade semantics comparison

| Feature | Mandarin/Cantonese | Min/Wu (this mode) |
|---------|--------------------|--------------------|
| Grade 1 | voiceless unaspirated | voiceless unaspirated |
| Grade 2 | voiceless aspirated | **voiced** |
| Grade 3 | fricative | fricative |
| Aspiration | grade distinction | **diacritic** |

Min mode is **incompatible** with Mandarin/Cantonese modes but **compatible** with Wu mode.

### Features shared with all modes

These design elements are consistent across all Sinitic Tengwar modes:

1. **Alveolar affricates ts** (extended tinco)
2. **Fricative s** (thule)
3. **Voiceless stops p/t/k** (parma, tinco, calma in Grade 1)
4. **Nasals m/n/ng** (malta, numen, noldo in Grade 5)
5. **Lateral l** (lambe in Grade 6)
6. **Nasal codas -n/-ng** (numen, noldo)
7. **Labiovelar glide w** (vala)
8. **Palatal glide j** as medial (anna)
9. **Null initial** (telco carrier)
10. **Quenya-style tehtar placement** (vowel on preceding consonant)
11. **Below-tengwa tone placement**
12. **Final -p/-t/-k** (parma, tinco, calma)

### Features shared with Wu mode only

1. **Classical voicing semantics** (Grade 2 = voiced)
2. **Aspiration diacritic** (U+E0B0)
3. **Voiced stops use Grade 2** (umbar /b/, anga /g/)

## Font requirements

### Glyphs from earlier modes

All Mandarin and Cantonese mode glyphs are used. The extended Alcarin Tengwar font includes them.

### New glyphs for Min

| Glyph | Purpose | Codepoint | Status |
|-------|---------|-----------|--------|
| Tilde-below | nasal vowel marker | U+E044 | New for Min |
| Aspiration-teng | aspiration diacritic | U+E0B0 | Shared with Wu |

**Tilde-below** (nasal vowel marker):
- Positioned in the below-tengwa zone
- Sized to be visually balanced with register dots
- Curved like a tilde (~), not angular

**Aspiration-teng** (aspiration diacritic):
- Positioned at upper-right of the tengwa, below the vowel tehta zone
- Small rightward-opening curl, approximately 1/3 the height of a vowel tehta
- Same glyph used in Wu mode

### Tengwar with classical semantics restored

In this mode, Grade 2 tengwar carry their traditional voicing meaning:

| Tengwa | Classical meaning | Min usage |
|--------|-------------------|-----------|
| umbar | voiced bilabial stop | /b/ voiced bilabial stop |
| anga | voiced velar stop | /g/ voiced velar stop |
| ando-ext | voiced alveolar affricate | /dz/ voiced affricate |

The glottal stop coda is a Min-specific usage:

| Tengwa | Traditional | Min usage |
|--------|-------------|-----------|
| halla (final) | /h/ glottal fricative | /-h/ glottal stop coda |

### Combination tehtar

These combinations require no new glyphs but may benefit from kerning adjustments:
- **oo-tehta** (o + underdot) for /o/
- **vowel + tilde-below** for nasal vowels
- **contour + register dots** for composed tones

## Summary

The Min Tengwar mode:

1. **Uses classical Tengwar voicing semantics** (Grade 2 = voiced), aligning with Wu mode
2. **Marks aspiration with a diacritic** (U+E0B0), not a grade distinction
3. **Uses 18 initials** mapped cleanly to the Tengwar grade system
4. **Represents nasal vowels** using a tilde-below diacritic
5. **Marks 7 tones** using 3 contour shapes and 2 register levels
6. **Writes final stops** including the unique glottal stop (halla)
7. **Outputs surface tones** after applying tone sandhi

**Compatibility:** This mode is incompatible with Mandarin and Cantonese modes (which use Grade 2 for aspiration). It is compatible with Wu mode (same grade semantics). A document must declare which mode applies.

The mode is phonemically accurate, visually systematic, and captures the distinctive features that make Southern Min unique among Sinitic languages.

## References

- Taiwan Ministry of Education. (2006). *Taiwan Minnan Language Romanization System* (Tai-lo).
- Douglas, C. (1873). *Chinese-English Dictionary of the Vernacular or Spoken Language of Amoy*.
- Cheng, R. L. (1968). Tone Sandhi in Taiwanese. *Linguistics*, 41, 19-42.
- Ang, U. (2013). *Taiwanese Grammar: A Concise Reference*. Greenhorn Media.
- Wikipedia: [Hokkien phonology](https://en.wikipedia.org/wiki/Hokkien_phonology)
- Wikipedia: [Taiwanese Hokkien](https://en.wikipedia.org/wiki/Taiwanese_Hokkien)
- Wikipedia: [Pe-oh-ji](https://en.wikipedia.org/wiki/Pe%CC%8Dh-%C5%8De-j%C4%AB)
