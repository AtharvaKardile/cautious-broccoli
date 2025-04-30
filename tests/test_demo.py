from src.demo import greet

def test_greet_world():
    assert greet() == "Hello, World!"

def test_greet_name():
    assert greet("Alice") == "Hello, Alice!"
