import psycopg

# Class for Database
class Database:
    def __init__(self):
        self.db_config = {
            "dbname": "sunsindb",
            "user": "sunsin",
            "password": "mysecretpassword",
            "host": "localhost",
            "port": "5432"
        }
        self.conn = psycopg.connect(**self.db_config)
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.excute(query)
        self.conn.commit()

    def insert_data(self, menu_name, member_name, dt):
        query = '''
        INSERT INTO lunch_menu (menu_name, member_name, dt)
        VALUES (%s, %s, %s)
        '''
        self.execute_query(query, (menu_name, member_name, dt))

    # TODO
    def select_data(self):
        query = f'SELECT INTO lunch_menu'

    # TODO
    def delete_data(self):
        query = f'DELETE INTO lunch_menu'        
    
    # TODO
    def update_data(self):
        query = f'UPDATE INTO lunch_menu'

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

