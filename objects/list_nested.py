M = [[1,2,3],
     [4,5,6],
     [7,8,9]]
# A nested list (list of lists)
print(M)  # Print the nested list
print(len(M))  # Print the number of rows in the nested list
print(M[0])  # Access the first row of the nested list
print(M[0][0])  # Access the first element of the first row
print(M[1][2])  # Access the third element of the second row

col2 = [row[1] for row in M]             # Collect the items in column 2
print(col2)  # Print the collected items in column 2

lastRow = [row[1] + 1 for row in M]
print(lastRow)
print(M)

G = (sum(row) for row in M)
print(next(G))  # Print the generator object
print(next(G))  # Print the generator object
print(next(G))  # Print the generator object

print({sum(row) for row in M})

print({i: sum(M[i]) for i in range(3)})

print(list(sum(row) for row in M)) # Print the list of sums of each row