import psycopg
from config.db_config import db_config

# Class for Database
class Database:
    def __init__(self):
        self.conn = psycopg.connect(**db_config)
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, menu_name, member_name, dt):
        menu_name = menu_name.upper()
        member_name = member_name.upper()

        query = '''
        INSERT INTO lunch_menu (menu_name, member_name, dt)
        VALUES (%s, %s, %s)
        '''
        self.execute_query(query, (menu_name, member_name, dt))

    def select_data(self) -> list:
        query = '''
        SELECT menu_name, member_name, dt
        FROM lunch_menu
        ORDER BY dt DESC
        '''
        self.execute_query(query)
        return self.cursor.fetchall()

    # TODO
    def delete_data(self):
        query = f'DELETE INTO lunch_menu'

    # TODO
    def update_data(self):
        query = f'UPDATE INTO lunch_menu'

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

