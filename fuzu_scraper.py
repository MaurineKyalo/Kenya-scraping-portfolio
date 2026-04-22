import requests
from bs4 import BeautifulSoup
import openpyxl

def clean(text):
    return " ".join(text.split()) if text else "N/A"

def scrape_fuzu():
    print("Scraping Fuzu jobs...")
    url = "https://www.fuzu.com/kenya/jobs"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    job_list = soup.find("section", class_="job-list")
    if not job_list:
        print("Not found!")
        return []
    jobs = job_list.find_all("a", class_="b2c-card")
    print(f"Found {len(jobs)} jobs")
    results = []
    for job in jobs:
        company = clean(job.get("company_slug", "N/A")).replace("-", " ").title()
    
    # Title — get from first heading inside card
        title_tag = job.find("h3") or job.find("h2") or job.find("h4")
        title = clean(title_tag.text) if title_tag else clean(job.get("aria-label", "N/A"))
    
    # Location — get visible text spans
        spans = job.find_all("span")
        location = "N/A"
        for span in spans:
            text = clean(span.text)
            if text and len(text) > 3 and text != "N/A":
                location = text
                break
    
    # Description
        desc = job.get("description", "N/A")
        if desc != "N/A":
            desc = clean(BeautifulSoup(desc, "html.parser").get_text())[:150]
    
        results.append([title, company, location, desc])
    return results

def save_to_excel(data, filename):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Kenya Jobs"
    ws.append(["Job Title", "Company", "Location", "Description"])
    for row in data:
        ws.append(row)
    wb.save(filename)
    print(f"Saved {len(data)} jobs to {filename}")

data = scrape_fuzu()
save_to_excel(data, "kenya_jobs.xlsx")