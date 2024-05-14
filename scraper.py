from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

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

class TribuneNGScraper:
    site = "https://tribuneonlineng.com/"
    def __init__(self):
        pass
    
    def scrape(self):
        req = Request(url=self.site, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")

        for h3 in soup.find_all('h3', class_='jeg_post_title'):
            a_tag = h3.find('a')
            if a_tag and a_tag.text != "":
                news_title = a_tag.text
                news_url = a_tag.get('href')
                print(news_title)
                print(news_url, end="\n\n")


if __name__ == "__main__":
    TribuneNGScraper().scrape()