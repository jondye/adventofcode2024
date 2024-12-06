from hamcrest import *

from day01 import *

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
    assert_that(
        parsed_input,
        contains_exactly(
            contains_exactly(3, 4, 2, 1, 3, 3),
            contains_exactly(4, 3, 5, 3, 9, 3)))

def test_diff():
    assert_that(diff((2,1,4,3), (7,7,5,3)), contains_exactly(2, 3, 4, 3))
