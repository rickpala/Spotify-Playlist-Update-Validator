from bs4 import BeautifulSoup
from lxml import html
import pprint
import json
from datetime import datetime

#Read Spotify's html for playlist webpage into BeautifulSoup
full_website_html = open('tracklist.html', 'r')
soup = BeautifulSoup(full_website_html, 'html.parser')

#Extract the tracklist as a BeautifulSoup Object
complete_tracklist = soup.find_all('div', class_='tracklist-col name')


#Create a list of the tracks, each track being a dictionary
parsed_list = []
for i in range(len(complete_tracklist)):
    track = BeautifulSoup(str(complete_tracklist[i]), 'html.parser')

    #Name: tracklist-name
    #Artist: tracklist-row__artist-name-link
    #Album: tracklist-row__album-name-link
    name = track.find('div', class_="tracklist-name").text
    artist = track.find('a', class_="tracklist-row__artist-name-link").text
    album = track.find('a', class_='tracklist-row__album-name-link').text

    parsed_list.append({'name': name, 'artist': artist, 'album': album})


#Convert list to a json file
wfilename = datetime.today().strftime('%b-%d-%Y') + " Tracklist.json"
wfile = open(wfilename, 'w')
wfile.write(json.dumps(parsed_list, indent=2))

wfile.close()
full_website_html.close()
