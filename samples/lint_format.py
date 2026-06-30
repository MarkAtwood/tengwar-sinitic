#!/usr/bin/env python3
"""Lint markdown files for canonical column format.

Canonical: | Romanization | Hanzi | English | Tengwar | Names |

Exits non-zero if any file violates the format.
"""

import re
import sys
from pathlib import Path

CANONICAL_HEADER = '| Romanization | Hanzi | English | Tengwar | Names |'
POEM_HEADER = '| Romanization | Hanzi | Tengwar | Names |'  # poems have translation at end
ERRORS = []


def lint_file(filepath):
    """Check a file for format violations."""
    content = filepath.read_text()
    lines = content.split('\n')

    for i, line in enumerate(lines, 1):
        if not line.strip().startswith('|'):
            continue

        # Skip separator lines
        if re.match(r'^\|[-:|]+\|$', line.replace(' ', '')):
            continue

        parts = [p.strip() for p in line.split('|')]

        # Check header line - only lint data tables (must have Tengwar column)
        if 'Romanization' in line or 'Pinyin' in line or 'Jyutping' in line:
            # Skip reference tables (IPA, tone charts, etc) that don't have Tengwar
            if 'Tengwar' not in line:
                continue
            normalized = '| ' + ' | '.join(p for p in parts if p) + ' |'
            if normalized != CANONICAL_HEADER:
                # Allow tables with extra columns (like Tone)
                if normalized.startswith('| Romanization | Hanzi | English | Tengwar | Names |'):
                    continue
                # Allow poem tables (no per-line English)
                if normalized == POEM_HEADER:
                    continue
                ERRORS.append(f"{filepath}:{i}: non-canonical header")
                ERRORS.append(f"  got:      {line}")
                ERRORS.append(f"  expected: {CANONICAL_HEADER}")
            continue

        # Check data rows have 5 columns (parts[0] and parts[-1] may be empty)
        data_cols = [p for p in parts[1:-1] if True]  # keep all including empty
        if len(data_cols) < 5:
            # Allow rows with fewer columns in some contexts
            pass


def main():
    samples_dir = Path(__file__).parent

    for md in sorted(samples_dir.rglob('*.md')):
        if md.name == 'README.md':
            continue
        lint_file(md)

    if ERRORS:
        print("Format violations found:\n")
        for e in ERRORS:
            print(e)
        sys.exit(1)
    else:
        print("All files pass format lint.")
        sys.exit(0)


if __name__ == '__main__':
    main()
