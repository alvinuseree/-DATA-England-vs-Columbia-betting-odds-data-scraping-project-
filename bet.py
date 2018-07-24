import re
import requests													#Request HTML 										
import bs4														#Beatufiul Soup to see source clearly
from decimal import *											#Easier floating point arithmetic

import matplotlib.pyplot as plt 								#To plot the data visually

import time
import datetime

import pandas

while(True):
	re = requests.get("https://www.oddschecker.com/football/world-cup/colombia-v-england/winner")				#request HTML 
	soup = bs4.BeautifulSoup(re.text, 'lxml')					#Convert to a readable sourcefile

	#find the numerical data we need 
	spans = soup.find_all('a', {'href' : 'javascript:void(0);'})	#list of bettign websites
	bets = soup.find_all("td", attrs={"data-o":True})	#list of bets

	list_site = []    
	for x in range (len(spans)):
		temp_string = str(spans[x])
		
		title_location= temp_string.find("title")
		end_location= temp_string.find("></a>")

		list_site.append(temp_string[title_location+7:end_location-1])

	wins = []
	draws = []
	losses = []

	for x in range(0,28,1):
		wins.append(bets[x])

	for x in range(28,56,1):
		draws.append(bets[x])

	for x in range(56,84,1):
		losses.append(bets[x])	

	bet_win = []
	bet_draw = []
	bet_loss = []	

	for x in range (len(wins)):
		temp_stringW = str(wins[x])
		temp_stringD = str(draws[x])
		temp_stringL = str(losses[x])

		
		bet_locationW= temp_stringW.find("data-o")
		end_locationW= temp_stringW.find("data-odig")

		bet_locationD= temp_stringD.find("data-o")
		end_locationD= temp_stringD.find("data-odig")

		bet_locationL= temp_stringL.find("data-o")
		end_locationL= temp_stringL.find("data-odig")

		bet_win.append(temp_stringW[bet_locationW+8:end_locationW-2])
		bet_draw.append(temp_stringD[bet_locationD+8:end_locationD-2])
		bet_loss.append(temp_stringL[bet_locationL+8:end_locationL-2])

	data= {"England to Win":bet_win,"Draw":bet_draw,"Columbia to Win":bet_loss}
	df = pandas.DataFrame(data, index=list_site)

	timer = int(time.clock()/60)
	print("\n",timer," Mins","\n")
	print(df)

	time.sleep(10)
