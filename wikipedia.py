from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import sqlite3
import re

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# fetch and read in urls from wikipedia website
url = "https://en.wikipedia.org/wiki/"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# create connection with PythonGirls database
conn = sqlite3.connect('PythonGirls.sqlite')
cur = conn.cursor()

def GetArtistUrl (artist):
    url = "https://en.wikipedia.org/wiki/"
    
# NOT SURE 
    # parse out the main artist with no featuring artists
    main_artist = artist.split("Featuring")[0]
    new_main_artist = main_artist.split("&")[0]
    final_artist = new_main_artist.split("X")[0]
    
    # create new url using wikipedia format (i.e. https://en.wikipedia.org/wiki/One_Right_Now)
    # separates artist name by replacing spaces with underscrores between words
    artist_name = final_artist.split()
    for word in artist_name:        
        url += word
# NOT SURE IF REPLACE FUNCTION WORKS
        url = url.replace(' ', '_')
        #url += '_'
    return url

def GetArtistAge (url):
    # try to find age of artist on wikipedia page, if not found then it is unknown
    try:
        html = urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        # create reg expression to find artist age
        reg_exp = "\d{2}"

        # find a list of all tr
        all_tr_tags = soup.find_all('tr')
        for tr in all_tr_tags:
            # find a list of all th tags
            all_th_tags = soup.find_all('th')
            for th in all_th_tags:
                # search for "Born" and store value that satisfies the regex
                if th.text == "Born":
                    reg_exp_found = re.findall(reg_exp, tr.text)
        '''
        table = soup.find('table', class_ = 'toccolours')
        all_rows = table.find_all('tr')
        '''
# NOT SURE
        artist_age = reg_exp_found[0]
        return(artist_age)
    except:
        # if regex fails, then indicate "Artist age is unknown."
        artist_age = "Artist age is unknown."
        return(artist_age)

def GetArtistData (artist_list):
    artist_dict = {}
    unknown_age = []
    
    for artist in artist_list:
        url = GetArtistUrl(artist)
        age = GetArtistAge(url)
        artist_dict[artist] = age
# NOT SURE WHAT THIS DOES
    for value in artist_dict.keys():
        if artist_dict[value] == "Artist age is unknown.":
            unknown_age.append(value)
    return artist_dict

def SetUpWikipediaTable (artist_dict):
    # create wikipedia table and insert artist data (name and age)
    cur.execute('DROP TABLE IF EXISTS Wikipedia')
    cur.execute('CREATE TABLE Wikipedia(source TEXT, artist TEXT, age INTEGER)')
    source = "Spotify"
    for artist in artist_dict.keys():
        cur.execute("INSERT OR IGNORE INTO Wikipedia (source, artist, age) VALUES (?,?,?)", (source, artist, artist_dict[artist]))
    conn.commit()

# create list of artists from spotify
artist_list = []
song_list = cur.execute("SELECT artist, song FROM Spotify")
for song in song_list:
    artist_list.append(song[0])

# NEEDED?
cur.close()

# get information from artist dictionary and write to wikipedia table
artist_data = GetArtistData(artist_list)
SetUpWikipediaTable(artist_data)

