#!/bin/env python3

# Solution for "Red-Nosed Reports", Day 2, Advent of Code 2024
# <https://adventofcode.com/2024/day/2>
#
# Author: jahinzee

import fileinput

# storing input as List[List[Int]]
with fileinput.input(encoding="utf-8") as file:
    puzzle_input = [[int(token) for token in line.strip().split()] for line in file]

# ******** Part A *******


def report_is_safe(report):
    adjacent_pairs = list(zip(report, report[1:]))

    in_ascending_order = all(li >= ri for li, ri in adjacent_pairs)
    in_descending_order = all(li <= ri for li, ri in adjacent_pairs)

    differences = (abs(li - ri) for li, ri in adjacent_pairs)
    # NOTE: range(x, y) -- y is exclusive
    in_valid_range = all(d in range(1, 4) for d in differences)

    return (in_ascending_order or in_descending_order) and in_valid_range


safe_reports = [r for r in puzzle_input if report_is_safe(r)]

print(len(safe_reports))

# ******** Part B ********


def report_is_safe_enough(report):
    if report_is_safe(report):
        return True
    reports_one_level_removed = [
        [level for idx, level in enumerate(report) if idx != idx_to_remove]
        for idx_to_remove in range(len(report))
    ]
    return any(report_is_safe(r) for r in reports_one_level_removed)


safe_enough_reports = [r for r in puzzle_input if report_is_safe_enough(r)]

print(len(safe_enough_reports))
