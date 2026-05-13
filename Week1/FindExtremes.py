# Algorithm: Find Extremes
# Input: Unsorted list A of n elements
# Output: Maximum and Minimum values

# Step 1: Define unsorted list
A = [4, 2, 7, 1, 5, 9]

# Step 2: Assume first element is both max and min
max_val = A[0]
min_val = A[0]

# Step 3: Loop through each number in the list
for num in A:
    
    # Step 4: If current number is greater → update max 
    if num > max_val:
        max_val = num
    
   # Step 5: If current number is smaller → update min 
    if num < min_val:
        min_val = num

# Step 6: Display the results
print("List:   ", A)
print("Maximum:", max_val)
print("Minimum:", min_val)
