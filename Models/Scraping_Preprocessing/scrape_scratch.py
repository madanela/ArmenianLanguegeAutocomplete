import requests
from bs4 import BeautifulSoup
import random
import re
from ArmScraping import Text_Cleaning
hy_url = 'https://hy.wikipedia.org/wiki/Special:Random'


corpus = []
mem = set()
# def Text_Cleaning(text):
#     clean_text = re.sub("([\(\[\«]).*?([\)\]\»])", "\g<1>\g<2>", text)
#     clean_text = re.sub("[\(\[\«].*?[\)\]\»]", " ", clean_text)
#     clean_text = clean_text.replace('²',' քառակուսի')
#     clean_text = clean_text.replace('³',' խորանարդ')
#     clean_text = re.sub("[^\u0561-\u0587\u0531-\u0556\ ։]+",' ',clean_text)
#  #   clean_text = re.sub(r'\b[\u0561-\u0587\u0531-\u0556{1-3}]\b',' ',clean_text)
#    # reduntant_words = ["են","էլ","սա","ոչ","մի","կա","է","եմ","ես","որ","ոք","ով","օր","ու","և","ուր","ում"]
#     clean_text = re.sub(' +', ' ', clean_text)
#     return clean_text #" ".join([w for w in clean_text.split(" ") if len(w)>2])


# Text_Cleaning("Մեքենան զարգացնում է առավելագույնը 60 կմ/ժ արագություն։")
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

    
 