Purscraper

A simple Python web scraper that retrieves information about faculty members from Purdue University's School of Electrical and Computer Engineering (ECE) website. The scraped data includes names, emails, research interests, and associated links, then writes everything to a CSV file.

TABLE OF CONTENTS
1. Prerequisites
2. Installation
3. Usage
4. Project Structure
5. How it Works
6. Contributing
7. License

PREREQUISITES
- Python 3.7 or higher
- pip
- Basic understanding of Python and running scripts in the terminal/command line

INSTALLATION
1. Clone the Repository:
   git clone https://github.com/your-username/purscraper.git
   cd purscraper

2. Create a Virtual Environment (Recommended):
   python -m venv venv
   source venv/bin/activate    # For macOS/Linux
   venv\\Scripts\\activate     # For Windows

3. Install Dependencies:
   pip install -r requirements.txt

USAGE
1. Run the Scraper:
   python purscraper.py
   This script will send a request to the Purdue ECE Faculty page and attempt to scrape:
   - Name
   - Email
   - Research summary
   - Primary interests (and links)
   - Other interests
   - Secondary link info

2. Check the Results:
   After running, a 'professors_data.csv' file is created or updated in the current directory.
   Open or import it with spreadsheet software or a text editor to review the scraped data.

PROJECT STRUCTURE
purscraper/
├─ README.md
├─ purscraper.py
├─ requirements.txt
└─ professors_data.csv

- purscraper.py contains the main scraping logic.
- requirements.txt lists the Python dependencies.
- professors_data.csv is the output CSV file containing the scraped data.

HOW IT WORKS
1. Web Request:
   The script uses the requests library to send an HTTP GET request to the Purdue ECE Faculty page.

2. HTML Parsing:
   The BeautifulSoup library parses the retrieved HTML content.

3. Data Extraction:
   The script locates relevant elements (name, email, research interest, related links) by searching specific HTML tags and class attributes.

4. Detailed Page Fetching:
   If a link to a professor’s detail page is found, the script makes an additional HTTP GET request to gather more information (Primary and Not Primary areas plus their corresponding links).

5. CSV Output:
   The script compiles all data into a structured CSV format, including:
   - Name
   - Email
   - Research
   - Primary
   - Not Primary
   - Primary Link
   - Sub Link

CONTRIBUTING
Contributions are welcome. If you have suggestions, bug reports, or want to add new features, please open an issue or submit a pull request.

1. Fork this repository
2. Create your feature branch: git checkout -b feature/awesome-feature
3. Commit your changes: git commit -m "Add awesome feature"
4. Push to the branch: git push origin feature/awesome-feature
5. Open a Pull Request

LICENSE
This project is licensed under the MIT License (see LICENSE file). You are free to use, modify, and distribute this project.
