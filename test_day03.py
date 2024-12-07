from textwrap import dedent
import day03

from hamcrest import assert_that, is_


def test_day03():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    assert_that(day03.part1(input), is_(161))

    assert_that(day03.disable(input), is_("xmul(2,4)&mul[3,7]!^?mul(8,5))"))
    assert_that(day03.disable("mul(2,4)don't()mul(3,2)"), is_("mul(2,4)"))
    assert_that(
        day03.disable("mul(1,2)don't()mul(3,4)do()mul(5,6)do()mul(7,8)"),
        is_("mul(1,2)mul(5,6)do()mul(7,8)"),
    )
    assert_that(
        day03.disable("mul(1,2)don't()mul(3,4)don't()mul(5,6)do()mul(7,8)"),
        is_("mul(1,2)mul(7,8)"),
    )
    assert_that(
        day03.disable("mul(1,2)don't()mul(3,4)\nmul(5,6)do()mul(7,8)"),
        is_("mul(1,2)mul(7,8)"),
    )

    assert_that(day03.part2(input), is_(48))
