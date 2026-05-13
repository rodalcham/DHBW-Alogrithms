A = [4, 2, 7, 1, 5, 9]

max_val = A[0]
min_val = A[0]

for num in A:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("List:   ", A)
print("Maximum:", max_val)
print("Minimum:", min_val)
