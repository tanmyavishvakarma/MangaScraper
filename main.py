import requests
from bs4 import BeautifulSoup
import webbrowser
headers = { 'User-Agent': 'My User Agent 1.0','From': 'youremail@domain.com'}  # This is another valid field}
manga_name=input(str("manga name: "))
manga_name=manga_name.replace(" ","_")
print(manga_name)
manga_chapter=input(str("which chapter do you wish to read: "))
try:
    r=requests.get("https://mangakakalot.com/search/story/"+str(manga_name),headers=headers)
    soup=BeautifulSoup(r.content,'html.parser')
    manga_anchors=soup.find("h3", {"class": "story_name"})
    manga_link=(manga_anchors.contents[1]['href'])
    parts=manga_link.split('/')
    manga_id=parts[4]
    webbrowser.open('https://manganelo.com/chapter/'+str(manga_id)+"/chapter_"+str(manga_chapter))
except:
    print("Sorry manga not found")





