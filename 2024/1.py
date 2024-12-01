#!/bin/env python3

# Solution for "Historian Hysteria", Day 1, Advent of Code 2024
# <https://adventofcode.com/2024/day/1>

import fileinput

# storing input as List[Tuple[Int, Int]]
with fileinput.input(encoding="utf-8") as file:
    puzzle_input = [
        tuple(int(token) for token in line.strip().split()) for line in file
    ]

# ******** Part A ********

left, right = zip(*puzzle_input)

sort_left = sorted(left)
sort_right = sorted(right)

sorted_pairs = zip(sort_left, sort_right)

difference = [abs(li - ri) for li, ri in sorted_pairs]
part_a = sum(difference)

print(part_a)

# ******** Part B ********

similarity_scores = [li * len([ri for ri in right if ri == li]) for li in left]

part_b = sum(similarity_scores)
print(part_b)
