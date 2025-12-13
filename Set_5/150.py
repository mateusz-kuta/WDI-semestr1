

def find_shortest_subarray(arr):
    result = []

    def recursion(sum_indexes=0, sum_values=0, index=0, counter=0):
        if sum_indexes == sum_values != 0:
            result.append((sum_values, counter))
            return
        if index == len(arr):
            return
        for i in range(index, len(arr)):
            recursion(sum_indexes+i, sum_values+arr[i], index+1, counter+1)

    recursion()
    print(result)
    return min(result, key=lambda x: x[1])


if __name__ == '__main__':
    T = [1, 7, 3, 5, 11, 2]
    print(find_shortest_subarray(T))
