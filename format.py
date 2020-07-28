'''
Author: Andrew Ruder
Last edited: 07/27/2020
Takes weather data scraped from https://en.tutiempo.net/climate/south-africa.html
and then gets the average temperature, average percipitation and total percipitation for each month
and then compares it to the prior month.
'''
import pandas
import csv


def diaAMes(weatherDict, f):
	'''
	This function find turns the daily values into  monthly averages and totals.
	Hence the name in spanish, day to month.
	'''
	for station in  weatherDict.keys():
		for date in weatherDict[station].keys():
			totalDays = len(weatherDict[station][date])
			f.write(station + "," + date + ",")
			for j in range(2):
				temp = 0
				for i in range(totalDays):
					temp += weatherDict[stationKey][date][i][j]
				if j != 1:
					f.write(str(temp / float(totalDays)) + ",")
				else:
					f.write(str(temp / float(totalDays)) + "," +str(temp)+"\n")
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
		dateKey = row[3][:6]
		temp = row[4]
		perc = row[8]
		if perc == '-':
			perc = 0
		weatherList = [float(temp),float(perc)]
		if stationKey in weatherDict.keys():
			if dateKey in weatherDict[stationKey].keys():
				weatherDict[stationKey][dateKey].append(weatherList)
			else:
				tempList = []
				weatherDict[stationKey][dateKey] = tempList
				weatherDict[stationKey][dateKey].append(weatherList)
		else: 
			tempDict = {}
			tempList = []
			tempList.append(weatherList)
			tempDict[dateKey] = tempList
			weatherDict[stationKey] = tempDict
	f.write("Station, Latitude, Longitude, Date, avgT, avgPP, totalPP\n")
	diaAMes(weatherDict, f)
