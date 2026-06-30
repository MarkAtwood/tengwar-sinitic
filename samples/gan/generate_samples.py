#!/usr/bin/env python3
"""Generate Gan sample markdown files with proper tengwar."""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from tengwar_gan import convert_text, tengwar_to_names

OUT_DIR = Path(__file__).parent


def process_markdown_file(filepath):
    """
    Read a markdown file, convert romanizations to tengwar, and write back.

    Expects tables with format:
    | Romanization | Hanzi | English | Tengwar | Names |
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    output_lines = []

    for line in lines:
        if line.startswith('|') and '|' in line[1:]:
            parts = [p.strip() for p in line.split('|')]
            # parts[0] is empty (before first |), parts[-1] may be empty

            # Skip header and separator rows
            if len(parts) >= 5 and parts[1] not in ('Romanization', '---', ''):
                # Check if this looks like a data row with romanization
                romanization = parts[1] if len(parts) > 1 else ''

                # Only process if romanization contains letters and numbers (tone marks)
                if romanization and re.search(r'[a-zA-Z]+[1-7]', romanization):
                    try:
                        tengwar = convert_text(romanization)
                        names = tengwar_to_names(tengwar)

                        # Rebuild the row with tengwar filled in
                        if len(parts) >= 6:
                            parts[4] = tengwar
                            parts[5] = f'`{names}`'
                        elif len(parts) >= 5:
                            parts[4] = tengwar

                        line = '| ' + ' | '.join(parts[1:-1]) + ' |'
                    except Exception as e:
                        print(f"Warning: Could not convert '{romanization}': {e}")

        output_lines.append(line)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))

    return filepath


def main():
    """Process all Gan markdown sample files."""
    sample_files = [
        'gan-common-phrases.md',
        'gan-proverbs.md',
    ]

    for filename in sample_files:
        filepath = OUT_DIR / filename
        if filepath.exists():
            process_markdown_file(filepath)
            print(f"Generated: {filename}")
        else:
            print(f"Skipped (not found): {filename}")


if __name__ == '__main__':
    main()
