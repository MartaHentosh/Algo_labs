def find_largest_number(numbers, k):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key > numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key

    largest_number = numbers[k - 1]
    index = numbers.index(largest_number)
    return largest_number, index


if __name__ == '__main__':
    array = [15, 7, 22, 9, 36, 2, 42, 18]
    k = 3
    result, index = find_largest_number(array, k)
    print(result)
    print(index)
