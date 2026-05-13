# Country Music Lyrics NLP Extractor

**End-to-End NLP Pipeline Demo** — Turning messy, unstructured country song lyrics into structured, actionable insights.

Live demo built with Streamlit.

## Overview
This project demonstrates a complete information extraction pipeline:
- Ingest raw song lyrics
- Clean and preprocess noisy text (phonetic spellings, contractions, disfluencies)
- Perform Named Entity Recognition and custom entity extraction with SpaCy
- Detect themes using c-TF-IDF
- Deliver results through an interactive web app

## Features
- Interactive song selector
- Side-by-side view of original lyrics vs extracted entities
- Theme detection
- Clean, production-ready Streamlit interface

## Tech Stack
- **Python** • **SpaCy** (NER + preprocessing)
- **c-TF-IDF** (theme extraction)
- **pandas** • **Streamlit** (UI)
- Jupyter Notebooks (exploration)

## Project Structure
country-music-lyrics-nlp/
├── app.py                    # Main Streamlit application ← Run this
├── .streamlit/config.toml    # Streamlit settings
├── data/
│   ├── raw/                  # Original lyrics
│   └── processed/            # Extracted JSON
├── notebooks/                # Exploration & pipeline development
├── src/                      # Reusable modules (optional)
├── requirements.txt
└── README.md

## How to Run
```bash
# 1. Clone & navigate
cd country-music-lyrics-nlp

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py

Why This Project
Shows high-agency execution: taking messy real-world unstructured data → clean pipeline → polished, interactive tool.
Directly relevant to enterprise use cases involving text analytics, information extraction, and operational insights.
Built as a portfolio project alongside full-time analytics work.