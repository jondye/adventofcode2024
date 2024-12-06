from hamcrest import *
from textwrap import dedent
import pytest
import day02

def test_day02():
    day02_input = dedent("""\
        7 6 4 2 1
        1 2 7 8 9
        9 7 6 2 1
        1 3 2 4 5
        8 6 4 4 1
        1 3 6 7 9""")

    lines = day02.parse_input(day02_input)
    assert_that(next(lines), contains_exactly(7, 6, 4, 2, 1))
    assert_that(next(lines), contains_exactly(1, 2, 7, 8, 9))
    assert_that(next(lines), contains_exactly(9, 7, 6, 2, 1))
    assert_that(next(lines), contains_exactly(1, 3, 2, 4, 5))
    assert_that(next(lines), contains_exactly(8, 6, 4, 4, 1))
    assert_that(next(lines), contains_exactly(1, 3, 6, 7, 9))

    assert_that(day02.safe1(x for x in (7, 6, 4, 2, 1)), is_(True))
    assert_that(day02.safe1(x for x in (1, 2, 7, 8, 9)), is_(False))
    assert_that(day02.safe1(x for x in (9, 7, 6, 2, 1)), is_(False))
    assert_that(day02.safe1(x for x in (1, 3, 2, 4, 5)), is_(False))
    assert_that(day02.safe1(x for x in (8, 6, 4, 4, 1)), is_(False))
    assert_that(day02.safe1(x for x in (1, 3, 6, 7, 9)), is_(True))

    lines = (
        (7, 6, 4, 2, 1),
        (1, 2, 7, 8, 9),
        (9, 7, 6, 2, 1),
        (1, 3, 2, 4, 5),
        (8, 6, 4, 4, 1),
        (1, 3, 6, 7, 9))
    assert_that(day02.part1(lines), is_(2))

    assert_that(day02.safe2(x for x in (7, 6, 4, 2, 1)), is_(True))
    assert_that(day02.safe2(x for x in (1, 2, 7, 8, 9)), is_(False))
    assert_that(day02.safe2(x for x in (9, 7, 6, 2, 1)), is_(False))
    assert_that(day02.safe2(x for x in (1, 3, 2, 4, 5)), is_(True))
    assert_that(day02.safe2(x for x in (8, 6, 4, 4, 1)), is_(True))
    assert_that(day02.safe2(x for x in (1, 3, 6, 7, 9)), is_(True))

    assert_that(day02.part2(lines), is_(4))

