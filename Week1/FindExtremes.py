#Algorithm: Find Extremes
#Input:
 #- A: An unsorted list of 'n' elements
# - n: The size of the list
#Output: Maximum and Minimum values in list A

#function findExtremes(A, n):
   # Step 1: Start
   # Step 2: Set max_val = A[0]
   # Step 3: Set min_val = A[0]
    #Step 4: For each num in A:
               # if num > max_val:
                 #   max_val = num
               # if num < min_val:
                #    min_val = num
    #Step 5: Print max_val and min_val
    #Step 6: Stop



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
