def full(n_first, n_last):
        print('{} {}'.format(n_first, n_last))

        if n_first.lower().strip() == '' or n_last.lower().strip() == '':
            print("It seems, that you have a very rare name ")

if __name__ == '__main__':
    first = input('Your name: ')
    last = input('Your last name: ')
    print('Greetings,')
    full(first, last)
