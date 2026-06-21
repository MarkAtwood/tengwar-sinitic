# Final Stop Consonants in Sinitic Tengwar Modes

## Scope

This document defines how final stop consonants are written in Tengwar modes for Sinitic languages. It applies to:

- **Cantonese** (Yue): final -p, -t, -k
- **Hakka**: final -p, -t, -k
- **Min** (Hokkien, Teochew, etc.): final -p, -t, -k, plus final -ʔ (glottal stop)

Mandarin lacks final stops entirely, so the Mandarin mode does not use this convention.

## The design decision

**Final stops use the same tengwar as their corresponding initial stops. Position distinguishes them.**

| Final | IPA | Tengwa | Same as initial |
|-------|-----|--------|-----------------|
| -p | /p̚/ | parma | p- (Cantonese b-) |
| -t | /t̚/ | tinco | t- (Cantonese d-) |
| -k | /k̚/ | calma | k- (Cantonese g-) |

No diacritics or modifications are required. A tinco before the vowel is initial /t/. A tinco after the vowel is final /-t/.

## Rationale

### Position is sufficient

Sinitic syllable structure is strictly (C)V(C). The initial consonant precedes the vowel; the final consonant follows it. This positional distinction is absolute and unambiguous. Using the same glyph in both positions follows the principle of "one phoneme, one tengwa."

### Tengwar precedent

Tolkien's Elvish modes use the same principle. The tengwa númen represents /n/ whether it appears as an onset or a coda. The Mandarin mode already follows this: númen and ñoldo serve as both potential initials (though Mandarin /ŋ/ only occurs finally) and codas. Extending this to stops is natural.

### Phonemic, not phonetic

In Cantonese, final stops are unreleased: /p̚/, /t̚/, /k̚/. The speaker's lips or tongue close but do not release with a burst of air. This is a phonetic detail, not a phonemic contrast. Cantonese has no released final stops to contrast with. Tengwar is a phonemic script; it does not mark allophonic variation.

The same applies to Hakka and Min finals.

### Use Grade 1 (unaspirated)

Final stops are always unaspirated. There is no aspirated/unaspirated contrast in coda position in any Sinitic language. Therefore finals map to Grade 1 tengwar:

- parma (II-1), not umbar (II-2)
- tinco (I-1), not ando (I-2)
- calma (III-1), not anga (III-2)

This matches the phonetics: an unreleased stop cannot be aspirated.

## Examples

### Cantonese

| Jyutping | IPA | Tengwar structure |
|----------|-----|-------------------|
| sap (ten) | /saːp̚/ | thule + a-tehta + parma + tone |
| jat (one) | /jɐt̚/ | anna + a-tehta + tinco + tone |
| luk (six) | /lʊk̚/ | lambe + u-tehta + calma + tone |
| baak (hundred) | /paːk̚/ | parma + a-tehta + calma + tone |

Note: The tone mark placement will be defined in the Cantonese mode specification. Cantonese has 6-9 tones depending on analysis; final-stop syllables (entering tones) carry their own tone marks.

### Hakka

| Romanization | Tengwar structure |
|--------------|-------------------|
| sip (ten) | thule + i-tehta + parma + tone |
| it (one) | telco + i-tehta + tinco + tone |
| liuk (six) | lambe + i-tehta + vala + calma + tone |

### Min (Hokkien)

| POJ | Tengwar structure |
|-----|-------------------|
| chap (ten) | [initial ch] + a-tehta + parma + tone |
| it (one) | telco + i-tehta + tinco + tone |
| lak (six) | lambe + a-tehta + calma + tone |

## Glottal stop (Min only)

Min languages have a final glottal stop /-ʔ/ in some syllables, distinct from the oral stops. This requires a separate tengwa assignment.

**Recommendation:** Use halla for final /-ʔ/.

Halla is the tengwa for /h/ in many modes, and /h/ and /ʔ/ are both glottal consonants. In Sinitic phonology, the glottal stop often alternates historically with other stops (it derives from earlier *-p, *-t, *-k in some varieties). Using a dedicated glyph keeps it distinct from the oral stops.

| Final | IPA | Tengwa |
|-------|-----|--------|
| -h/-ʔ | /ʔ/ | halla |

The exact romanization varies: POJ uses -h, Tâi-lô uses -h, some systems use -ʔ directly.

## Interaction with tones

In Cantonese, Hakka, and Min, syllables with final stops carry special tones traditionally called "entering tones" (入聲). These are typically higher and shorter than their open-syllable counterparts.

The tone marking system is orthogonal to the final stop representation. Each language mode will define its own tone marks. The final stop tengwa appears after the vowel tehta and before the tone mark (in below-tengwa placement) or before the tone carrier (in carrier placement).

```
Below-tengwa placement:
  [vowel tehta]
  [  initial  ] [final stop]
  [tone mark  ]

Carrier placement:
  [vowel tehta]              [tone tehta]
  [  initial  ] [final stop] [  telco   ]
```

## Summary

1. Final -p is parma, same glyph as initial p-.
2. Final -t is tinco, same glyph as initial t-.
3. Final -k is calma, same glyph as initial k-.
4. Final -ʔ (Min only) is halla.
5. No diacritics or modifications are needed; position distinguishes initial from final.
6. This convention applies to all Sinitic modes with final stops: Cantonese, Hakka, Min.
