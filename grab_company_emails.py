#!/usr/bin/env python3.6

#key:b50129e51f77b14c12bc83fb7ff3e8ec
from bs4 import BeautifulSoup
import requests
import re
import requests
import json
import pickle
import csv

# lists that data will be saved to 
list1 = []
list2 = []
list3 = []
new_list = []
url_data_file = (open("COMPANYURL.csv","r"))
company_emails = (open("COMPANYEMAILS.csv","w"))

# create company url for zaubacorp.com with cin numner and company name
def company_name_search():
	df1 = pickle.load(open( "companiesjson.txt", "rb" ))
	for i in range():
		company_name = df1["records"][0]["COMPANYNAME"]
		cin_number = df1["records"][0]['CORPORATEIDENTIFICATIONNUMBER']
		list1.append(company_name)
		list2.append(cin_number)
	for i in list1:
		delimited_name = i.replace(" ","-")
		url = 'https://www.zaubacorp.com/company/' # website to take emails from
		new_url = url + delimited_name + "/" 
		list3.append(new_url)

company_name_search()

#write url's to csv
for each in range(0,len(list2)):
    new_list.append(list3[each] + str(list2[each]))
for i in new_list:
   	url_data_file.write("%s\n" % i)

# go into comapny page in zaubacorp.com and extract email 
# write emails to new csv
def grabemail():
	for i in url_data_file:
		r = requests.get(i)
		data = r.text
		soup = BeautifulSoup(data,'html.parser')
		try:
			email = soup.find_all(string=re.compile('@'))[1]
			company_emails.write("%s\n" % email)
		except:
			company_emails.write("%s\n" % 'NA')

grabemail()
