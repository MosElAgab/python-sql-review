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
                     '(:department)', department=department[0])


def populate_dim_features(features):
    username = getpass.getuser()
    database = 'nc_sells_fridges'
    if len(get_table('dim_features', database)) > 0:
        return 'table already filled'
    with pg.Connection(user=username, database=database) as conn:
        for feature in features:
            conn.run('INSERT INTO dim_features (feature_name)'
                     ' VALUES (:feature)', feature=feature[0])


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


def populate_stock_feature_junc(junction_table):
    username = getpass.getuser()
    database = 'nc_sells_fridges'
    if len(get_table('stock_feature_junc', database)) > 0:
        return 'table already filled'
    with pg.Connection(user=username, database=database) as conn:
        for row in junction_table:
            conn.run('INSERT INTO stock_feature_junc (stock_id, feature_id)'
                     'VALUES (:stock_id, :feature_id)',
                     stock_id=row[0], feature_id=row[1])
    

def populate_dim_staff(staff):
    username = getpass.getuser()
    database = 'nc_sells_fridges'
    if len(get_table('dim_staff', database)) > 0:
        return 'table already filled'
    with pg.Connection(user=username, database=database) as conn:
        for worker in staff:
            conn.run('INSERT INTO dim_staff (first_name, last_name, department_id)'
                     'VALUES (:first_name, :last_name, :department_id)',
                     first_name=worker[0], last_name=worker[1],
                     department_id=worker[2])


def populate_fact_sales(sales):
    username = getpass.getuser()
    database = 'nc_sells_fridges'
    if len(get_table('fact_sales', database)) > 0:
        return 'table already filled'
    with pg.Connection(user=username, database=database) as conn:
        for sale in sales:
            conn.run('INSERT INTO fact_sales (item_id,'
                     ' salesperson, price, quantity, created_at)'
                     'VALUES (:item_id, :salesperson,'
                     ':price, :quantity, :created_at)',
                     item_id=sale[0],
                     salesperson=sale[1], price=sale[2],
                     quantity=sale[3], created_at=[sale[4]])

# test load utilites
