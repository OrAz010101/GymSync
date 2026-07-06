streamlit
pandas
streamlit-folium
folium
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="GymSync Pro", layout="wide")

# נתונים לדוגמה (בעתיד יגיעו מ-Google Sheets)
data = {
    'שם': ['אייקון נתניה', 'ספייס תל אביב', 'הולמס פלייס חיפה', 'גרייט שייפ ירושלים'],
    'עיר': ['נתניה', 'תל אביב', 'חיפה', 'ירושלים'],
    'lat': [32.3215, 32.0853, 32.7940, 31.7683],
    'lon': [34.8532, 34.7818, 34.9896, 35.2137],
    'עומס': [30, 85, 10, 50]
}
df = pd.DataFrame(data)

st.title("🏋️‍♂️ GymSync - הווייז של המכון")

# בחירת עיר
city = st.selectbox("איפה אתה מתאמן היום?", df['עיר'].unique())
filtered_df = df[df['עיר'] == city]

# יצירת מפה
m = folium.Map(location=[filtered_df.lat.mean(), filtered_df.lon.mean()], zoom_start=13)
for _, row in filtered_df.iterrows():
    color = 'green' if row['עומס'] < 50 else 'red'
    folium.Marker([row['lat'], row['lon']], 
                  popup=row['שם'], 
                  icon=folium.Icon(color=color)).add_to(m)

# הצגת המפה והנתונים
col1, col2 = st.columns([1, 1])
with col1:
    st_folium(m, width=500)
with col2:
    st.write(f"### מכונים ב{city}:")
    for _, row in filtered_df.iterrows():
        st.write(f"**{row['שם']}** - עומס: {row['עומס']}%")
        if st.button(f"דווח על עומס ב-{row['שם']}", key=row['שם']):
            st.toast("דיווחך נשלח! תודה על העזרה לקהילה 🦾")