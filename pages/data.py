from helpers import *
import streamlit as st

db = Database()
statistic = Statistic_manager(db.select_data())

st.markdon('# Data')
st.sidebar.markdown('# Data')

inintial_df = statistic.get_initial_df()
st.table(initial_df)

db.close_connection()
