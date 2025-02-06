from datetime import datetime
import psycopg
from config.db_config import db_config

# Class for Database
class Database:
    def __init__(self):
        self.conn = psycopg.connect(**db_config)
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=None):
        if params:
            self.cursor.executemany(query, params)
        else:
            self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, data):
        if isinstance(data, tuple):
            data = [data]

        data = [(menu_name.upper(), member_id, dt) for (menu_name, member_id, dt) in data]

        query = '''
        INSERT INTO lunch_menu (menu_name, member_id, dt)
        VALUES (%s, %s, %s)
        '''
        self.execute_query(query, data)

    def get_member_need_enter(self) -> list:
        query = '''
        select distinct
            m.name
        from
            member m
        inner join lunch_menu l
            on m.id = l.member_id 
        '''
        self.execute_query(query)

        return ', '.join([record[0] for record in self.cursor.fetchall()])

    def bulk_insert_homework(self, data):
        members = self.get_member_dict()
        query = '''
        INSERT INTO lunch_menu (menu_name, member_id, dt)
        VALUES (%s, %s, %s)
        '''
        
        results = []

        for _, row in data.iterrows():
            try:
                m_id = members[row['ename'].upper()]
                self.cursor.execute(query, (row['menu'], m_id, row['date']))
                results.append(1)
            except Exception as e:
                results.append(0)
        
        self.conn.commit()

        total_cnt = len(results)
        true_cnt = sum(results)
        false_cnt = total_cnt - true_cnt
        
        return (total_cnt, true_cnt, false_cnt)
                
    def select_data(self) -> list:
        query = '''
        SELECT
            menu_name,
            name,
            dt
        FROM lunch_menu l
        JOIN member m ON l.member_id = m.id
        '''
        self.execute_query(query)
        return self.cursor.fetchall()

    # TODO
    def delete_data(self):
        query = f'DELETE INTO lunch_menu'

    # TODO
    def update_data(self):
        query = f'UPDATE INTO lunch_menu'

    def get_member_dict(self) -> dict:
        query = '''
        SELECT jsonb_object_agg(name, id)
        FROM member;
        '''
        self.execute_query(query)
        return self.cursor.fetchone()[0]

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
