# 🇰🇪 Fuzu Kenya Jobs Scraper

## What It Does
Automatically scrapes live job listings from
Fuzu.com/kenya and exports clean structured
data to Excel. Collects job title, company
and description for all listings.

## Tools Used
- Python 3
- requests - fetching web pages
- BeautifulSoup4 - parsing HTML
- openpyxl - exporting to Excel

## How To Run
1. Install dependencies:
pip install requests beautifulsoup4 openpyxl

2. Run the scraper:
python fuzu_scraper.py

3. Find your data in:
kenya_jobs.xlsx

## Sample Output
| Job Title | Company | Description |
|-----------|---------|-------------|
| ERP Assistant | Printpak Kenya | Seeking detail oriented... |
| Marketing Officer | Sipranda Capital | Results driven marketer... |

## What I Learned
- Identifying JavaScript vs static HTML sites
- Finding data in HTML attributes vs text
- Searching multiple tag types simultaneously
- Cleaning HTML from description text
- Testing multiple sites before committing
- Building competitive intelligence scripts

## Author
MaurineKyalo - Nairobi, Kenya