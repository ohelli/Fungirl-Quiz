# Fungirl Quiz App 🍄

A fun personality quiz built with Streamlit to determine if you're a Fungirl, Becky, or Peter!

## Features

- **Interactive Quiz**: Answer 5 questions with A, B, or C options
- **Personality Types**: Get classified as Fungirl, Becky, or Peter
- **Visual Results**: Beautiful pie chart showing your personality breakdown
- **Result Images**: Personalized images based on your quiz result
- **German Interface**: Fully localized in German

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   streamlit run app.py
   ```

3. Open your browser to the provided local URL (usually `http://localhost:8501`)

## Required Files

Make sure you have these image files in the `images/` folder:
- `images/Quiz-Banner.png` - Main banner image
- `images/Fungirl-Result.png` - Result image for Fungirl type
- `images/Becky-Result.png` - Result image for Becky type  
- `images/Peter-Result.png` - Result image for Peter type

## Quiz Logic

The quiz uses a mapping system where each question's A, B, C answers correspond to different personality types. Your final result is determined by which type you selected most frequently across all 5 questions.

## Technologies Used

- **Streamlit** - Web app framework
- **Matplotlib** - Pie chart visualization
- **Pandas** - Data processing

Enjoy discovering your personality type! 🚀
