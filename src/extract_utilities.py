import pg8000.native as pg
import getpass


def get_table(table_name, database):
    username = getpass.getuser()
    with pg.Connection(user=username, database=database) as conn:
        data = conn.run(f'SELECT * FROM {pg.identifier(table_name)}')
        columns_title = [column['name'] for column in conn.columns]

        final_data = []
        for row in data:
            dict_row = {key: value for key, value in zip(columns_title, row)}
            final_data.append(dict_row)

        return final_data
