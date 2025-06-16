import random

# Random number generation
print(random.random())
print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.uniform(1.0, 10.0))  # Random float between 1.0 and 10.0
print(random.choice(['red', 'green', 'blue']))  # Randomly choose an element from the list
print(random.sample(range(100), 5))  # Randomly sample 5 unique elements from range 0-99
print(random.shuffle(['apple', 'banana', 'cherry']))  # Shuffle the list in place
print(random.seed(42))  # Set the seed for reproducibility
print(random.getstate())  # Get the current state of the random number generator
