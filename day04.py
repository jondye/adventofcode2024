#!/usr/bin/env python


from itertools import chain


def parse_input(text):
    return text.splitlines()


def count(sequence):
    sequence = "".join(sequence)
    return sequence.count("XMAS") + sequence.count("SAMX")


def count_all(sequences):
    return sum(count(s) for s in sequences)


def vertical(sequences):
    # AKA transpose
    return zip(*sequences)


def shiftr(sequences):
    return (
        chain([None] * (len(sequences) - n - 1), s, [None] * n)
        for n, s in enumerate(sequences)
    )


def shiftl(sequences):
    return (
        chain([None] * n, s, [None] * (len(sequences) - n - 1))
        for n, s in enumerate(sequences)
    )


def diagonal_tlbr(sequences):
    return (filter(bool, x) for x in zip(*shiftr(sequences)))


def diagonal_trbl(sequences):
    return (filter(bool, x) for x in zip(*shiftl(sequences)))


def part1(grid):
    return (
        count_all(grid)
        + count_all(vertical(grid))
        + count_all(diagonal_tlbr(grid))
        + count_all(diagonal_trbl(grid))
    )


def main():
    with open("input04.txt") as f:
        text = f.read()
        print(f"Part1: {part1(text)}")


if __name__ == "__main__":
    main()
