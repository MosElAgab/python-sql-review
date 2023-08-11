from src.utilities import (format_departments)
import pytest


# test function return type list
def test_format_departments_returns_list_with_valid_input():
    assert type(format_departments([{'department': ''}])) == list


# it only accepts input of type list
def test_format_departments_raises_type_error_for_invalid_input_type():
    with pytest.raises(TypeError):
        format_departments('')


# test function with empty list
def test_format_departments_raises_index_error_for_empty_list_input():
    match = 'invalid input, list must not be empty'
    with pytest.raises(IndexError, match=match):
        format_departments([])


# test fucntion throws type error if list contain non dictonary data type
def test_format_departments_raises_type_error_if_list_input_contains_non_dictionary():
    match = 'invalid_input, input must be a list of dictionaries'
    with pytest.raises(TypeError, match=match):
        format_departments([{}, '', {}])


# test fucntion basic (single values)
def test_format_departments_handles_single_value_input():
    staff = [{
        'staff_id': 1,
        'first_name': 'Will',
        'last_name': 'Crawley',
        'department': 'Beauty'
    }]
    expected_result = [['Beauty']]
    assert format_departments(staff) == expected_result


# test multiple values
def test_format_departments_handles_multiple_values_input():
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


# test function for duplicate departments
def test_format_department_removes_duplicate():
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
        }, {
        'staff_id': 3,
        'first_name': 'Ali',
        'last_name': 'Haider',
        'department': 'Footwear'
        }
        ]
    expected_result = [['Beauty'], ['Footwear']]
    assert format_departments(staff) == expected_result

# test case to handle missing departments
# tets case to handle departments with wrong data type
