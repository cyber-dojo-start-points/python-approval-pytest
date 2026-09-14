# Named neither test_*.py nor *_test.py, so pytest never collects it, and
# half written so it does not parse either. Nothing compiles every .py file
# here, so the run stays green and only mypy and coverage mention it.
from hiker import answer

from approvaltests import verify, Options
from approvaltests.inline.inline_options import InlineOptions

options = Options().inline(InlineOptions.semi_automatic())


def test_the_answer_is_two_digits_long():
    """
    2
    """
    verify(str(len(str(answer())), options=options)
