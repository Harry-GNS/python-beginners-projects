import pandas as pd
import numpy as np 

try:
    file_name = input('Enter CSV file name: ')
    try:
        csv = pd.read_csv(file_name)
        print('File loaded successfully!\n\n')
        try:
            print('Dataset Information \n-------------------')
            print('Total Rows:',csv.shape[0])
            print('Total Cols:',csv.shape[1])
            print('\n')
            print('Column Names \n-------------------')

            for i in range(csv.shape[1]):
                cols = csv.columns
                print(f"{i+1}. {cols[i]}")
            print('\n')
        except Exception as e:
            print('Try Again With Valid File')

        try:
            print('All Numeric Cols Statistical Summary \n-------------------')
            data = csv.select_dtypes([int,float])
            for i in range(data.shape[1]):
                print(f'{data.columns[i]}  → Mean: {data[data.columns[i]].mean()} | Min: {data[data.columns[i]].min()} | Max: {data[data.columns[i]].max()}\n')

            print('\n\nAnalysis completed successfully. \nThank you for using CSV Data Analyzer!\n\n')
        except Exception as e:
            print('Try Again With Valid File')
    except:
        print('Enter valid csv file.')

except:
    print('Error: File not found. \nPlease make sure the CSV file is in the same folder.')