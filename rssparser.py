import feedparser

allurls = 'https://comicstripblog.com/feed/?paged='

#Create empty list
comiclist = []

# Loop through pages of feeds and add dictionary of title:url for each comic
i=1
while (i<=5):
    urlpage = (allurls + str(i))
    f = feedparser.parse(urlpage)
    for feedentry in f.entries:
        comic = {feedentry.title : feedentry.media_content[1].get('url')}
        comiclist.append(comic)
      
    i=i+1
else:
    print("End of the loop")

#print list
print (comiclist)
 

