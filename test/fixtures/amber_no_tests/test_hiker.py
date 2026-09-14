from hiker import answer

from approvaltests import verify, Options
from approvaltests.inline.inline_options import InlineOptions

options = Options().inline(InlineOptions.semi_automatic())

# The learner has the imports in place and has not written a test yet.
