# # # STRING BASICS # # #

# Step 1:

name = "Rud"
message = f"Hello, {name}! Welcome to Python."
print("Step 1.0: ", message)


# Step 2:

char_in_message = len(message)
print("Step 2.1: ", char_in_message)

o_in_message = message.count("o")
print("Step 2.2: ", o_in_message)

vowels_in_message = 0
vowels = "aeiou"
for char in message:
    if char in vowels:
        vowels_in_message +=1
print("Step 2.3: vowels count: ", vowels_in_message)


# Step 3:

print("Step: 3.0: updated message: ", message.replace("Python", "Javascript"))
