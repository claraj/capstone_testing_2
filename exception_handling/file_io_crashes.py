"""
Close your file when done writing
But what happens if the program crashes before the file is closed?
This program has a bug in it, and crashes before the file is closed
Depending on your OS, the data may be saved.... but it's not guaranteed!
"""


example_data = ['ACDC', 'Yes', 'David Bowie', 'Debbie Harry']

output_file = open('data.txt', 'w')

# This line has a bug in - the list doesn't have 5 elements.
# It's a good idea to use the for item in list form for looping over lists.
for line in range(5):
    output_file.write(example_data[line] + '\n')

output_file.close()


