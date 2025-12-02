#!/usr/bin/env python3

# Solution for "Secret Entrance", Day 1, Advent of Code 2025
# <https://adventofcode.com/2025/day/1>
#
# Author: jahinzee

import fileinput
from itertools import accumulate, chain

# Storing data as tuple[int, ...], where:
#    Ln : n < 0
#    Rn : n > 0
#
with fileinput.input(encoding="utf-8") as f:
    _data_1 = ((line[0], line[1:].strip()) for line in f)
    _data_0 = (int(u) * (-1 if d == "L" else 1) for d, u in _data_1)
    data = tuple(_data_0)


# ******** Part A ********


def rotate_dial(current: int, rotation: int) -> int:
    return (current + rotation) % 100


turns = accumulate(chain((50,), data), rotate_dial)
turns_ending_in_zero = (t for t in turns if t == 0)

print(sum(1 for _ in turns_ending_in_zero))


# ******** Part B ********


def rotate_dial_and_count_zero_passes(current: int, rotation: int) -> tuple[int, int]:
    result = (current + rotation) % 100

    # Figuring out `zero_passes` using a brute-force iterative method. There's probably a more
    # elegant maths-y way to get `zero_passes`.
    #
    zero_passes = 0
    direction = 1 if rotation > 0 else -1

    for _ in range(abs(rotation)):
        current = (current + direction) % 100
        zero_passes += 1 if current == 0 else 0

    return result, zero_passes


# Unrolling accumulator function into prodecural code, since tracking `zero_passes` with
# `itertools.accumulate` gets real messy real quick.
#
accumulator = 50
values: list[tuple[int, int]] = []

for turn in data:
    accumulator, zero_passes = rotate_dial_and_count_zero_passes(accumulator, turn)
    values.append((accumulator, zero_passes))

print(sum(zero_passes for _, zero_passes in values))
