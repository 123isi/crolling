import requests
from bs4 import BeautifulSoup
url = "https://www.melon.com/chart/index.htm"

headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
print(soup)
songs = soup.select("div.ellipsis.rank01 a")  
artists = [artist.find('a') for artist in soup.select("div.ellipsis.rank02")]


for i in range(len(songs)):
    song_title = songs[i].get_text()
    artist_name = artists[i].get_text()
    print(f"{i+1}. {song_title} - {artist_name}")
