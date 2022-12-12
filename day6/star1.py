#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: (C) 2022 nfitzen <https://github.com/nfitzen>

import more_itertools as mi
import sys

def main():
    fname = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    with open(fname) as f:
        stream = f.read().rstrip('\n')

    for i, window in enumerate(mi.windowed(stream, 4)):
        if mi.all_unique(window):
            print(i+4)
            break


if __name__ == "__main__":
    main()
