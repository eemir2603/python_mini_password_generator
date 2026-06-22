# 1. CHEAT CODE (Module): Instead of writing our own random selection algorithm, 
# we import Python's built-in 'random' toolkit.
import random

print("--- CYBER SECURITY ORACLE: PASSWORD GENERATOR ---")

# 2. ARSENAL (String): All the characters the computer will choose from.
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"

# 3. VARIABLES: The length of our password (Integer) and our empty password box (String)
length = 12
new_password = ""

# 4. LOOP (For): Instead of doing the manual labor 12 times, we put the process in a loop.
# range(length) means "repeat this process 'length' (12) times".
for i in range(length):
    # Pick 1 random character from our characters string using the 'choice' tool from the 'random' module
    random_char = random.choice(characters)
    
    # Add the selected character to our password box
    new_password = new_password + random_char

# 5. FINISH: The process is complete, print it to the screen!
print("Your Generated Password:", new_password)