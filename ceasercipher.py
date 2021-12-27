import string

alphabets = string.ascii_lowercase + string.ascii_lowercase
sentence = list(input('Enter your text: \n').lower())
choice = input('Choose e for Encrypt or d for decrypt\n').lower()
shift_number = int(input('Choose a shift number from 1 to 25: \n'))

end_program = False

while not end_program:
    if choice == 'e':
        for a in range(len(sentence)):
            if sentence[a] == ' ':
                sentence[a] = ' '
            else:
                new_letter = alphabets.index(sentence[a]) + shift_number
                sentence[a] = alphabets[new_letter]
        print(''.join(map(str, sentence)))
        end_program = True
    elif choice == 'd':
        for a in range(len(sentence)):
            if sentence[a] == ' ':
                sentence[a] = ' '
            else:
                new_letter = alphabets.index(sentence[a]) - shift_number
                sentence[a] = alphabets[new_letter]
        print(''.join(map(str, sentence)))
        end_program = True
    else:
        decide = input(
            'Invalid Entry, try again Y for YES, N for NO: \n').lower()
        if decide == 'y':
            sentence = list(input('Enter your text: \n').lower())
            choice = input('Choose e for encrypt or d for decrypt\n').lower()
            shift_number = int(input('Choose a shift number from 1 to 25: \n'))
        else:
            end_program = True
