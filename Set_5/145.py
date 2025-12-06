

def is_prime(n) -> bool:
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0: return False
    return True


def possible_combinations(number):
    answer = []

    def recursion(num, result):
        string = str(num)
        if len(string) == 2:
            if is_prime(num):
                result.append(num)
            return
        if is_prime(num):
            result.append(num)
        for i in range(len(string)):
            recursion(int(string[:i] + string[i+1:]), result)

    recursion(number, answer)
    print(set(answer))


if __name__ == '__main__':
    n = int(input("Enter a number: "))
    possible_combinations(n)
