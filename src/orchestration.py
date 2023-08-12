from extract_utilities import (get_table)
from utilities import (format_departments, format_features, format_stock,
                       format_stock_feature, format_staff, format_sales)
from load_utilities import (populate_dim_department, populate_dim_features, populate_dim_stock,
                            populate_stock_feature_junc, populate_dim_staff, populate_fact_sales)


# original_tables
items = get_table('items', 'nc_sells_fridges_draft')
original_staff = get_table('staff', 'nc_sells_fridges_draft')
original_sales = get_table('sales', 'nc_sells_fridges_draft')


# dim_department
departments = format_departments(items)
populate_dim_department(departments)
new_dim_department = get_table('dim_department', 'nc_sells_fridges')
# for i in new_dim_department:
#     print(i)


# dim_features
features = format_features(items)
populate_dim_features(features)
new_dim_features = get_table('dim_features', 'nc_sells_fridges')
# for i in new_dim_features:
#     print(i)


# dim_stock
stock = format_stock(items)
populate_dim_stock(stock)
new_dim_stock = get_table('dim_stock', 'nc_sells_fridges')
# for i in new_dim_stock:
#     print(i)


# stock_feature_junc
junction_table = format_stock_feature(new_dim_stock, new_dim_features, items)
populate_stock_feature_junc(junction_table)
new_stock_feature_junc = get_table('stock_feature_junc', 'nc_sells_fridges')
# print('....')
# for i in new_stock_feature_junc:
#     print(i)


# dim_staff
staff = format_staff(original_staff, new_dim_department)
populate_dim_staff(staff)
new_dim_staff = get_table('dim_staff', 'nc_sells_fridges')
# print('....')
# for i in new_dim_staff:
#     print(i)


# fact_sales
sales = format_sales(new_dim_stock, new_dim_staff, original_sales)
# print('...')
# print(sales)
populate_fact_sales(sales)
new_fact_sales = get_table('fact_sales', 'nc_sells_fridges')
# print('....')
# for i in new_fact_sales:
#     print(i)

