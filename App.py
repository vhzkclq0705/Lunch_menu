import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("""
# 천하제일 점심 자랑 대회

![img](https://mblogthumb-phinf.pstatic.net/MjAxNzA4MDFfMjgg/MDAxNTAxNTk3MjMyMzE1.lzhfDRW62nO2az__0v9ww-eKlbMyMwI7Knsev0FZp2Ig.0uyl5Cvhb5SLLgsCAfqy_PyMkwc42YonwRhPhrGGBaEg.JPEG.enviableb/%EC%84%BC%EA%B3%BC_%EC%B9%98%ED%9E%88%EB%A1%9C%EC%9D%98_%ED%96%89%EB%B0%A9%EB%B6%88%EB%AA%85_Spirited_Away_2001_720p_HDTV_x264-somedouches.mkv_20170801_222503.470.jpg?type=w800)
""")

df = pd.read_csv('./note/lunch_menu.csv')

start_idx = df.columns.get_loc('2025-01-07')
melted_df = df.melt(id_vars=['ename'], value_vars=df.columns[start_idx:-2], var_name='dt', value_name='menu')

not_na_df = melted_df[~melted_df['menu'].isin(['-', 'x', '<결석>'])]
gdf = not_na_df.groupby('ename')['menu'].count().reset_index()

# Matplotlib로 Bar Chart 그리기
fig, ax = plt.subplots()
gdf.plot(x='ename', y='menu', kind='bar', ax=ax)
st.pyplot(fig)
