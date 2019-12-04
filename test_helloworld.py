import pytest
from helloworld import *

# THIS IS A TEST HELLO JENKINS DEMO!

def test_hello():
    result = hello()
    assert result == "Hello!"
