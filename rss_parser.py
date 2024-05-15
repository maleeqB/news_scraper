import feedparser

url = "https://tribuneonlineng.com/feed"
feed = feedparser.parse(url)

for item in feed.entries:
    print(item.title)
    print(item.link)
    print(item.published, end= "\n\n")
