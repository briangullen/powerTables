print('Learn your squares and cubes!')
# ask_continue = 'y'
while True:
    chosen_number = int(input('Enter an integer: '))
    print('Number\tSquared\tCubed')
    print('======\t=======\t=====')
    for i in range(1, int(chosen_number)+1):
        print(f'{i}\t\t{i**2}\t\t{i**3}')
    print()

    for x in range(1, chosen_number + 1):
        print(f'\t{x}', end='')
    print()
    for x in range(1, chosen_number + 1):
        print('\t=', end="")
    print()

    for x in range(1, chosen_number + 1):
        print(int(x), '| ', end="")
        for y in range(1, chosen_number + 1):
            print((x * y), '\t', end="")
        print()

    ask_continue = input('Continue? (y/n): ')
    ask_continue = ask_continue.lower()
    if ask_continue == 'y':
        continue
    else:
        break
