# # # LISTS: SORTING, COUNTING & REVERSING # # #

# Step 1:

numbers = [2,8,3,5,7]

numbers.sort()
print("Step 1.2: Sorting by ascending order: ", numbers)

count_number_5 = numbers.count(5)
print("Step 1.3: Count of number '5': ", count_number_5)

max_number = max(numbers)
print("Step 1.4: Max number in 'numbers': ", max_number)

min_number = min(numbers)
print("Step 1.4: Min number in 'numbers': ", min_number)


# Step 2:

students = ["Nedim", "Max", "Waqar", "Umi", "Ben"]
print("Step 2.2: Students in my class: ", students)

sorted_students = sorted(students)
print("Step 2.4: Students sorted by alphabet: ", sorted_students)

students = sorted(students, reverse=True)
print("Step 2.6: Students reversed order: ", students)

sort_reversed = sorted(sorted_students, reverse=True)
print("Step 2.8: sorted_students reversed order: ", sort_reversed)
