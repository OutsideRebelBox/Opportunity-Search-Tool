# job_tracker.py
import pandas as pd
from tabulate import tabulate
import argparse

parser = argparse.ArgumentParser(description="Summarize job applications from a CSV file.")
parser.add_argument("--input", required=True, help="Path to job applications CSV")
args = parser.parse_args()

# Load the data
df = pd.read_csv(args.input)

# Basic stats
total_apps = len(df)
statuses = df["status"].value_counts()
response_rate = (df["response_date"].notna().sum() / total_apps) * 100

# Display summary
print("\n================ Job Tracker Summary ================")
print(f"Total applications: {total_apps}")
print("\nBy status:")
print(tabulate(statuses.reset_index().values, headers=["Status", "Count"], tablefmt="github"))
print(f"\nResponse rate: {response_rate:.1f}%")
print("=====================================================\n")
