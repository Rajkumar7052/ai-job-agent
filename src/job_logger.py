
class JobLogger:
    def __init__(self):
        self.log_file = "applied_jobs.txt"

    def log(self, job_description):
        with open(self.log_file, "a") as f:
            f.write(f"Applied to job:\n{job_description[:300]}\n{'-'*40}\n")
