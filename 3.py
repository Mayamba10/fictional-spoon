#!/usr/bin/env python3
"""Demo: open a file in read ('r'), write ('w'), and append ('a') modes.

This script performs the exact operations you requested on a target file:
  1) Read mode: print current contents (if any).
  2) Write mode: overwrite with a brief introduction.
  3) Append mode: add 'Favorite subject: Science'.
  4) Re-read and print final contents.

Usage:
  python 3.py            # uses default 'demo_target.txt'
  python 3.py --file myfile.txt
"""

from pathlib import Path
import argparse


DEFAULT = 'demo_target.txt'


def show_contents(path: Path, label: str = 'Contents'):
    print(f"\n--- {label} of {path} ---")
    if not path.exists():
        print("(file does not exist)")
        return
    text = path.read_text(encoding='utf-8')
    if not text:
        print("(file is empty)")
    else:
        print(text.rstrip())


def main():
    parser = argparse.ArgumentParser(description='Demo file modes: r, w, a')
    parser.add_argument('--file', '-f', default=DEFAULT, help='Target filename')
    args = parser.parse_args()

    target = Path(args.file)

    # 1) Read mode: show current contents
    show_contents(target, 'Before (read)')

    # 2) Write mode: overwrite with brief introduction
    intro = ("Hello, I'm GitHub Copilot.\n"
             "This file demonstrates opening a file in different modes.\n")
    with target.open('w', encoding='utf-8') as fh:
        fh.write(intro)
    print(f"\nWritten intro to {target} (write mode, 'w').")

    # 3) Append mode: add favourite subject
    with target.open('a', encoding='utf-8') as fh:
        fh.write('\nFavorite subject: Science\n')
    print(f"Appended favorite subject to {target} (append mode, 'a').")

    # 4) Final read to show result
    show_contents(target, 'After (final)')


if __name__ == '__main__':
    main()
