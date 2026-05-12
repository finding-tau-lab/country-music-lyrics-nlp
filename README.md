# Country Music Lyrics NLP Parser & Information Extractor

**End-to-end NLP pipeline for information extraction from unstructured song lyrics.**

Built as a portfolio project to demonstrate skills in:
- Handling unstructured text data
- Named Entity Recognition (NER)
- Rule-based + custom entity extraction
- Data processing pipelines
- Reproducible Python workflows

## Project Goals
- Ingest raw lyrics
- Clean and preprocess text
- Extract structured information (Song Title, Artist, Themes, Key Elements)
- Output clean JSON for downstream use
- Build toward a deployable demo (Streamlit planned)

## Technologies Used
- Python, pandas, spaCy
- Jupyter Notebooks
- Git + GitHub

## Project Structure
country-music-lyrics-nlp/
├── data/
│   ├── raw/              # Original lyrics JSON
│   └── processed/        # Extracted structured data
├── notebooks/
│   └── 01_data_exploration.ipynb
├── src/                  # Future scripts
├── .venv/                # Virtual environment
└── README.md

## Quick Start
```bash
python -m venv venv
venv\Scripts\activate
pip install pandas spacy matplotlib seaborn
python -m spacy download en_core_web_sm

Results
Successfully extracts Song Title, Artist, Themes, and Key Elements from lyrics with rule-based + spaCy pipeline.