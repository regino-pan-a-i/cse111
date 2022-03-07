print()
import random 

def main():
    numbers = [1.45, 3.5, 5.13, 7.45, 11.3, 15.5]
    print(numbers)
    print()
    append_random_numbers(numbers)
    print(numbers)
    print()
    append_random_numbers(numbers, 2)
    print(numbers)
    print()
    words = ['people', 'study', 'computer', 'apartment']
    print(words)
    print()
    append_random_words(words)
    print(words)
    print()
    append_random_words(words,3)
    print(words)
    print()



def append_random_numbers(numbers_list, quantity = 1):
    for _ in range (quantity):
        new_number = random.uniform(1,100)
        rounded = round(new_number)
        numbers_list.append(rounded)


def append_random_words(words_list, quantity = 1):
    random_list = ['word', 'clock', 'mind', 'turtle', 'life', 'friends', 'cats', 'phone', 'piano'] 
    for _ in range (quantity):
        word = random.choice(random_list)
        words_list.append(word)

if __name__ == '__main__':
    main()