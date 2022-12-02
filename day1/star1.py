#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: (C) 2022 nfitzen <https://github.com/nfitzen>

def main():
    with open("input.txt") as f:
        data: str = f.read()
    elves: list[str] = data.split("\n\n")
    # yes ik I could use max() but whatever
    m = 0
    for elf in elves:
        current = sum(int(line) for line in elf.splitlines())
        if current > m:
            m = current
    print(m)


if __name__ == "__main__":
    main()
