#!/usr/bin/env python

import re


def part1(input):
    return sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", input))

def main():
    with open("input03.txt") as f:
        print(f"Part 1: {part1(f.read())}")

if __name__ == '__main__':
    main()
