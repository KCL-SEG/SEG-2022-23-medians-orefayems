""""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = sorted([float(value) for value in input().split(",")])
        #let n be numberOfElements 
        n = len(numbers)
        if n%2 != 0:
        	if n == 1:
        		print(numbers)
        		
        	else:
        		print(numbers[round(n/2)])
        		
        else:
        	x1 = round((n/2)-1)
        	x2= round(n/2)
        	print((numbers[x1] + numbers[x2])/2)
        	
        
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print('hi')

