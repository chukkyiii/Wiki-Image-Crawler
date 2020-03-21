import requests
from bs4 import BeautifulSoup
import urllib
import time
import keyarchivemanager as kam

kn = kam.kam
class wikifinder:

    def wikiimagedownload(image_url, key):
        filepath = "/Users/jessegodwin_0333/Downloads/Computer science/pythonproject/imagearchive/"
        filename = kn.knm(key) + "w" + ".jpg"
        full_path = filepath + filename
        imgreq = urllib.request.urlretrieve(image_url, full_path)


    def wikiwalk():
        url = 'https://en.wikipedia.org/wiki/Special:Random'
        key = 0
        while True:
            try:
                wiki = requests.get(url)
                #print(wiki.status_code)# --> just to show website status_code

                soup = BeautifulSoup(wiki.content, 'html.parser')
                imglink = soup.find('img', class_="thumbimage")
                image_url = imglink.get('src')

                image_url = 'https:' + image_url
                print("Image Found")
                key += 1
                #print(image_url) #--> just to show image url
                wikifinder.wikiimagedownload(image_url, key)

            except AttributeError:
                print("No Image Located")
