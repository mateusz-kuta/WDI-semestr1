

def scale(table):
    for i in range(len(table)):
        divisors = set()
        divisor = 2
        while table[i] > 2:
            if table[i] % divisor == 0:
                divisors.add(divisor)
                table[i] //= divisor
            else:
                divisor += 1
        table[i] = len(divisors)
    return table


def can_divide(table, index=0, stack1=0, stack2=0, stack3=0) -> bool:
    if stack1 == stack2 == stack3 and stack1+stack2+stack3 == sum(table):
        return True
    if index == len(table):
        return False
    return can_divide(table, index + 1, stack1+table[index], stack2, stack3) or can_divide(table, index + 1, stack1, stack2+table[index], stack3) or can_divide(table, index + 1, stack1, stack2, stack3+table[index])


if __name__ == '__main__':
    T = [6, 6, 6, 6, 6, 6]
    print(can_divide(scale(T)))

