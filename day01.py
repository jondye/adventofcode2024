def parse_input(lines):
    return zip(*((int(v) for v in l.split()) for l in lines.splitlines()))

def diff(a, b):
    return (abs(x-y) for (x,y) in zip(sorted(a), sorted(b)))

def day01(lines):
    lists = parse_input(lines)
    return sum(diff(*lists))

def main():
    with open("input01.txt") as f:
        print(day01(f.read()))

if __name__ == '__main__':
    main()
