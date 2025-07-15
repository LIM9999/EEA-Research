import pandas as pd

# Load your Excel file (replace 'your_file.xlsx' and 'link' with actual names)
df = pd.read_excel("Webpages List(IDEAS schools) v2.xlsx", sheet_name="HERE")  # Or use pd.read_csv if CSV
link_col = 'Link'  # Change this to your actual column name

links = df[link_col].dropna().astype(str).str.strip()
formatted_links = [f'"{link}",' for link in links]
with open("formatted_links.txt", "w") as f:
    for line in formatted_links:
        f.write(line + "\n")

'''
# If you want all in one line (comma-separated, like a big array):
all_in_one_line = " ".join(formatted_links)
with open("formatted_links_one_line.txt", "w") as f:
    f.write(all_in_one_line)
'''

print("Done! Output written to formatted_links.txt")


