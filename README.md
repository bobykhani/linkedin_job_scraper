
# LinkedIn Job Scraper and Analyzer

This project is a Python-based tool to scrape job listings from LinkedIn and analyze them based on your CV. It uses Selenium for scraping and OpenAI's GPT model for analyzing how well your qualifications match the job descriptions. The tool can be customized to fit various job titles and locations and provides suggestions on how to improve your chances of landing a job.

## Features

- **Scrapes job listings** from LinkedIn based on job title and location.
- **Analyzes job descriptions** using OpenAI GPT to match your qualifications from a PDF CV.
- **CSV output** of job listings and analysis results.
- **Object-Oriented Design** for better scalability and maintenance.

## Project Structure

```
job_scraper/
│
├── scraper/
│   ├── __init__.py               # Makes the directory a package
│   ├── job_scraper.py            # Class for scraping jobs from LinkedIn
│   └── utils.py                  # Utility functions (scrolling, PDF extraction, etc.)
│
├── analysis/
│   ├── __init__.py               # Makes the directory a package
│   └── job_analyzer.py           # Class for analyzing jobs using OpenAI
│
├── data/                         # Directory for storing downloaded jobs and CV
│   ├── CV_En_BABAK.pdf           # Your CV (as an example)
│
├── tests/
│   ├── test_scraper.py           # Unit tests for scraping functionality
│   ├── test_analysis.py          # Unit tests for analyzing jobs
│
├── main.py                       # Main entry point to run the application
├── requirements.txt              # Required Python packages
└── README.md                     # This README file
```

## Prerequisites

Before you can run the project, you need to install the following dependencies:

1. Python 3.7+
2. Google Chrome and [ChromeDriver](https://chromedriver.chromium.org/downloads)
3. An [OpenAI API key](https://beta.openai.com/signup/)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-repo/job_scraper.git
    cd job_scraper
    ```

2. **Install the required packages**:

    You can install the dependencies listed in `requirements.txt` using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up ChromeDriver**:

    Download and install the correct version of [ChromeDriver](https://chromedriver.chromium.org/downloads) for your operating system. Ensure `chromedriver` is in your system's PATH or provide the path to it in the `JobScraper` class.

4. **Add your OpenAI API key**:

    In the file `analysis/job_analyzer.py`, replace `'your-api-key'` with your actual OpenAI API key:

    ```python
    job_analyzer = JobAnalyzer(api_key='your-api-key')
    ```

## Usage

1. **Run the scraper and analyzer**:

    The main file will scrape job listings from LinkedIn and analyze them using your CV:

    ```bash
    python main.py
    ```

2. **Specify a job title and location**:

    The `JobScraper` can be configured to search for specific jobs in specific locations. By default, it's set to search for "Data Engineer" jobs in "Montreal, Quebec, Canada", but you can modify this in the `main.py` file.

    ```python
    job_scraper.input_search_details("Data Engineer", "Montreal, Quebec, Canada")
    ```

3. **Results**:

    After the script runs, you’ll find the job analysis results saved as `job_analysis_results.csv` in the project directory. This file contains the job listings and an analysis of how well your CV matches each job description.

## Example Output

An example of the job analysis output in `job_analysis_results.csv`:

| Job Title        | Company         | Location               | Analysis                                          |
|------------------|-----------------|------------------------|--------------------------------------------------|
| Data Engineer    | ABC Tech        | Montreal, QC           | Your qualifications match 80%. Suggested skills...|
| Senior Data Analyst | XYZ Analytics   | Toronto, ON            | You need more experience with cloud technologies. |
| ...              | ...             | ...                    | ...                                              |

## Customization

- **Change search criteria**: Update `job_scraper.input_search_details()` in `main.py` to modify the job title and location you want to search for.
- **Update your CV**: Replace the example CV (`CV_En_BABAK.pdf`) in the `data/` directory with your own CV.

<!-- ## Testing

Unit tests are available in the `tests/` directory. To run the tests:

```bash
pytest tests/
```

## Contributing

Feel free to submit issues and pull requests! Contributions are welcome to improve the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. -->
