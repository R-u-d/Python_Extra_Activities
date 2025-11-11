# # # FOR / WHILE LOOPS # # #

# _________________________________________________________________________________________

# a for loop that counts from 0 to 10, and prints odd numbers to the screen
for i in range(0, 11):
    if i % 2 != 0:
        print(i)

# _________________________________________________________________________________________

# a while loop that counts from 0 to 10, and prints odd numbers to the screen
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1

# _________________________________________________________________________________________

# a program with a for loop and a break statement which iterates over characters
# in an email address, exits the loop when it reaches the @ symbol, and prints the
# part before @ on one line.
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

# _________________________________________________________________________________________

# a program with a for loop and a continue statement which iterates over a string of
# digits, replaces each 0 with x, and prints the modified string to the screen
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

# _________________________________________________________________________________________

# iterate with while loop
n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

# output:
# 4
# 3
# 2
# 0 (else)

# _________________________________________________________________________________________

# iterate with for loop
n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)

# output:
# -1
# 0
# 1
# 2
# 3 (else)

# _________________________________________________________________________________________

#
for i in range(0, 6, 3):
    print(i)

# output:
# 0
# 3
