import pandas as pd
import requests
import csv

# === Configuration ===
input_file = "Webpages List(IDEAS schools) v2.xlsx"
sheet_name = "HERE"
link_col = "Link"
# ======

df = pd.read_excel(input_file, sheet_name=sheet_name)
links = (
    df[link_col]
    .dropna()
    .astype(str)
    .str.strip()
    .str.strip('"')
    .tolist()
)


results = []
for idx, url in enumerate(links, start=1):
    try:
        response = requests.head(url, allow_redirects=True, timeout=15)
        status = response.status_code
    except requests.RequestException as e:
        status = f"ERROR: {e}"
    print(f"{idx}: {url} -> {status}")
    results.append((idx, url, status))

#Save results to CSV
output_file = "link_statuses_indexed.csv"
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Index", "URL", "Status"]);
    writer.writerows(results)

print(f"Done! Results written to {output_file}")
