<h2 align="center">Spotify Data Extraction Pipeline</h2>

<h2 align="center">Introduction</h2>

This project involves building a pipeline to retrieve and process data from the Spotify API using Python and the SpotiPy library. This pipeline extracts the features of every song of a named artist and returns a ".csv" type file with the following variables (<a href="https://developer.spotify.com/documentation/web-api/reference/get-audio-features">1</a>):

- **Artist:** Name of the artist.
- **Album:** Name of the album the track belongs to.
- **Track:** Name of the track.
- **ID:** Spotify ID of the track.
- **Danceability:** It describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
- **Energy:** It is a measure from 0.0 to 1.0 and rerpresents a perceptual measure of intensity and activity. Perceptual features contributing to this attitude include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
- **Loudness:** The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Values usually range between -60 and 0 dB.
- **Acousticness:** A confidence measure from 0.0 to 1.0 of whether the track is acoustic.
- **Instrumentalness:** Predicts whether a track contains no vocals. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
- **Liveness:** Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.
- **Valence:** A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).
- **Tempo:** The overall estimated tempo of a track in beats per minute (BPM).
- **Duration:** The duration of the track in milliseconds.

<h2 align="center">Pipeline</h2>

The pipeline can be used by calling the class ```Spotify_ETL``` and adding the desired artist name as a string. Afterwards, the ```run_pipeline(CLIENT_ID, CLIENT_SECRET)``` method can be called to start running the pipeline. Both ```CLIENT_ID``` and ```CLIENT_SECRET``` are personal keys than can be requested at the Spotify API and are imported to the pipeline from the ```login_test.py``` file

Here are the processes that the pipeline does in order:

- Log in with credentials (```CLIENT_ID```, ```CLIENT_SECRET```).
- Search by artist name.
- Get artist URI.
- Get artist's album names and IDs.
- Get album's track names and IDs.
- Get track's features.
- Gather the data in a Pandas dataframe.
- Save the data in a ".csv" file.

<h2 align="center">Example</h2>

In this part, we will run a usage example to this pipeline as shown in "<a href="https://github.com/romaniegaa/spotify_etl/blob/main/etl_test.py">etl_test.py</a>". We will first import ```os```, the ```Spotify_ETL``` class from "<a href="https://github.com/romaniegaa/spotify_etl/blob/main/etl.py">etl.py</a>" and the login credentials from "<a href="https://github.com/romaniegaa/spotify_etl/blob/main/login_test.py">login_test.py</a>". Then, we will choose our working directory and call the ```Spotify_ETL``` class with the artist's name as string. In this case, we will look for Taylor Swift's whole music catalogue by running ```Spotify_ETL("Taylor Swift")``` and saving it into the ```data``` variable. Then we will run the pipeline by adding our credentials as shown next: ```data.run_pipeline(CLIENT_ID, CLIENT_SECRET)```. After running the code, we get a ".csv" file as shown in "<a href="https://github.com/romaniegaa/spotify_etl/blob/main/taylor_swift_track_features.csv">taylor_swift_track_features.csv</a>".
