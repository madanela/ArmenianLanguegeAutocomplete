"""
funtions which removes unnecessary words, phrases, characters, symbols and returns cleaner text.
"""

import re

NonRedundantWords = ['ալ', 'ակ', 'աղ',  'աջ',
       'առ', 'ափ',  'դե', 'դի',  'ել', 'եմ', 'են', 'ես', 'եվ', 'ետ', 'եր', 'եւ', 'եք',
       'է', 'էգ',  'էի', 'էլ',  'էշ', 'էջ', 'էվ',
       'էր', 'թե', 'ի', 'իմ', 'իր', 'կա', 'ձի', 'ձև', 'մի',  'նա',  'ոճ', 'ոչ',
       'ով', 'որ', 'ու', 'ոք',  'չէ', 'չի', 'սա', 'սև', 'օդ', 'օձ',  'օր', 'և',  'ևս']

def Text_Cleaning(text):
    clean_text = re.sub("([\(\[\«]).*?([\)\]\»])", "\g<1>\g<2>", text)
    clean_text = re.sub("[\(\[\«].*?[\)\]\»]", " ", clean_text)
    clean_text = clean_text.replace('²',' քառակուսի')
    clean_text = clean_text.replace('³',' խորանարդ')
    clean_text = re.sub("[^\u0561-\u0587\u0531-\u0556\ ։]+",' ',clean_text)
    clean_text = re.sub(' +', ' ', clean_text)
    return " ".join([word for word in clean_text.split(' ') if len(word)>2 or word in NonRedundantWords]) #" ".join([w for w in clean_text.split(" ") if len(w)>2])

opt_treshold = 1.4
def Validate_corpus(clean_text,actual_text):
    return len(clean_text)<2 or len(actual_text)/len(clean_text) < opt_treshold
    
