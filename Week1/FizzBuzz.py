for i in range(1, 101):        # Go from 1 to 100
	print(i, ": ", end="")     # Print the number
	if (i%3 == 0):             # Check 3 first, then 5 so we dont need a third if
		print("Fizz", end="")  #
	if (i%5 == 0):             #
		print("Buzz", end="")  #
	print()                    # Print newline


"""
For each number 1–100, print the number, then independently check if it's divisible by 3 ("Fizz") and 5 ("Buzz").
Because these are two separate if statements, a number divisible by both naturally prints "FizzBuzz" without needing a third check.
"""