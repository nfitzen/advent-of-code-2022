#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: (C) 2022 nfitzen <https://github.com/nfitzen>

def calculate_score(line: str) -> int:
    """Calculates a score for a given line."""
    TYPE_SCORES = {
        "A": 1,
        "B": 2,
        "C": 3,
    }
    SCORE_LOSS = 0
    SCORE_DRAW = 3
    SCORE_WIN = 6
    TYPES = ("A", "B", "C")

    opp, result = line.strip().split()

    opp_num: int = TYPE_SCORES[opp]-1

    if result == "X":
        return SCORE_LOSS + TYPE_SCORES[TYPES[(opp_num - 1) % 3]]
    elif result == "Y":
        return SCORE_DRAW + TYPE_SCORES[opp]
    else:
        return SCORE_WIN + TYPE_SCORES[TYPES[(opp_num + 1) % 3]]

def main():
    with open("input.txt") as f:
        print(sum(calculate_score(line) for line in f))

if __name__ == "__main__":
    main()
