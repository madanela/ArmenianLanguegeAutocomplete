"""
Main Scraping script from wikipedia random pages
"""
import requests
from bs4 import BeautifulSoup
import random
import re
from ArmScraping import Text_Cleaning
hy_url = 'https://hy.wikipedia.org/wiki/Special:Random'


corpus = []
mem = set()

token = ""

opt_treshold = 1.4
for _ in range(100000):
    
    response = requests.get(url = hy_url)
    cur_url = response.url
    if cur_url in mem:
        continue
    mem.add(cur_url)
    soup = BeautifulSoup(response.content,'html.parser')

   # print(response.status_code)
    Title = soup.find( id="firstHeading")

    text = soup.find(id = "bodyContent").find_all("p")#.find("a")
    #print(len(text))
   # print(response.url)
    for each in text:
        if len(each.text)<100:
           continue
        clean_text = Text_Cleaning(each.text)

        with open('Data/Scraped/wiki_data_5.txt','a') as f:
            for each_sent in clean_text.split('։'):
                
                
                #check number of words in sentence
                if len(each_sent)<3:
                    continue
                # print(each_sent)
                break_spaces = each_sent.strip()
         #       break_spaces = " ".join(break_spaces.split(" "))
                f.write("%s:\n" % break_spaces.replace("\n","").lstrip())

    
 
