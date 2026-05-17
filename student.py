print("===================================")
print("   STUDENT PERFORMANCE PROJECT")
print("===================================")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

study_hours = int(input("Enter study hours per day: "))
attendance = int(input("Enter attendance percentage: "))
marks = int(input("Enter internal marks (out of 100): "))

print("\n--- STUDENT DETAILS ---")
print("Name:", name)
print("Roll No:", roll_no)
print("Study Hours:", study_hours)
print("Attendance:", attendance)
print("Marks:", marks)

if study_hours >= 4 and attendance >= 70 and marks >= 50:
    result = "PASS"
    grade = "A"
elif study_hours >= 3 and attendance >= 60 and marks >= 40:
    result = "PASS"
    grade = "B"
else:
    result = "FAIL"
    grade = "No Grade"

print("\n--- RESULT ---")
print("Final Result:", result)
print("Grade:", grade)

if result == "PASS":
    print("Suggestion: Keep studying regularly!")
else:
    print("Suggestion: Improve attendance and practice more.")