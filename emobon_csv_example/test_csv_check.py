# example file for testing a csv file with python dataclasses to see if it is valid

import csv
from dataclasses import dataclass
from linkml.validator import validate
import os
import json

WD = os.path.dirname(os.path.abspath(__file__))
SCHEMA = os.path.join(WD, 'test_csv_row.yaml')

# read in the csv file
with open(os.path.join(WD, "test_auto_error_solving.csv"), newline='', encoding="utf-8") as f:
    # make a dict with keys being header names and values being the values in the row
    reader = csv.DictReader(f)
    data = [row for row in reader]
    

print(data)

for row in data:
    report= validate(row, SCHEMA,"DataRow")
    if not report.results:
        print("Valid")
    else:
        for result in report.results:
            print(result.message)