
from pytest import raises
from binsearch import binary_search
import numpy as np

from pytest import raises
from binsearch import binary_search
import numpy as np

def test_wired_data_1():
    with raises(TypeError):
        binary_search([None, None],1) 

def test_wired_data_2():
    with raises(TypeError):
        binary_search(["a", "b"],1) 

def test_size_1_1():
    assert binary_search([5], 5) == 0
    
def test_size_1_2():
    assert binary_search([4], 5) == -1

def test_size_0():
    assert binary_search([],1) == -1

def test_inf_1():
    assert binary_search([1,2,np.inf], 2) == 1
    
def test_inf_1():
    assert binary_search([1,2,np.inf], np.inf) == 2

def test_search_out_of_bound_1():
    assert binary_search([1,2,3,4,5], 0) == -1

def test_search_out_of_bound_2():
    assert binary_search([1,2,3,4,5], 6) == -1

def test_search_out_of_bound_3():
    with raises(TypeError):
        assert binary_search([1,2,3,4,5], "a") 

def test_search_out_of_bound_4():
    assert binary_search([1,2,3,4,5],1,3,4) == -1

def test_search_out_of_bound_5():
    assert binary_search([1,2,3,4,5],5,0,3) == -1

def test_search_in_bound_1():
    assert binary_search([1,2,3,4,5],3,2,2) == 2
    
def test_search_in_bound_2():
    assert binary_search([1,2,3,4,5],3,0,3) == 2
