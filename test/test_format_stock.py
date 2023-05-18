from src.utilities import (format_stock)
import pytest 


# # test function return type list
def test_it_returns_a_list():
    assert type(format_stock([{'item_name': '', 'amount': 9}])) == list