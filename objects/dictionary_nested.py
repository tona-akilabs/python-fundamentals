person = {'name': 'Pat', 'jobs': { 'dev', 'mgr' }, 'age': 40, 'address': {'city': 'New York', 'zip': '10001'}}
print(person)  # prints the dictionary with nested structures
print(len(person))  # prints the number of key-value pairs in the dictionary
print(person['name'])  # prints the value associated with the key 'name'
print(person['jobs'])  # prints the set of jobs associated with the key 'jobs'
print(person['address'])  # prints the nested dictionary associated with the key 'address'
print(person['address']['city'])  # prints the city from the nested address dictionary
print(person['address']['zip'])  # prints the zip code from the nested address dictionary
print(person.get('name'))  # prints the value associated with the key 'name' using get method
print(person.get('salary', 'Not Found'))  # tries to get the value for 'salary', returns 'Not Found' if not found
print('name' in person)  # checks if 'name' is a key in the dictionary
print('salary' in person)  # checks if 'salary' is a key in the dictionary
print('name' not in person)  # checks if 'name' is not a key in the dictionary

print(person.keys())  # prints all the keys in the dictionary
print(person.values())  # prints all the values in the dictionary
print(person.items())  # prints all key-value pairs in the dictionary
# Adding a new key-value pair to the dictionary
person['email'] = 'dev@info.com'  # adds a new key-value pair to the dictionary
print(person)  # prints the updated dictionary with the new key-value pair
# Updating an existing key-value pair in the dictionary
person['age'] = 30  # updates the value associated with the key 'age'
print(person)  # prints the updated dictionary with the new age
# Removing a key-value pair from the dictionary
del person['jobs']  # removes the key 'jobs' and its associated value
print(person)  # prints the dictionary after removing the 'jobs' key

for key, value in person.items():
    print(f"{key}: {value}")  # prints each key-value pair in the dictionary
# Iterating through the keys of the dictionary
for key in person.keys():
    print(key)  # prints each key in the dictionary
# Iterating through the values of the dictionary
for value in person.values():
    print(value)  # prints each value in the dictionary
# Iterating through the items (key-value pairs) of the dictionary
for item in person.items():
    print(item)  # prints each key-value pair as a tuple in the dictionary
# Checking if a key exists in the dictionary
if 'name' in person:
    print("Name exists in the dictionary")  # prints if 'name' key exists