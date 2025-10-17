# BMI and Ideal Weight Calculator

A simple Python calculator that determines your weight category based on Body Mass Index (BMI) and shows your ideal weight range.

## Features

- **BMI Calculation**: Calculates your Body Mass Index using the standard formula: weight (kg) / height² (m²)
- **Weight Classification**: Categorizes your BMI according to WHO standards:
  - Underweight: BMI < 18.5
  - Normal weight: BMI 18.5-24.9
  - Overweight: BMI 25-29.9
  - Obesity: BMI ≥ 30
- **Ideal Weight Range**: Displays the healthy weight range for your height
- **Input Validation**: Handles invalid inputs gracefully with error messages

## How to Use

1. Run the program:
   ```bash
   python imc_calculator.py
   ```

2. Enter your weight in kilograms when prompted
3. Enter your height in meters when prompted
4. View your BMI, weight category, and ideal weight range

## Example Output

```
BMI and Ideal Weight Calculator
-------------------------------
Enter your weight in kg: 70
Enter your height in meters: 1.75

BMI: 22.9
Category: Normal weight

For your height (1.75m), the ideal weight would be between 56.7kg and 76.3kg
```

## Requirements

- Python 3.x
- No external dependencies required

## About BMI

The Body Mass Index (BMI) is a measure that uses height and weight to work out if weight is healthy. While BMI is a useful screening tool, it doesn't directly measure body fat and may not be accurate for athletes, pregnant women, or elderly individuals.

## License

This project is open source and available under the MIT License.