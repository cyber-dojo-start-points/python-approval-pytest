from hiker import global_answer, Hiker

from approvaltests import verify, Options
from approvaltests.inline.inline_options import InlineOptions

options = Options().inline(InlineOptions.semi_automatic())


def test_global():
    """
    42
    """
    result = str(global_answer())
    verify(result, options=options)


def test_instance():
    """
    42
    """
    result = str(Hiker().instance_answer())
    verify(result, options=options)
