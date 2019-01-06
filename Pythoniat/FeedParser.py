import feedparser

# d = feedparser.parse('https://www.nasa.gov/content/nasa-rss-feeds')

for p in d.entries :
    print(p.title + ":" + p.link + "\n")


