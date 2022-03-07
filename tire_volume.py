print()
from datetime import datetime 
import math
answer = None
current_date = datetime.now()

while answer != '0':
    print()
    width = int(input('Please type the width of your tire in mm: '))
    ratio = int(input('Please input the aspect ratio of your tire: '))
    diameter = int(input('Plese input the diameter of your wheel in inches: '))
    print()
    volume = float((math.pi * (width ** 2) * ratio * (width * ratio + 2540 * diameter))/10000000000)

    print(f'The aproximate volume is {volume: 0.2f} liters')

    with open ('volumes.txt', 'at') as v_file:
        print(f'{current_date:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume: 0.2f}', file=v_file)
    print()    
    
    answer = input('Do you want to input a different tire info? (no type: 0 / yes type : 1): ')
    if answer == '1':
        print()
        width = int(input('Please type the width of your tire in mm: '))
        ratio = int(input('Please input the aspect ratio of your tire: '))
        diameter = int(input('Plese input the diameter of your wheel in inches: '))
        print()
        volume = float((math.pi * (width ** 2) * ratio * (width * ratio + 2540 * diameter))/10000000000)

        print(f'The aproximate volume is {volume: 0.2f} liters')

        with open ('volumes.txt', 'at') as v_file:
            print(f'{current_date:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume: 0.2f}', file=v_file)
        print()    
        
        answer = input('Do you want to input a different tire info? (no type: 0 / yes type : 1): ')
    else:
        print()
        print('Please try again.')
        answer = input('Do you want to input a different tire info? (no type 0: / yes type: 1): ')
print()
print('Thank you.')
print()