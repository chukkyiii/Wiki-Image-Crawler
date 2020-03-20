import requests
from bs4 import BeautifulSoup
import webbrowser
import shutil
import urllib
import time

class wikifinder:

    def imagedownload(image_url, ):
        a = 0
        imageresp = requests.get(image_url, stream=True)
        local_file = open(str(a) + '.jpg', 'wb')
        imageresp.raw.decode_content = True
        shutil.copyfileobj(imageresp.raw, local_file)
        a = int(a)
        a += 1
        del imageresp


    def wikiwalk():
        url = 'https://en.wikipedia.org/wiki/Special:Random'

        while True:
            try:
                wiki = requests.get(url)
                #print(wiki.status_code)# --> just to show website status_code

                soup = BeautifulSoup(wiki.content, 'html.parser')
                imglink = soup.find('img', class_="thumbimage")
                image_url = imglink.get('src')

                image_url = 'https:' + image_url
                print("Image Found")
                #print(image_url) #--> just to show image url
                time.sleep(1)
                wikifinder.imagedownload(image_url)

            except AttributeError:
                print("No Image Located")
