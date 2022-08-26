import feedparser

url = 'https://comicstripblog.com/feed/'

f = feedparser.parse(url)

""" Print number of entries from feed """
print(len(f['entries']))


""" Print key and values of first entry """
""" for k, v in f['entries'][0].items():
    print(k + " = " + str(v)) """

""" Get specific data of 'title' and 'media_content url' for first entry """
""" print(f['entries'][0].title)
print(f['entries'][0].media_content[1]) """

""" Get specific data for multiple entries """
for feedentry in f.entries:
    print(feedentry.title)
    print(feedentry.get("media_content[1]" , ""))
