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

    opp, you = line.strip().split()
    you = you.replace("X", "A").replace("Y", "B").replace("Z", "C")
    if opp == you:
        return SCORE_DRAW + TYPE_SCORES[you]

    if opp == 'A' and you == 'B' \
       or opp == 'B' and you == 'C' \
       or opp == 'C' and you == 'A':
        return TYPE_SCORES[you] + SCORE_WIN
    else:
        return TYPE_SCORES[you] + SCORE_LOSS


def main():
    with open("input.txt") as f:
        print(sum(calculate_score(line) for line in f))

if __name__ == "__main__":
    main()
