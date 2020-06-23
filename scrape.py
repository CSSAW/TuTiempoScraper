'''
Web scraper that collects weather data from tutiempo.net for the Limpopo region in South Africa
Author: Andrew Ruder
Last updated: 6/23/2020
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
def monthlyWeatherData(month_soup,month, year, lat, lon, f):
	'''
	Reads weather data from a location for a particular month into a .csv
	'''
	station = (month_soup.findAll("h2")[0].text).split()[1]
	monthTable = month_soup.findAll("div",{"class":"mt5 minoverflow tablancpy"})[0].findAll("tr")
	for day in range(1, len(monthTable) - 2):
		dayArray = monthTable[day].findAll("td")
		f.write(station + "," +str(lat) + "," + str(lon) + "," + str(year) + "," + month + "," + dayArray[0].text + "," + dayArray[1].text + "," +dayArray[2].text + "," +dayArray[3].text + "," +dayArray[4].text + "," +dayArray[5].text + "," +dayArray[6].text + "," + dayArray[8].text + "," +dayArray[9].text + "," +dayArray[10].text + "\n")

def parseMonths(station_soup, year, lat, lon, f):
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
		temp = monthUrl.find('-')
		monthNum = monthUrl[temp - 2] + monthUrl[temp - 1]
		monthlyWeatherData(month_soup, monthNum, year, lat, lon, f)

def inLimpopo(lat, lon):
	'''
	Checks if a station is within the Limpopo region
	'''
	if lon > 26.395269 and lon < 31.844487 and lat > -25.368371 and lat < -22.133315:
		return True
	return False


def stationList(citylist, year, f):
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
		lat = float(longandlat[0].text)
		lon = float(longandlat[1].text)
		if(inLimpopo(lat, lon)):
			parseMonths(station_soup, year, lat, lon, f)
			

if __name__ == '__main__':
	filename = "tutiempodata.csv"
	f = open(filename, "w")

	headers = "Station, Latitude, Longitude, Year, Month, Day, T, TMax, TMin, SLP, H, PP, V, VM, VG\n"
	f.write(headers)
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
			stationList(citylist, year, f)
	f.close()
