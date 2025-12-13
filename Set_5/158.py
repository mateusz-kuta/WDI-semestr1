

def possible_sums(n, result=''):
    if n == 0:
        if result.find('+') != result.rfind('+'):
            print(result[:-1])
        return
    for i in range(1, n+1):
        possible_sums(n-i, result+str(i)+'+')


if __name__ == "__main__":
    num = int(input("Enter the number: "))
    possible_sums(num)
