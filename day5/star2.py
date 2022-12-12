#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: (C) 2022 nfitzen <https://github.com/nfitzen>

import re
import sys

Stack = list[str]


def create_stacks(lines: list[str]) -> list[Stack]:
    """
    Creates stacks.
    The box numbering must be the last line.
    """

    box_lines = lines[-1]
    stack_nums = [int(i) for i in box_lines.strip().split()]

    lines.pop()

    stacks: list[list[str]] = [list() for _ in range(len(stack_nums))]

    for line in lines:
        for i, v in enumerate(line[1::4]):
            if v != " ":
                stacks[i].insert(0, v)

    return stacks


CMD_RE = re.compile(r"move (\d+) from (\d+) to (\d+)")


def perform_cmd(stacks: list[Stack], cmd: str) -> None:
    m = CMD_RE.match(cmd)
    if m is None:
        raise Exception("dafuq")
    amount = int(m.group(1))
    n1 = int(m.group(2))
    n2 = int(m.group(3))

    stacks[n2 - 1].extend(stacks[n1 - 1][-amount:])
    del stacks[n1-1][-amount:]


def main() -> None:
    fname = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    with open(fname) as f:
        data = [l.rstrip("\n") for l in f.readlines()]

    line_num = 0
    for line in data:
        line_num += 1
        if line.lstrip()[0].isdigit():
            break

    stacks = create_stacks(data[:line_num])
    start = line_num + 1

    for cmd_line in data[start:]:
        perform_cmd(stacks, cmd_line)

    print("".join(stack[-1] for stack in stacks))


if __name__ == "__main__":
    main()
