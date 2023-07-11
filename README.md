# song-management-portal

This repository contains a Python code file that implements a Song Management Portal using Streamlit. The portal allows users to search and manage songs based on genres, territories, and other attributes. It also provides the functionality to create playlists and generate playlist links for sharing.

# Dependencies
To run the application, you need to have the following dependencies installed:

- pandas
- streamlit

You can install the dependencies using pip:

`pip install pandas streamlit`

# Getting Started

1. Clone this repository:

  `git clone https://github.com/your-username/song-management-portal.git`
   
2. Navigate to the project directory:

   `cd song-management-portal`

3. Place your song data in an Excel file named songs.xlsx and make sure it has the following columns:
- Major Genre: Genre of the song
- PMO: Territory of the song
- Artist Display Name: Artist name
- Product Display Title: Song title
- GPID: Unique song identifier
- Category: Song category
- Product Type: Product type
- Sub Type: Sub type
- Total Playing Time: Duration of the song
- Explicit Rating: Explicit rating

4. Run the Streamlit web app:
  
  `streamlit run app.py`

5. Access the application in your web browser at http://localhost:8501. The App is not yet deployed to the cloud.

# Usage
- Select a genre and territory from the respective dropdown menus.
- Click the "Show Songs" button to display the songs in the selected genre and territory.
- If songs are found, they will be listed along with their details.
- You can select songs to create a playlist by using the checkboxes.
- Enter a playlist name in the text input field.
- Click the "Create Playlist" button to create the playlist.
- If the playlist is created successfully, its details will be displayed, including the playlist name and the selected songs.
A playlist link will also be generated, which you can visit or share with others.

Note: Please ensure that you have the necessary permissions and licenses to use the song data and create playlists.

For any questions or further assistance, feel free to reach out.

Enjoy managing your songs!

## License
This project is licensed under Warner Music Africa.
