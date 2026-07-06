import streamlit as st
import pandas as pd

st.set_page_config(page_title="GymSync", page_icon="🏋️‍♂️", layout="wide")

st.title("🏋️‍♂️ GymSync")
st.subheader("ברוכים הבאים למערכת ניהול האימונים")

branches = ['תל אביב', 'חיפה', 'ירושלים', 'ראשון לציון', 'אילת']
selected_branch = st.selectbox("בחר סניף:", branches)

st.write("---")
st.success(f"מחובר כעת לסניף: {selected_branch}")

st.info("האפליקציה באוויר! כאן נוכל להוסיף את כל הפיצ'רים בהמשך (שעות פתיחה, עומס, הרשמה לאימונים ועוד).")