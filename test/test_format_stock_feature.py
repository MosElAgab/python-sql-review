from src.utilities import (format_stock_feature)

# test data
new_stock_data = [
    {
        'stock_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'amount_in_stock': 5
    }, {
        'stock_id': 2,
        'item_name': 'Eau de Fromage',
        'amount_in_stock': 10
    }
]
new_feature_data = [
    {
        'feature_id': 1,
        'feature_name': 'Designer'
    }, {
        'feature_id': 2,
        'feature_name': 'Faux-Faux-Leather'
    }
]

original_stock_data = [
    {
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer', 'Faux-Faux-Leather'],
        'department': 'Footwear',
        'amount_in_stock': 5
    }, {
        'item_id': 2,
        'item_name': 'Eau de Fromage',
        'features': ['Designer'],
        'department': 'Beauty',
        'amount_in_stock': 10
    }
]


# test function retuns a list
def test_format_stock_feature_returns_list_with_valid_input():
    output = format_stock_feature(new_stock_data, new_feature_data,
                                  original_stock_data)
    assert isinstance(output, list)


# test fucntion with valid multiple data
def test_format_stock_feature_handles_multiple_data():
    output = format_stock_feature(new_stock_data, new_feature_data,
                                  original_stock_data)
    expected_output = [[1, 1], [1, 2], [2, 1]]
    assert output == expected_output
    new_stock_data[0]['stock_id'] = 7
    output = format_stock_feature(new_stock_data, new_feature_data,
                                  original_stock_data)
    expected_output = [[7, 1], [7, 2], [2, 1]]
    assert output == expected_output
    new_stock_data[0]['stock_id'] = 1
    # example does not use new_stock_data to update item_id !!!


# test fucntion with empty list input
def test_fucntion_returns_empty_list_for_empty_list_input():
    output = format_stock_feature(new_stock_data, [],
                                  original_stock_data)
    expected_output = []
    assert output == expected_output
    output = format_stock_feature(new_stock_data, new_feature_data,
                                  [])
    expected_output = []
    assert output == expected_output
    output = format_stock_feature([], new_feature_data,
                                  original_stock_data)
    expected_output = []
    print(output)
    assert output == expected_output


# test function with invalid input datatype
# test fucntion with invalid list
# test fucntion with invalid dictionary
# test fucntion with valid single data
# test fucntion with no matching data
