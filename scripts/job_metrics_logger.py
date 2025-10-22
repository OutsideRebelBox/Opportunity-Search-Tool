import csv
from datetime import datetime

# Define your CSV file path
CSV_FILE = "applications.csv"

# Define the job application entry
job_entry = {
    "Date Applied": datetime.today().strftime('%Y-%m-%d'),
    "Company": "Example Company",
    "Job Title": "Data Analyst",
    "Source": "LinkedIn",
    "Status": "Applied",  # e.g., Applied, Interviewing, Rejected, Offer
    "Response Time (days)": "",  # To fill in later
    "Notes": "Submitted resume and cover letter"
}

# Write headers if file is new
def init_csv(file_path, headers):
    try:
        with open(file_path, "x", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
    except FileExistsError:
        pass  # File already exists

# Append job entry to CSV
def log_job_application(file_path, entry):
    with open(file_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=entry.keys())
        writer.writerow(entry)

# Initialize and log
init_csv(CSV_FILE, job_entry.keys())
log_job_application(CSV_FILE, job_entry)

print("✅ Job application logged successfully.")
