import os
from etl import Spotify_ETL
from login import *

dir = ""
os.chdir(dir)

# Test
artist_name = "Taylor Swift"
data = Spotify_ETL(artist_name)
data.run_pipeline(CLIENT_ID = CLIENT_ID, 
                  CLIENT_SECRET = CLIENT_SECRET)