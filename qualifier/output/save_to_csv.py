import csv
from pathlib import Path
import sys
import questionary
import os

def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    
    if len(qualifying_loans) <= 0:
        sys.exit("Sorry, you do not qualify for any loans")
    save_loan = questionary.confirm("Would you like to save qualifying loans to a CSV file?").ask()
    if save_loan == True:
        desired_path = questionary.text("Enter a file path to the folder where you would like to save your file:").ask()
        desired_path = Path(desired_path)
        if not desired_path.exists():
            sys.exit(f"Oops! Can't find this path: {desired_path}")
        header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
        csvpath = os.path.join(desired_path, "qualifying_loans.csv")
        with open(csvpath, 'w', newline= '') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(header)
            for row in qualifying_loans:
                csvwriter.writerow(row)
        print("Saving qualifying loans to a CSV file...")
        return csvfile
