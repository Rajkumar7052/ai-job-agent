
from playwright.sync_api import sync_playwright

class NaukriBot:
    def __init__(self, username, password, resume_modifier, job_logger):
        self.username = username
        self.password = password
        self.resume_modifier = resume_modifier
        self.job_logger = job_logger

    def search_and_apply(self, job_title):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://www.naukri.com/mnjuser/login")

            page.fill("input[type='text']", self.username)
            page.fill("input[type='password']", self.password)
            page.click("button[type='submit']")
            page.wait_for_timeout(5000)

            page.goto("https://www.naukri.com/")
            page.fill("input[placeholder='Skills, Designations, Companies']", job_title)
            page.keyboard.press("Enter")
            page.wait_for_timeout(5000)

            jobs = page.query_selector_all("article.jobTuple")
            for job in jobs[:3]:
                job_desc = job.inner_text()
                modified_resume = self.resume_modifier.modify(job_desc)
                self.job_logger.log(job_desc)
            browser.close()
