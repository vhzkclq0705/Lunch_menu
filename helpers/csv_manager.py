import pandas as pd
import os

# Class for csv
class CSV_manager:
    def __init__(self, db):
        self.db = db

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_file_path = os.path.join(base_dir, 'note', 'lunch_menu.csv')

        self.df = pd.read_csv(csv_file_path)

    def extract_data(self) -> list:
        member_dict = self.db.get_member_dict()
        start_idx = self.df.columns.get_loc('2025-01-07')

        extracted_data = (
            self.df.melt(
                id_vars=['ename'],
                value_vars=self.df.columns[start_idx:-2],
                var_name='date',
                value_name='menu'
            )
            .query("menu != '-'")
            .reindex(columns=['menu', 'ename', 'date'])
        )

        extracted_data['member_id'] = extracted_data['ename'].str.upper().map(member_dict)

        return list(extracted_data[['menu', 'member_id', 'date']].itertuples(index=False, name=None))

    def insert_data(self):
        data = self.extract_data()
        self.db.insert_data(data)
