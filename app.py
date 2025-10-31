import streamlit as st
import random
import requests
from bs4 import BeautifulSoup

# --- Page config ---
st.set_page_config(page_title="🎬 Trending & Smart Movie Recommender", page_icon="🍿", layout="centered")

st.title("🎬 Trending & Smart Movie Recommender")
st.write("Discover **trending, new-release movies** and find films based on your mood or interest! 🍿")

# --- Function to fetch trending/new movies from web ---
@st.cache_data(ttl=3600)
def fetch_trending_movies():
    url = "https://editorial.rottentomatoes.com/guide/best-new-movies/"  # Example source
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        items = []
        # Parse titles (this depends on site structure; this is example)
        for h3 in soup.select("h3.article_movie_title"):
            title = h3.get_text().strip()
            items.append(title)
        return list(dict.fromkeys(items))  # unique
    except Exception as e:
        st.error(f"Error fetching trending movies: {e}")
        return []

trending_list = fetch_trending_movies()

# --- Show trending / new releases ---
st.subheader("🔥 Trending / New Release Movies")
if trending_list:
    # limit to e.g. first 20
    for idx, t in enumerate(trending_list[:20], start=1):
        st.markdown(f"{idx}. **{t}**")
else:
    st.write("Could not fetch trending movies at this time. Please try again later.")

st.write("---")

# --- Manual dataset for browse by genre (fallback) ---
recommendations = {
    "Action": ["John Wick", "Mad Max: Fury Road", "Inception", "Die Hard", "Black Panther", "Mission Impossible – Fallout"],
    "Romance": ["The Notebook", "La La Land", "Pride & Prejudice", "Titanic", "Crazy Rich Asians", "About Time"],
    "Comedy": ["The Hangover", "Superbad", "Step Brothers", "Yes Man", "21 Jump Street", "The Intern"],
    "Thriller": ["Se7en", "Gone Girl", "Shutter Island", "Memento", "Fight Club", "Nightcrawler"],
    "Sci-Fi": ["Interstellar", "The Matrix", "Blade Runner 2049", "Dune", "Arrival", "Edge of Tomorrow"]
}

# --- Search functionality ---
st.subheader("🔍 Search by interest or keyword")
query = st.text_input("Enter mood, genre or keyword (e.g., 'space adventure', 'funny movie', 'romantic comedy')")

if query:
    q = query.lower()
    results = []
    # search in trending list
    for title in trending_list:
        if q in title.lower():
            results.append({"Title": title, "Source": "Trending"})
    # search in manual dataset
    for genre, titles in recommendations.items():
        for t in titles:
            if q in t.lower() or q in genre.lower():
                results.append({"Title": t, "Source": f"{genre} (manual)"})
    # remove duplicates
    seen = set()
    filtered = []
    for r in results:
        if r["Title"] not in seen:
            seen.add(r["Title"])
            filtered.append(r)
    if filtered:
        st.success(f"Found {len(filtered)} titles related to '{query}':")
        for idx, r in enumerate(filtered[:15], 1):
            st.markdown(f"{idx}. **{r['Title']}** — *{r['Source']}*")
    else:
        st.warning("No matching titles found. Try a different keyword.")

st.write("---")

# --- Browse by Genre fallback ---
st.subheader("🎭 Browse by Genre (manual dataset)")
genre = st.selectbox("Select a genre:", list(recommendations.keys()))
if genre:
    titles = recommendations[genre]
    random.shuffle(titles)
    st.write(f"Top picks in **{genre}**:")
    for i, t in enumerate(titles[:6], 1):
        st.markdown(f"- {i}. **{t}**")

st.caption("Developed with ❤️ using Streamlit — Live trends + smart search 🎬")

