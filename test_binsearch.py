from pytest import raises
from binsearch import binary_search
import numpy as np

#array contains None - not comparable type
def test_wired_data_1():
    with raises(TypeError):
        binary_search([None, None],1)

#array is char and needle is int
def test_wired_data_2():
    with raises(TypeError):
        binary_search(["a", "b"],1)

#one element with needle inside array
def test_size_1_1():
    assert binary_search([5], 5) == 0

#one element without needle inside array
def test_size_1_2():
    assert binary_search([4], 5) == -1

#zero element array
def test_size_0():
    assert binary_search([],1) == -1

#array contains infinity, search for a number 
def test_inf_1():
    assert binary_search([1,2,np.inf], 2) == 1

#array contains infinity, search for infinity
def test_inf_1():
    assert binary_search([1,2,np.inf], np.inf) == 2

#needle not in array, less than smallest
def test_search_out_of_bound_1():
    assert binary_search([1,2,3,4,5], 0) == -1

#needle not in array, larger than biggest
def test_search_out_of_bound_2():
    assert binary_search([1,2,3,4,5], 6) == -1

#search char in int array
def test_search_out_of_bound_3():
    with raises(TypeError):
        assert binary_search([1,2,3,4,5], "a")

#search without the range but inside array
def test_search_out_of_bound_4():
    assert binary_search([1,2,3,4,5],1,3,4) == -1

#search without the range but inside array
def test_search_out_of_bound_5():
    assert binary_search([1,2,3,4,5],5,0,3) == -1

#search within the range
def test_search_in_bound_1():
    assert binary_search([1,2,3,4,5],3,2,2) == 2

#search within the range
def test_search_in_bound_2():
    assert binary_search([1,2,3,4,5],3,0,3) == 2

#search range min is greater than range max
def test_search_in_bound_3():
    assert binary_search([1,2,3,4,5], 1,5,3) == -1

#duplicates in array
def test_multiple_num():
    assert binary_search([1,2,2,3,4,5],2) == 1 or binary_search([1,2,2,3,4,5],2) == 2