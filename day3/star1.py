#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: (C) 2022 nfitzen <https://github.com/nfitzen>

import string

VALUES = {val: n+1 for n, val in enumerate(string.ascii_letters)}

def main():
    with open("input.txt") as f:
        total = 0
        for line in f:
            line = line.strip()
            first = line[:len(line)//2]
            last = line[len(line)//2:]
            common = set(first) & set(last)
            total += sum(VALUES[v] for v in common)
    print(total)

if __name__ == "__main__":
    main()
