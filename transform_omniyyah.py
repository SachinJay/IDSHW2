"""
This script is meant to be used to transform Omniyyah's collected data
into a format my model can handle
"""

import sys

import pandas as pd

from utils import convert_windows_date

DROP_COLS = ["EventCategory", "EventSource", "EventID", "Account", "TESTDATA"]

def transform(input_csv = "test.csv", output_csv = "output.csv"):
    """
    Transforms Omniyyah's data to something my model can test on
    """

    csv_input = pd.read_csv(input_csv)

    # Remove the unnamed column
    csv_input = csv_input.loc[:, ~csv_input.columns.str.contains("Unnamed")]

    for col in DROP_COLS:
        # axis = 1 in order to drop a column instead of a row
        csv_input.drop(col, inplace=True, axis=1)

    print(csv_input["TimeGenerated"].replace())


    # Adds the code col
    csv_input["3016"] = ["3016"] * len(csv_input)
        
    # Adds class col
    csv_input['Class'] = ["Normal"] * len(csv_input)
    csv_input.to_csv(output_csv, index=False)

def driver():
    argc = len(sys.argv)

    if argc == 1:
        transform()
    elif argc == 3:
        transform(sys.argv[1], sys.argv[2])
    else:
        print("Need an input and output csv or no args at all")
        exit(1)

if __name__ == "__main__":
    driver()