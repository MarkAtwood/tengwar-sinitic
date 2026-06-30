#!/usr/bin/env python3
"""Migrate all sample markdown files to canonical column format.

Canonical: | Romanization | Hanzi | English | Tengwar | Names |

Handles various source formats:
- | Pinyin | 汉字 | English | Tengwar | Romanized |
- | Jyutping | 粵字 | Tengwar | Romanized Names |  (missing English)
- | Chinese | Romanization | English | Tengwar | Names |  (swapped)
- |Romanization|Chinese|...| (no spaces)
"""

import re
from pathlib import Path

CANONICAL_HEADERS = ['Romanization', 'Hanzi', 'English', 'Tengwar', 'Names']

# Map various header names to canonical
ROMANIZATION_HEADERS = {'Pinyin', 'Jyutping', 'Hakka', 'Tai-lo', 'Wu Pinyin', 'Romanization', 'Beta', 'Gan', 'Xiang'}
HANZI_HEADERS = {'汉字', '粵字', '客字', '閩字', '吳字', 'Chinese', 'Hanzi'}
TENGWAR_HEADERS = {'Tengwar'}
NAMES_HEADERS = {'Names', 'Romanized', 'Romanized Names'}


def detect_column_type(header):
    """Detect what type of data a column contains."""
    header = header.strip()
    if header in ROMANIZATION_HEADERS:
        return 'romanization'
    if header in HANZI_HEADERS:
        return 'hanzi'
    if header == 'English':
        return 'english'
    if header in TENGWAR_HEADERS:
        return 'tengwar'
    if header in NAMES_HEADERS:
        return 'names'
    return None


def has_cjk(s):
    """Check if string contains CJK characters."""
    return any('一' <= c <= '鿿' for c in s)


def has_pua(s):
    """Check if string contains PUA (tengwar) characters."""
    return any('' <= c <= '' for c in s)


def detect_column_type_by_content(value):
    """Detect column type from actual content."""
    value = value.strip()
    if not value:
        return None
    if has_pua(value):
        return 'tengwar'
    if value.startswith('`{') or value.startswith('`['):
        return 'names'
    if has_cjk(value):
        return 'hanzi'
    # Romanization typically has tone numbers or diacritics
    if re.search(r'[a-zA-Z]', value):
        return 'romanization'
    return None


def migrate_table(lines):
    """Migrate a markdown table to canonical format."""
    result = []
    header_line_idx = None
    separator_idx = None
    col_mapping = None  # maps canonical col -> source col index

    for i, line in enumerate(lines):
        if not line.strip().startswith('|'):
            result.append(line)
            continue

        parts = [p.strip() for p in line.split('|')]
        # parts[0] is empty (before first |), parts[-1] may be empty

        # Detect separator line
        if all(p == '' or set(p) <= {'-', ':'} for p in parts):
            result.append('|---|---|---|---|---|')
            separator_idx = i
            continue

        # Detect header line (first non-separator table line)
        if header_line_idx is None:
            header_line_idx = i

            # Build column mapping from headers
            col_mapping = {}
            for j, h in enumerate(parts[1:], 1):  # skip empty parts[0]
                col_type = detect_column_type(h)
                if col_type:
                    col_mapping[col_type] = j

            # If no English column found, mark it as missing
            if 'english' not in col_mapping:
                col_mapping['english'] = None

            result.append('| Romanization | Hanzi | English | Tengwar | Names |')
            continue

        # Data row - reorder columns
        if col_mapping is None:
            result.append(line)
            continue

        # If mapping is incomplete, try to detect from content
        if len(col_mapping) < 4:
            for j, p in enumerate(parts[1:], 1):
                if j not in col_mapping.values():
                    ct = detect_column_type_by_content(p)
                    if ct and ct not in col_mapping:
                        col_mapping[ct] = j

        # Build new row in canonical order
        def get_col(col_type):
            idx = col_mapping.get(col_type)
            if idx is None or idx >= len(parts):
                return ''
            return parts[idx]

        new_row = [
            get_col('romanization'),
            get_col('hanzi'),
            get_col('english'),
            get_col('tengwar'),
            get_col('names'),
        ]

        result.append('| ' + ' | '.join(new_row) + ' |')

    return result


def migrate_file(filepath):
    """Migrate a single markdown file."""
    content = filepath.read_text()
    lines = content.split('\n')

    # Check if file has tables
    if not any('|' in line for line in lines):
        return False

    new_lines = migrate_table(lines)
    new_content = '\n'.join(new_lines)

    if new_content != content:
        filepath.write_text(new_content)
        return True
    return False


def main():
    samples_dir = Path(__file__).parent
    changed = 0

    for md in sorted(samples_dir.rglob('*.md')):
        if md.name == 'README.md':
            continue
        if migrate_file(md):
            print(f"Migrated: {md.relative_to(samples_dir)}")
            changed += 1

    print(f"\nTotal files migrated: {changed}")


if __name__ == '__main__':
    main()
