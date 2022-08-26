import feedparser

allurls = 'https://comicstripblog.com/feed/?paged='

i=1
while (i<=5):
    urlpage = (allurls + str(i))
    f = feedparser.parse(urlpage)
    for feedentry in f.entries:
        print(feedentry.title)
        print(feedentry.media_content[1].get('url'))
    i=i+1
else:
    print("End of the loop")
 

