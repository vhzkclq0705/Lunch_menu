import pandas as pd
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
            self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, menu_name, member_name, dt):
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

# Class for Statistic
class Statistic:
    def __init__(self, data):
        self.data = data
        self.initial_df = pd.DataFrame(data, columns=['menu_name', 'member_name', 'date'])

        self.melted_df = self.initial_df.melt(
            id_vars=['member_name'],
            value_vars=['date'],
            value_name='menu'
        )

        self.grouped_df = self.melted_df.groupby('member_name')['menu'].count().reset_index()
        
    def get_initial_df(self) -> pd.DataFrame:
        return self.initial_df

    def get_grouped_df(self) -> pd.DataFrame:
        return self.grouped_df

# Class for csv
class CSV_manager:
    def __init__(self, db):
        self.db = db
        self.df = pd.read_csv('./note/lunch_menu.csv')

    def extract_data(self) -> list:
        start_idx = self.df.columns.get_loc('2025-01-07')
        extracted_data = (
            self.df.melt(id_vars=['ename'], value_vars=self.df.columns[start_idx:-2], var_name='date', value_name='menu')
            .query("menu != '-'")
            .to_records(index=False)
        )
        
        return extracted_data

    def insert_data(self):
        data = self.extract_data()
        for (member_name, date, menu) in data:
            self.db.insert_data(menu, member_name, date)
