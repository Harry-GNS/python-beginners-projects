print("Student Marks Validator")
print("-------------------------")

marks = int(input("Enter the marks obtained by the student out of 100: "))


if marks <0:
    print("Invalid marks: marks cannot be negative.")
elif marks >100:
    print("Invalid marks: marks cannot exceed 100.")
else:
    if marks >=40:
        print("Result: Pass")
    else:
        print("Result: Fail")
