'''
Author: Andrew Ruder
Last edited: 07/19/2020

Takes original scraped data and creates a new csv where it only
writes inputs from days where temperature was recorded
'''
import csv
with open('tutiempodataset.csv', 'r') as inp:
	filename = "relevantWeatherData.csv"
	f = open(filename, "w")
	for row in csv.reader(inp):
		if row[4] != '-':
			f.write(row[0] + "," +row[1] + "," + row[2] + "," + row[3]  + "," + row[4] + "," +row[5] + "," +row[6] + "," +row[7] + "," +row[8] + "\n")
