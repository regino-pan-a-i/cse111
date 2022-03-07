print()
import csv
KEY_INDEX = 0
NAME_INDEX = 1
PRICE_INDEX = 2

def main ():

    products_dict = read_dict('products.csv', KEY_INDEX)
    print(products_dict)

    with open('request.csv', 'rt') as request:
        next(request)

        for i in (request):
            if request[i] in products_dict:
                receipt = products_dict[i]
                print(receipt)

        '''if query in student_dict: 
            student = student_dict[query]
            print(student)'''


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
    dictionary = {}

    with open(filename, 'rt') as cvsv_file:
        reader = csv.reader(cvsv_file)

        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]

            dictionary[key] = row_list
    
    return dictionary 




if __name__ == '__main__':
    main()