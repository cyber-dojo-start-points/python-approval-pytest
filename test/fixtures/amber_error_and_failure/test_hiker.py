from hiker import answer, checksum

from approvaltests import verify, Options
from approvaltests.inline.inline_options import InlineOptions

options = Options().inline(InlineOptions.semi_automatic())


def test_life_the_universe_and_everything():
    """
    42
    """
    verify(str(answer()), options=options)


def test_the_checksum_of_the_answer():
    """
    0
    """
    verify(str(checksum()), options=options)
