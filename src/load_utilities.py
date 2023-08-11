import pg8000.native as pg
import getpass
from extract_utilities import (get_table)


def populate_dim_department(departments):
    username = getpass.getuser()
    database = 'nc_sells_fridges'
    if len(get_table('dim_department', database)) > 0:
        return 'table already filled'
    with pg.Connection(user=username, database=database) as conn:
        for department in departments:
            conn.run('INSERT INTO dim_department'
                     '(department_name) VALUES '
                     '(:department)', department=department)


def populate_dim_features(features):
    username = getpass.getuser()
    database = 'nc_sells_fridges'
    if len(get_table('dim_features', database)) > 0:
        return 'table already filled'
    with pg.Connection(user=username, database=database) as conn:
        for feature in features:
            conn.run('INSERT INTO dim_features (feature_name)'
                     ' VALUES (:feature)', feature=feature)


def populate_dim_stock(stock):
    username = getpass.getuser()
    database = 'nc_sells_fridges'
    if len(get_table('dim_stock', database)) > 0:
        return 'table already filled'
    with pg.Connection(user=username, database=database) as conn:
        for item in stock:
            conn.run('INSERT INTO dim_stock (item_name, amount_in_stock)'
                     ' VALUES (:item_name, :amount_in_stock)',
                     item_name=item[0],
                     amount_in_stock=item[1])


# test load utilites
