# Sample Texts

Reference texts rendered in Tengwar for each supported Sinitic language.

## Structure

```
samples/
├── mandarin/     # Standard Mandarin (普通话)
├── cantonese/    # (planned)
├── hokkien/      # (planned)
├── shanghainese/ # (planned)
└── hakka/        # (planned)
```

Each language directory contains:
- `*.md` — Source texts with pinyin, hanzi, tengwar, and romanized glyph names
- `svg/` — Vector renderings
- `png/` — Raster renderings
- `render.py` — Generation script
- `tengwar_<language>.py` — Converter module

## Regenerating

```bash
cd samples/mandarin
python render.py           # all samples
python render.py jing_ye_si  # single sample
```

Requires the extended Alcarin Tengwar font from `fonts/Alcarin-Tengwar/Font source/build/`.
