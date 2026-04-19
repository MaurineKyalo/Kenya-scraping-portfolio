# 🇰🇪 PigiaMe Property Scraper

## What It Does
Automatically scrapes rental property listings from PigiaMe.co.ke
and exports clean, structured data to an Excel file.
Collects property title, price and location for all listings.

## Tools Used
- Python 3
- requests - fetching web pages
- BeautifulSoup4 - parsing HTML
- openpyxl - exporting to Excel

## How To Run
1. Install dependencies:
pip install requests beautifulsoup4 openpyxl

2. Run the scraper:
python pigiamescrapper_script.py

3. Find your data in:
kenya_properties.xlsx

## Sample Output
| Title | Price | Location |
|-------|-------|----------|
| 4 Bed House in Karen | KSh 400,000 | Karen,Nairobi |
| 5 Bed Villa in Runda | KSh 550,000 | Runda,Nairobi |

## What I Learned
- How to inspect HTML structure to find data
- Handling JavaScript vs static HTML sites
- Cleaning messy text data with Python
- Exporting scraped data to Excel professionally
- Debugging HTTP status codes 200, 403, 404
- Building defensive code that handles missing data

## Author
MaurineKyalo - Nairobi, Kenya