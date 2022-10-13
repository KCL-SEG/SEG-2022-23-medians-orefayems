"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
        
sortedNumbers = sorted(numbers)
n = len(numbers)/2

if len(numbers) == 1:
    print(numbers)
elif len(numbers)%2 != 0:
    print(sortedNumbers[n])
else:
    print(sortedNumbers[sum(n-1,n)/2])


