from hiker import answer

from approvaltests import verify, Options
from approvaltests.inline.inline_options import InlineOptions

options = Options().inline(InlineOptions.semi_automatic())


def test_life_the_universe_and_everything():
    """
    42
    """
    verify(str(answer()), options=options)


def test_the_answer_is_three_digits_long():
    """
    3
    """
    verify(str(len(str(answer()))), options=options)


def test_the_answer_is_the_question():
    """
    True
    """
    verify(str(str(answer()) == '6 * 7'), options=options)
