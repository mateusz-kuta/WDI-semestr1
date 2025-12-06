

def newton_symbol(n, k) -> int:
    if n == k or k == 0:
        return 1
    return newton_symbol(n - 1, k - 1) + newton_symbol(n - 1, k)


if __name__ == '__main__':
    print(newton_symbol(6, 3))
