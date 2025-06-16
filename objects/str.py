name = 'Python'

print(name)
print(len(name))
print(name[0])
print(name[1:4])
print(name[-1])
print(name[1:])  # from index 1 to the end
print(name[:3])  # from the start to index 3 (not inclusive)
print(name[1:4:2])  # from index 1 to 4, step by 2
print(name[::-1])  # reverse the string
print(name.upper())  # convert to uppercase
print(name.lower())  # convert to lowercase
print(name.replace('P', 'J'))  # replace 'P' with 'J'
print(name.startswith('Py'))  # check if it starts with 'Py'
print(name.endswith('on'))  # check if it ends with 'on'
print(name.find('th'))  # find the index of 'th', returns -1 if not found
print(name.index('th'))  # find the index of 'th', raises ValueError if not found
print(name.count('o'))  # count occurrences of 'o'
print(name.split('t'))  # split the string by 't'
print(name.split())  # split the string by whitespace
print(name.strip())  # remove leading and trailing whitespace
print(name.isalpha())  # check if all characters are alphabetic
print(name.isdigit())  # check if all characters are digits
print(name.isalnum())  # check if all characters are alphanumeric
print(name.capitalize())  # capitalize the first character
print(name.title())  # capitalize the first character of each word
print(name.swapcase())  # swap case of all characters
print(name.center(20, '*'))  # center the string in a field of width 20, padding with '*'
print(name.ljust(20, '*'))  # left justify the string in a field of width 20, padding with '*'
print(name.rjust(20, '*'))  # right justify the string in a field of width 20, padding with '*'
print(name.zfill(10))  # pad the string with zeros on the left to make it 10 characters long
print(name.format('World'))  # format the string with 'World'
print('python programming'.title())  # capitalize the first character of each word

print('Hello, {}!'.format('World'))  # format the string with 'World'
print(f'Hello, {name}!')  # f-string formatting

print(name + ' is a programming language.')  # string concatenation
print(name .__add__(' is a programming language.'))  # using __add__ method

S = 'A\nB\tC'
print(S)  # prints A, B, C with newline and tab
print(len(S)) # length of the string, including newline and tab characters
S = 'A\0B\0C'
print(len(S)) # length of the string, including null characters
print(S)  # prints A, B, C with null characters

print(S .encode('utf-8'))  # encode the string to bytes using utf-8 encoding
