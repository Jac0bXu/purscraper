import requests
from bs4 import BeautifulSoup
import csv
import time

url = "https://engineering.purdue.edu/ECE/Research/People/Faculty"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    html_content = response.text
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    exit()

soup = BeautifulSoup(html_content, "html.parser")
profs = soup.find_all("div", class_="col-8 col-sm-9 list-info")

with open("professors_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # Updated header to include "Sub Link"
    writer.writerow(["Name", "Email", "Research", "Primary", "Not Primary", "Primary Link", "Sub Link"])
    ctr = 1
    for prof in profs:
        list_name = prof.find("div", class_="col-12 list-name")
        name_tag = list_name.find("a") if list_name else None
        name = name_tag.get_text(strip=True) if name_tag else "N/A"
        link = name_tag.get("href") if name_tag else None

        # Default values if info is not found
        email = "N/A"
        research = "N/A"
        primary = []
        not_primary = []
        primary_link = []
        sub_link = []

        # Extract email
        list_email = prof.find("div", class_="email")
        if list_email is not None:
            email_tag = list_email.find("a")
            email = email_tag.get_text(strip=True) if email_tag else "N/A"

        # Fetch detail page if link exists
        if link:
            detail_response = requests.get(link, headers=headers)
            if detail_response.status_code == 200:
                detail_html_content = detail_response.text
            else:
                print(f"Failed to retrieve the detail page. Status code: {detail_response.status_code}")
                continue
            prof_detail = BeautifulSoup(detail_html_content, "html.parser")

            research_tag = prof_detail.find("p", class_="profile-research")
            if research_tag:
                research = research_tag.get_text(strip=True)

            primary_tags = prof_detail.find_all("li", class_="primary")
            if primary_tags:
                for primary_tag in primary_tags:
                    list_primary = primary_tag.find("a")
                    if list_primary:
                        primary_text = list_primary.get_text(strip=True)
                        plink = list_primary.get("href")
                        if plink:
                            # Extract the substring after the last slash
                            plink_after_slash = plink.split("/")[-1]

                            primary.append(primary_text)
                            primary_link.append(plink)  # Store the full link
                            sub_link.append(plink_after_slash)  # Store the substring after slash

            not_primary_tags = prof_detail.find_all("li", class_="not-primary")
            if not_primary_tags:
                for not_primary_tag in not_primary_tags:
                    not_primary.append(not_primary_tag.get_text(strip=True))

        # Convert lists to comma-separated strings
        primary_str = ", ".join(primary) if primary else ""
        not_primary_str = ", ".join(not_primary) if not_primary else ""
        primary_link_str = ", ".join(primary_link) if primary_link else ""
        sub_link_str = ", ".join(sub_link) if sub_link else ""

        # Write the data to the CSV file
        writer.writerow([name, email, research, primary_str, not_primary_str, primary_link_str, sub_link_str])
        print(f'professor #{ctr} : {name} finished')
        ctr += 1

print("Data extraction complete. Check the 'professors_data.csv' file.")
