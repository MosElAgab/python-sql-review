
def format_departments(staff):
    if isinstance(staff, list) is not True:
        raise TypeError('invalid input, input must be a list')
    if len(staff) == 0:
        raise IndexError('invalid input, list must not be empty')
    for member in staff:
        if isinstance(member, dict) is not True:
            messege = 'invalid_input, input must be a list of dictionaries'
            raise TypeError(messege)
    departments = [member['department'] for member in staff]
    unique_departments = []
    for department in departments:
        if department not in unique_departments:
            unique_departments.append(department)
    unique_departments = [[department] for department in unique_departments]
    return unique_departments


def format_stock(stock):
    if isinstance(stock, list) is not True:
        raise TypeError('invalid input, input must be a list')
    if len(stock) == 0:
        raise IndexError('invalid input, list must not be empty')
    for item in stock:
        if isinstance(item, dict) is not True:
            messege = 'invalid_input, input must be a list of dictionaries'
            raise TypeError(messege)
    items = [[item['item_name'], item['amount_in_stock']] for item in stock]
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


def format_stock_feature(dim_stock, dim_features,
                         items):
    if len(dim_stock) == 0:
        return []
    result = []
    for item in items:
        stock_id = None
        for stock in dim_stock:
            if stock['item_name'] == item['item_name']:
                stock_id = stock['stock_id']
        for feature in item['features']:
            for dim_feature in dim_features:
                if dim_feature['feature_name'] == feature:
                    result.append([stock_id, dim_feature['feature_id']])
    
    return result


def format_sales(new_stock_data, new_staff_data,
                 original_sales_data):
    result = []

    def find_staff_id(name):
        for staff in new_staff_data:
            if staff['first_name'] + ' ' + staff['last_name'] == name:
                return staff['staff_id']

    def find_item_id(item_name):
        for item in new_stock_data:
            if item['item_name'] == item_name:
                return item['stock_id']

    for sale in original_sales_data:
        row = []
        row.append(find_item_id(sale['item_name']))
        row.append(find_staff_id(sale['salesperson']))
        row.append(sale['price'])
        row.append(sale['quantity'])
        row.append(sale['created_at'])
        result.append(row)
    return result
