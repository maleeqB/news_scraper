from bs4 import BeautifulSoup
from urllib.request import urlopen

class Scraper:
    site = ""
    def __init__(self, site):
        self.site = site

    def scrape(self):
        response = urlopen(self.site)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")

        for tag in soup.find_all('a'):
            url = tag.get('href')
            if url and 'articles' in url and tag.text != "":
                news_url = self.site + url[2:]
                print(tag.text)
                print(news_url, end="\n\n")

if __name__ == "__main__":
    Scraper('https://news.google.com.ng/').scrape()