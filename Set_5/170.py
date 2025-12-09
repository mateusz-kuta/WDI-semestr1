

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_valid(bin_format):
    if bin_format[0] == '1' and not is_prime(int(bin_format, 2)):
        return True
    return False


def possible_numbers(a, b, result=''):
    global counter
    if a == b == 0:
        print(result, int(result, 2))
        if is_valid(result):
            counter += 1
        return counter
    if a != 0:
        possible_numbers(a-1, b, result+'1')
    if b != 0:
        possible_numbers(a, b-1, result+'0')

if __name__ == '__main__':
    counter = 0
    possible_numbers(2, 3)
    print(counter)
