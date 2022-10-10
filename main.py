# Import randomizer
import random

# Create list called numbers
numbers = []

# Get 10 int values and add to list
i = 0
while i < 10:
    num = random.randint(0, 100)
    numbers.append(num)
    i += 1

# Print smallest value in list and its index
print("List of random numbers:", numbers)
print("Smallest value:", min(numbers))
print("Index of", min(numbers), "is", numbers.index(min(numbers)))