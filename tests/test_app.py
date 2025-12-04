import sys
from pathlib import Path
root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add

def test_add_1():
    assert add(5, 6) == 11

def test_add_2():
    assert add(5, 6) != 10
