import math

numbers = [4, 9, 16, 25]

# Calculate square roots
print("Square roots:")
for num in numbers:
    print(f"√{num} = {math.sqrt(num)}")

# Calculate average
average = sum(numbers) / len(numbers)
print(f"\nAverage: {average}")