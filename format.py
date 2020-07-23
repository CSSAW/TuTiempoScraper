'''
Author: Andrew Ruder
Last edited: 07/22/2020
Takes weather data scraped from https://en.tutiempo.net/climate/south-africa.html
and then gets the average temperature, average percipitation and total percipitation for each month
and then compares it to the prior month.
'''
import pandas
import csv


def diaAMes(weatherDict):
	'''
	This function find turns the daily values into  monthly averages and totals.
	Hence the name in spanish, day to month.
	'''
	monthDict = {}


if __name__ == '__main__':
	inp = open('relevantWeatherData.csv', 'r')
	filename = "new.csv"
	f = open(filename, "w")
	'''
	Putting all the csv data into a dictionary of dictionaries of list of lists (yea ikr)
	to be in a format that makes it easier to do the math required for the diaAMes() function
	'''
	weatherDict={}
	for row in csv.reader(inp):
		stationKey = row[0] + "," +row[1] + "," + row[2]
		dateKey = row[3][6]
		weatherList = [float(row[4]),float(row[5]),float(row[6]),float(row[8])]
		if stationKey in weatherDict.keys():
			if dateKey in weatherDict[stationKey].keys():
				weatherDict[stationKey][dateKey].apepend(weatherList)
			else:
				tempList = []
				weatherDict[stationKey][dateKey] = tempList
				weatherDict[stationKey][dateKey].apepend(weatherList)
		else: 
			tempDict = {}
			tempList = []
			tempList.append(weatherList)
			tempDict[dateKey] = tempList
			weatherDict[stationKey] = tempDict

	diaAMes(weatherDict)
