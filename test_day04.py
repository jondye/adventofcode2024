from textwrap import dedent

from hamcrest import (
    assert_that,
    contains_exactly,
    contains_inanyorder,
    empty,
    instance_of,
    is_,
)
import pytest

import day04


def test_count():
    assert_that(day04.count("...."), is_(0))
    assert_that(day04.count("XMAS"), is_(1))
    assert_that(day04.count("...XMAS..."), is_(1))
    assert_that(day04.count("..XXMAS..."), is_(1))
    assert_that(day04.count("..XMASS..."), is_(1))
    assert_that(day04.count("X.M.A.S..."), is_(0))
    assert_that(day04.count("XX.M.A.S.S"), is_(0))


def test_count_all():
    assert_that(day04.count_all(("..XMASS...", "..XMAS..")), is_(2))
    assert_that(day04.count_all((".XMASSAMX.", "..XMAS..")), is_(3))


def test_vertical():
    v = iter(day04.vertical(("1234", "abcd", "wxyz")))
    assert_that(next(v), contains_exactly("1", "a", "w"))
    assert_that(next(v), contains_exactly("2", "b", "x"))
    assert_that(next(v), contains_exactly("3", "c", "y"))
    assert_that(next(v), contains_exactly("4", "d", "z"))


def test_shift():
    assert_that(day04.shiftr([]), is_(contains_exactly()))
    s = iter(day04.shiftr([[1], [2]]))
    assert_that(next(s), contains_exactly(None, 1))
    assert_that(next(s), contains_exactly(2, None))


def test_diagonal_tlbr():
    d = iter(day04.diagonal_tlbr(("1",)))
    assert_that(d, contains_inanyorder(contains_exactly("1")))

    d = day04.diagonal_tlbr(("12", "ab"))
    assert_that(next(d), contains_exactly("a"))
    assert_that(next(d), contains_exactly("1", "b"))
    assert_that(next(d), contains_exactly("2"))

    d = iter(day04.diagonal_tlbr(("1234", "abcd", "wxyz")))
    assert_that(next(d), contains_exactly("w"))
    assert_that(next(d), contains_exactly("a", "x"))
    assert_that(next(d), contains_exactly("1", "b", "y"))
    assert_that(next(d), contains_exactly("2", "c", "z"))
    assert_that(next(d), contains_exactly("3", "d"))
    assert_that(next(d), contains_exactly("4"))


def test_diagonal_trbl():
    d = iter(day04.diagonal_trbl(("1",)))
    assert_that(d, contains_inanyorder(contains_exactly("1")))

    d = day04.diagonal_trbl(("12", "ab"))
    assert_that(next(d), contains_exactly("1"))
    assert_that(next(d), contains_exactly("2", "a"))
    assert_that(next(d), contains_exactly("b"))

    d = iter(day04.diagonal_trbl(("1234", "abcd", "wxyz")))
    assert_that(next(d), contains_exactly("1"))
    assert_that(next(d), contains_exactly("2", "a"))
    assert_that(next(d), contains_exactly("3", "b", "w"))
    assert_that(next(d), contains_exactly("4", "c", "x"))
    assert_that(next(d), contains_exactly("d", "y"))
    assert_that(next(d), contains_exactly("z"))


def test_day04():
    text = dedent(
        """\
        MMMSXXMASM
        MSAMXMSMSA
        AMXSXMAAMM
        MSAMASMSMX
        XMASAMXAMM
        XXAMMXXAMA
        SMSMSASXSS
        SAXAMASAAA
        MAMMMXMMMM
        MXMXAXMASX"""
    )

    grid = day04.parse_input(text)
    row = iter(grid)
    assert_that(next(row), contains_exactly(*"MMMSXXMASM"))
    assert_that(next(row), contains_exactly(*"MSAMXMSMSA"))
    assert_that(next(row), contains_exactly(*"AMXSXMAAMM"))
    assert_that(next(row), contains_exactly(*"MSAMASMSMX"))
    assert_that(next(row), contains_exactly(*"XMASAMXAMM"))
    assert_that(next(row), contains_exactly(*"XXAMMXXAMA"))
    assert_that(next(row), contains_exactly(*"SMSMSASXSS"))
    assert_that(next(row), contains_exactly(*"SAXAMASAAA"))
    assert_that(next(row), contains_exactly(*"MAMMMXMMMM"))
    assert_that(next(row), contains_exactly(*"MXMXAXMASX"))

    assert_that(day04.count_all(grid), is_(5))
    assert_that(day04.count_all(day04.vertical(grid)), is_(3))
    assert_that(day04.count_all(day04.diagonal_tlbr(grid)), is_(5))
    assert_that(day04.count_all(day04.diagonal_trbl(grid)), is_(5))

    assert_that(day04.part1(grid), is_(18))
