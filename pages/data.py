from helpers import *
import streamlit as st

# ----------Helper Class----------

db = Database()
statistic = Statistic_manager(db.select_data())

# ----------Properties----------

initial_df = statistic.get_initial_df()

# ----------UI----------

st.markdown('# Data')
st.sidebar.markdown('# Data')

st.table(initial_df)

# ---------Logic----------

db.close_connection()
