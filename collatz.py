# collatz


def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return number
    elif number % 2 == 1:
        number = number * 3 + 1
        print(number)
        return number
    else:
        print('error')


while True:
    print('input a number')
    try:
        n = int(input())
        tries = 0
        while n != 1:
            n = collatz(n)
            tries += 1
        print('it took ' + str(tries) + ' steps')
        break
    except ValueError:
        print('you have to input an integer number')
