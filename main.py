
import argparse
from src.linkedin_bot import LinkedInBot
from src.naukri_bot import NaukriBot
from src.resume_modifier import ResumeModifier
from src.job_logger import JobLogger
import config

def run(job_title):
    resume_modifier = ResumeModifier("resume/base_resume.docx")
    job_logger = JobLogger()

    # LinkedIn
    linkedin_bot = LinkedInBot(config.LINKEDIN_USERNAME, config.LINKEDIN_PASSWORD, resume_modifier, job_logger)
    linkedin_bot.search_and_apply(job_title)

    # Naukri
    naukri_bot = NaukriBot(config.NAUKRI_USERNAME, config.NAUKRI_PASSWORD, resume_modifier, job_logger)
    naukri_bot.search_and_apply(job_title)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Job Application Automation Agent")
    parser.add_argument("--job", type=str, required=True, help="Job title to search and apply")
    args = parser.parse_args()
    run(args.job)
