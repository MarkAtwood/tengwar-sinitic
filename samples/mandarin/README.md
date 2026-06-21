# Sample Texts

Reference texts in Chinese, Pinyin, and Tengwar (Mandarin mode).

## Classical Poetry (Tang Dynasty)

| File | Title | Author |
|------|-------|--------|
| jing_ye_si.md | 静夜思 (Quiet Night Thought) | Li Bai |
| chun_xiao.md | 春晓 (Spring Dawn) | Meng Haoran |
| deng_guanque_lou.md | 登鹳雀楼 (Climbing Stork Tower) | Wang Zhihuan |
| min_nong.md | 悯农 (Pitying the Farmers) | Li Shen |
| yong_e.md | 咏鹅 (Ode to the Goose) | Luo Binwang |
| xiang_si.md | 相思 (Longing) | Wang Wei |
| feng_qiao_ye_bo.md | 枫桥夜泊 (Mooring at Maple Bridge) | Zhang Ji |
| you_zi_yin.md | 游子吟 (Song of the Wandering Son) | Meng Jiao |

## Practical Texts

| File | Contents |
|------|----------|
| greetings.md | Common phrases (你好, 谢谢, etc.) |
| numbers.md | Numbers 1–10 |
| places.md | Major cities and landmarks |
| chengyu.md | Four-character idioms |
| tongue_twisters.md | Phonological stress tests |

## Viewing the Tengwar

The Tengwar text uses Unicode Private Use Area codepoints (U+E000–E0FF). To see the glyphs:

1. Install [Alcarin Tengwar](https://github.com/MarkAtwood/Alcarin-Tengwar) or build from `fonts/Alcarin-Tengwar/`
2. Open the markdown files in an editor/viewer with the font configured

The `tengwar_mandarin.py` script can convert additional Pinyin text.

## Generating Images

With the font built and cairosvg installed:

```bash
pip install cairosvg
python render.py
```

This generates `svg/` and `png/` directories with rendered images.
