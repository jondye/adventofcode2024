from itertools import pairwise


def parse_input(input):
    return ((int(val) for val in line.split()) for line in input.splitlines())

def safe(sequence):
    diffs = list(a-b for a,b in pairwise(sequence))
    return (all(1 <= d <= 3 for d in diffs)
        or all(-3 <= d <= -1 for d in diffs))

def part1(reports):
    return sum(safe(sequence) for sequence in reports)

def main():
    with open("input02.txt") as f:
        reports = parse_input(f.read())
        print(f"Part 1: {part1(reports)}")

if __name__ == '__main__':
    main()