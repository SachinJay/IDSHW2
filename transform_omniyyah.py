"""
This script is meant to be used to transform Omniyyah's collected data
into a format my model can handle
"""

import sys
import csv

import pandas as pd

from utils import convert_omniyyah_date_time

DROP_COLS = ["EventCategory", "EventSource", "EventID", "Account", "TESTDATA"]

def transform(input_csv = "test.csv", output_csv = "tmp.csv"):
    """
    Transforms Omniyyah's data to something my model can test on
    """

    csv_input = pd.read_csv(input_csv)

    # Remove the unnamed column
    csv_input = csv_input.loc[:, ~csv_input.columns.str.contains("Unnamed")]

    # drop columns I don't use in my sensor
    for col in DROP_COLS:
        # axis = 1 in order to drop a column instead of a row
        csv_input.drop(col, inplace=True, axis=1)

    print(csv_input["TimeGenerated"].replace())


    # Adds the code col
    csv_input["3016"] = ["3016"] * len(csv_input)
        
    # Adds class col
    csv_input['Class'] = ["Normal"] * len(csv_input)

    # Rename ProcessName
    csv_input.rename(columns={"ProcessName" : "C:\\Users\\sachi\\OneDrive\\Documents\\IDS\\HW2\\IDSHW2"}, inplace=True)


    # Write to csv
    csv_input.to_csv(output_csv, index=False)

    

def add_time(input_csv = "tmp.csv", output_csv = "output.csv"):
    # First, add the two new columns for day and time
    
    in_csv = open(input_csv, 'r')
    out_csv = open(output_csv, 'w')

    writer = csv.writer(out_csv, lineterminator='\n')
    reader = csv.reader(in_csv)

    all = []

    # Header
    row = next(reader)
    row.insert(0, "11")
    row.insert(0,"4")
    all.append(row)

    for row in reader:
        # ASSUMES time generated is the first column
        time_gen = row[0]
        day, hour = convert_omniyyah_date_time(time_gen)

        row.insert(0,hour)
        row.insert(0,day)

        all.append(row)
    
    writer.writerows(all)

    in_csv.close()
    out_csv.close()

    # second, delete the time generated column
    df = pd.read_csv(output_csv)
    df.drop("TimeGenerated", inplace=True, axis=1)
    df.to_csv(output_csv, index=False)


def driver():
    argc = len(sys.argv)

    if argc == 1:
        transform()
        add_time()
    elif argc == 3:
        transform(input_csv=sys.argv[1])
        add_time(output_csv=sys.argv[2])
    else:
        print("Need an input and output csv or no args at all")
        exit(1)

if __name__ == "__main__":
    driver()