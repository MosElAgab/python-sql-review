from src.utilities import (format_stock)
import pytest


# test function return type list
def test_format_stock_returns_list_with_valid_input():
    assert type(format_stock([{'item_name': '', 'amount_in_stock': 9}])) == list


# it only accepts input of type list
def test_format_stock_raises_type_error_for_invalid_input_type():
    with pytest.raises(TypeError):
        format_stock('')


# test function with empty list
def test_format_stock_raises_index_error_for_empty_list_input():
    match = 'invalid input, list must not be empty'
    with pytest.raises(IndexError, match=match):
        format_stock([])


# test fucntion throws type error if list contain non dictonary data type
def test_format_stock_raises_type_error_if_list_input_contains_non_dictionary():
    match = 'invalid_input, input must be a list of dictionaries'
    with pytest.raises(TypeError, match=match):
        format_stock([{}, '', {}])


# test fucntion basic (single values)
def test_format_departments_handles_single_value_input():
    stock = [{
        'item_id': 1,
        'item_name': 'Nike Air Max Sneakers',
        'features': ['Air Cushioning', 'Mesh Upper'],
        'department': 'Footwear',
        'amount_in_stock': 8
    }]
    expected_result = [['Nike Air Max Sneakers', 8]]
    assert format_stock(stock) == expected_result


# test multiple values
def test_format_stock_handles_multiple_values_input():
    stock = [{
        'item_id': 1,
        'item_name': 'Nike Air Max Sneakers',
        'features': ['Air Cushioning', 'Mesh Upper'],
        'department': 'Footwear',
        'amount_in_stock': 8
    }, {
        'item_id': 2,
        'item_name': 'Gourmet Chocolate Box',
        'features': ['Assorted Flavors', 'Luxury Packaging'],
        'department': 'Food & Beverages',
        'amount_in_stock': 15
    }
    ]
    expected_result = [['Nike Air Max Sneakers', 8],
                       ['Gourmet Chocolate Box', 15]]
    assert format_stock(stock) == expected_result


# test for missing values
