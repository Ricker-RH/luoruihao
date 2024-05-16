# tests/test_main.py 
from src.main import hello_world 
def test_helo_world(): 
    assert hello_world() == "Hello, world!"