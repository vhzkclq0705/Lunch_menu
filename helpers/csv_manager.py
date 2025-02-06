import pandas as pd
import os

# Class for csv
class CSV_manager:
    def __init__(self, db):
        self.db = db

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_file_path = os.path.join(base_dir, 'note', 'lunch_menu.csv')

        self.df = pd.read_csv(csv_file_path)

    def extract_data(self) -> pd.DataFrame:
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

        return extracted_data

    def insert_data(self):
        data = self.extract_data()
        total_cnt, true_cnt, false_cnt = self.db.bulk_insert_homework(data)

        return (total_cnt, true_cnt, false_cnt)
