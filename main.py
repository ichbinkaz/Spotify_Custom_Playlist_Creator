from Billboard import Billboard
from Spotify import Spotify

billboard = Billboard()
billboard.retrieve_songs()

# Obtains token and creates a playlist

spotify = Spotify(billboard)
spotify.add_song_to_playlist()
