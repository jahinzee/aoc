#!/bin/env python3

# Solution for "Print Queue", Day 5, Advent of Code 2024
# <https://adventofcode.com/2024/day/5>
#
# Author: jahinzee

import fileinput

# storing input as
# - List[Tuple[Int, Int]] -- rules, and
# - List[List[Int]] -- updates
with fileinput.input(encoding="utf-8") as file:
    puzzle_input = [line.strip() for line in file]

    sep = puzzle_input.index("")
    ordering_rules = [
        (int(li), int(ri))
        for li, ri in (line.split("|") for line in puzzle_input[:sep])
    ]
    updates = [
        [int(n) for n in update]
        for update in (line.split(",") for line in puzzle_input[sep + 1 :])
    ]
    del puzzle_input

# ******** Part A *******


def find_bad_ordering(update, ordering_rules):
    for li, ri in ordering_rules:
        try:
            lidx, ridx = update.index(li), update.index(ri)
        except ValueError:
            # Atleast one of the values of this rule is not
            # in the update -- this rule is not violated.
            continue
        if lidx > ridx:
            # Update does not follow order -- returning the errant indices.
            return (lidx, ridx)
    # Update follows all ordering rules.
    return None


good_updates = (u for u in updates if find_bad_ordering(u, ordering_rules) is None)
middle_values = (u[len(u) // 2] for u in good_updates)

print(sum(middle_values))

# ******** Part B *******


def find_correct_update_order(update, ordering_rules):
    while (result := find_bad_ordering(update, ordering_rules)) is not None:
        # Swap the bad items and try again.
        lidx, ridx = result
        update[lidx], update[ridx] = update[ridx], update[lidx]
    return update


fixed_bad_updates = (
    find_correct_update_order(u, ordering_rules)
    for u in updates
    if find_bad_ordering(u, ordering_rules) is not None
)
middle_values = (u[len(u) // 2] for u in fixed_bad_updates)

print(sum(middle_values))
