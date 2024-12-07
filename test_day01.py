import day01

from hamcrest import *


def test_day01():
    day01_input = """
        3   4
        4   3
        2   5
        1   3
        3   9
        3   3
        """.strip()

    assert_that(
        day01.parse_input(day01_input),
        contains_exactly(
            contains_exactly(3, 4, 2, 1, 3, 3), contains_exactly(4, 3, 5, 3, 9, 3)
        ),
    )

    assert_that(day01.diff((2, 1, 4, 3), (7, 7, 5, 3)), contains_exactly(2, 3, 4, 3))

    lists = ((3, 4, 2, 1, 3, 3), (4, 3, 5, 3, 9, 3))
    assert_that(day01.part1(lists), is_(11))

    assert_that(day01.part2(lists), is_(31))
