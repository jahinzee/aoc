#!/bin/env python3

# Solution for "Ceres Search", Day 4, Advent of Code 2024
# <https://adventofcode.com/2024/day/4>
#
# Author: jahinzee

import fileinput
import re

# storing input as List[List[str (char)]]
with fileinput.input(encoding="utf-8") as file:
    puzzle_input = [[char for char in line.strip()] for line in file]

# ******** Part A *******


def get_diagonals(matrix, other_way=False):
    # Assuming a square matrix, returns all possible diagonals in
    # a direction -- use `other_way` flag to change this direction.
    #
    # This function is very janky and confusing, but it does work.

    dimension = len(matrix)

    far_corner = dimension - 1 if other_way else 0
    topside_start = dimension - 1 if other_way else 0
    topside_end = 0 if other_way else dimension - 1
    topside_step = -1 if other_way else 1

    start_points = [(far_corner, y) for y in range(dimension - 1, 0, -1)] + [
        (x, 0 if other_way else far_corner)
        for x in range(topside_start, topside_end - 1, topside_step)
    ]

    for x, y in start_points:
        curr_x, curr_y, curr_diag = x, y, []
        while curr_x in range(0, dimension) and curr_y in range(0, dimension):
            curr_element = matrix[curr_y][curr_x]
            curr_diag.append(curr_element)
            curr_x += -1 if other_way else 1
            curr_y += 1
        yield curr_diag


horizontal = ["".join(line) for line in puzzle_input]
vertical = ["".join(line) for line in zip(*horizontal)]
diagonals_a = ["".join(line) for line in get_diagonals(puzzle_input)]
diagonals_b = ["".join(line) for line in get_diagonals(puzzle_input, other_way=True)]

search_space = "\n".join(horizontal + vertical + diagonals_a + diagonals_b)

search_a = re.compile("XMAS")
search_b = re.compile("SAMX")

results = search_a.findall(search_space) + search_b.findall(search_space)

print(len(results))

# ******** Part B *******

centre_coords = [
    # double comprehension to flatten 2D to 1D
    coord
    for line in [
        # For all stars, the A must be in the centre.
        [(yi, xi) for xi, x in enumerate(y) if x == "A"]
        for yi, y in enumerate(puzzle_input)
    ]
    for coord in line
]

dimension = len(puzzle_input)
centre_coords = [
    (y, x)
    for y, x in centre_coords
    if y not in (0, dimension - 1) and x not in (0, dimension - 1)
    # removing As that are on the edges -- they can't be Xs
]


def is_x_mas(matrix, x, y):
    char = matrix[y][x]
    if char != "A":
        return False
    # checking in clockwise order: NE, SE, SW, and NW.
    patterns = [
        ("S", "S", "M", "M"),
        ("M", "S", "S", "M"),
        ("M", "M", "S", "S"),
        ("S", "M", "M", "S"),
    ]
    current_mas = (
        matrix[y - 1][x + 1],
        matrix[y + 1][x + 1],
        matrix[y + 1][x - 1],
        matrix[y - 1][x - 1],
    )
    return current_mas in patterns


x_mases = [(y, x) for y, x in centre_coords if is_x_mas(puzzle_input, x, y)]

print(len(x_mases))
