import requests
from bs4 import BeautifulSoup
from getTheSoup import getTheSoup
import csv

# URL for the SURF Research Projects page
url = "https://engineering.purdue.edu/Engr/Research/EURO/SURF/Research/Y2025"

# Use your getTheSoup function to retrieve the BeautifulSoup object and headers
soup, headers = getTheSoup(url)

# Find all divs containing research-project data
projects = soup.find_all("div", class_="research-project")

# Open a CSV file to write the extracted project data
with open("SURF_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    # Write the header row, adding "More Info" as a new column
    writer.writerow([
        "Name",
        "Description",
        "Campus",
        "Research Categories",
        "Citizenship Req",
        "Preferred Major",
        "School/Dept",
        "Professor",
        "More Info"
    ])

    # Iterate over each "research-project" div
    for project in projects:
        # 1. Extract the Name (h3.research-title)
        title_tag = project.find("h3", class_="research-title")
        name = title_tag.get_text(strip=True) if title_tag else "N/A"

        # Default/placeholder values
        description = "N/A"
        campus = "N/A"
        research_cat = "N/A"
        citizenship_req = "N/A"
        preferred_major = "N/A"
        school_dept = "N/A"
        professor = "N/A"
        more_info = "N/A"

        # 2. Each row has a label and value column we can parse
        rows = project.find_all("div", class_="row")
        for row in rows:
            label_div = row.find("div", class_="col-sm-3 label")
            value_div = row.find("div", class_="col-sm-9 value")

            if not label_div or not value_div:
                continue  # skip if structure doesn't match

            label_text = label_div.get_text(strip=True)
            value_text = value_div.get_text(" ", strip=True)

            if label_text == "Description:":
                description = value_text
            elif label_text == "Campus:":
                campus = value_text
            elif label_text == "Research categories:":
                research_cat = value_text
            elif label_text == "Citizenship requirements:":
                citizenship_req = value_text
            elif label_text == "Preferred major(s):":
                preferred_major = value_text
            elif label_text in ["School/Dept.:", "School/Dept."]:
                # Some pages might have a small difference in punctuation
                school_dept = value_text
            elif label_text == "Professor:":
                # Professor name might be in multiple <span> tags
                prof_spans = value_div.find_all("span")
                # Join the text from each <span> for a full name
                professor = " ".join(span.get_text(strip=True) for span in prof_spans) or "N/A"

        # 3. Find the "More information:" link, usually in a <p> after the row divs
        #    This might differ in your actual HTML structure, so adjust if needed.
        #    Here, we look for <p> containing "More information" and then <a> tag.
        info_paragraphs = project.find_all("p")
        for p_tag in info_paragraphs:
            # Check if paragraph has text "More information:"
            if "More information:" in p_tag.get_text():
                link_tag = p_tag.find("a")
                if link_tag:
                    more_info = link_tag.get("href", "N/A")
                break  # assume only one "More information" section per project

        # Write the extracted fields into the CSV
        writer.writerow([
            name,
            description,
            campus,
            research_cat,
            citizenship_req,
            preferred_major,
            school_dept,
            professor,
            more_info
        ])

print("Data extraction complete. Check the 'SURF_data.csv' file.")
