"""
Automatically close file in event of error by using a context manager
"""


example_data = ['ACDC', 'Yes', 'David Bowie', 'Debbie Harry']

with open('data.txt', 'w') as output_file:
    # This line has a bug in - the list doesn't have 5 elements.
    # It's a good idea to use the for item in list form for looping over lists.
    for line in range(5):
        output_file.write(example_data[line] + '\n')


# No need to close the file - by using the context manager, the file will be
# closed whether it is written to successfully or if an error is raised.
# And, fix the bug in this code!
