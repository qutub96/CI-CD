import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.app import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0