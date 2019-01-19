""" the with keyword in Python automatically closes the file when done. """

# This line errors if data.txt does not exist.
data = open('data.txt', 'w').readlines()

for line in data:
    print(line)

