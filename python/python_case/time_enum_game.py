# coding:utf-8
if __name__ == '__main__':
    import time

    play_it = input('do you want to play it.(\'y\' or \'n\')\n')
    while play_it == 'y':
        c = int(input('input a character:'))
        print('please input number you guess:\n')
        start = time.clock()
        a = time.time()
        guess = int(input('input your guess:'))
        while guess != c:
            if guess > c:
                print('please input a little smaller')
                guess = int(input('input your guess:'))
            if guess < c:
                print('please input a little bigger')
                guess = int(input('input your guess:'))
        end = time.clock()
        b = time.time()
        var = (end - start) / 18.2
        print(var)

        if var < 15:
            print('you are very clever!')
        elif var < 25:
            print('you are normal!')
        else:
            print('you are stupid!')
        print('Congradulations')
        print('The number you guess is %d' % c)
        play_it = input('do you want to paly it.')
