#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: (C) 2022 nfitzen <https://github.com/nfitzen>

import string
from itertools import islice
import more_itertools

VALUES = {val: n+1 for n, val in enumerate(string.ascii_letters)}

def main():
    with open("input.txt") as f:
        total = 0
        for group in more_itertools.grouper(f, 3):
            common = set(group[0].strip())
            for line in group[1:]:
                common &= set(line.strip())
            total += sum(VALUES[v] for v in common)
    print(total)

if __name__ == "__main__":
    main()
