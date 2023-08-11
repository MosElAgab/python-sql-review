from src.extract_utilities import (get_table)
from src.utilities import (format_features, format_departments)
import pg8000.native as pg
import getpass


items = get_table('items')
# print(items)
features = format_features(items)
# print(features)

staff = get_table('staff')
departments = format_departments(staff)
departments = [department[0] for department in departments]
print(departments)

def populate_dim_departments():
    username = getpass.getuser()
    database = 'nc_sells_fridges'
    with pg.Connection(user=username, database=database) as conn:
        for department in departments:
            conn.run('INSERT INTO dim_department (department_name) VALUES (:department)', department=department)

populate_dim_departments()