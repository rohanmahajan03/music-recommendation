import streamlit as st
import pandas as pd

# Inject background patterns HTML and CSS
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    
    .stApp {
        background-color: black;
        color: white;
        font-family: 'Roboto', sans-serif;
    }

    .stTextInput > div > input {
        color: red;
        background-color: white;
    }

    .stTextInput > div > label {
        color: white;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: white;
    }
    
    .stButton>button {
        color: black;
        background-color: white;
    }
    header, .main {
        padding-top: 0;
        margin-top: -50px;
    }
    
    footer {
        visibility: hidden;
    }
    
    .css-18ni7ap {
        visibility: hidden;
    }

    .background-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 10; 
        pointer-events: none; 
    }

    .left-pattern, .right-pattern {
        position: absolute;
        top: 0;
        bottom: 0;
        width: 27.00%;
    }

    .left-pattern {
        left: 0;
        background: repeating-linear-gradient(
            45deg,
            rgba(255,255,255,0.1),
            rgba(255,255,255,0.1) 10px,
            rgba(255,255,255,0.2) 10px,
            rgba(255,255,255,0.2) 20px
        );
    }

    .right-pattern {
        right: 0;
        background: repeating-linear-gradient(
            -45deg,
            rgba(255,255,255,0.1),
            rgba(255,255,255,0.1) 10px,
            rgba(255,255,255,0.2) 10px,
            rgba(255,255,255,0.2) 20px
        );
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="background-container"><div class="left-pattern"></div><div class="right-pattern"></div></div>', unsafe_allow_html=True)

st.title('🎵 Music Recommendation System')

st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)

st.header('Input a song of your choice:')
song_name = st.text_input('', placeholder='Type a song name here...')

class DataFunctions:
    def __init__(self):
        self.df = pd.read_csv("labeled_df.csv")

    def recommend_songs(self, song_name):
        input_track = song_name.lower()

        self.df['track_name_lower'] = self.df['track_name'].str.lower()
        self.df['track_genre_lower'] = self.df['track_genre'].str.lower()

        # Get the genre and song cluster of the input song
        input_genre = self.df.loc[self.df['track_name_lower'] == input_track, 'track_genre'].values[0]
        song_cluster = self.df.loc[self.df['track_name_lower'] == input_track, 'cluster'].values[0]

        recommended_rows = self.df.query('(track_genre_lower == @input_genre) & (cluster == @song_cluster)').sample(n=3)

        # display recommended songs
        if not recommended_rows.empty:
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.subheader("Here are some songs you might enjoy:")
            for index, row in recommended_rows.iterrows():
                st.write(f"**{row.track_name}** by {row.artists}")
        else:
            st.warning("No recommendations found. Please try another song.")

        return

data_functions = DataFunctions()

if len(song_name) >= 1:
    try:
        data_functions.recommend_songs(song_name)
    except:
        st.error("Sorry, the song you have selected is not in the database. Please try another.")
