from helpers import Database
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import psycopg

# DataBase
db = Database()

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

# DataBase
def create_lunch_menu_data():
    DB_CONFIG = {
        "dbname": "sunsindb",
        "user": "sunsin",
        "password": "mysecretpassword",
        "host": "localhost",
        "port": "5432"
    }

    conn = psycopg.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO lunch_menu(menu_name, member_name, dt) VALUES (%s, %s, %s);",
        (menu_name, member_name, dt)
    )

    conn.commit()
    cursor.close()

# Logic
if is_tapped_save_button:
    if menu_name and member_name and dt:
        db.insert_data(menu_name, member_name, dt)
#        create_lunch_menu_data()
        st.success('저장 완료!')
    else:
        st.warning('모든 값을 입력해주세요.')

# Statistic
st.subheader('통계')

df = pd.read_csv('./note/lunch_menu.csv')

start_idx = df.columns.get_loc('2025-01-07')
melted_df = df.melt(id_vars=['ename'], value_vars=df.columns[start_idx:-2], var_name='dt', value_name='menu')

not_na_df = melted_df[~melted_df['menu'].isin(['-', 'x', '<결석>'])]
gdf = not_na_df.groupby('ename')['menu'].count().reset_index()

# Matplotlib로 Bar Chart 그리기
fig, ax = plt.subplots()
gdf.plot(x='ename', y='menu', kind='bar', ax=ax)
ax.set_xticklabels(gdf['ename'], rotation=45)
st.pyplot(fig)
