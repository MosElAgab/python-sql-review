from src.utilities import (format_staff)
import pytest

# test data
staff_list = [{
    'staff_id': 1,
    'first_name': 'Ali',
    'last_name': 'Coa',
    'department': 'Electronics'
}, {
    'staff_id': 2,
    'first_name': 'Cat',
    'last_name': 'Hoang',
    'department': 'Toys'
}, {
    'staff_id': 3,
    'first_name': 'Ella',
    'last_name': 'Martinez',
    'department': 'Beauty'
}, {
    'staff_id': 4,
    'first_name': 'Daniel',
    'last_name': 'Williams',
    'department': 'Footwear'
}]
departments_list = [{
    'department_id': 1,
    'department_name': 'Beauty'
}, {
    'department_id': 2,
    'department_name': 'Footwear'
}, {
    'department_id': 3,
    'department_name': 'Toys'
}, {
    'department_id': 4,
    'department_name': 'Electronics'
}]


# test function return type list
def test_format_staff_returns_list_with_valid_input():
    output = format_staff(staff_list, departments_list)
    assert isinstance(output, list)


# test function throws error for unvalid input type
def test_format_staff_raises_type_error_for_invalid_input_type():
    match = 'invalid input, input must be a list'
    with pytest.raises(TypeError, match=match):
        format_staff('', departments_list)
    with pytest.raises(TypeError, match=match):
        format_staff(staff_list, '')


# test function with empty list
def test_format_staff_raises_index_error_for_empty_list_input():
    match = 'invalid input, list must not be empty'
    with pytest.raises(IndexError, match=match):
        format_staff([], departments_list)
    with pytest.raises(IndexError, match=match):
        format_staff(staff_list, [])


# test fucntion throws type error if list contain non dictonary data type
def test_format_staff_raises_type_error_if_list_input_contains_non_dictionary():
    match = 'invalid_input, input must be a list of dictionaries'
    with pytest.raises(TypeError, match=match):
        format_staff([{}, '', {}], departments_list)
    with pytest.raises(TypeError, match=match):
        format_staff(staff_list, [{}, '', {}])


# test function basic with single staff
def test_format_staff_handles_single_value_input():
    expected_output = [['Ali', 'Coa', 4]]
    output = format_staff(staff_list[0:1], departments_list)
    assert output == expected_output


# test function basic with multiple staff
def test_format_staff_handles_multiple_value_input():
    expected_output = [['Ali', 'Coa', 4], ['Cat', 'Hoang', 3],
                       ['Ella', 'Martinez', 1], ['Daniel', 'Williams', 2]]
    output = format_staff(staff_list, departments_list)
    print('here', output)
    assert output == expected_output

# test no matching departments
# for an empty list input > should return an empty list
