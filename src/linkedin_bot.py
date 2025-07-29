
from playwright.sync_api import sync_playwright

class LinkedInBot:
    def __init__(self, username, password, resume_modifier, job_logger):
        self.username = username
        self.password = password
        self.resume_modifier = resume_modifier
        self.job_logger = job_logger

    def search_and_apply(self, job_title):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
            )
            page = context.new_page()
            page.goto("https://www.linkedin.com/login")

            # Wait for login fields
            page.wait_for_selector("input#username", timeout=10000)

            # Perform login
            page.fill("input#username", self.username)
            page.fill("input#password", self.password)
            page.click("button[type='submit']")

            # Add a wait for navigation
            page.wait_for_load_state("networkidle")

            # Navigate to job search
            page.goto(f"https://www.linkedin.com/jobs/search/?keywords={job_title}")
        # Continue with job application logic...
            page.keyboard.press("Enter")
            page.wait_for_timeout(50000)

            jobs = page.query_selector_all("ul.jobs-search__results-list li")
            for job in jobs[:3]:
                job.click()
                page.wait_for_timeout(20000)
                job_desc = page.inner_text("div.description")
                modified_resume = self.resume_modifier.modify(job_desc)
                self.job_logger.log(job_desc)
            browser.close()
            
