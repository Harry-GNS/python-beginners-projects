# Student Marks Validator

## Description 
A beginner-friendly Python program that checks whether marks are valid and determines whether a student passes or fails.

## Features
- Rejects marks below 0.
- Rejects marks above 100.
- Declares a pass for marks of 40 or above.
- Declares a fail for marks below 40.

## Requirements 
Python 3

## How to Run

Open Terminal inside the folder and run:

python3 main.py

## Test Cases

| Input | Expected Result | 
|---|---|
| 40 | Result: Pass |
| 39 | Result: Fail |
| -1 | Invalid marks: marks cannot be negative. |
| 101 | Invalid marks: marks cannot exceed 100. |