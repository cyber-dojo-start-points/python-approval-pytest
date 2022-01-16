from hiker import global_answer, Hiker
from approvaltests.approvals import verify
from approvaltests.reporters import PythonNativeReporter
from approvaltests import Options
from approvaltests import set_default_reporter
import pytest

@pytest.fixture(autouse=True)
def run_around_tests():
    set_default_reporter(PythonNativeReporter())

def test_global():
    result = str(global_answer())
    verify(result)

def test_instance():
    result = str(Hiker().instance_answer())
    verify(result)
