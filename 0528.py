# Original dictionary of students and their courses
student_courses = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102']
}

# Function to invert the dictionary
def invert_dictionary(original_dict):
    inverted = {}
    for student, courses in original_dict.items():
        for course in courses:
            if course not in inverted:
                inverted[course] = [student]
            else:
                inverted[course].append(student)
    return inverted

# Invert the dictionary
course_students = invert_dictionary(student_courses)

# Print the original and inverted dictionaries
print("Original Dictionary:")
print(student_courses)

print("\nInverted Dictionary:")
print(course_students)
