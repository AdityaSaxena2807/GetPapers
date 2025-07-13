# get_papers/export.py
from typing import List, Dict
from pprint import pprint
import csv

def export_to_csv(results: List[Dict], filename: str) -> None:
    keys = results[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)

def print_results(results: List[Dict]) -> None:
    for result in results:
        pprint(result)