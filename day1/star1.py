#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: (C) 2022 nfitzen <https://github.com/nfitzen>

from typing import Generator, Iterable


def main():
    with open("input.txt") as f:
        elves = line_group(f)
        # yes ik I could use max() but whatever
        m = 0
        for elf in elves:
            current = sum(int(line) for line in elf)
            if current > m:
                m = current
        print(m)


def line_group(lines: Iterable[str]) -> Generator[list[str], None, None]:
    """Groups an iterable by empty lines."""
    it = iter(lines)
    l = []
    for val in it:
        if val == "\n":
            yield l
            l = []
            continue
        l.append(val)


if __name__ == "__main__":
    main()
