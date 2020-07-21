'''
Author: Andrew Ruder
Last edited: 07/19/2020
Takes weather data scraped from https://en.tutiempo.net/climate/south-africa.html
and then gets the average temperature, average percipitation and total percipitation for each month
and then compares it to the prior month.
'''
import pandas
import csv

if __name__ == '__main__':
	inp = open('relevantWeatherData.csv', 'r')
	filename = "new.csv"
	f = open(filename, "w")
	weatherDict={}
	for row in csv.reader(inp):
		stationKey = row[0] + "," +row[1] + "," + row[2]
		tempDict = {}
		dateKey = row[3][6]
		weatherList = [float(row[4]),float(row[5]),float(row[6]),float(row[8])]
		tempDict[dateKey] = weatherList
