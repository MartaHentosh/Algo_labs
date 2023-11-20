def count_cross_tribal_pairs(N, pairs):
    graph = {}

    for boy, girl in pairs:
        if boy not in graph:
            graph[boy] = []
        graph[boy].append(girl)

    odd_boys = set()
    even_girls = set()

    for boy, girl_list in graph.items():
        if boy % 2 == 1:
            odd_boys.add(boy)
        for girl in girl_list:
            if girl % 2 == 0:
                even_girls.add(girl)

    cross_tribal_pairs = len(odd_boys) * len(even_girls)

    return cross_tribal_pairs


def read_input(filename):
    with open(filename, 'r') as file:
        N = int(file.readline().strip())
        pairs = [tuple(map(int, line.strip().split())) for line in file]

    return N, pairs


def write_output(filename, result):
    with open(filename, 'w') as file:
        file.write(str(result))


input_filename = 'input2.txt'
output_filename = 'output2.txt'

N, pairs = read_input(input_filename)
result = count_cross_tribal_pairs(N, pairs)
write_output(output_filename, result)
