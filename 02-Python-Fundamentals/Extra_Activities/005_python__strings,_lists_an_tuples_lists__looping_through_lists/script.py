students = ['Tom', 'Alice', 'Jorge', 'Sara', 'Paul', 'Sara'];
fruits = ['Mango', 'Apple', 'Kiwi'];
healthy_food = ['Brocoli', 'Kiwi', 'Salad'];

# # # LISTS: LOOPING THROUGH LISTS # # #

# Step 1:

for student in students:
    print("Step 1.1: Hello", student)

students_upper = []

for student in students:
    students_upper.append(student.upper())
print("Step 1.3: Uppercase students list: ", students_upper)

# INDEX ALTERNATIVE TO STEP 1.2:
for index in range(len(students)):
    students[index] = students[index].upper()
print("Step 1.3: Uppercase students list via index: ",students)

# LIST COMPREHENSION ALTERNATIVE TO STEP 1.2:
students_lower = [student.lower() for student in students]
print("Step 1.3: Lowercase students list via list comprehension: ", students_lower)


students = ['Tom', 'Alice', 'Jorge', 'Sara', 'Paul', 'Sara']
students_wo_Sara = []

for student in students:
    if student != "Sara":
        students_wo_Sara.append(student)
        
print("Step 1.4: removed 'Sara' from students list: ", students_wo_Sara)

# COUNT/RANGE ALTERNATIVE TO STEP 1.4:
students = ['Tom', 'Alice', 'Jorge', 'Sara', 'Paul', 'Sara']
sara_count = students.count("Sara")
for each in range(sara_count):
    students.remove("Sara") 
print("Step 1.4: removed 'Sara' via count: ", students)

# LIST COMPREHENSION ALTERNATIVE TO STEP 1.4:
students = ['Tom', 'Alice', 'Jorge', 'Sara', 'Paul', 'Sara']
students_wo_Sara_comp = [student for student in students if student != "Sara"]
print("Step 1.4: removed 'Sara' from students list via list comprehension: ", students_wo_Sara_comp)


# Step 2:

fruits = ['Mango', 'Apple', 'Kiwi']
fruits_With_A = fruits.copy()
fruits_lower = []

for fruit in fruits:
    if "a" in fruit or "A" in fruit:
        fruits_lower.append(fruit.lower())
    else: 
        fruits_lower.append(fruit)
    
print("Step 2.2: fruits with 'a' in lowercase: ", fruits_lower)

# LIST COMPREHENSION ALTERNATIVE TO STEP 2.2

fruits_lower_comp = [fruit.lower() if "a" in fruit or "A" in fruit else fruit for fruit in fruits]
print("Step 2.2: fruits with 'a' in lowercase via list comprehension: ", fruits_lower_comp)


for fruit in fruits:
    print("Step 2.3: I like:", fruit)


healthy_food = ['Brocoli', 'Kiwi', 'Salad']
for fruit in fruits:
    healthy_food.append(fruit)

print("Step 2.5: Updated healthy food list: ", healthy_food)
