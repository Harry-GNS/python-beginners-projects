# CSV Data Analyzer

A small command-line program that loads a CSV file and prints a quick summary of it:

- the number of rows and columns
- the column names
- the mean, minimum and maximum of every numeric column

## Requirements

- Python 3
- [pandas](https://pandas.pydata.org/)

```bash
pip install -r requirements.txt
```

## How to run

Run the script from this folder and type the name of a CSV file when asked. A sample file, `sample_data.csv`, is included.

```bash
python main.py
```

```text
Enter CSV file name: sample_data.csv
File loaded successfully!

Dataset Information
-------------------
Total Rows: 506
Total Cols: 14

Column Names
-------------------
1. crim
2. zn
...

All Numeric Cols Statistical Summary
-------------------
crim  → Mean: 3.61 | Min: 0.00632 | Max: 88.9762
...
```

If the file does not exist, or is not a valid CSV file, the program prints an error message instead.
