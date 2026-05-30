
from agentwatch import LoopDetector

def test_loop_detection():
    d = LoopDetector()
    for _ in range(4):
        assert d.check("run") is False
    assert d.check("run") is True
