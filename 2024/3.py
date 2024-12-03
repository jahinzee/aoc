#!/bin/env python3

# Solution for "Mull It Over", Day 3, Advent of Code 2024
# <https://adventofcode.com/2024/day/3>
#
# Author: jahinzee

import fileinput
import re

# storing input as Str
with fileinput.input(encoding="utf-8") as file:
    puzzle_input = "\n".join(line for line in file)

# ******** Part A *******

# matches `mul(INT,INT)`
regex_mul = re.compile(r"mul\(\d+,\d+\)")
valid_muls = regex_mul.findall(puzzle_input)

operand_pairs = [re.compile(r"\d+").findall(mul) for mul in valid_muls]
results = [int(li) * int(ri) for li, ri in operand_pairs]
part_a = sum(results)

print(part_a)

# ******** Part B *******

# matches `mul(INT,INT)`, `do()` and `don't()`
regex_muldo = re.compile(r"mul\(\d+,\d+\)|do(?:n't)?\(\)")
valid_muldos = regex_muldo.findall(puzzle_input)

kept_muls = []
dont_mode = False

for mul in valid_muldos:
    # NOTE: checking "don't" before "do" and short-circuiting
    #       avoids double matches.
    if "don't" in mul:
        dont_mode = True
        continue
    if "do" in mul:
        dont_mode = False
        continue
    if dont_mode:
        continue
    kept_muls.append(mul)

operand_pairs = [re.compile(r"\d+").findall(mul) for mul in kept_muls]
results = [int(li) * int(ri) for li, ri in operand_pairs]
part_b = sum(results)

print(part_b)
