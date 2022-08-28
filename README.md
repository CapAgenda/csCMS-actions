# cscms-actions
github actions repository

- rssparser.py will get the title and image url for a designated number of pages in an rss feed from wordpress.
- It will then create a list of dictionaries that include the titles and image urls. [{comicTitle : comicWordpressURL}, ...]

In progress:
- the workflow will then push the the image associated with each url into an images directory on the respository.
