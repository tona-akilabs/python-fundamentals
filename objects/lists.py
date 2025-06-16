L = [123, 'text', 1.23] # A list containing integers, strings, and floats
print(L)  # Print the list
print(len(L))  # Print the length of the list
print(L[0])  # Access the first element of the list
print(L[1:3])  # Access a slice of the list from index 1 to 2 (not inclusive of 3)
print(L[-1])  # Access the last element of the list
print(L[1:])  # Access the list from index 1 to the end
print(L[:2])  # Access the list from the start to index 2 (not inclusive of 2)
print(L[1:3:2])  # Access the list from index 1 to 3, stepping by 2
print(L[::-1])  # Reverse the list
print(L + [4, 5])  # Concatenate the list with another list
print(L .__add__([4, 5]))  # Using __add__ method to concatenate the list with another list
print(L * 2)  # Repeat the list twice
print(L .__mul__(2))  # Using __mul__ method to repeat the list twice
print(1 in L)  # Check if 1 is in the list
print(1 not in L)  # Check if 1 is not in the list
print(L .__contains__(1))  # Using __contains__ method to check if 1 is in the list
print(L .__getitem__(0))  # Using __getitem__ method to access the first element of the list
L .__setitem__(0, 456)  # Using __setitem__ method to set the first element of the list to 456
print(L)  # Print the modified list after setting the first element to 456
L .__delitem__(0)  # Using __delitem__ method to delete the first element of the list
print(L)  # Print the list after deleting the first element
L .append(789)  # Append 789 to the end of the list
print(L)  # Print the list after appending 789
L .insert(1, 'inserted')  # Insert 'inserted' at index 1
print(L)  # Print the list after inserting 'inserted' at index 1
L .extend([10, 20])  # Extend the list with another list [10, 20]
print(L)  # Print the list after extending it with [10, 20]
L .remove('inserted')  # Remove 'inserted' from the list
print(L)  # Print the list after removing 'inserted'
L .pop()  # Pop the last element from the list
print(L)  # Print the list after popping the last element
L .clear()  # Clear the list
print(L)  # Print the list after clearing it
L = [1, 2, 3, 4, 5]
L .reverse()  # Reverse the list in place
print(L)  # Print the list after reversing it
L.sort()
print(L)