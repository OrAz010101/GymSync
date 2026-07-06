import streamlit as st
import pandas as pd

# הגדרת עיצוב דף
st.set_page_config(page_title="GymSync", page_icon="💪", layout="centered")

# כותרת ראשית
st.title("🏋️‍♂️ GymSync")
st.markdown("### המדריך החכם לעומס בחדרי כושר")

# בסיס נתונים פנימי (בהמשך נחבר ל-Google Sheets)
gyms = {
    'אייקון נתניה': {'עומס': 30, 'ציוד': 5, 'תיאור': 'מכון חדש, המון מכונות'},
    'ספייס תל אביב': {'עומס': 85, 'ציוד': 4, 'תיאור': 'עמוס מאוד בשעות הערב'},
    'הולמס פלייס חיפה': {'עומס': 10, 'ציוד': 2, 'תיאור': 'ציוד ישן, דורש שיפוץ'}
}

# בחירת סניף
selected_gym = st.selectbox("איזה מכון מעניין אותך?", list(gyms.keys()))

# הצגת נתונים
gym = gyms[selected_gym]

# תצוגה גרפית של עומס
st.write(f"### סטטוס: {selected_gym}")
st.progress(gym['עומס'] / 100)
st.write(f"רמת עומס: {gym['עומס']}%")

# דירוג ציוד
st.write(f"**רמת ציוד:** {'⭐' * gym['ציוד']} ({gym['ציוד']}/5)")
st.info(f"💡 הערה: {gym['תיאור']}")

# קריאה לפעולה (מה שהופך את זה לאפליקציה חברתית)
st.write("---")
st.write("### איך המכון עכשיו?")
col1, col2 = st.columns(2)
if col1.button("ריק יחסית 🟢"):
    st.success("תודה! הדיווח עודכן.")
if col2.button("מפוצץ! 🔴"):
    st.error("דיווחת שהמקום עמוס, תודה שעזרת לאחרים!")
