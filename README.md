# Opportunity-Search-Tool

A data-driven approach to job hunting. This project includes resume and cover letter templates, an application tracker, helpful scripts, and visual insights into outreach performance—showcasing organization, strategy, and analytics in action.

## 📁 Folder Structure

- `resumes/` – Tailored resumes and cover letters for different roles and industries.
- `scripts/` – Automation tools and helper scripts for job tracking and metrics.
  
  📌 [job_tracker.py](scripts/job_tracker.py) – Simple Python script that runs a job tracker and prints stats to the console.
- `trackers/` – Application tracking templates, interview logs, and offer tracking spreadsheets.
- `visualizations/` – Power BI/Tableau visuals showing application trends, response rates, and more.

## 💡 Purpose

This repository serves as both a personal toolkit and a public example of how data analytics can be applied to the job search process. It blends organization, creativity, and storytelling to turn a stressful process into an insightful one.

📌 See the full [Project Roadmap](scripts/Roadmap.md) for upcoming features.

## 🧰 Technologies Used

This project combines data, automation, and visualization tools to make the job search process measurable and efficient.  

**Languages & Tools**  
- 🐍 **Python** – Core scripting for job tracking, automation, and data cleaning (`job_tracker.py`, `scripts/` folder).  
- 📊 **Power BI / Tableau** – Visualization of application metrics, response trends, and success rates.  
- 📈 **Excel / VBA** – Application tracking templates, pivot tables, and macros for manual or offline workflows.  
- 🗃️ **SQL (Planned)** – Querying and summarizing job application datasets for analysis.  
- 📉 **R (Planned)** – Statistical analysis and trend visualization (response patterns, conversion rates).  
- 💻 **GitHub Actions** – Workflow automation and repository maintenance.  

**Supporting Libraries**  
- `pandas` – Data manipulation and CSV handling  
- `matplotlib` / `seaborn` – Basic visualization (for Python scripts)  
- `openpyxl` – Reading/writing Excel files  
- `tabulate` – Console-based tabular reporting  

## ▶️ Usage

`job_tracker.py` reads your job applications file and prints quick stats (applications by status, response rates, and time-to-response). It can also filter by date or export a summary.

### 1) Prerequisites
- Python 3.10+  
- Packages: `pandas`, `tabulate`  
- (Optional) Install via:
  ```bash
  pip install pandas tabulate
  ```
### 2) Run the Script

From the project root folder, run:

```bash
python scripts/job_tracker.py --input trackers/applications.csv
```
  
### 3) Example Output
```text
============== Job Tracker Summary ==============
Total applications: 21

By status:
| Status  | Count |
|----------|-------|
| applied  | 21    |

Response rate: 0.0%
=================================================
```

---
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Built With](https://img.shields.io/badge/built%20with-Excel%20%7C%20Power%20BI%20%7C%20Tableau-blue)
