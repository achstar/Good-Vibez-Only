import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# major: hue value 0 to 0.5
# minor: hue value 0.5 to 1
features = spotify.audio_features("https://open.spotify.com/track/7HKxTNVlkHsfMLhigmhC0I?si=f1def96c279c4506")[0]
print(str(features["danceability"]))
print(str(features["energy"]))
hueAvg = 0.25
hueValue = (features["danceability"] + features["energy"])/4
hueValue = (0.5 - hueValue)

if features["mode"] == 0:
    hueAvg = 1 - hueAvg
    hueValue = 1 - hueValue
hueDiff = hueValue - hueAvg
hueValue = hueValue*360
print(hueValue)
