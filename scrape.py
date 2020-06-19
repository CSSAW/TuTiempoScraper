'''
Web scraper that collects weather data from tutiempo.net for the Limpopo region in South Africa
Author: Andrew Ruder
Last updated: 6/19/2020
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
def monthlyWeatherData(month_soup):
	'''
	Reads weather data from a location for a particular month into a .csv
	NEED TO FINISH THIS FUNCTION
	'''
def parseMonths(station_soup):
	'''
	Goes through each month that a station has weather data for and creates a soup
	for the weather dta for that month. It then calls monthlyWeatherData() to read the data into a .csv
	'''
	tturl = "https://en.tutiempo.net"
	months = station_soup.findAll("div",{"class":"mlistados mt10"})[0].findAll("a")
	for month in months:
		monthHref = month["href"]
		monthUrl = tturl + monthHref
		uclient = urlopen(monthUrl)
		month_html = uclient.read()
		uclient.close()
		month_soup = soup(month_html, "html.parser")
		monthlyWeatherData(month_soup)

def inLimpopo(lat, lon):
	'''
	Checks if a station is within the Limpopo region
	'''
	if lon > 26.395269 and lon < 31.844487 and lat > -25.368371 and lat < -22.133315:
		return True
	return False


def stationList(citylist):
	'''
	Goes through all the stations are in a given "citylist" and checks if it is in the Limpopo region
	If it is it will call parseMonths() to go through all the month data for the station in that year
	'''
	tturl = "https://en.tutiempo.net"
	for station in citylist:
		stationHref = station["href"]
		newUrl = tturl + stationHref
		uclient = urlopen(newUrl)
		station_html = uclient.read()
		uclient.close()
		station_soup = soup(station_html, "html.parser")
		longandlat = station_soup.findAll("p", {"class" : "mt5"})[0].findAll("b")
		lat = longandlat[0].text
		lon = longandlat[1].text
		if(inLimpopo(lat, lon)):
			parseMonths(station_soup)
			

if __name__ == '__main__':
	for year in range(2000,2021):
		'''
		Finds list of cities of the specific year starting with 2000
		'''
		 url = "https://en.tutiempo.net/climate/south-africa/" + str(year) + ".html"
		 uclient = urlopen(url)
		 page_html = uclient.read()
		 uclient.close()
		 page_soup = soup(page_html, "html.parser")
		 cities = page_soup.findAll("div",{"class":"mlistados mt10"})
		 '''
		 Finds the list of cities of the specific year on the second page
		 and then adds them to the first city list
		 '''
		 page2 = "https://en.tutiempo.net/climate/south-africa/" + str(year) + "/2/"
		 uclient = urlopen(page2)
		 page2_html = uclient.read()
		 uclient.close()
		 page2_soup = soup(page2_html, "html.parser")
		 cities2 = page2_soup.findAll("div",{"class":"mlistados mt10"})
		 cities.extend(cities2)
		 '''
		 The current "Cities" list is broken up between letters,
		 so we are making a list of cities out of each portion
		 '''
		 for city in cities:
		 	citylist = city.findAll("a")
		 	stationList(citylist)