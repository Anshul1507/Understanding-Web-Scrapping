#youtube link : https://www.youtube.com/watch?v=ng2o98k983k

from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://coreyms.com').text

#naming of csv file 
csv_file = open('ms_corey_csv_file.csv','w')

#defining structure
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','video_link'])

soup = BeautifulSoup(source,'lxml')

#print full content
print(soup.prettify())

#find first article from content
article = soup.find('article')
print(article.prettify())

#if find more than one article that is in array list format
article = soup.find_all('article')
print(article)  #No use of prettify as data are in the form of array list

#fetching headline from first content
headline = article.h2.a.text
print(headline)

#fetching article para content from first content
summary = article.find('div',class_='entry-content').p.text
print(summary)

#fetching youtube video link from first content
youtube_link = article.find('iframe',class_='youtube-player')['src']
#splitting into to get youtube video id
yt_id = youtube_link.split('/')[4]
yt_id = yt_id.split('?')[0]
#now append that yt id with watch youtube link
yt_link = f'https://youtube.com/watch?v={yt_id}'
print(yt_link)

#For Fetching Main Data from whole ArrayList
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    try:
        youtube_link = article.find('iframe',class_='youtube-player')['src']
        yt_link = youtube_link.split('/')[4]
        yt_link = yt_link.split('?')[0]
        yt_link = f'https://youtube.com/watch?v={yt_link}'
    except Exception as e:
        yt_link = 'None'
        
    print(yt_link)
    print()
    #putting data in the structure
    csv_writer.writerow([headline,yt_link])

csv_file.close()
