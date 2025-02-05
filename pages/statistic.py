from helpers import *
import matplotlib.pyplot as plt
import streamlit as st

db = Database()
statistic = Statistic_manager(db.select_data())

st.markdown('# Statistic')
st.sidebar.markdown('# Statistic')

groupded_df = statistic.get_grouped_df()
if not grouped_df.empty:
    fig, ax = plt.subplots()
    grouped_df.plot(x='member_name', y='menu', kind='bar', ax=ax)
    ax.set_xticklabels(grouped_df['member_name'], rotation=45)
    st.pyplot(fig)
else:
    st.warning('데이터가 존재하지 않아 통계를 확인할 수 없습니다.')
