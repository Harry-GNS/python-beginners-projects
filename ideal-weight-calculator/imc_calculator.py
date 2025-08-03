def calculate_bmi(weight, height):
    """Calculate the Body Mass Index"""
    return weight / (height ** 2)

def classify_weight(bmi):
    """Returns the category according to BMI"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("BMI and Ideal Weight Calculator")
    print("-------------------------------")
    
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        
        bmi = calculate_bmi(weight, height)
        category = classify_weight(bmi)
        
        print(f"\nBMI: {bmi:.1f}")
        print(f"Category: {category}")
        
        # Show ideal weight range
        min_weight = 18.5 * (height ** 2)
        max_weight = 24.9 * (height ** 2)
        print(f"\nFor your height ({height}m), the ideal weight would be between {min_weight:.1f}kg and {max_weight:.1f}kg")
    
    except ValueError:
        print("\nError: Please enter valid numeric values")

if __name__ == "__main__":
    main()