import pytest
#import requests #if it not highliting means we are not using it
@pytest.mark.parametrize("a,b,output",[(2,3,5)])
def test_example(a,b,output):
   assert a+b==output
    