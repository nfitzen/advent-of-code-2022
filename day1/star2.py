#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: (C) 2022 nfitzen <https://github.com/nfitzen>

from typing import Generator, Iterable


def main():
    with open("input.txt") as f:
        elves = line_group(f)
        # yes ik I could use max() but whatever
        maxes = [0, 0, 0]  # 3rd, 2nd, 1st
        for elf in elves:
            current = sum(int(line) for line in elf)
            if current >= maxes[0]:
                maxes[2] = maxes[1]
                maxes[1] = maxes[0]
                maxes[0] = current
            elif current >= maxes[1]:
                maxes[2] = maxes[1]
                maxes[1] = current
            elif current > maxes[2]:
                maxes[2] = current

        print(maxes, sum(maxes))


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
