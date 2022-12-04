#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: (C) 2022 nfitzen <https://github.com/nfitzen>

def main():
    with open("input.txt") as f:
        stripped = (line.strip() for line in f)
        count = 0
        for line in stripped:
            x, y = line.split(",")
            print(x, y)
            r1 = set(range(int(x.split("-")[0]), int(x.split("-")[1]) + 1))
            r2 = set(range(int(y.split("-")[0]), int(y.split("-")[1]) + 1))
            if r1.issubset(r2) or r2.issubset(r1):
                count += 1
    print(count)


if __name__ == "__main__":
    main()
