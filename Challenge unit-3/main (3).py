
def sort_students(students):
    students.sort(key=lambda x: x.cgpa, reverse=True)

# Define the Student class
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Test case:
# Creating a list of student objects
students = [
    Student("Alice", "123", 3.8),
    Student("Bob", "456", 3.5),
    Student("Charlie", "789", 4.0)
]

# Sort the list of students based on CGPA in descending order
sort_students(students)

# Print the sorted list of students
for student in students:
    print(student.name, student.roll_number, student.cgpa)
