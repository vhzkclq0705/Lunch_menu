from helpers import *
import streamlit as st

# ----------Helper Class----------

db = Database()

# ----------Properties----------

member_dict = db.get_member_dict()
member_need_enter = db.get_member_need_enter()
error_message = "삽입 실패! 중복된 데이터이거나 시스템 에러가 발생했습니다."

# ----------UI----------

# Title
st.title('점심기록장')
st.sidebar.markdown('Main Page')

# Image
st.write("""
![img](https://mblogthumb-phinf.pstatic.net/MjAxNzA4MDFfMjgg/MDAxNTAxNTk3MjMyMzE1.lzhfDRW62nO2az__0v9ww-eKlbMyMwI7Knsev0FZp2Ig.0uyl5Cvhb5SLLgsCAfqy_PyMkwc42YonwRhPhrGGBaEg.JPEG.enviableb/%EC%84%BC%EA%B3%BC_%EC%B9%98%ED%9E%88%EB%A1%9C%EC%9D%98_%ED%96%89%EB%B0%A9%EB%B6%88%EB%AA%85_Spirited_Away_2001_720p_HDTV_x264-somedouches.mkv_20170801_222503.470.jpg?type=w800)
""")

# Input
menu_name = st.text_input('메뉴 이름', placeholder='ex) 설렁탕')

member_name = st.selectbox(
    "작성자 선택",
    list(member_dict.keys()),
    index=member_dict['JERRY']%len(member_dict)
)
member_id = member_dict[member_name]

dt = st.date_input('날짜')

is_tapped_save_button = st.button('저장')

st.markdown('## 입력 안 한 사람 확인')
is_tapped_check_button = st.button('확인')

# ----------Logic----------

# Save Button
if is_tapped_save_button:
    if menu_name and member_name and dt:
        try:
            db.insert_data((menu_name, member_id, dt))
            st.success('저장 완료!')
        except Exception as e:
            st.error(error_message)
            st.error(f'error message: {str(e)}')
    else:
        st.warning('모든 값을 입력해주세요.')

# Check Button
if is_tapped_check_button:
    print(member_need_enter)
    if member_need_enter:
        st.warning(member_need_enter)
    else:
        st.success('모두 금일 점심을 입력하였습니다!')

db.close_connection()
