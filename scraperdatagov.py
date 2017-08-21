#!/usr/bin/env python3

#import required libraries
import requests
import csv
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


url = "https://data.gov.in/catalog/company-master-data"
output_file = open("datagovlinks.csv", "a", newline='')
driver = webdriver.Chrome()

# Selenium driver inititalization 
driver = webdriver.Chrome()
driver.wait = WebDriverWait(driver, 5)
driver.get(url)

# list to gather endpoints
list_=[] 
# output file for API endpoints
output_file = open("datagovAPIendpoints.csv", "a", newline='')  

# One of two functions to extract API endpoints 
def scrape1():
	for x in range(1,4):
		xpath = '//*[@id="catalog-details-wrapper"]/div[2]/div/div[4]/div['
		xpath += str(x)
		xpath += ']/div[8]/span/a'
		driver.find_element_by_xpath(xpath).click()
		time.sleep(5)
		links = driver.find_element_by_css_selector("a[href*='json']")
		text = links.text
		driver.back()
		time.sleep(5)
		list_.append(text)	
		print(list_)
		unique = set(list_)
		driver.get(url)
		for item in unique:
  			output_file.write("%s\n" % item)
  			
# Second function to extract endpoints
def scrape2():
	for x in range(1,4):
		xpath = '//*[@id="catalog-details-wrapper"]/div[2]/div/div[5]/div['
		xpath += str(x)
		xpath += ']/div[8]/span/a'
		driver.find_element_by_xpath(xpath).click()
		time.sleep(5)
		links = driver.find_element_by_css_selector("a[href*='json']")
		text = links.text
		driver.back()
		time.sleep(5)
		list_.append(text)	
		print(list_)
		unique = set(list_)
		driver.get(url)
		for item in unique:
  			output_file.write("%s\n" % item)

# Navigate to next page and extract endpoints for 1st extraction func.
def scrape_looping1():
	for i in range(2,7):
		scrape1()
		driver.get(url)
		button = driver.find_element_by_link_text(str(i)).click()
		time.sleep(5)
# Navigate to next page and extract endpoints for 2nd extraction func.
def scrape_looping2():
	for i in range(2,7):
		scrape2()
		button = driver.find_element_by_link_text(str(i)).click()
		time.sleep(5)

if __name__ == "__main__":
scrape_looping1()
scrape_looping2()


