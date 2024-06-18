from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.client import Spotify

import pandas as pd
import time

class Spotify_ETL:
    def __init__(self, artist_name):
        # Artist name
        self.__artist_name = artist_name

    def __credentials(self, CLIENT_ID, CLIENT_SECRET):
        # Credentials
        self.__sp = Spotify(auth_manager = SpotifyClientCredentials(client_id = CLIENT_ID,
                                                                            client_secret = CLIENT_SECRET))
        
    def __search_artist(self):
        # Search by artist name
        self.__results = self.__sp.search(q = self.__artist_name, type = "artist")

    def __get_uri_artist(self):
        # Get artist URI
        self.__artist_uri = self.__results["artists"]["items"][0]["id"]

    def __get_artist_albums(self):
        # Get artistalbum names and IDs
        self.__artist_albums = self.__sp.artist_albums(artist_id = "spotify:artist:"+self.__artist_uri,
                                                       album_type = "album", 
                                                       limit = 50)
        
        self.__album_names = []
        self.__album_ids = []
        self.__album_n_tracks = []

        for i in range(len(self.__artist_albums["items"])):
            self.__album_names.append(self.__artist_albums["items"][i]["name"])
            self.__album_ids.append(self.__artist_albums["items"][i]["id"])
            self.__album_n_tracks.append(self.__artist_albums["items"][i]["total_tracks"])
        
    def __get_album_tracks(self):
        # Get track names and IDs
        self.__album = []
        self.__track_names = []
        self.__track_ids = []

        for i_album in range(len(self.__album_ids)):
            self.__album_tracks = self.__sp.album_tracks(album_id = self.__album_ids[i_album],
                                                         limit = 50)
            for i_track in range(self.__album_n_tracks[i_album]):
                self.__track_names.append(self.__album_tracks["items"][i_track]["name"])
                self.__track_ids.append(self.__album_tracks["items"][i_track]["id"])
                self.__album.append(self.__album_names[i_album])

    def __get_track_features(self):
        # Features
        self.__track_danceability = []
        self.__track_energy = []
        self.__track_loudness = []
        self.__track_acousticness = []
        self.__track_instrumentalness = []
        self.__track_liveness = []
        self.__track_valence = []
        self.__track_tempo = []
        self.__track_duration = []

        # Divide the track IDs into chunks
        batch_size = 100
        self.__batches = [self.__track_ids[i:i + batch_size] for i in range(0, len(self.__track_ids), batch_size)]

        for batch in self.__batches:
            self.__track_features = self.__sp.audio_features(tracks = batch)
            for i in range(len(batch)):
                # Save the features
                self.__track_danceability.append(self.__track_features[i]["danceability"])
                self.__track_energy.append(self.__track_features[i]["energy"])
                self.__track_loudness.append(self.__track_features[i]["loudness"])
                self.__track_acousticness.append(self.__track_features[i]["acousticness"])
                self.__track_instrumentalness.append(self.__track_features[i]["instrumentalness"])
                self.__track_liveness.append(self.__track_features[i]["liveness"])
                self.__track_valence.append(self.__track_features[i]["valence"])
                self.__track_tempo.append(self.__track_features[i]["tempo"])
                self.__track_duration.append(self.__track_features[i]["duration_ms"])

            # Add 5s delay to the for loop
            time.sleep(5)


    def __get_dataframe(self):
        # Gather the data in a DataFrame
        self.__raw_data = pd.DataFrame(
            {"artist": self.__artist_name,
             "album": self.__album,
             "track": self.__track_names,
             "id": self.__track_ids,
             "danceability": self.__track_danceability,
             "energy": self.__track_energy,
             "loudness": self.__track_loudness,
             "acousticness": self.__track_acousticness,
             "instrumentalness": self.__track_instrumentalness,
             "liveness": self.__track_liveness,
             "valence": self.__track_valence,
             "tempo": self.__track_tempo,
             "duration": self.__track_duration
            })
        
    def __save_file(self):
        # Save the data in a ".csv" file
        self.__filename = self.__artist_name.lower().replace(" ", "_")+"_track_features.csv"
        self.__raw_data.to_csv(self.__filename, index = False)

    def run_pipeline(self, **kwargs):
        self.__credentials(kwargs.get("CLIENT_ID", None), kwargs.get("CLIENT_SECRET", None))
        self.__search_artist()
        self.__get_uri_artist()
        self.__get_artist_albums()
        self.__get_album_tracks()
        self.__get_track_features()
        self.__get_dataframe()
        self.__save_file()
