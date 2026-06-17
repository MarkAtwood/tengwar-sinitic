# Submission to Amanye Tenceli

**To:** Amanye Tenceli editors
**Subject:** Tengwar Mode for Mandarin Chinese — submission for review

---

Dear editors,

I would like to submit a Tengwar mode for Mandarin Chinese for your consideration.

## Summary

This is a phonemic tehtar mode for Standard Mandarin, transcribing the language as analyzed through Pinyin. To my knowledge, no Tengwar mode for any Chinese language has been published. The only prior mode for a tonal language is Laicasaane's Vietnamese mode from 2016.

## Key design decisions

**Consonants:** Mandarin's four places of articulation (alveolar, labial, velar, retroflex) map onto the four Tengwar series. Column IV (quessetéma) is reassigned from labiovelars to retroflexes, following the principle in Appendix E that series assignments shift between modes. The retroflex series fills the column completely (four members: zh, ch, sh, r).

**Aspiration:** Mandarin contrasts aspiration rather than voicing. Grade 1 represents unaspirated consonants; Grade 2 represents aspirated. The doubled bow signifies "more energy at the same place," which matches aspiration phonetically.

**Palatals:** The palatal series (j, q, x) is in complementary distribution with velars. Following the tyelpetéma convention, palatals are written as velar tengwar with the double-dot palatal diacritic.

**Affricates:** The alveolar affricates z /ts/ and c /tsʰ/ use extended-stem Column I tengwar, following the German phonemic mode's precedent for /ts/ and /pf/.

**Tones:** Four iconographic marks trace pitch contour (horizontal bar, rising stroke, chevron, falling stroke). The mode defines two placement strategies:
- Below-tengwa placement (preferred for handwriting and extended fonts)
- Carrier placement (fallback for stock fonts, using existing tehtar on a post-syllable telco)

**The ü vowel:** Rather than requiring a modified tehta, the mode uses context. After palatals, plain u-tehta is unambiguous. After l/n, u-tehta and i-tehta appear together.

**Apical vowels:** Syllables like zī, chī, rì have no true vowel; the consonant is syllabic. The mode writes these as bare consonants with tone marks and no vowel tehta.

## Compatibility

The fallback rendering strategy works with unmodified Tengwar Annatar, Eldamar, Parmaite, and other standard fonts. The preferred below-tengwa strategy requires four new glyph positions but is natural for handwriting.

## Materials

The full specification with rationale is available at:
https://github.com/MarkAtwood/tengwar-sinitic

I am preparing rendered sample texts (UDHR Article 1, classical poetry) and can provide these as supplementary materials.

This Mandarin mode is the first in a planned family of Sinitic modes covering Cantonese, Hokkien, Shanghainese, and Hakka. The modes will share core conventions while adapting to each language's phonology.

## Request

I welcome critical review of the phonological mapping, the tone encoding system, and any edge cases I may have overlooked. If the mode meets your standards, I would be honored to have it included in the Amanye Tenceli catalog.

Thank you for your time and for maintaining this invaluable resource.

Respectfully,
Mark Atwood
