# -*- coding: utf-8 -*-
"""
Student Name:       Karina Jonina 
Student ID:         10543032
Github:             https://github.com/KarinaPS11/B8IT105
Module:             B8IT105 
Module Name:        Programming for Big Data (DBS)

Assignment 1        10% - Beautiful Soup
"""


#importing important packages
import requests 
import codecs
from bs4 import BeautifulSoup
import pandas as pd

##website
#https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_London

##Getting the cURL
#headers = {
#    'authority': 'en.wikipedia.org',
#    'cache-control': 'max-age=0',
#    'upgrade-insecure-requests': '1',
#    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
#    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#    'sec-fetch-site': 'same-origin',
#    'sec-fetch-mode': 'navigate',
#    'sec-fetch-user': '?1',
#    'sec-fetch-dest': 'document',
#    'referer': 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_United_Kingdom',
#    'accept-language': 'en-US,en;q=0.9',
#    'cookie': 'WMF-Last-Access=11-Apr-2020; WMF-Last-Access-Global=11-Apr-2020; GeoIP=IE:L:Dublin:53.33:-6.25:v4; enwikimwuser-sessionId=834a72b8c1d593eba087',
#    'if-modified-since': 'Sat, 11 Apr 2020 11:07:07 GMT',
#}
#
##getting the live page
#def get_page_contents():
#    response = requests.get('https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_London', headers=headers)
#    return response.content

'''
The Wikipedia table was changed during this assignment and 
therefore an copy of HTML was downloaded and used.
Above code will bring a different table and code may not work with the new website.
The used HTML code was submitted with this assignment.
'''  

#loading saved html submitted with this assingment.
def load_saved_html():
    data = codecs.open('corona_London.html',"r", "utf-8")
    response = data.read()
    #print(response) #View the HTML code
    return response

#check it works
load_saved_html()


#function to parste html code
def convert_to_soup(content):
    return BeautifulSoup(content, features="html.parser")


#defintion to extract title
def get_title():
    return soup.title.string

def find_all_links(soup):
    links = soup.find_all('a')
    for link in links:
        print(links)
#    return links

#Getting Data from the table
def process_data(soup):
    
    table = soup.find('table', class_='wikitable sortable').tbody
    rows =  table.find_all('tr')
    columns = [v.text.replace('\n', '') for v in rows[0].find_all('th')]
    
    df = pd.DataFrame(columns = columns)
    
    for i in range(1, len(rows)):
        tds = rows[i].find_all('td')
        
        if len(tds) == 4:
            values = [ tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text]
        else:
            values = [td.text.replace('\n', '') for td in tds]
        #Checks the values
        print(values)
        
        df = df.append(pd.Series(values, index = columns), ignore_index = True)
       #checks the values
        print(df)
        
    #save csv file   
    df.to_csv(r"Corona_London_html.csv", index =  False)


def main():
    contents = load_saved_html()
    soup = convert_to_soup(contents)
    process_data(soup)
    
    

    
if __name__ == '__main__':
    main()    

 
    
    
    
    
    
    

