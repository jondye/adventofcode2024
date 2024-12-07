#!/usr/bin/env python

import re


def part1(text):
    return sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", text))


def disable(text):
    return re.sub(r"don't\(\).*?(do\(\)|$)", "", text, flags=re.DOTALL)


def part2(text):
    return sum(
        int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", disable(text))
    )


def main():
    with open("input03.txt") as f:
        text = f.read()
        print(f"Part 1: {part1(text)}")
        print(f"Part 2: {part2(text)}")


if __name__ == "__main__":
    main()
