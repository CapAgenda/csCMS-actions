import feedparser

url = 'https://comicstripblog.com/feed/'

f = feedparser.parse(url)

""" Print number of entries from feed """
print(len(f['entries']))

""" Get specific data for multiple entries """
for feedentry in f.entries:
    print(feedentry.title)
    print(feedentry.media_content[1].get('url'))
