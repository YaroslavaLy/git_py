def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def dev(a, b):
    if b == 0:
        return 'incorrect value'
    return a / b


def mul(a, b):
    return a * b


def ex(a, b):
    return a ** b


def sq(a):
    return a ** -1


def cub(a):
    return a ** -2


print("Select the number of operation:")
print('1.plus')
print('2.minus')
print('3.divide')
print('4.multiply')
print('5.exponentiation')
print('6.square root')
print('7.cube root')
print('8.exit')

while True:
    op = input("Enter your choice: ")
    match op:
        case '1':
            a = int(input("Enter first number:"))
            b = int(input("Enter second number:"))
            print(plus(a, b))
        case '2':
            a = int(input("Enter first number:"))
            b = int(input("Enter second number:"))
            print(minus(a, b))
        case '3':
            a = int(input("Enter first number:"))
            b = int(input("Enter second number:"))
            print(dev(a, b))
        case '4':
            a = int(input("Enter first number:"))
            b = int(input("Enter second number:"))
            print(mul(a, b))
        case '5':
            a = int(input("Enter first number:"))
            b = int(input("Enter second number:"))
            print(ex(a, b))
        case '6':
            a = int(input("Enter a number:"))
            print(sq(a))
        case '7':
            a = int(input("Enter a number:"))
            print(cub(a))
        case '8':
            break
