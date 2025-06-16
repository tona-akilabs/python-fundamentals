T = (1, 2, 3, 4)
print(len(T))

result = T + (5, 6, 7, 8)  # Concatenation of tuples
print(result)

# Tuple unpacking
a, b, c, d = T
print(a, b, c, d)

# Tuple slicing
print(T[1:3])  # Output: (2, 3)

# Tuple repetition
print(T * 2)  # Output: (1, 2, 3, 4, 1, 2, 3, 4)

# Tuple membership
print(2 in T)  # Output: True

# Tuple immutability
#T[0] = 10  # This will raise a TypeError since tuples are immutable

print(T.index(4))  # Output: 3, index of the value 4 in the tuple
print(T.count(2))  # Output: 1, count of the value 2 in the tuple
