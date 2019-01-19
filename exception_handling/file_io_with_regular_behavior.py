"""
Automatically close file in event of error by using a context manager
"""


example_data = ['ACDC', 'Yes', 'David Bowie', 'Debbie Harry']

with open('data.txt', 'w') as output_file:
    for line in example_data:
        output_file.write(line + '\n')


# No need to close the file - by using the context manager, the file will be
# closed whether it is written to successfully or if an error is raised.

