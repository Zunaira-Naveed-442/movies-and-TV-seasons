import streamlit as st
import random

# --- App Configuration ---
st.set_page_config(page_title="🎬 Ultimate Movie & Season Recommender", page_icon="🍿", layout="centered")

st.title("🎬 Ultimate Movie & Season Recommender")
st.write("Find the perfect movie or TV season for your mood or interest! 🍿")

# --- Expanded Dataset ---
recommendations = {
    "Action": {
        "Movies": [
            "John Wick", "Mad Max: Fury Road", "The Dark Knight", "Inception", "Gladiator",
            "Mission Impossible: Fallout", "Die Hard", "Black Panther", "Avengers: Endgame",
            "The Batman", "Top Gun: Maverick", "Skyfall", "Atomic Blonde", "The Equalizer", 
            "Taken", "The Raid", "Edge of Tomorrow", "The Bourne Ultimatum", "Tenet"
        ],
        "Seasons": [
            "The Boys", "Vikings", "Daredevil", "The Punisher", "Jack Ryan", 
            "Peacemaker", "Reacher", "24", "Arrow", "The Mandalorian", 
            "The Witcher", "The Falcon and the Winter Soldier", "Loki", "Hawkeye", "Andor"
        ]
    },
    "Romance": {
        "Movies": [
            "The Notebook", "La La Land", "Pride and Prejudice", "Me Before You", "Titanic",
            "Crazy Rich Asians", "To All the Boys I've Loved Before", "About Time", 
            "The Fault in Our Stars", "Love, Rosie", "Notting Hill", "A Walk to Remember", 
            "Letters to Juliet", "Pretty Woman", "Before Sunrise", "The Vow"
        ],
        "Seasons": [
            "Bridgerton", "Emily in Paris", "Modern Love", "Outlander", "Normal People", 
            "Virgin River", "The Summer I Turned Pretty", "Love Life", "You Me Her", 
            "Heartstopper", "Dash & Lily", "Crazy Ex-Girlfriend", "Gossip Girl", "Grey’s Anatomy"
        ]
    },
    "Comedy": {
        "Movies": [
            "The Hangover", "Superbad", "21 Jump Street", "Step Brothers", "Yes Man", 
            "Crazy Rich Asians", "The Intern", "The Other Guys", "We’re the Millers", 
            "Horrible Bosses", "Game Night", "Bridesmaids", "The 40-Year-Old Virgin", 
            "The Dictator", "The Nice Guys", "Tropic Thunder", "Dumb and Dumber"
        ],
        "Seasons": [
            "Brooklyn Nine-Nine", "The Office", "Friends", "How I Met Your Mother", 
            "Parks and Recreation", "Ted Lasso", "New Girl", "Scrubs", "The Big Bang Theory",
            "Superstore", "Community", "Modern Family", "Schitt’s Creek", "Young Sheldon"
        ]
    },
    "Thriller": {
        "Movies": [
            "Se7en", "Gone Girl", "Shutter Island", "The Prestige", "Nightcrawler", 
            "Memento", "Fight Club", "Prisoners", "The Girl with the Dragon Tattoo", 
            "The Sixth Sense", "Oldboy", "Parasite", "The Invisible Man", "Zodiac", 
            "The Others", "A Quiet Place", "Panic Room"
        ],
        "Seasons": [
            "Breaking Bad", "Mindhunter", "You", "True Detective", "Ozark", 
            "Luther", "The Night Agent", "The Blacklist", "Money Heist", 
            "Narcos", "The Killing", "Bodyguard", "Dexter", "Mr. Robot", "The Outsider"
        ]
    },
    "Sci-Fi": {
        "Movies": [
            "Interstellar", "The Matrix", "Blade Runner 2049", "Dune", "Arrival", 
            "Edge of Tomorrow", "Ex Machina", "Star Wars: Rogue One", "Avatar", 
            "Minority Report", "Inception", "Oblivion", "Looper", "District 9", 
            "The Martian", "Elysium", "I, Robot"
        ],
        "Seasons": [
            "Black Mirror", "Stranger Things", "Westworld", "The Expanse", 
            "Altered Carbon", "Foundation", "The 100", "Lost in Space", 
            "The Mandalorian", "Halo", "Dark", "Doctor Who", "Fringe", "The Peripheral"
        ]
    },
    "Horror": {
        "Movies": [
            "The Conjuring", "Hereditary", "It", "A Quiet Place", "The Ring", 
            "Insidious", "Get Out", "Annabelle", "The Babadook", "Sinister", 
            "The Nun", "Smile", "The Blair Witch Project", "Us", "Evil Dead Rise", 
            "Barbarian", "The Others"
        ],
        "Seasons": [
            "The Haunting of Hill House", "Marianne", "American Horror Story", 
            "The Walking Dead", "Penny Dreadful", "The Fall of the House of Usher", 
            "The Haunting of Bly Manor", "The Mist", "Slasher", "From", "Chucky", 
            "Fear the Walking Dead", "Midnight Mass"
        ]
    },
    "Drama": {
        "Movies": [
            "Forrest Gump", "The Shawshank Redemption", "The Pursuit of Happyness", 
            "A Beautiful Mind", "The Green Mile", "The Social Network", 
            "Good Will Hunting", "Cast Away", "Whiplash", "The Imitation Game", 
            "12 Years a Slave", "Marriage Story", "The King’s Speech", "The Revenant"
        ],
        "Seasons": [
            "Breaking Bad", "The Crown", "This Is Us", "The Morning Show", 
            "Mad Men", "Suits", "The Good Doctor", "Euphoria", "Better Call Saul", 
            "House of Cards", "Big Little Lies", "Succession", "Billions", "Severance"
        ]
    },
    "Animation": {
        "Movies": [
            "Toy Story", "Spirited Away", "Zootopia", "Inside Out", "Finding Nemo", 
            "Coco", "Up", "The Lion King", "How to Train Your Dragon", "The Incredibles", 
            "Frozen", "Encanto", "Ratatouille", "Wall-E", "Turning Red", "Moana"
        ],
        "Seasons": [
            "Avatar: The Last Airbender", "The Legend of Korra", "Rick and Morty", 
            "BoJack Horseman", "Arcane", "Castlevania", "Adventure Time", "Blue Eye Samurai", 
            "Samurai Jack", "Cyberpunk: Edgerunners", "Invincible", "The Simpsons", 
            "Family Guy", "Futurama"
        ]
    }
}

# --- Flatten all items for keyword search ---
all_titles = []
for genre, types in recommendations.items():
    for category, titles in types.items():
        for t in titles:
            all_titles.append({"Genre": genre, "Type": category, "Title": t})

# --- Smart Search ---
st.subheader("🔍 Search by Mood or Keyword")
query = st.text_input("Enter any mood, keyword or genre (e.g., 'romantic comedy', 'dark thriller', 'space adventure')")

if query:
    q = query.lower()
    results = [item for item in all_titles if q in item["Genre"].lower() or q in item["Title"].lower()]
    if results:
        st.success(f"Found {len(results)} results for **'{query}'**:")
        for idx, r in enumerate(results[:20], 1):
            st.markdown(f"{idx}. **{r['Title']}** — *{r['Genre']} {r['Type']}*")
    else:
        st.warning("No matching titles found. Try another keyword!")

st.write("---")

# --- Browse by Genre ---
st.subheader("🎭 Browse by Genre")
genre = st.selectbox("Select a genre:", list(recommendations.keys()))
content_type = st.radio("Choose Type:", ["Movies", "Seasons"])

if genre and content_type:
    items = recommendations[genre][content_type]
    random.shuffle(items)
    st.write(f"🎥 **Top {content_type} in {genre}:**")
    for i, title in enumerate(items[:10], 1):
        st.markdown(f"{i}. **{title}**")

st.write("---")
st.caption("Developed with ❤️ using Streamlit — Expanded Smart Recommender 🎬")


