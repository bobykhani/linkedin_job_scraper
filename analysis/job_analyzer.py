import time
from openai import OpenAI

class JobAnalyzer:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def analyze_job(self, cv_text, job_title, company, location, description):
        prompt = f"""
        I have the following CV:
        {cv_text}
        
        Now analyze the following job description for the role of '{job_title}' at '{company}' located in '{location}'.
        Please provide the following:
        1. A match score based on my qualifications.
        2. Key skills or qualifications I meet or don't meet.
        3. Suggestions on how to improve my chances of getting the job.

        Job Description:
        {description}
        """
        response = self.client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {"role": "system", "content": "You are a helpful assistant that analyzes job descriptions and compares them to CVs."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()

    def analyze_multiple_jobs(self, jobs_df, cv_text):
        analysis_results = []
        for index, job in jobs_df.iterrows():
            analysis = self.analyze_job(cv_text, job['Job Title'], job['Company'], job['Location'], job['Description'])
            analysis_results.append({
                'Job Title': job['Job Title'],
                'Company': job['Company'],
                'Location': job['Location'],
                'Analysis': analysis
            })
            time.sleep(2)
        return analysis_results
