def find_last_occurrence(haystack, needle):
    comparisons = 0
    last_index = -1

    for i in range(len(haystack) - len(needle) + 1):
        match = True
        comparisons += 1

        for j in range(len(needle)):
            comparisons += 1
            if haystack[i + j] != needle[j]:
                match = False
                break

        if match:
            last_index = i

    print(f"Needle: {needle}, Last Index: {last_index}, Comparisons: {comparisons}")

    return last_index, comparisons


haystack = "hello world"
needle = "world"
result = find_last_occurrence(haystack, needle)
