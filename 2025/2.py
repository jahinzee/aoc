#!/usr/bin/env python3

# Solution for "Gift Shop", Day 2, Advent of Code 2025
# <https://adventofcode.com/2025/day/2>
#
# Author: jahinzee

import fileinput
from itertools import batched
from typing import Iterator

# Storing data as tuple[tuple[int, int], ...].
#
with fileinput.input(encoding="utf-8") as f:
    _data_2 = f.readline().split(",")
    _data_1 = (tuple(d.split("-")) for d in _data_2)
    _data_0 = ((int(a), int(b)) for a, b in _data_1)
    data = tuple(_data_0)


# ******** Part A ********


def id_is_valid(id: int) -> bool:
    str_id = str(id)
    if len(str_id) % 2 == 1:
        return True

    mid = len(str_id) // 2
    left, right = str_id[:mid], str_id[mid:]
    return left != right


id_ranges = (range(start, end + 1) for start, end in data)
invalid_id_ranges = ((id for id in r if not id_is_valid(id)) for r in id_ranges)

print(sum(sum(r) for r in invalid_id_ranges))


# ******** Part B ********

# WARNING: This solution is quite slow to run, very bruteforce and unoptimised, but it gets the
# job done in a reasonable time so :shrug:.
#


def get_repeat_counts(string: str, substr: str) -> int:
    substr_as_tuple = tuple(c for c in substr)
    substrings = tuple(batched(string, len(substr)))

    all_substrings_same = substrings.count(substr_as_tuple) == len(substrings)
    return 0 if not all_substrings_same else len(substrings)


def get_potential_repeatable_substrings(string: str) -> Iterator[str]:
    # Return substrings from the start until about halfway through the string, after that point
    # the substrings can't possibly be repeatable.
    #
    mid = len(string) // 2
    for idx in range(mid):
        yield string[: idx + 1]


def id_is_valid_b(id: int) -> bool:
    str_id = str(id)
    return all(
        get_repeat_counts(str_id, substr) < 2
        for substr in get_potential_repeatable_substrings(str_id)
    )


id_ranges = (range(start, end + 1) for start, end in data)
invalid_id_ranges = tuple((id for id in r if not id_is_valid_b(id)) for r in id_ranges)

print(sum(sum(r) for r in invalid_id_ranges))
