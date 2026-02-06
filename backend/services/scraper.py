import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title_tag = soup.find('h1', {'id': 'firstHeading'})
        title = title_tag.text if title_tag else "Unknown Title"
       
        content_div = soup.find('div', {'id': 'bodyContent'})
        
        paragraphs = content_div.find_all('p')
        text_content = "\n".join([p.get_text() for p in paragraphs if p.get_text().strip()])
        
        return {
            "title": title,
            "text": text_content[:15000] 
        }

    except Exception as e:
        print(f"Error scraping URL: {e}")
        return None