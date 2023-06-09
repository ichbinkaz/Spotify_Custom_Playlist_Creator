import requests
import os
from dotenv import load_dotenv
from Billboard import Billboard

load_dotenv("variables.env")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_id = os.getenv("USER_ID")
authorization_url = "https://accounts.spotify.com/authorize"
redirect_uri = "https://example.com/callback"
token_url = "https://accounts.spotify.com/api/token"
creation_playlist_endpoint = f"https://api.spotify.com/v1/users/{user_id}/playlists"

scope = "playlist-modify-public playlist-modify-private"


class Spotify:
    def __init__(self, billboard: Billboard):
        self.billboard = billboard
        self.uris = []
        self.access_token = self.obtain_access_token()
        self.headers_authentication = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        self.playlist_id = self.create_playlist()
        self.playlist_endpoint = f"https://api.spotify.com/v1/playlists/{self.playlist_id}/tracks"



    def obtain_access_token(self):

        authorization_params = {
            "client_id": client_id,
            "response_type": "code",
            "redirect_uri": {redirect_uri},
            "scope": scope
        }

        response = requests.get(authorization_url, params=authorization_params)
        print(response.url)
        authorization_code = input("Enter the authorization code: ")
        # Step 2: Exchange authorization code for access token

        data = {
            "grant_type": "authorization_code",
            "code": authorization_code,
            "redirect_uri": redirect_uri,
            "client_id": client_id,
            "client_secret": client_secret,
        }
        response = requests.post(token_url, data=data)
        access_token = response.json()["access_token"]

        return access_token


    def get_spotify_username(self):
        response = requests.get("https://api.spotify.com/v1/me", headers=self.headers_authentication)
        print(response.json())

    def create_playlist(self):

        body = {
            "name": f"Top 100 Hits for {self.billboard.prompt} period",
            "description": f"My awesome new playlist for {self.billboard.prompt} period",
            "public": False,
        }

        playlist_id = requests.post(creation_playlist_endpoint, headers=self.headers_authentication,
                                    json=body).json()['external_urls']['spotify'].split("/")[4]

        return playlist_id

    def add_song_to_playlist(self):
        print(self.billboard.labels)
        # uris = [requests.get(f"https://api.spotify.com/v1/search?q={self.billboard.labels[index]}&type=track",
        #                      headers=self.headers_authentication).json()['tracks']['items'][0]['uri']
        #         for index in range(len(self.billboard.labels))]
        for index in range(len(self.billboard.labels)):
            try:
                response = requests.get(f"https://api.spotify.com/v1/search?q={self.billboard.labels[index]}&type=track", headers=self.headers_authentication).json()['tracks']['items'][0]['uri']
                self.uris.append(response)
            except KeyError:
                print("Track not found")
                continue

        print(self.uris)

        for index in range(len(self.uris)):
            try:
                response = requests.post(self.playlist_endpoint, json={"position": index, "uris": [self.uris[index]]}, headers=self.headers_authentication)
                response.raise_for_status()
                print(f"Added track {index + 1} to playlist")
            except requests.exceptions.HTTPError as error:
                print(f"Error adding track {index + 1} to playlist: {error}")



