#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: (C) 2022 nfitzen <https://github.com/nfitzen>

def main():
    with open("input.txt") as f:
        data: str = f.read()
    elves: list[str] = data.split("\n\n")
    # yes ik I could use max() but whatever
    maxes = [0, 0, 0] # 3rd, 2nd, 1st
    for elf in elves:
        current = sum(int(line) for line in elf.splitlines())
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


if __name__ == "__main__":
    main()
