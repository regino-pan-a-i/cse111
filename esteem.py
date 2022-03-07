print()


def main():
    print('This program is an implementation of the Rosenberg')
    print('Self-Esteem Scale. This program will show you ten')
    print('statements that you could possibly apply to yourself.')
    print('Please rate how much you agree with each of the')
    print('statements by responding with one of these four letters:')
    print()
    print('D means you strongly disagree with the statement.')
    print('d means you disagree with the statement.')
    print('a means you agree with the statement.')
    print('A means you strongly agree with the statement.')
    print()

    print('I feel that I am a person of worth, at least on an equal plane with others.')
    answer_1 = input('Enter D, d, a, or A: ')
    print('I feel that I have a number of good qualities.')
    answer_2 = input('Enter D, d, a, or A: ')
    print('All in all, I am inclined to feel that I am a failure.')
    answer_3 = input('Enter D, d, a, or A: ')
    print('I am able to do things as well as most other people.')
    answer_4 = input('Enter D, d, a, or A: ')
    print('I feel I do not have much to be proud of.')
    answer_5 = input('Enter D, d, a, or A: ')
    print('I take a positive attitude toward myself.')
    answer_6 = input('Enter D, d, a, or A: ')
    print('On the whole, I am satisfied with myself.')
    answer_7 = input('Enter D, d, a, or A: ')
    print('I wish I could have more respect for myself.')
    answer_8 = input('Enter D, d, a, or A: ')
    print('I certainly feel useless at times.')
    answer_9 = input('Enter D, d, a, or A: ')
    print('At times I think I am no good at all.')
    answer_10 = input('Enter D, d, a, or A: ')
    print()
    score =float(answer_counter(answer_1) + answer_counter(answer_2) + +negative_answer_counter(answer_3) + answer_counter(answer_4) + negative_answer_counter(answer_5) + answer_counter(answer_6) + answer_counter(answer_7) + negative_answer_counter(answer_8) + negative_answer_counter(answer_9) + negative_answer_counter(answer_10))
    print(f'Your score is: {score}')
    print()
    print('A score below 15 may indicate problematic low self-esteem.')



def answer_counter(answer):
    counter = 0
    if answer == 'D':
        counter = 0
    elif answer == 'd':
        counter = 1
    elif answer == 'a':
        counter = 2
    elif answer == 'A':
        counter = 3
    
    return counter

def negative_answer_counter(answer):
    counter = 0
    if answer == 'D':
        counter = 3
    elif answer == 'd':
        counter = 2
    elif answer == 'a':
        counter = 1
    elif answer == 'A':
        counter = 0
    
    return counter


main()