

import os
import sys
import csv 
import json
import spotipy
import sqlite3
import webbrowser
import matplotlib
import unittest
import requests
import sqlite3
import urllib.request, urllib.parse, urllib.error
import spotipy.util as util
import matplotlib
import matplotlib.pyplot as plt




username = "miainakage@msn.com"
scope = 'user-library-read'
token = util.prompt_for_user_token(username, scope, client_id='e192483549944492a872412ca0106029', client_secret='35790b625ce542929b76fbfb4bcd5d10', redirect_uri='http://localhost:8888/callback')
spotify = spotipy.Spotify(auth = token)
 

#This function generates a list of tuples (artist name, song title, popularity value) given an artists URI
def top_10_songs_popularity(artist_uri):
    artist_data = spotify.artist_top_tracks(artist_uri)
    popularity_list = []
    for song in artist_data['tracks'][:11]:
        artist = song['artists'][0]['name']
        song_title = song['name']
        popularity = song['popularity']
        popularity_list.append((artist, song_title, popularity))
        #createSpotifyDatabase(conn, cur, top_10_songs_popularity)
    return popularity_list




conn = sqlite3.connect('PythonGirls.db')
cur = conn.cursor()

def createSpotipyDatabaseTable(conn, cur, top_10_songs_popularity):

	cur.execute('DROP TABLE IF EXISTS Spotipy')
	cur.execute('CREATE TABLE Spotipy (artist TEXT, song_title TEXT, popularity INTEGER)')
	for info in top_10_songs_popularity:
		cur.execute('INSERT INTO Spotipy (artist, song_title, popularity) VALUES (?,?,?)''', (info['singer'], info['best songs'], info['popularity']))
	conn.commit()


# This calls the function so that the database table is created
createSpotifyDatabaseTable(conn, cur, top_10_songs_popularity)



if __name__ == "__main__":
   
    conn = sqlite3.connect('PythonGirls.db')
    cur = conn.cursor()
   

    #Olivia Rodrigo's URI
    olivia_rodrigo_uri = 'spotify:artist:1McMsnEElThX1knmY4oliG'
    print(top_10_songs_popularity(olivia_rodrigo_uri))

    #The Weeknd's URI
    the_weeknd_uri = 'spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ'
    print(top_10_songs_popularity(the_weeknd_uri))

    #Billie Eilish's URI
    billie_eilish_uri = 'spotify:artist:6qqNVTkY8uBg9cP3Jd7DAH'
    print(top_10_songs_popularity(billie_eilish_uri))

    #Khlaid's URI
    khalid_uri = 'spotify:artist:6LuN9FCkKOj5PcnpouEgny'
    print(top_10_songs_popularity(khalid_uri))

    #Dua Lipa's URI
    dua_lipa_uri = 'spotify:artist:6M2wZ9GZgrQXHCFfjv46we'
    print(top_10_songs_popularity(dua_lipa_uri))

    #Harry Styles's URI
    harry_styles_uri = 'spotify:artist:6KImCVD70vtIoJWnq6nGn3'
    print(top_10_songs_popularity(harry_styles_uri))

    #Post Malone's URI
    post_malone_uri = 'spotify:artist:246dkjvS1zLTtiykXe5h60'
    print(top_10_songs_popularity(post_malone_uri))

    #Rihanna's URI
    rihanna_uri = 'spotify:artist:5pKCCKE2ajJHZ9KAiaK11H'
    print(top_10_songs_popularity(rihanna_uri))

    #Snoop Dogg's URI
    snoop_dogg_uri = 'spotify:artist:7hJcb9fa4alzcOq3EaNPoG'
    print(top_10_songs_popularity(snoop_dogg_uri))

    #Madonna's URI
    madonna_uri = 'spotify:artist:6tbjWDEIzxoDsBA1FuhfPW'
    print(top_10_songs_popularity(madonna_uri))




    
    