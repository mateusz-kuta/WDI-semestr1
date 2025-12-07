

def two_three_five(limit, number=1):
    if number > limit:
        return
    if number == limit:
        print(number)
        return
    print(number)
    two_three_five(limit, number * 5)
    two_three_five(limit, number * 3)
    two_three_five(limit, number * 2)


if __name__ == '__main__':
    two_three_five(10)
