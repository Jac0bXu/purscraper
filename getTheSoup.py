import requests
from bs4 import BeautifulSoup

def getTheSoup(inputUrl):
    # url = "https://engineering.purdue.edu/Engr/Research/EURO/SURF/Research/Y2025"
    url = inputUrl
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)

    # Check if request was successful
    if response.status_code == 200:
        html_content = response.text
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        exit()

    soup = BeautifulSoup(html_content, "html.parser")
    return soup, headers

