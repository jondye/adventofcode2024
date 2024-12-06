def parse_input(lines):
    return [tuple(l.split()) for l in lines.splitlines()]

def day01(lines):
    parse_input(lines)

def test_day01():
    data = """
        3   4
        4   3
        2   5
        1   3
        3   9
        3   3
        """.strip()
    assert day01(data) == 11

def test_parse_input():
    data = """
        3   4
        4   3
        2   5
        1   3
        3   9
        3   3
        """.strip()
    parsed_input = parse_input(data)
    assert parsed_input[0] == (3,4)
