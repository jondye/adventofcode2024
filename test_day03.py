import day03

from hamcrest import assert_that, is_


def test_day03():
    input = r"xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert_that(day03.part1(input), is_(161))
