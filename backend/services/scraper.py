import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url: str):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        response = requests.get(url, headers= headers)
        response.raise_for_status() 
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title_tag = soup.find('h1', {'id': 'firstHeading'})
        title = title_tag.text if title_tag else "Unknown Title"
       
        content_div = soup.find('div', {'id': 'bodyContent'})
        
        if not content_div:
            return None


        paragraphs = content_div.find_all('p')
        text_content = "\n".join([p.get_text() for p in paragraphs if p.get_text().strip()])
        
        return {
            "title": title,
            "text": text_content[:15000] 
        }

    except Exception as e:
        print(f"Error scraping URL: {e}")
        return None