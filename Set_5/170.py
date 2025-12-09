

def advanced_number(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True
    return False


def is_valid(bin_format):
    if bin_format[-1] == '1' and advanced_number(int(bin_format, 2)):
        return True
    return False


def possible_numbers(a, b, result=''):
    global counter
    if a == b == 0:
        # print(result, int(result, 2))
        if is_valid(result):
            counter += 1
        return counter
    if a != 0:
        possible_numbers(a-1, b, result+'1')
    if b != 0:
        possible_numbers(a, b-1, result+'0')

if __name__ == '__main__':
    counter = 0
    possible_numbers(5, 5)
    print(counter)
