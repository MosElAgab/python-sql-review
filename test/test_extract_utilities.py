from src.extract_utilities import (get_table)


# test get department
def test_get_table():
    output = get_table('items')
    assert isinstance(output, list)
    assert len(output) > 0
    for row in output:
        assert isinstance(row, dict)
