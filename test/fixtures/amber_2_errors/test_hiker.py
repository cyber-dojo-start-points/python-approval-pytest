from hiker import answer

from approvaltests import verify, Options
from approvaltests.inline.inline_options import InlineOptions

options = Options().inline(InlineOptions.semi_automatic())


def test_life_the_universe_and_everything():
    """
    42
    """
    verify(str(answer()), options=options)


def test_the_answer_is_two_digits_long():
    """
    2
    """
    verify(str(len(str(answer()))), options=options)
