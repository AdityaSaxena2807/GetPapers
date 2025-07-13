# get_papers/export.py
import csv
from typing import List, Dict

def export_to_csv(results: List[Dict], filename: str):
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

def print_results(results: List[Dict]):
    for row in results:
        print(row)
