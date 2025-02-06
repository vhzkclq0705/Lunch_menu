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

st.warning('데이터가 초기화 됐을 시에 클릭하세요.')
is_tapped_insert_button = st.button('Bulk Insert!')

# ----------Logic----------

if is_tapped_insert_button:
    total_cnt, true_cnt, false_cnt = csv_manager.insert_data()

    if total_cnt == true_cnt:
        st.success(f'모든 데이터를 성공적으로 삽입했습니다! -> 총 {total_cnt}건')
    else:
        st.error(f'총 {total_cnt}건 중 {false_cnt}건 삽입에 실패했습니다.')

db.close_connection()
