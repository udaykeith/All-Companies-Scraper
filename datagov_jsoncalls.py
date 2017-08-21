#!/usr/bin/env python3

import csv

# files to write and read from for API endpoints
data_file = open("datagovAPIendpoints.csv","r", newline = '')	
reader = csv.reader(data_file)
key = 'Your API Key'
output_file = open("endpointswithkey.csv", "a", newline='')  
reader1 = csv.reader(output_file)

# Since data.gov only returns a 100 rows with each call
# offset allows to make recursive calls until all rows are called
offset  = "&offset=%d" 

# appends API key to endpoints
def addkey():
	for i in reader:
		if i[-7:] == "YOURKEY":
			new_url =  i[:-7] + key
			output_file.write("%s\n" % new_url)

# writes(pickles) json ojects to .txt file
def callapi():
    count = 0
    for i in range(100):
        count += 1
        full_url = url + offset % i
        r = requests.get(full_url)
        df = r.json()
        #print(df)
        pickle.dump(df, open("companiesjson.txt",'wb'))

if __name__ == '__main__':
	addkey()
	callapi()
	

	
    