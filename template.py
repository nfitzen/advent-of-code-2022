#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: (C) 2022 nfitzen <https://github.com/nfitzen>

from typing import Generator, Iterable
import itertools as it
import more_itertools as mi


def main() -> None:
    with open("input.txt") as f:
        ...


def line_groups(lines: Iterable[str]) -> Generator[list[str], None, None]:
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
