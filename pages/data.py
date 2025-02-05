from helpers import *
import streamlit as st

# ----------Helper Class----------

db = Database()
statistic = Statistic_manager(db.select_data())

# ----------UI----------

st.markdown('# Data')
st.sidebar.markdown('# Data')

inintial_df = statistic.get_initial_df()
st.table(initial_df)

# ---------Logic----------

db.close_connection()
