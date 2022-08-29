from urllib import response
import feedparser
import requests
import urllib
import concurrent.futures
import os

allurls = 'https://comicstripblog.com/feed/?paged='

#Create empty list
comiclist = []

# Loop through pages of feeds and add dictionary of title:url for each comic
i=1
while (i<=1):
    urlpage = (allurls + str(i))
    f = feedparser.parse(urlpage)
    for feedentry in f.entries:
        comic = [feedentry.title, feedentry.media_content[1].get('url')]
        comiclist.append(comic)
      
    i=i+1
else:
    print("End of the loop")
        
#print list
""" print (comiclist) """

# list of only the urls
""" comicurls = "url"
list_of_urls = [comic_dict[comicurls] for comic_dict in comiclist]
 """
# List of only the titles
"""comictitles = "title"
list_of_titles = [comic_dict[comictitles] for comic_dict in comiclist]
 """
#function that downloads a file and saves it 
def download_image(location, file_name):
    # determine and get filetype extension
    h = requests.head(location, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    extension = content_type.split('/')
    
    #send GET request
    response = requests.get(location)
    #write file using extension
    with open(file_name+'.'+extension[1], "wb") as f:
            f.write(response.content)
    
# initializing bad_chars_list
bad_chars = [';', ':', '!', "*", "?"]

#download the files
for item in comiclist:
    location = item[1]
    file_name = ''.join(b for b in item[0] if not b in bad_chars)
   #Run download function  
    download_image(location, str(file_name))

