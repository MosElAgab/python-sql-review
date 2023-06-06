
def format_departments(staff):
    if isinstance(staff, list) is not True:
        raise TypeError('invalid input, input must be a list')
    if len(staff) == 0:
        raise IndexError('invalid input, list must not be empty')
    for member in staff:
        if isinstance(member, dict) is not True:
            messege = 'invalid_input, input must be a list of dictionaries'
            raise TypeError(messege)
    departments = [[member['department']] for member in staff]
    return departments


def format_stock(stock):
    if isinstance(stock, list) is not True:
        raise TypeError('invalid input, input must be a list')
    if len(stock) == 0:
        raise IndexError('invalid input, list must not be empty')
    for item in stock:
        if isinstance(item, dict) is not True:
            messege = 'invalid_input, input must be a list of dictionaries'
            raise TypeError(messege)
    items = [[item['item_name'], item['amount']] for item in stock]
    return items


def format_features():
    pass


def format_staff():
    pass


def format_stock_feature():
    pass


def format_sales():
    pass
