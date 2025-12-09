

def hanoi_tower(n, a, b, c):
    if n == 0:
        return
    hanoi_tower(n-1, a, c, b)
    print(n, a, '->', c)
    hanoi_tower(n-1, b, a, c)


if __name__ == '__main__':
    hanoi_tower(4, 'a', 'b', 'c')
