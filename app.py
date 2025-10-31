import streamlit as st
import random

# --- App Configuration ---
st.set_page_config(page_title="Movie & Season Recommender", page_icon="🎬", layout="centered")

st.title("🎬 Movie & Season Recommender")
st.write("Get personalized movie and TV season suggestions based on your interests!")

# --- Sample Dataset ---
recommendations = {
    "Action": {
        "Movies": ["Mad Max: Fury Road", "John Wick", "The Dark Knight", "Inception", "Gladiator"],
        "Seasons": ["The Boys", "Daredevil", "The Punisher", "Vikings", "Peacemaker"]
    },
    "Romance": {
        "Movies": ["The Notebook", "Pride and Prejudice", "La La Land", "Me Before You", "Titanic"],
        "Seasons": ["Bridgerton", "Emily in Paris", "Outlander", "Modern Love", "Normal People"]
    },
    "Comedy": {
        "Movies": ["The Hangover", "Superbad", "21 Jump Street", "Crazy Rich Asians", "Step Brothers"],
        "Seasons": ["Brooklyn Nine-Nine", "The Office", "Friends", "How I Met Your Mother", "Ted Lasso"]
    },
    "Thriller": {
        "Movies": ["Se7en", "Gone Girl", "Shutter Island", "The Prestige", "Nightcrawler"],
        "Seasons": ["Breaking Bad", "Mindhunter", "You", "True Detective", "Ozark"]
    },
    "Sci-Fi": {
        "Movies": ["Interstellar", "The Matrix", "Blade Runner 2049", "Dune", "Arrival"],
        "Seasons": ["Black Mirror", "Stranger Things", "Westworld", "The Expanse", "Altered Carbon"]
    }
}

# --- User Inputs ---
genre = st.selectbox("🎭 Select a genre you like:", list(recommendations.keys()))
content_type = st.radio("📺 What do you want to watch?", ["Movies", "Seasons"])
mood = st.text_input("💭 (Optional) Describe your mood (e.g., adventurous, romantic, funny)")

# --- Generate Recommendations ---
if st.button("🎥 Get Recommendations"):
    choices = recommendations[genre][content_type]
    random.shuffle(choices)
    st.subheader(f"Top {content_type} for you:")
    for item in choices[:3]:
        st.markdown(f"- **{item}**")

    if mood:
        st.info(f"Since you're feeling *{mood}*, you might also enjoy exploring more {genre.lower()} {content_type.lower()}!")

st.write("---")
st.caption("Developed with ❤️ using Streamlit")
