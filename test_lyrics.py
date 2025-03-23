import requests
import pytest

BASE_URL = "https://api.lyrics.ovh/v1/"

def get_lyrics(artist, song):
    url = f"{BASE_URL}{artist}/{song}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("lyrics", "No lyrics found")
    return None

def test_get_lyrics_success():
    lyrics = get_lyrics("Coldplay", "Yellow")
    assert lyrics is not None
    assert isinstance(lyrics, str)

def test_get_lyrics_fail():
    lyrics = get_lyrics("InvalidArtist", "InvalidSong")
    assert lyrics is None
