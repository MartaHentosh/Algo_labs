# Функція для зчитування графу з файлу
def read_graph(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                u, v = map(int, line.strip().split(','))
                if u in graph:
                    graph[ u ].append(v)
                else:
                    graph[ u ] = [ v ]
    return graph


# Функція для знаходження мінімальної глибини
def find_minimum_depth(graph, root):
    if root not in graph:
        print("Root node not found in the graph")
        return 0

    visited = set()
    queue = [ (root, 0) ]
    depth = float('inf')

    while queue:
        node, current_depth = queue.pop(0)
        visited.add(node)

        if current_depth > depth:
            break

        children = graph.get(node, [ ])
        for child in children:
            if child not in visited:
                queue.append((child, current_depth + 1))

        if not children:
            depth = min(depth, current_depth)

    return depth + 1


if __name__ == "__main__":
    graph = read_graph("input.txt")
    root = 1

    depth = find_minimum_depth(graph, root)

    with open("output.txt", 'w') as output_file:
        output_file.write(str(depth))
