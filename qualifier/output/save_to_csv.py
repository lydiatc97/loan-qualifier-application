""" Save to CSV Function.

This script allows the user to save the loans that they qualify for to a CSV file if they choose to do so"""


#import required libraries
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
    
    #checks to see if the user qualified for any loans and exits the application if they did not
    if len(qualifying_loans) <= 0:
        sys.exit("Sorry, you do not qualify for any loans")
    
    #a prompt to ask the user if they want to save their qualifying loan data
    save_loan = questionary.confirm("Would you like to save qualifying loans to a CSV file?").ask()

    #if they choose to save the loan, the rest of the application will run
    if save_loan == True:
        #the user is prompted to specify the folder where they would like to save their file
        desired_path = questionary.text("Enter a file path to the folder where you would like to save your file:").ask()
        #the file path the user specified is assigned to the variable 'desired_path'
        desired_path = Path(desired_path)
        #if the path the user specified does not exist, the application exits with a message
        if not desired_path.exists():
            sys.exit(f"Oops! Can't find this path: {desired_path}")
        #add the header
        header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
        #specify the location where the file will be saved and name the file
        csvpath = os.path.join(desired_path, "qualifying_loans.csv")
        #write the data from the qualifying_loans list to the CSV file
        with open(csvpath, 'w', newline= '') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(header)
            for row in qualifying_loans:
                csvwriter.writerow(row)
        print("Saving qualifying loans to a CSV file...")
        return csvfile
