from bs4 import BeautifulSoup
from urllib.request import urlopen

class GoogleNewsScraper:
    site = "https://news.google.com.ng/"
    def __init__(self):
        pass

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
    GoogleNewsScraper().scrape()