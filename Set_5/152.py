

def is_possible(table, target, index=0) -> bool:
    table.sort(reverse=True)
    if target == 0:
        return True
    if (index == len(table)) or (target < 0):
        return False
    return is_possible(table, target - table[index], index + 1) or is_possible(table, target, index + 1)


if __name__ == '__main__':
    from random import randint
    T = [randint(1, 10) for i in range(5)]
    print(T)
    print(is_possible(T, 10))
