import requests
import csv

# Full list of URLs(example)
department_page_urls = [
" https://www.uni-goettingen.de/de/duz-brosch%C3%BCre/646499.html ",
" https://www.uni-goettingen.de/de/duz-brosch%C3%BCre/646499.html "
]

results = []
for idx, url in enumerate(department_page_urls, start=1):
    try:
        r = requests.head(url, allow_redirects=True, timeout=15)
        status = r.status_code
    except requests.RequestException as e:
        status = f"ERROR: {e}"
    print(f"{idx}: {url} -> {status}")
    results.append((idx, url, status))

# Output CSV
with open("link_statuses_indexed.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Index", "URL", "Status"])
    writer.writerows(results)
