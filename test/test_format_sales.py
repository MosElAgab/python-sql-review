from src.utilities import (format_sales)

# test data
new_stock_data = [
    {
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'amount_in_stock': 5
    },
    {
        'item_id': 2,
        'item_name': 'Eau de Fromage',
        'amount_in_stock': 10
    },
    {
        'item_id': 3,
        'item_name': 'Luxury Watch',
        'amount_in_stock': 8
    },
    {
        'item_id': 4,
        'item_name': 'Designer Handbag',
        'amount_in_stock': 15
    }
]
new_staff_data = [
    {
        'staff_id': 1,
        'first_name': 'Duncan',
        'last_name': 'Crawley',
        'department_id': 1
    },
    {
        'staff_id': 2,
        'first_name': 'Cat',
        'last_name': 'Hoang',
        'department_id': 2
    },
    {
        'staff_id': 3,
        'first_name': 'Ella',
        'last_name': 'Martinez',
        'department_id': 3
    },
    {
        'staff_id': 4,
        'first_name': 'Daniel',
        'last_name': 'Williams',
        'department_id': 1
    }
]
original_sales_data = [
    {
        'sale_code': 'guiiljnevn',
        'item_name': 'Louboutin Flip Flops',
        'salesperson': 'Duncan Crawley',
        'price': 22.49,
        'quantity': 1,
        'created_at': '2023-01-03 10:34:56'
    },
    {
        'sale_code': 'abcd1234',
        'item_name': 'Luxury Watch',
        'salesperson': 'Daniel Williams',
        'price': 1499.99,
        'quantity': 2,
        'created_at': '2023-01-05 15:45:23'
    }
]


# test function retuns a list
def test_format_sales_returns_list_with_valid_input():
    output = format_sales(new_stock_data, new_staff_data,
                          original_sales_data)
    assert isinstance(output, list)


# test fucntion with valid sales data
def test_format_sales_handles_orginal_sales_date():
    output = format_sales(new_stock_data, new_staff_data,
                          original_sales_data[0:1])
    expected_output = [[1, 1, 22.49, 1, '2023-01-03 10:34:56']]
    assert output == expected_output
    output = format_sales(new_stock_data, new_staff_data,
                          original_sales_data)
    expected_output = [[1, 1, 22.49, 1, '2023-01-03 10:34:56'],
                       [3, 4, 1499.99, 2, '2023-01-05 15:45:23']]
    assert output == expected_output
