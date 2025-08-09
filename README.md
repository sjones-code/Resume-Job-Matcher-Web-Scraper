# Resume and Job Matcher Web Scraper

This project scrapes job descriptions from job listing websites and compares them with your resume to calculate a keyword match score. It helps you quickly assess how well your resume fits a particular job posting. However, you can also use this for any application involving comparing texts to texts from a URL.

## Features

- Scrapes job descriptions from websites (currently supports ZipRecruiter and Indeed)
- Processes text to extract meaningful keywords using NLP
- Calculates a match score based on overlapping keywords between job description and resume
- Command-line interface for easy use

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Google Chrome browser installed
- [ChromeDriver](https://chromedriver.chromium.org/) compatible with your Chrome version (or use `undetected-chromedriver` as in the project)
- Required Python packages (see below)

### Installation

1. Clone this repository: 
   ```bash
   git clone https://github.com/sjones-code/Resume-Job-Matcher-Web-Scraper.git
   cd Resume-Job-Matcher-Web-Scraper

2. Install Python dependencies:
   ```bash
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')

3. Make sure to add your resume text to my_resume.txt.

4. Update main.py with the job posting URL you want to analyze.

### Usage
Only need to run the main script:
  python main.py

Output: a match score and list keywords that appear in both your resume and the job description.

### Notes
- (VERY IMPORTANT) Make sure the job URL is accessible and the scraper supports its page structure.
    - Use websites like ZipRecruiter and not LinkedIn or Indeed as they require prior signin or have bot protection like CloudFlare
- Adjust the scraper if you use different job sites or if page layouts change.
- The match score is a basic keyword overlap metric — further improvements can be made.

### Liscence
This project is entirely open source and free to use!
