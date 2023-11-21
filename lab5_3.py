def build_tribes_graph(pairs):
    tribes = [set(pairs[0])]
    for pair in pairs[1:]:
        merged = False
        for tribe in tribes:
            if any(person in tribe for person in pair):
                tribe.update(pair)
                merged = True
                break
        if not merged:
            tribes.append(set(pair))
    return tribes


def count_possible_pairs(tribes):
    count = 0
    pairs = []
    for i in range(len(tribes)):
        for j in range(i + 1, len(tribes)):
            for first_person_man in tribes[i]:
                for second_person_woman in tribes[j]:
                    if first_person_man % 2 != second_person_woman % 2:
                        count += 1
                        pairs.append(f"{first_person_man}/{second_person_woman}")
    return count, pairs


def read_input(filename):
    with open(filename, 'r') as file:
        N = int(file.readline())
        if not (0 < N < 10000):
            raise ValueError("0 < N < 10000")
        pairs = [tuple(map(int, line.split())) for line in file.readlines()]
    return N, pairs


def write_output(filename, result):
    count, pairs = result
    with open(filename, 'w') as file:
        file.write(f"{count} (")
        possible_pairs = ', '.join(pairs)
        file.write(f"{possible_pairs})")


def main():
    input_filename = 'input2.txt'
    output_filename = 'output2.txt'

    try:
        N, pairs = read_input(input_filename)
        tribes = build_tribes_graph(pairs)
        result = count_possible_pairs(tribes)
        write_output(output_filename, result)
        if not (0 < N < 10000):
            raise ValueError("0 < N < 10000")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
