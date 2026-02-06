import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url: str):
    try:
         # Wikipedia may block requests that look like bots,
        # so we mimic a real browser using a User-Agent header.
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        # Send a request to the Wikipedia page
        response = requests.get(url, headers= headers)
        # If the request failed (e.g., 404 or 500), raise an exception immediately
        response.raise_for_status() 
         # Parse the raw HTML into a structured format we can navigate
        soup = BeautifulSoup(response.content, 'html.parser')
        # Wikipedia stores the main article title inside an <h1> tag with id="firstHeading"
        title_tag = soup.find('h1', {'id': 'firstHeading'})
        # If for some reason we can't find the title, we use a safe fallback
        title = title_tag.text if title_tag else "Unknown Title"
       # The main article text is usually inside this div
        content_div = soup.find('div', {'id': 'bodyContent'})
         # If we can't find the main content, there's no point continuing
        if not content_div:
            return None


        paragraphs = content_div.find_all('p')
        text_content = "\n".join([p.get_text() for p in paragraphs if p.get_text().strip()])
         # Return structured data that other parts of your program can use
        # We also limit text length to avoid sending extremely large content downstream

        return {
            "title": title,
            "text": text_content[:15000] 
        }

    except Exception as e:
        print(f"Error scraping URL: {e}")
        return None