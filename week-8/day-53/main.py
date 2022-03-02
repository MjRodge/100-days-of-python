import requests
from bs4 import BeautifulSoup

ZILLOW_URL = 'https://www.zillow.com/toronto-on/rentals/2-_beds/?searchQueryState={"pagination"%3A{}%2C"usersSearchTerm"%3A"Toronto%2C ON"%2C"mapBounds"%3A{"west"%3A-79.85038135858876%2C"east"%3A-78.90281055780751%2C"south"%3A43.38217289221158%2C"north"%3A44.03239701322502}%2C"regionSelection"%3A[{"regionId"%3A792680%2C"regionType"%3A6}]%2C"isMapVisible"%3Atrue%2C"filterState"%3A{"price"%3A{"min"%3A0%2C"max"%3A688795}%2C"mp"%3A{"min"%3A0%2C"max"%3A2500}%2C"beds"%3A{"min"%3A2}%2C"fsba"%3A{"value"%3Afalse}%2C"nc"%3A{"value"%3Afalse}%2C"fore"%3A{"value"%3Afalse}%2C"cmsn"%3A{"value"%3Afalse}%2C"fr"%3A{"value"%3Atrue}%2C"ah"%3A{"value"%3Atrue}%2C"apco"%3A{"value"%3Afalse}%2C"apa"%3A{"value"%3Afalse}%2C"con"%3A{"value"%3Afalse}}%2C"isListVisible"%3Atrue}'

response = requests.get(ZILLOW_URL)
response.raise_for_status()
zillow_html = response.text
zillow_soup = BeautifulSoup(zillow_html, "html.parser")

print(zillow_soup)
