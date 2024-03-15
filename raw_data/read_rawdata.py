# read_rawdata.py
import pandas as pd
import openpyxl


def main():
    # Specify the path to your Excel file
    excel_file = 'raw_data/files/Financial Sample.xlsx'
    
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file)
    
    # Print the DataFrame to inspect the data
    print(df)

if __name__ == "__main__":
    main()