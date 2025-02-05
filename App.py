from helpers import *
import matplotlib.pyplot as plt
import streamlit as st

# Class from helper files
db = Database()
statistic = Statistic_manager(db.select_data())
csv_manager = CSV_manager(db)

# Properties
error_message = "삽입 실패! 중복된 데이터이거나 시스템 에러가 발생했습니다."

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
        try:
            db.insert_data(menu_name, member_name, dt)
            st.success('저장 완료!')
        except Exception as e:
            st.error(error_message)
            st.error(f'error message: {str(e)}')
    else:
        st.warning('모든 값을 입력해주세요.')

# Select data
initial_df = statistic.get_initial_df()

st.write('## 확인')
st.table(initial_df)

# Statistic data
grouped_df = statistic.get_grouped_df()

st.write('## 통계')
if not grouped_df.empty:
    fig, ax = plt.subplots()
    grouped_df.plot(x='member_name', y='menu', kind='bar', ax=ax)
    ax.set_xticklabels(grouped_df['member_name'], rotation=45)
    st.pyplot(fig)
else:
    st.warning('데이터가 존재하지 않아 통계를 확인할 수 없습니다.')


# Insert all data from .csv
st.write('## Bulk Insert')
is_tapped_insert_button = st.button('Bulk Insert!')

if is_tapped_insert_button:
    try:
        csv_manager.insert_data()
        st.success('모든 데이터를 성공적으로 삽입했습니다!')
    except Exception as e:
        st.error(error_message)
        st.error(f'error message: {str(e)}')

# Disconnect
db.close_connection()
