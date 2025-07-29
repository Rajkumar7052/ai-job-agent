
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
            page = browser.new_page()
            page.goto("https://www.linkedin.com/in/raj-maurya-gcp-data-engineer/")

            page.fill("input#username", self.username)
            page.fill("input#password", self.password)
            page.click("button[type='submit']")

            page.wait_for_url("https://www.linkedin.com/feed/")
            page.goto("https://www.linkedin.com/jobs")
            page.fill("input[aria-label='Search jobs']", job_title)
            page.keyboard.press("Enter")
            page.wait_for_timeout(10000)

            jobs = page.query_selector_all("ul.jobs-search__results-list li")
            for job in jobs[:3]:
                job.click()
                page.wait_for_timeout(20000)
                job_desc = page.inner_text("div.description")
                modified_resume = self.resume_modifier.modify(job_desc)
                self.job_logger.log(job_desc)
            browser.close()
