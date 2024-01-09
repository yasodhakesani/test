import pytest
class TestClass:
    age=36
    def test_sample(self):
        assert pow(2,3)==8,"test case passed test_sample1"
    def test_sum(self):
        
        assert hasattr(TestClass,"age"),"Hi"

    example = [5,3,1,6,6]
    booleans = [False, False,True, False]
    assert any(booleans)==True
    assert 5 in example    
    
