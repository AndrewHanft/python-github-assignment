# -------------------------------------------------------------
# Study Time Tracker Program
# This program asks the user for daily study hours, converts
# the input to a number, performs a calculation, and prints
# a clear result. Includes basic error handling.
# -------------------------------------------------------------

print("Welcome to my Python program!")

# Ask the user for input
hours = input("How many hours did you study today? ")

# Convert input with error handling
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()

# Perform calculation
weekly_hours = hours * 7

# Display result
print(f"You are on track to study {weekly_hours} hours this week. Keep it up!")
