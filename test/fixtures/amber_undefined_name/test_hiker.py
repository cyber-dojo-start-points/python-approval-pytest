from hiker import answer

from approvaltests import verify, Options
from approvaltests.inline.inline_options import InlineOptions

options = Options().inline(InlineOptions.semi_automatic())


def test_life_the_universe_and_everything():
    """
    42
    """
    verify(str(ansewr()), options=options)
