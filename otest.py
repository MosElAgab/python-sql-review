from src.extract_utilities import (get_table)
from src.utilities import (format_features, format_departments, format_stock_feature)
import pg8000.native as pg
import getpass


items = get_table('items', 'nc_sells_fridges_draft')
print('.....')
print(items[0:3])
dim_stock = get_table('dim_stock', 'nc_sells_fridges')
print('.....')
print(dim_stock[0:3])
dim_features = get_table('dim_features', 'nc_sells_fridges')
print('.....')
print((dim_features[0:3]))
junction_table = format_stock_feature(dim_stock, dim_features, items)
print('.....')
print(junction_table)




# dim_stock = get_table('dim_stock', 'nc_sells_fridges')
# # print(dim_stock)
# dim_features = get_table('dim_features', 'nc_sells_fridges')
# print((dim_features[0]['feature_name']))
# junction_table = format_stock_feature(dim_stock, dim_features, items)
# print(junction_table)
# for i in junction_table:
#     print(i)
