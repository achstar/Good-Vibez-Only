import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def find_HSV(URL):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    # major: hue value 0 to 0.5
    # minor: hue value 0.5 to 1
    feat = spotify.audio_features(URL)[0]
    valen = feat['valence']
    acc = feat['acousticness']
    hue = 360*((feat['energy']+feat['danceability']) + (feat['energy']+feat['danceability'])/feat['energy'])
    hue2 = hue%360
    if feat['mode']==0:
        hue2 =hue2*-1%360

    sat = 1-acc

    vals = valen*.7+acc*.3
    return (hue2, sat, vals)

(H, S, V) = find_HSV("https://open.spotify.com/track/7HKxTNVlkHsfMLhigmhC0I?si=f1def96c279c4506")