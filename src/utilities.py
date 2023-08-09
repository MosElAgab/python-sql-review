
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


def format_features(stock):
    if not isinstance(stock, list):
        raise TypeError('invalid input, input must be a list')
    if len(stock) == 0:
        raise IndexError('invalid input, list must not be empty')
    for item in stock:
        if not isinstance(item, dict):
            messege = 'invalid_input, input must be a list of dictionaries'
            raise TypeError(messege)
    features = []
    for item in stock:
        for feature in item['features']:
            if [feature] not in features:
                features.append([feature])
    return features


def format_staff(staff_list: list, departments_list: list) -> list:
    # errors handling
    if not isinstance(staff_list, list) or\
     not isinstance(departments_list, list):
        raise TypeError('invalid input, input must be a list')
    if len(staff_list) == 0 or len(departments_list) == 0:
        raise IndexError('invalid input, list must not be empty')
    for staff in staff_list:
        if not isinstance(staff, dict):
            raise TypeError('invalid_input, input must be a '
                            'list of dictionaries')
    for department in departments_list:
        if not isinstance(department, dict):
            raise TypeError('invalid_input, input must be a '
                            'list of dictionaries')
    # matching
    output = []
    for staff in staff_list:
        for department in departments_list:
            if staff['department'] == department['department_name']:
                output.append([staff['first_name'], staff['last_name'],
                               department['department_id']])
                break
    # result
    return output


def format_stock_feature(new_stock_data, new_feature_data,
                         original_stock_data):
    if len(new_stock_data) == 0:
        return []
    result = []
    for item in original_stock_data:
        for feature in item['features']:
            item_id = None
            for new_stock in new_stock_data:
                if item['item_name'] == new_stock['item_name']:
                    item_id = new_stock['item_id']
                    break
            for new_feature in new_feature_data:
                if new_feature['feature_name'] == feature:
                    result.append([item_id, new_feature['feature_id']])
    return result


def format_sales():
    pass
