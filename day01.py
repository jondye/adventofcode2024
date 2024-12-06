from collections import Counter
import itertools


def parse_input(lines):
    return zip(*((int(v) for v in l.split()) for l in lines.splitlines()))

def diff(a, b):
    return (abs(x-y) for (x,y) in zip(sorted(a), sorted(b)))

def part1(lists):
    return sum(diff(*lists))

def part2(lists):
    left, right = lists
    counts = Counter(right)
    return sum(val * counts[val] for val in left)

def main():
    with open("input01.txt") as f:
        lists1, lists2 = itertools.tee(parse_input(f.read()))
        print(f"Part 1: {part1(lists1)}")
        print(f"Part 2: {part2(lists2)}")

if __name__ == '__main__':
    main()
