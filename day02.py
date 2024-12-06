from itertools import pairwise, tee


def parse_input(input):
    return (tuple(int(val) for val in line.split()) for line in input.splitlines())

def safe1(sequence):
    diffs = list(a-b for a,b in pairwise(sequence))
    return (all(1 <= d <= 3 for d in diffs)
        or all(-3 <= d <= -1 for d in diffs))

def part1(reports):
    return sum(safe1(sequence) for sequence in reports)

def dampener(sequence):
    s = list(sequence)
    for i in range(len(s)):
        yield s[:i] + s[i+1:]

def safe2(sequence):
    return any(safe1(s) for s in dampener(sequence))

def part2(reports):
    return sum(safe2(sequence) for sequence in reports)

def main():
    with open("input02.txt") as f:
        reports = list(parse_input(f.read()))
        print(f"Part 1: {part1(reports)}")
        print(f"Part 2: {part2(reports)}")

if __name__ == '__main__':
    main()