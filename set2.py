n = int(input("Enter number of students: "))
m = int(input("Enter number of subjects: "))

names = []
marks = []
totals = []
percentages = []
grades = []

# Input student details
for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    names.append(name)

    student_marks = []
    total = 0
    fail = False

    for j in range(m):
        mark = int(input("Enter marks in subject " + str(j + 1) + ": "))

        student_marks.append(mark)
        total = total + mark

        if mark < 40:
            fail = True

    marks.append(student_marks)
    totals.append(total)

    percentage = total / m
    percentages.append(percentage)

    # Grade calculation
    if fail:
        grade = "F"
    else:
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

    grades.append(grade)


# Find class topper
topper = 0

for i in range(1, n):
    if percentages[i] > percentages[topper]:
        topper = i


# Subject analysis
highest_marks = []
subject_average = []

for j in range(m):
    highest = marks[0][j]
    total = 0

    for i in range(n):
        if marks[i][j] > highest:
            highest = marks[i][j]

        total = total + marks[i][j]

    average = total / n

    highest_marks.append(highest)
    subject_average.append(average)


# Students scoring above subject average in every subject
print("\nStudents scoring above subject average in every subject:")

for i in range(n):
    above_average = True

    for j in range(m):
        if marks[i][j] <= subject_average[j]:
            above_average = False
            break

    if above_average:
        print(names[i])


# Subject Analysis
print("\n----- SUBJECT ANALYSIS -----")

for j in range(m):
    print("Subject", j + 1)
    print("Highest Mark:", highest_marks[j])
    print("Average Mark:", subject_average[j])


# Class Topper
print("\n----- CLASS TOPPER -----")

print("Name:", names[topper])
print("Percentage:", percentages[topper])


# Complete Result
print("\n----- COMPLETE RESULT -----")

for i in range(n):
    print("\nStudent Name:", names[i])
    print("Marks:", marks[i])
    print("Total:", totals[i])
    print("Percentage:", percentages[i])
    print("Grade:", grades[i])