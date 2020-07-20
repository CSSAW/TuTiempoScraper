# TuTiempoScraper
Scraper that collects weather data from tutiempo.net for the Limpopo region in South Africa

The source: https://en.tutiempo.net/climate/south-africa.html

scrape.py will go through the webpages starting from the year 2000 and find locations within the Limpopo region using   
'''
26.395269 < longitude < 31.844487 
'''
and
'''
 -25.368371 < lat < -22.133315 
 ''' 
 as the boundaries. It will then write all of the data on that page to a csv. 
 '''
 usage: scrape.py
 '''
 After all the data is collected to a csv nonull.py with create a new csv that removes the data from days where there was no weather. Additionally, it removes irrelevant data such as wind speed. 
  '''
 usage: nonull.py
 '''
 The two must be run in that order or they will not give you the correct results
 
 
