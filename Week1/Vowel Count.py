def count_vowels(text):
    # Create a list of the vowels we want to look for
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Create a counter variable and start it at 0
    count = 0

    # Convert the entire text to lowercase
    # This ensures we don't miss uppercase vowels like 'A' or 'E'
    text = text.lower()

    # Start a loop to look at every single character in the text, one by one
    for char in text:

        # Check if the current character is inside our list of vowels
        if char in vowels:
            # If it is a vowel, add 1 to our running total
            count += 1

    # Once the loop has finished checking every character,
    # give the final tally back to the user
    return count


"""
=========================================
      ALGORITHM: VOWEL COUNTER
=========================================
Here is the step-by-step logic for the code above:

PLAIN ENGLISH:
1. Start with a piece of text (a string).
2. Define what a vowel is (a, e, i, o, u).
3. Create a counter and set it to 0.
4. Convert the entire text to lowercase so you don't miss uppercase letters.
5. Look at every single character in the text, one at a time.
6. Ask: "Is this character in my list of vowels?"
   - If Yes, add 1 to the counter.
   - If No, do nothing and move to the next character.
7. Stop looking when you reach the end of the text.
8. Return the final number in the counter.

=========================================
"""