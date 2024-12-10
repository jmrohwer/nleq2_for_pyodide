from .nleq2 import nleq2

import os
testdir = os.path.dirname(__file__)

def test():
    try:
        import pytest
    except ModuleNotFoundError as e:
        print(repr(e))
        print('Testing requires the `pytest` module. Install with `pip install pytest`.')
        return

    pytest.main([testdir])
