from extract_utilities import (get_table)
from utilities import (format_departments, format_features, format_stock)
from load_utilities import (populate_dim_department, populate_dim_features, populate_dim_stock)


# original_tables
items = items = get_table('items', 'nc_sells_fridges_draft')


# dim_department
departments = format_departments(items)
populate_dim_department(departments)
new_dim_department = get_table('dim_department', 'nc_sells_fridges')
for i in new_dim_department:
    print(i)


# dim_features
features = format_features(items)
populate_dim_features(features)
new_dim_features = get_table('dim_features', 'nc_sells_fridges')
for i in new_dim_features:
    print(i)


# dim_stock
stock = format_stock(items)
populate_dim_stock(stock)
new_dim_stock = get_table('dim_stock', 'nc_sells_fridges')
for i in new_dim_stock:
    print(i)
