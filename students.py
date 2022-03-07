print()
import csv
from lib2to3.pgen2.token import NAME
from pickle import NONE

# Index of the I-number column
# in the students.csv file.
INUMBER_INDEX = 0
# Index of the name column
# in the students.csv file.
NAME_INDEX = 1

def main():
    # Read the contents of the student.csv into a
    # compound dictionary named student.cvs. Use
    # the I-numbers as the keys in the dictionary.
    student_dict = read_dict("students.csv", INUMBER_INDEX)

    query = input('Please enter an I-Number (xxxxxxxxx): ')
    if query in student_dict:
       student = student_dict[query]
       print(student)
    else:
        print("No such student")


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:


        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        
        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)
        

       # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # From the current row, retrieve the data
            # from the column that contains the key.
            key = row_list[key_column_index]

            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row_list[NAME_INDEX]

    # Return the dictionary.
    return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()
