# # # TUPLES: CREATE AND ACCESS TUPLES # # #

# Step 1: 

person = ("Alice", 30, "Paris")
print("Step 1.2: ", person[0], person[1], person[2])

for item in person:
    print("Step 1.3 Printing items in 'person' via for loop: ", item)


# Step 2:

students = ("Alice", "Louis", "Paris", "Alice", "Sara", "Alex", "Alice")

for student in students:
    if "s" in student.lower():
        print("Step 2.2: Printing sudents with 's' in their name via for loop: ", student)

alice_count = 0
for student in students:
    if student == "Alice":
        alice_count += 1

print("Step 2.3: Number of students named Alice:", alice_count) 

# Non-for loop alternative
alice_count = students.count("Alice")
print("Step 2.3: Non-for loop alternative: Alice count: ", alice_count)

middle = (students[2:5])
print("Step 2.4: Slicing the middle of the 'students' tuple and assigning them to a new tuple named 'middle'" ,middle)

concat_tuple = (person + students)
print("Step 2.5: concat_tuple: ", concat_tuple)


# Step 3:

numbers = (6,2,8,1,3)
numbers_2 = ()

for num in numbers:
    print("Step 3.2: ", num)

numbers_2 = numbers * len(numbers)
print("Step 3.3: ", numbers_2)
        
middle_index = len(numbers_2) // 2
print("Step 3.4: Middle item:", numbers_2[middle_index])