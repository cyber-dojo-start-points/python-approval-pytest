from hiker import global_answer, Hiker
from approvaltests.approvals import verify
from approvaltests.reporters import PythonNativeReporter
from approvaltests import Options


def test_global():
    result = str(global_answer())
    verify(result, options=Options().with_reporter(PythonNativeReporter()))

def test_instance():
    result = str(Hiker().instance_answer())
    verify(result, options=Options().with_reporter(PythonNativeReporter()))
