print()

def main():
    text = read_text('provinces.txt')
    print(text)

    for i in range (len(text)):
        if text[i] == 'AB':
            text[i] = 'Alberta'
    
    count = text.count('Alberta')
    print()
    print(f'Alberta occurs {count} times in the modified list.')
    

def read_text(filename):
    text_list = []
    with open(filename, 'rt') as text_file:
        for line in text_file:
            clean_text = line.strip()
            text_list.append(clean_text)


    return text_list 

if __name__ == "__main__":
    main()