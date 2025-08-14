# # # CONVERSIONS: STRINGS, LISTS AND TUPLES

# Step 1:

hobbies = ["coding", "swimming", "jogging"]
print("Step 1.1: ", hobbies)

hobbies_tuple = tuple(hobbies)
print("Step 1.2: ", hobbies_tuple)

hobbies_list = list(hobbies_tuple)
print("Step 1.3: ", hobbies_list)

hobbies_list.append("rubberducking")
print("Step 1.4: ", hobbies_list)

hobbies_string = ", ".join(hobbies_list)
print("Step 1.5: ", hobbies_string)


# Step 2:

person = ("Alice", 30, "New York")
print("Step 2.1: ", person)

person_list = list(person)
print("Step 2.2: ", person_list)

person_list.append(hobbies_string)
print("Step 2.3: ", person_list)

person_tuple = tuple(person_list)
print("Step 2.4: ", person_tuple)


# Step 3:

students = ("Alice", "Louis", "Paris", "Alice", "Sara", "Alex", "Alice")
students_with_a = []

for student in students:
    if "a" in student.lower():
        students_with_a.append(student)
print("Step 3.4: Students_with_a_list: ", students_with_a)

"""Alternative way
for student in students:
    if student != "Louis":
        students_with_a.append(student)
print("Step 3.4 alternative: ", students_with_a)"""

students_with_a_tuple = tuple(students_with_a)
print("Step 3.6: Students_with_a_tuple: ", students_with_a_tuple)


