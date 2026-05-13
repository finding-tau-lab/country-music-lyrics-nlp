import streamlit as st
import pandas as pd
from pathlib import Path
import json

st.set_page_config(page_title="Country Lyrics NLP Extractor", layout="wide")
st.title("🎸 Country Music Lyrics Information Extractor")
st.markdown("**NLP Pipeline Demo** — Turning unstructured lyrics into structured insights")

# Load data
@st.cache_data
def load_data():
    data_file = Path("data/processed/lyrics_extracted.json")
    if data_file.exists():
        return pd.read_json(data_file)
    else:
        st.error("Processed data not found. Run the notebook first.")
        return pd.DataFrame()

df = load_data()

if not df.empty:
    song_choice = st.selectbox("Select a song", df['song'].unique())
    song_data = df[df['song'] == song_choice].iloc[0]
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original Lyrics")
        st.write(song_data['lyrics'])
    
    with col2:
        st.subheader("Extracted Information")
        for ent in song_data['extracted_info']:
            st.write(f"**{ent[0]}** → {ent[1]}")
        
        st.subheader("Theme")
        st.success(song_data.get('theme', 'N/A'))

else:
    st.info("No processed data yet. Go back to the notebook and run the extraction pipeline.")

st.caption("Built as a portfolio project to demonstrate NLP + Information Extraction skills")