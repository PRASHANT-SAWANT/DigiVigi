# urllib, urllib.request and Beautiful Soup are the three important libraries needed in this script
# This Script only captures data from Webiron web page only. For different URL data,
# one will have to change the URL passed in make_soup() and make slight changes to code
# This script captures data with respect to current date and appends it to an exiting csv
# This code runs fine to its purpose.

import urllib
import urllib.request
from bs4 import BeautifulSoup
import datetime
from dateutil import parser

#this is a function which takes whatever url is passed from the code or UI
def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

#Here's where you have captured the html page
soup = make_soup("http://www.webiron.com/abuse_feed/")

def foo():
    # Assigning null value is necessary otherwise garbage value may exist while running the program
    global abusedatasaved
    abusedatasaved = ""
    for record in soup.findAll('tr'):
        abusedata = ""
        for data in record.findAll('td'):
            for dateComparer in record.findAll('td')[1:2]:
                if datetime.datetime.now().date() == parser.parse(dateComparer.text).date():
                    temptext = ''  #Using this variable to store text data in td tag
                    modtext = ''   #Using this variable to remove comma in text data, as it will be further stored in a csv
                    temptext += data.text
                    modtext += temptext.replace(',', '/')
                    abusedata = abusedata + "," + modtext
                else:
                    return
                    #print("Hey, there's no new data out there :P")
        abusedatasaved =abusedatasaved + "\n" + abusedata[1:] #The [1:] will loop through 1st column and next ones

foo()
#print(abusedatasaved)
filepath = "D:\codegen\Abusedata.csv"
file = open(filepath, 'a')
file.write(abusedatasaved)
file.close()
