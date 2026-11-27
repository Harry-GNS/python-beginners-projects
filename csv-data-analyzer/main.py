import pandas as pd

file_name = input('Enter CSV file name: ').strip()

try:
    csv = pd.read_csv(file_name)
except FileNotFoundError:
    print('Error: File not found. \nPlease make sure the CSV file is in the same folder.')
except Exception:
    print('Enter valid csv file.')
else:
    print('File loaded successfully!\n\n')

    print('Dataset Information \n-------------------')
    print('Total Rows:', csv.shape[0])
    print('Total Cols:', csv.shape[1])
    print('\n')

    print('Column Names \n-------------------')
    for i, column in enumerate(csv.columns, 1):
        print(f"{i}. {column}")
    print('\n')

    print('All Numeric Cols Statistical Summary \n-------------------')
    data = csv.select_dtypes('number')
    if data.shape[1] == 0:
        print('No numeric columns found.')
    for column in data.columns:
        print(f'{column}  → Mean: {data[column].mean():.2f} | Min: {data[column].min()} | Max: {data[column].max()}\n')

    print('\n\nAnalysis completed successfully. \nThank you for using CSV Data Analyzer!\n\n')
