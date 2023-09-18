import pandas as pd
import streamlit as st
import urllib
import openpyxl

# Read the excel file
data = pd.read_excel('songs.xlsx')

# Create genre and territory dictionaries
genres = data['Major Genre'].unique()
territories = data['PMO'].unique()

# Create a dictionary to store songs by genre and territory
songs_by_genre_and_territory = {genre: {territory: [] for territory in territories} for genre in genres}

# Populate the dictionary
for _, row in data.iterrows():
    genre = row['Major Genre']
    territory = row['PMO']
    song = {
        'Artist': row['Artist Display Name'],
        'Title': row['Product Display Title'],
        'GPID': row['GPID'],
        'Category': row['Category'],
        'Product Type': row['Product Type'],
        'Sub Type': row['Sub Type'],
        'Duration': row['Total Playing Time'],
        'Explicit Rating': row['Explicit Rating']
    }
    songs_by_genre_and_territory[genre][territory].append(song)

# Streamlit web app
st.title('Song Management Portal')

genre = st.selectbox('Select Genre', genres)
territory = st.selectbox('Select Territory', territories)

if st.button('Show Songs'):
    songs = songs_by_genre_and_territory[genre][territory]
    if len(songs) > 0:
        st.subheader(f'Songs in {genre} from {territory}:')
        for song in songs:
            st.write('Artist:', song['Artist'])
            st.write('Title:', song['Title'])
            st.write('GPID:', song['GPID'])
            st.write('Category:', song['Category'])
            st.write('Product Type:', song['Product Type'])
            st.write('Sub Type:', song['Sub Type'])
            st.write('Duration:', song['Duration'])
            st.write('Explicit Rating:', song['Explicit Rating'])
            st.write('---')

        # Create a playlist
        selected_songs = st.multiselect('Select songs for the playlist', songs)
        playlist_name = st.text_input('Enter playlist name')
        create_playlist = st.button('Create Playlist')

        if create_playlist and playlist_name and len(selected_songs) > 0:
            playlist = {
                'Playlist Name': playlist_name,
                'Songs': selected_songs
            }
            st.write('Playlist created successfully!')
            st.write('Playlist Name:', playlist['Playlist Name'])
            st.write('Songs:')
            for song in playlist['Songs']:
                st.write('- Title:', song['Title'], ', Artist:', song['Artist'])
            st.write('---')

            # Generate playlist link
            sanitized_playlist_name = urllib.parse.quote(playlist_name)
            playlist_link = f'https://spotifyyy.com/playlists/{sanitized_playlist_name}'
            st.write('Playlist Link:')
            st.write(playlist_link)
            st.write('Click the link to visit the playlist or copy it for sharing.')


    else:
        st.write(f'No songs found in {genre} from {territory}.')
