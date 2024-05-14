from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import sys


class ParagraphsScraper:
    site = ""
    def __init__(self, site):
        self.site = site

    def scrape(self):
        req = Request(url=self.site, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req)

        html = response.read()
        soup = BeautifulSoup(html, "html.parser")

        for p in soup.find_all('p'):
            print(p.text, end = "\n\n")

if __name__ == "__main__":
    args = sys.argv[1:]
    if(len(args) < 1):
        print("Error! no url passed")
        sys.exit()
    ParagraphsScraper(args[0]).scrape()
