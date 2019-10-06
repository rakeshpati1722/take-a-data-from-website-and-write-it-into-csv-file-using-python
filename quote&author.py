import urllib.request
import requests
from bs4 import BeautifulSoup
import csv


csv_file = open("b.csv",'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Author','Quote'])


url = 'https://www.goodreads.com/'
        
quote_from_good_read = urllib.request.urlopen(url)

soup = BeautifulSoup(quote_from_good_read)

div_tags = soup.find("div",class_='featureTeaserBox__quotesBox').find("div",class_="featureTeaserBox__quotesBoxQuote")

all_quotes = div_tags.findAll("div",class_="quoteText")

for i in all_quotes:
    qq = i.find(text=True)
    qq = qq.replace("\n",'')
    qw = qq.lstrip()
    q= qq.rstrip()
    aa = i.find("span",class_="authorOrTitle").find(text=True)
    aa = aa.replace("\n",'')
    aa = aa.lstrip()
    a = aa.rstrip()

    csv_writer.writerow([a,q])
csv_file.close()

    