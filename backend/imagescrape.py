from urllib.request import urlopen
from urllib import request 
from bs4 import BeautifulSoup
import json
import re
import requests
import urllib.request

HISTORYCENTER_ATL_IN_50 = {}
HISTORYCENTER_VIETNAM_WAR = {}

dictionaries = [None] * 3

name = "Atlanta-History-Center"
collections = [None] * 2
coordinates = [None] * 2

atl_histcenter_c1 = 'https://www.atlantahistorycenter.com/explore/online-exhibitions/atlanta-in-50-objects'
atl_histcenter_c2 = 'https://www.atlantahistorycenter.com/explore/online-exhibitions/more-than-self'

html = urlopen(atl_histcenter_c1)
bs = BeautifulSoup(html, 'html.parser')
images1 = bs.find_all('img', {'src':re.compile('.jpg')})
i = 1;
for image in images1: 
    HISTORYCENTER_ATL_IN_50['image' + str(i)] = image['src']
    i = i + 1


html = urlopen(atl_histcenter_c2)
bs = BeautifulSoup(html, 'html.parser')
images2 = bs.find_all('img', {'src':re.compile('.jpg')})
i = 1;
for image in images2: 
    HISTORYCENTER_VIETNAM_WAR['image' + str(i)] = image['src']
    i = i + 1


collections[0] = {"name":"Atlanta-In-50-Objects","images": HISTORYCENTER_ATL_IN_50}
collections[1] = {"name":"Living-The-Vietnam-War","images": HISTORYCENTER_VIETNAM_WAR}


coordinates[0] = 33.84282
coordinates[1] = -84.38573

Atlanta_History_Center = {"name":name, "coordinates":coordinates, "collections":collections}

#############################################################################################
#############################################################################################

HIGHMUSEUM_PHOTOGRAPHY = {}
HIGHMUSEUM_DEC_ARTS_DESIGN = {}
HIGHMUSEUM_AFRICANART = {}
HIGHMUSEUM_EURO_ART = {}
HIGHMUSEUM_AMERICAN_ART = {}
HIGHMUSEUM_MODERN_CONTEMP_ART = {}
HIGHMUSEUM_FOLK_SELFTAUGHT_ART = {}

name1 = "High-Museum-of-Art"
collections1 = [None] * 7
coordinates1 = [None] * 2


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
highmuseum_link = [None] * 7
highmuseum_link[0] = 'https://high.org/collection_area/photography/'
highmuseum_link[1] = 'https://high.org/collection_area/decorative-arts-and-design/'
highmuseum_link[2] = 'https://high.org/collection_area/african-art/'
highmuseum_link[3] = 'https://high.org/collection_area/european-art/'
highmuseum_link[4] = 'https://high.org/collection_area/american-art/'
highmuseum_link[5] = 'https://high.org/collection_area/modern-and-contemporary-art/'
highmuseum_link[6] = 'https://high.org/collection_area/folk-and-self-taught-art/'
page_request = [None] * 7
page = [None] * 7
html = [None] * 7
for i in range(7):
page_request[i] = request.Request(highmuseum_link[i], headers=headers)
page[i] = request.urlopen(page_request[i])
html[i] = BeautifulSoup(page[i], 'html.parser')
div_container = html[i].find('div', id = 'a11y_body_wrap')
main_container = div_container.find('main')
section_list = main_container.find_all('section')
j = 1;
for div in section_list[2].find_all('div', class_="row"):
for div2 in div.find_all('div', class_="grid new-media col-1 not-on-view"):
a = div2.find("a")

div_3 = div2.find('div', class_="image-container col-1 not-on-view")
picture = div_3.find("picture")
img = picture.find("img")
string = img["srcset"]

m = re.search('(.+?) 317w', string)
if m:
string = m.group(1)

link = string
if (i == 0):
HIGHMUSEUM_PHOTOGRAPHY['image' + str(j)] = link
if (i == 1):
HIGHMUSEUM_DEC_ARTS_DESIGN['image' + str(j)] = link
if (i == 2):
HIGHMUSEUM_AFRICANART['image' + str(j)] = link
if (i == 3): 
HIGHMUSEUM_EURO_ART['image' + str(j)] = link
if (i == 4):
HIGHMUSEUM_AMERICAN_ART['image' + str(j)] = link
if (i == 5):
HIGHMUSEUM_MODERN_CONTEMP_ART['image' + str(j)] = link
if (i == 6):
HIGHMUSEUM_FOLK_SELFTAUGHT_ART['image' + str(j)] = link
j = j + 1


collections1[0] = {"name":"Photography","images": HIGHMUSEUM_PHOTOGRAPHY}
collections1[1] = {"name":"Decorative-Arts-and-Design","images": HIGHMUSEUM_DEC_ARTS_DESIGN}
collections1[2] = {"name":"African-Art","images": HIGHMUSEUM_AFRICANART}
collections1[3] = {"name":"European-Art","images": HIGHMUSEUM_EURO_ART}
collections1[4] = {"name":"American-Art","images": HIGHMUSEUM_AMERICAN_ART}
collections1[5] = {"name":"Modern-and-Contemporary-Art","images": HIGHMUSEUM_MODERN_CONTEMP_ART}
collections1[6] = {"name":"Folk-and-Self-Taught-Art","images": HIGHMUSEUM_FOLK_SELFTAUGHT_ART}

coordinates1[0] = 33.79051
coordinates1[1] = -84.38517

High_Museum_Of_Art = {"name":name1, "coordinates":coordinates1, "collections":collections1}

#############################################################################################
#############################################################################################


GEORGIAMUSEUM_EXHIBITIONS = {} 
name2 = "Georgia-Museum-of-Art"
collections2 = [None] * 1
coordinates2 = [None] * 2

gamuseum_link = 'https://georgiamuseum.org/category/on-view-exhibit/'

page_request = request.Request(gamuseum_link, headers=headers)
page = request.urlopen(page_request)
html = BeautifulSoup(page, 'html.parser')

div_containers = html.find_all('div', class_='flex-row wow fadeInUp')
j = 1
for d in div_containers:
img = d.find('img', alt="Feature Image")
link = img["src"]
GEORGIAMUSEUM_EXHIBITIONS['image' + str(j)] = link
j = j + 1


collections2[0] = {"name":name2,"images":GEORGIAMUSEUM_EXHIBITIONS}

coordinates2[0] = 33.94119
coordinates2[1] = -83.36968

Museum_of_Design = {"name":name2,"coordinates":coordinates2,"collections":collections2}


dictionaries[0] = Atlanta_History_Center
dictionaries[1] = High_Museum_Of_Art
dictionaries[2] = Museum_of_Design

#print(dictionaries[0])
#print('\n\n\n\n\n')
#print(dictionaries[1])
#print('\n\n\n\n\n')
#print(dictionaries[2])
with open('MUSEUM.json', 'w') as fp:
json.dump(dictionaries, fp)


