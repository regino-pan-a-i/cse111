print()
import math
items = int(input('Write the number of manufactured items: '))
items_per_box = int(input('Write the number of items that to pack in each box: '))
print()

result = math.ceil(items/items_per_box)
print(f'For {items} items, packing {items_per_box} items in each box, you will need {result} boxes.')

