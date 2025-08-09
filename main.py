# main.py
import scraper
print("Using scraper.py from:", scraper.__file__)
from scraper import get_job_description
from nlp_processor import process_text

def calculate_match_score(job_keywords, resume_keywords):
    """Calculates a match score based on shared keywords."""
    job_set = set(job_keywords)
    resume_set = set(resume_keywords)

    matching_keywords = job_set.intersection(resume_set)

    if len(job_set) == 0:
        return 0, []

    score = (len(matching_keywords) / len(job_set)) * 100
    return score, list(matching_keywords)

if __name__ == "__main__":
    # Load resume text
    try:
        with open("my_resume.txt", "r", encoding="utf-8") as f:
            resume_text = f.read()
    except FileNotFoundError:
        print("Error: 'my_resume.txt' not found.")
        exit()

    resume_keywords = process_text(resume_text)

    # Get job description
    job_url = "https://www.ziprecruiter.com/c/Hermeus/Job/Software-Engineer-Intern-(HMI)-Fall-2025/-in-Atlanta,GA?jid=c0a95d47b7e23c10"  # Replace with a real job URL
    job_description = get_job_description(job_url)

    if job_description:
        job_keywords = process_text(job_description)
        score, matched_keywords = calculate_match_score(job_keywords, resume_keywords)

        print("\n--- Match Report ---")
        print(f"Resume and Job Description Match Score: {score:.2f}%")
        print("\nKeywords Found in Both:")
        for keyword in matched_keywords:
            print(f"- {keyword}")
    else:
        print("Failed to get job description. Check the scraper and URL.")
