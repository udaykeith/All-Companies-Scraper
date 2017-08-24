# All Companies Scraper
Pythonic scraper for extracting data for all Indian Registered Companies from https://data.gov.in/catalog/company-master-data with an additional feature of finding all their email ID's (if available)

The Indian Data.gov's API's are notoriously difficult to use and make it hard for public data to be well, public. I wrote a scraper to extract the names and associated data fields (Address, Paidup capital etc.) I have also included code on how to extract the companies's email address, if available, (not a feature on data.gov) from zaubacorp.com, a popular data collection platform. 

Yes, this is for ALL REGEISTERED COMPANIES IN INDIA AND THEIR EMAIL ADDRESSES

1) scraperdatagov.py - Contains code for extracting API endpoints for all 29 states and 7 Union territories
2) datagov_jsoncalls.py - Code for calling each API and pickling JSON objects to a local file.
3) grab_compnay_emails.py - Create's urls for zaubacrop.com and write email addresses (if available) to local file.
