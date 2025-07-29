
# AI Job Application Automation Agent 🤖

This project automates job applications on LinkedIn and Naukri using Playwright in Python. It reads job descriptions, modifies your resume, and applies with a tailored version.

## 🛠️ Requirements

- Python 3.8+
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  playwright install
  ```

## ⚙️ Setup

1. Clone the repo or unzip the project.
2. Edit `config.py` with your credentials.
3. Place your base resume at `resume/base_resume.docx`.

## 🚀 Run

```bash
python main.py --job "Data Engineer"
```

## 🧠 What It Does

- Logs into LinkedIn and Naukri
- Searches for jobs matching the title
- Downloads job descriptions
- Customizes your resume
- Applies automatically
