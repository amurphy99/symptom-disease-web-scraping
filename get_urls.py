#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:34:26 2023

@author: andrewmurphy
"""



import requests
from bs4 import BeautifulSoup

def create_urls_list(filename):
	# Create a list of URLs for each letter entry of the encyclopedia
	URL  = "https://medlineplus.gov/encyclopedia.html"
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, "html.parser")

	urls_list = []
	for link in soup.find_all('a'):
	    temp = link.get('href')
	    
	    if type(temp) == str:
	        if "ency/encyclopedia" in temp:
	            urls_list.append(temp)



	# Create a list of URLs within a single letter entry
	start = "https://medlineplus.gov/"
	all_urls_list = []
	for entry in urls_list:

	    page  = requests.get(start+entry)
	    soup  = BeautifulSoup(page.content, "html.parser")
	    
	    temp_entry_URLs = []
	    for link in soup.find_all('a'):
	        temp = link.get('href')
	        
	        if type(temp) == str:
	            if "article/" in temp:
	                temp_entry_URLs.append(temp)
	    
	    all_urls_list.append(temp_entry_URLs)



	# Write the entries links to a file for testing
	count = 0
	textfile = open("{}.txt".format(filename), "w")
	for letter_list in all_urls_list:
		for element in letter_list:
		    textfile.write(element + "\n")
		    count += 1
	textfile.close()
	print("{} urls saved".format(count))



'''
for url in all_urls_list:
    print(url[0])
    print(url[-1])
    print('\n')



# Write the A entries links to a file for testing
a_list = all_urls_list[0]
textfile = open("data/A_file.txt", "w")
for element in a_list:
    textfile.write(element + "\n")
textfile.close()

'''







