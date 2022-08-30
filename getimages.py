from urllib import response
import feedparser
import requests
import os

allurls = 'https://comicstripblog.com/feed/?paged='

#Create empty list
comiclist = []

# Loop through pages of feeds and add to list the title and url for each comic
i=1
while (i<=5):
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
    file_name = file_name +'.'+ extension[1]
    dir_path = 'images'
    with open(os.path.join(dir_path, file_name), "wb") as f:
            f.write(response.content)
    
# initializing bad_chars_list
bad_chars = [';', ':', '!', "*", "?"]

#download the files
for item in comiclist:
    location = item[1]
    #Remove bad chars from file name
    file_name = ''.join(b for b in item[0] if not b in bad_chars)
    #Run download function  
    download_image(location, str(file_name))

