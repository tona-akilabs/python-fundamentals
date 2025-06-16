
f = open('data.txt', 'w')
f.write('Hello, World!')
f.close()

# read the file after writing
f = open('data.txt')
result = f.read()
print(result)
f.close()

print(result.split())

for line in open('data.txt'):
    print(line.strip())