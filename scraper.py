import requests
from bs4 import BeautifulSoup
import csv
import time
from datetime import datetime

class WebScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def get_page_content(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            print(f"Error fetching page: {e}")
            return None

    def scrape_data(self, max_pages=5):
        all_data = []
        
        for page in range(1, max_pages + 1):
            url = f"{self.base_url}/page/{page}"
            soup = self.get_page_content(url)
            
            if not soup:
                continue

            # Example: Scraping article titles and dates
            articles = soup.find_all('article')
            
            for article in articles:
                title = article.find('h2').text.strip() if article.find('h2') else 'No title'
                date = article.find('time').text.strip() if article.find('time') else 'No date'
                
                all_data.append({
                    'title': title,
                    'date': date,
                    'url': url
                })
            
            # Be nice to the server
            time.sleep(2)
            
        return all_data

    def save_to_csv(self, data, filename=None):
        if not filename:
            filename = f"scraped_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                if not data:
                    print("No data to save")
                    return
                
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
                print(f"Data successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving data: {e}")

def main():
    # Example usage
    target_url = "https://example.com"  # Replace with your target website
    scraper = WebScraper(target_url)
    
    # Scrape the data
    scraped_data = scraper.scrape_data(max_pages=3)
    
    # Save the data
    scraper.save_to_csv(scraped_data)

if __name__ == "__main__":
    main() 