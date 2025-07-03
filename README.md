# Emotion-Based Music Recommender

This is a machine learning-based system that recommends songs based on the user's emotional input in text form. It supports both **English** and **Telugu** songs and offers an interactive frontend using **Streamlit**.

## Features

- Takes user emotion as **text input** or from a list of options.
- Classifies the emotion using a **LinearSVC** model.
- Recommends songs that match the emotional context.
- Supports **English** and **Telugu** music datasets.
- Simple and interactive **Streamlit UI**.

## Tech Stack

- Python
- Scikit-learn
- Pandas
- Streamlit
- Custom datasets for songs

## Project Structure

<pre> Emotion-Based Music Recommender/ │ ├── cluster_emotions.ipynb # Clusters similar emotions ├── predict_emotions.ipynb # Trains emotion classifier ├── recommend_music.ipynb # Recommends songs based on emotion ├── app.py # Streamlit app ├── songs_dataset_en.csv # English songs dataset ├── songs_dataset_te.csv # Telugu songs dataset ├── original_datasets/ # Raw emotion and GoEmotions datasets ├── models/ # (Optional) Saved models └── README.md </pre>

## Datasets

- `songs_dataset_en.csv` - English songs labeled by emotion
- `songs_dataset_te.csv` - Telugu songs labeled by emotion
- `goemotions_*.csv` - Used for training emotion classifier

## Author

**Vedulla Sai Vardhan**  
[VSaiVardhan](https://github.com/VSaiVardhan)
