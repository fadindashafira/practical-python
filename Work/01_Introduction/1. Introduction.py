import urllib.request # moudules for opening URLs
u = urllib.request.urlopen('https://ctabustracker.com/home?stop=14791&route=22')
from xml.etree.ElementTree import parse # implements a simple API for parsing XML data
doc = parse(u)
for pt in doc.findall('.//pt'): # finds all matching subelements by tag name
    print(pt.text) # converts html codes into readable text to work