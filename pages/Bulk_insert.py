from helpers import *
import streamlit as st

# ----------Helper Class----------

db = Database()
csv_manager = CSV_manager(db)

# ----------Properties----------

error_message = "삽입 실패! 중복된 데이터이거나 시스템 에러가 발생했습니다."

# ----------UI----------

st.markdown('# Bulk Insert')
st.sidebar.markdown('# Bulk Insert')

is_tapped_insert_button = st.button('Bulk Insert!')

# ----------Logic----------

if is_tapped_insert_button:
    try:
        csv_manager.insert_data()
        st.success('모든 데이터를 성공적으로 삽입했습니다!')
    except Exception as e:
        st.error(error_message)
        st.error(f'error message: {str(e)}')

db.close_connection()
