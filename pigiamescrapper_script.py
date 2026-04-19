import requests
from bs4 import BeautifulSoup
import openpyxl

def clean(text):
    return " ".join(text.split()) if text else "N/A"

def scrape_pigiame():
    print("Scraping PigiaMe properties...")
    
    url = "https://www.pigiame.co.ke/houses-for-rent"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    listings = soup.find_all("div", class_="listing-card")
    print(f"Found {len(listings)} properties")
    
    results = []
    
    for listing in listings:
        title = listing.find("div", class_="listing-card__header__title")
        price = listing.find("div", class_="listing-card__info-bar__price")
        location = listing.find("div", class_="listing-card__header__location")
        loc_parts = [t.strip() for t in location.get_text().split("\n") if t.strip()]
        loc = ",".join(loc_parts) if location else "N/A"
        
        results.append([
            clean(title.text) if title else "N/A",
            clean(price.text) if price else "N/A",
            loc
        ])
    
    return results

def save_to_excel(data, filename):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Properties"
    
    ws.append(["Title", "Price", "Location"])
    
    for row in data:
        ws.append(row)
    
    wb.save(filename)
    print(f"Saved {len(data)} properties to {filename}")

data = scrape_pigiame()
save_to_excel(data, "kenya_properties.xlsx")