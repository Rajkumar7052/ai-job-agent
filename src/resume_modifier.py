
from docx import Document
import uuid
import os

class ResumeModifier:
    def __init__(self, resume_path):
        self.resume_path = resume_path

    def modify(self, job_description):
        doc = Document(self.resume_path)
        doc.add_paragraph(f"Modified for: {job_description[:100]}...")

        new_filename = f"resume/modified_resume_{uuid.uuid4().hex[:6]}.docx"
        doc.save(new_filename)
        return new_filename
