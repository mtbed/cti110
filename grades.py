# CTI-110
# P4HW1 - Grade List
# Matthew Bedsole
# 11/1

# Ask for 6 grads for the 6 modules
# Add them to a list.

grades = []

for grade in range(6):
        grade = int(input("Enter grade: "))
        grades.append(grade)
print(grades)

# max(grades) and min(grades)
# to show lowest and highest in the list

print("Your highest grade is: ", max(grades))
print("Your lowest grade is: ", min(grades))
print("Sum of grades: ", sum(grades))
print("Your average is: ", sum(grades)/len(grades))
