# Named neither test_*.py nor *_test.py, so pytest does not collect it and
# this test does not run. The approved value in the docstring is one that
# would mismatch, so a green says it really did not run rather than that it
# ran and matched.
from hiker import answer

from approvaltests import verify, Options
from approvaltests.inline.inline_options import InlineOptions

options = Options().inline(InlineOptions.semi_automatic())


def test_the_answer_is_three_digits_long():
    """
    3
    """
    verify(str(len(str(answer()))), options=options)
