from scraper.job_scraper import JobScraper
from analysis.job_analyzer import JobAnalyzer
from scraper.utils import extract_text_from_pdf
import pandas as pd

def main():
    # Step 1: Scrape LinkedIn jobs
    job_scraper = JobScraper(headless=False)
    job_scraper.navigate_to_linkedin()
    job_scraper.input_search_details("Data Engineer", "Montreal, Quebec, Canada")
    jobs = job_scraper.scrape_jobs()
    job_scraper.close()

    # Convert jobs to a DataFrame
    jobs_df = pd.DataFrame(jobs)

    # Step 2: Analyze the scraped jobs with your CV
    cv_text = extract_text_from_pdf('./data/CV_En_BABAK.pdf')
    job_analyzer = JobAnalyzer(api_key='your-api-key')
    job_analysis = job_analyzer.analyze_multiple_jobs(jobs_df, cv_text)

    # Step 3: Save the analysis results
    analysis_df = pd.DataFrame(job_analysis)
    analysis_df.to_csv('job_analysis_results.csv', index=False)

if __name__ == "__main__":
    main()
