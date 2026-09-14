# The learner has reached for the file-based half of ApprovalTests, where the
# approved value lives in a .approved.txt beside the test rather than in the
# docstring, and has not written that file yet.
from hiker import answer

from approvaltests import verify


def test_life_the_universe_and_everything():
    verify(str(answer()))
