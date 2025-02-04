from helpers import *
import matplotlib.pyplot as plt
import streamlit as st

# Class from helper files
db = Database()
statistic = Statistic_manager(db.select_data())
csv_manager = CSV_manager(db)

# Title
st.title('점심기록장')

# Image
st.write("""
![img](https://mblogthumb-phinf.pstatic.net/MjAxNzA4MDFfMjgg/MDAxNTAxNTk3MjMyMzE1.lzhfDRW62nO2az__0v9ww-eKlbMyMwI7Knsev0FZp2Ig.0uyl5Cvhb5SLLgsCAfqy_PyMkwc42YonwRhPhrGGBaEg.JPEG.enviableb/%EC%84%BC%EA%B3%BC_%EC%B9%98%ED%9E%88%EB%A1%9C%EC%9D%98_%ED%96%89%EB%B0%A9%EB%B6%88%EB%AA%85_Spirited_Away_2001_720p_HDTV_x264-somedouches.mkv_20170801_222503.470.jpg?type=w800)

""")

# Input
menu_name = st.text_input('메뉴 이름', placeholder='ex) 설렁탕')
member_name = st.text_input('작성자', placeholder='ex) Jerry', value='Jerry')
dt = st.date_input('날짜')
is_tapped_save_button = st.button('저장')

# Logic - Save button
if is_tapped_save_button:
    if menu_name and member_name and dt:
        db.insert_data(menu_name, member_name, dt)
        st.success('저장 완료!')
    else:
        st.warning('모든 값을 입력해주세요.')

# Select data
initial_df = statistic.get_initial_df()

st.write('## 확인')
st.table(initial_df)

# Statistic data
grouped_df = statistic.get_grouped_df()
fig, ax = plt.subplots()
grouped_df.plot(x='member_name', y='menu', kind='bar', ax=ax)
ax.set_xticklabels(grouped_df['member_name'], rotation=45)

st.write('## 통계')
st.pyplot(fig)

# Insert all data from .csv
st.write('## Bulk Insert')
is_tapped_insert_button = st.button('Insert!')

if is_tapped_insert_button:
   csv_manager.insert_data()
   st.success('성공!')

# Disconnect
db.close_connection()
