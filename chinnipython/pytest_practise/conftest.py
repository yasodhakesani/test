import pytest

@pytest.fixture
def input_value():
   input = 39
   return input

@pytest.fixture
def fix_fun():
   return "fixture test"

@pytest.fixture
def mul_fix_fun(fix_fun):
   return fix_fun