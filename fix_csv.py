"""
My implementation of sec.py does not add column title and does not add a class
column (needed for one class SVM)

This script is intended to remedy that by adding that column and renaming the
others
"""

import csv
import pandas as pd
import sys

one_day_rename_dict = {
        "4" : "day",
        "11" : "hour",
        "C:\\Users\\sachi\\OneDrive\\Documents\\IDS\HW2\\IDSHW2": "File",
        "3016" : "Code"
        }

four_day_rename_dict = {
    "2" : "day",
    "15" : "hour",
    "C:\\Users\\sachi\\OneDrive\\Documents\\IDS\\HW2\IDSHW2\\__pycache__\\utils.cpython-310.pyc" : "File",
    "456" : "Code"

}

RENAME_DICT = four_day_rename_dict

def fix(input_csv = "test.csv", output_csv = "output.csv"):
    """
    Renames columns and adds new class column
    """

    csv_input = pd.read_csv(input_csv)
    csv_input.rename(columns=RENAME_DICT, inplace=True)

    # Adds new col
    csv_input['Class'] = ["Normal"] * len(csv_input)
    csv_input.to_csv(output_csv, index=False)

def driver():
    argc = len(sys.argv)

    if argc == 1:
        fix()
    elif argc == 3:
        fix(sys.argv[1], sys.argv[2])
    else:
        print("Need an input and output csv or no args at all")
        exit(1)

if __name__ == "__main__":
    driver()