import streamlit as st
import pandas as pd

st.set_page_config(page_title="GymSync", layout="wide")

st.title("🏋️‍♂️ GymSync")
st.write("ברוך הבא למערכת ניהול העומס בחדרי הכושר.")

# נתוני בסיס
data = {
    'שם המכון': ['אייקון נתניה', 'ספייס תל אביב'],
    'עומס': [40, 90]
}
df = pd.DataFrame(data)

# תצוגה
for index, row in df.iterrows():
    st.write(f"### {row['שם המכון']}")
    st.progress(row['עומס'] / 100)
    st.write(f"עומס נוכחי: {row['עומס']}%")