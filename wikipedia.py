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

# create connection with SIProject Database
conn = sqlite3.connect('SIProject.sqlite')
cur = conn.cursor()

def get_artist_url (artist):
    
    url = "https://en.wikipedia.org/wiki/"
    
    # NOT SURE 

    # parse out the main artist with no featuring artists
    main_artist = artist.split("Featuring")[0]
    new_main_artist = main_artist.split("&")[0]
    final_artist = new_main_artist.split("X")[0]
    
    # NOT SURE

    # create new url based on typical wikipedia format (i.e. https://en.wikipedia.org/wiki/One_Right_Now)
    # separates artist name by replacing spaces with underscrores between words
    artist_name = final_artist.split()
    for word in artist_name:        
        url += word
        url = url.replace(' ', '_')
        #url += '_'
    return url