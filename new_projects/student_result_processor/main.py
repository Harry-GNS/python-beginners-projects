students = [
    {"name": "Pranav", "marks": 90},
    {"name": "Amit", "marks": 40},
    {"name": "Isha", "marks": 87},
    {"name": "Ishika", "marks": 45},
    {"name": "Rahul", "marks": 72},
    {"name": "Sneha", "marks": 95},
    {"name": "Vikram", "marks": 33},
    {"name": "Ananya", "marks": 68},
    {"name": "Rohan", "marks": 55},
    {"name": "Kavya", "marks": 82},
    {"name": "Arjun", "marks": 28},
    {"name": "Zoya", "marks": 91}
]

def separate_students(students):
    passed = [s for s in students if s["marks"] >= 75]
    failed = [s for s in students if s["marks"] < 75]
    return passed, failed

def generate_report(students):
    passed, failed = separate_students(students)

    print("STUDENT RESULT REPORT\n")

    print("Passed Students:")
    for s in passed:
        print("-", s["name"])

    print("\nFailed Students:")
    for s in failed:
        print("-", s["name"])

    print("\nTop Performers (90+):")
    for s in passed:
        if s["marks"] >= 90:
            print("-", s["name"])

    pass_percentage = (len(passed) / len(students)) * 100
    print(f"\nPass Percentage: {pass_percentage:.2f}%")

generate_report(students)
