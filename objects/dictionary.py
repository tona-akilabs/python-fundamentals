D = {'name': 'Pat', 'job': 'dev', 'age': 40}
print(D)  # prints the dictionary
print(len(D))  # prints the number of key-value pairs in the dictionary
print(D['name'])  # prints the value associated with the key 'name'
print(D['job'])  # prints the value associated with the key 'job'
print(D['age'])  # prints the value associated with the key 'age'
print(D.get('name'))  # prints the value associated with the key 'name' using get method
print(D.get('salary', 'Not Found'))  # tries to get the value for 'salary', returns 'Not Found' if not found

print('name' in D)  # checks if 'name' is a key in the dictionary
print('salary' in D)  # checks if 'salary' is a key in the dictionary
print('name' not in D)  # checks if 'name' is not a key in the dictionary

print(D.keys())  # prints all the keys in the dictionary
print(D.values())  # prints all the values in the dictionary
print(D.items())  # prints all key-value pairs in the dictionary

D = {}
D['name'] = 'Pat'  # adds a new key-value pair to the dictionary
D['job'] = 'dev'  # adds another key-value pair to the dictionary
D['age'] = 30  # adds another key-value pair to the dictionary
print(D)  # prints the updated dictionary

person = dict(name='Pat', job='dev', age=40)  # creates a dictionary using the dict constructor
print(person)  # prints the created dictionary
print(person['name'])  # prints the value associated with the key 'name'

person2 = dict([('name', 'Pat'), ('job', 'dev'), ('age', 40)])  # creates a dictionary from a list of tuples
print(person2)  # prints the created dictionary from tuples

person3 = dict(zip(['name', 'job', 'age'], ['Pat', 'dev', 40]))  # creates a dictionary by zipping two lists
print(person3)  # prints the created dictionary from zipped lists
print(person3['name'])  # prints the value associated with the key 'name' in the zipped dictionary
print(person3.get('salary', 'Not Found'))  # tries to get the value for 'salary', returns 'Not Found' if not found
print(person3.get('name'))  # prints the value associated with the key 'name' using get method
print(person3.get('name', 'Not Found'))  # tries to get the value for 'name', returns 'Not Found' if not found
