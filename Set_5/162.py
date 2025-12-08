

def is_prime(num):
    if num < 2: return False
    if num % 2 == 0: return True
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0: return False
    return True


def find_combinations(number1, number2):
    number1 = list(str(number1))
    number2 = list(str(number2))

    def recursion(num1, num2, result=''):
        if len(num1) == len(num2) == 0:
            print(result)
            return True
        if not len(num1) == 0:
            recursion(num1[1:], num2, result+num1[0])
        if not len(num2) == 0:
            recursion(num1, num2[1:], result+num2[0])

    recursion(number1, number2)


if __name__ == '__main__':
    find_combinations(123, 75)
