from src.utilities import (format_departments)
import pytest


# test function return type list
def test_it_returns_a_list():
    assert type(format_departments([{'department': ''}])) == list


# it only accepts input of type list
def test_fucntion_raise_typeerror_for_invalid_input_type():
    with pytest.raises(TypeError):
        format_departments('')


# test function with empty list
def test_fucntion_raises_IndexError_for_empty_list_input():
    match = 'invalid input, list must not be empty'
    with pytest.raises(IndexError, match=match):
        format_departments([])


# test fucntion throws type error if list contain non dictonary data type
def test_function_raises_TypeError_if_list_input_contains_non_dictionary():
    match = 'invalid_input, input must be a list of dictionaries'
    with pytest.raises(TypeError, match=match):
        format_departments([{}, '', {}])


# test fucntion basic (single values)
def test_fucntion_basics():
    staff = [{
        'staff_id': 1,
        'first_name': 'Will',
        'last_name': 'Crawley',
        'department': 'Beauty'
    }]
    expected_result = [['Beauty']]
    assert format_departments(staff) == expected_result


# test multiple values
def test_fucntion_multiple_values():
    staff = [{
        'staff_id': 1,
        'first_name': 'Will',
        'last_name': 'Crawley',
        'department': 'Beauty'
        }, {
        'staff_id': 2,
        'first_name': 'Cat',
        'last_name': 'Hoang',
        'department': 'Footwear'
        }
        ]
    expected_result = [['Beauty'], ['Footwear']]
    assert format_departments(staff) == expected_result
# test case to handle missing departments
# tets case to handle departments with wrong data type
# test for duplicate departments
