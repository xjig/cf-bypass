import cloudscraper
from bs4 import BeautifulSoup

def crawl(url):
    scraper = cloudscraper.create_scraper()
    try:
        response = scraper.get(url)
        if response.status_code == 200:
            print(f"✔️ {url}")
            return response.text
        else:
            print(f"error {response.status_code}")
            return None
    except Exception as e:
        print(f"error {e}")
        return None

def contnent(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string if soup.title else 'no title found'
    print(f"title:{title}")

if __name__ == "__main__":
    url = "https://google.com" #put ur url u want tocrawl here
    html_content = crawl(url)
    if html_content:
        contnent(html_content)
