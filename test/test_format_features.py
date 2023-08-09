from src.utilities import (format_features)
import pytest


# test function return type list
def test_format_features_returns_list_with_valid_input():
    assert type(format_features([{
        'item_name': '', 
        'amount': 9,
        'features': ['Designer']
        }]
        )) == list


# test function only accepts input of type list
def test_format_features_raises_type_error_for_invalid_input_type():
    with pytest.raises(TypeError):
        format_features('')


# test function with empty list
def test_format_features_raises_index_error_for_empty_list_input():
    match = 'invalid input, list must not be empty'
    with pytest.raises(IndexError, match=match):
        format_features([])


# test fucntion throws type error if list contain non dictonary data type
def test_format_features_raises_type_error_if_list_input_contains_non_dictionary():
    match = 'invalid_input, input must be a list of dictionaries'
    with pytest.raises(TypeError, match=match):
        format_features([{}, '', {}])


# test fucntion basic (single values)
def test_format_features_handles_single_value_input():
    stock = [{
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer'],
        'department': 'Footwear',
        'amount': 5
    }]
    expected_result = [['Designer']]
    assert format_features(stock) == expected_result

# test function basic (single value) multiple features
def test_format_features_handles_multiple_features():
    stock = [{
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer', 'Faux-Faux-Leather'],
        'department': 'Footwear',
        'amount': 5
    }]
    expected_result = [['Designer'], ['Faux-Faux-Leather']]
    assert format_features(stock) == expected_result


# test multiple values
def test_format_features_handles_multiple_values_input():
    stock = [{
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer', 'Faux-Faux-Leather'],
        'department': 'Footwear',
        'amount': 5
    }, {
        'item_id': 2,
        'item_name': 'Eau de Fromage',
        'features': ['Fragrance'],
        'department': 'Beauty',
        'amount': 10
    }]
    expected_result = [['Designer'], ['Faux-Faux-Leather'], ['Fragrance']]
    assert format_features(stock) == expected_result


# test for duplicate features
def test_format_features_removes_duplicate_features():
    stock = [{
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer', 'Faux-Faux-Leather'],
        'department': 'Footwear',
        'amount': 5
    }, {
        'item_id': 2,
        'item_name': 'Eau de Fromage',
        'features': ['Fragrance', 'Designer'],
        'department': 'Beauty',
        'amount': 10
    }]
    expected_result = [['Designer'], ['Faux-Faux-Leather'], ['Fragrance']]
    assert format_features(stock) == expected_result


# test case for missing values
