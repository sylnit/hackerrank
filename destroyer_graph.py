def get_egde_weight(graph, s, v):
    for row in graph:
        if row[0] == s and row[1] == v:
            return row[2]
    return None


def get_neighbors(graph, s):
    neighbors = []
    for item in graph:
        if item[0] == s:
            neighbors.append(item[1])
        if item[1] == s:
            neighbors.append(item[0])
    return neighbors


def get_priority(s, v):
    if s in machine_list and v in machine_list:
        return 1
    elif s in machine_list or v in machine_list:
        return 2
    else:
        return 3


def clean_queue(queue):
    if queue:
        for item in queue:
            if item in visited:
                queue.pop(queue.index(item))
    return queue


def get_destroy_edges(graph, s, neighbors):

    if not neighbors:
        return

    first_edge_priority = get_priority(s, neighbors[0])
    second_edge_priority = get_priority(s, neighbors[1])
    if first_edge_priority == second_edge_priority and first_edge_priority == 1:
        for neighbor in neighbors:
            edge_weight = get_egde_weight(s, neighbor)
            edges_destruction.append(edge_weight)
    elif first_edge_priority == second_edge_priority and first_edge_priority == 2:
        first_edge = get_egde_weight(s, neighbors[0])
        second_edge = get_egde_weight(s, neighbors[1])
        min_edge = min([first_edge, second_edge])
        edges_destruction.append(min_edge)
    elif first_edge_priority == 1 and second_edge_priority > 1:
        edge_weight = get_egde_weight(s, neighbors[0])
        edges_destruction.append(edge_weight)
    elif first_edge_priority > 1 and second_edge_priority == 1:
        edge_weight = get_egde_weight(graph, s, neighbors[1])
        edges_destruction.append(edge_weight)
    elif first_edge_priority == 2 and second_edge_priority > 2:
        edge_weight = get_egde_weight(graph, s, neighbors[0])
        edges_destruction.append(edge_weight)
    elif first_edge_priority > 2 and second_edge_priority == 2:
        edge_weight = get_egde_weight(graph, s, neighbors[1])
        edges_destruction.append(edge_weight)


def bfs(graph, source):
    queue = [source]
    while len(queue) > 0:
        current = queue.pop(0)
        if current in visited:
            continue

        neighbors = get_neighbors(graph, current)
        for neighbor in neighbors:
            queue.append(neighbor)

        get_destroy_edges(graph, current, neighbors)
        visited.append(current)

    print('edges for destruction')
    print(edges_destruction)


def minTime(roads, machines):
    # Write your code here
    global edges_destruction
    global machine_list
    global visited
    edges_destruction = []
    machine_list = machines
    visited = []
    print(roads)
    print(machines)
    print(machine_list)
    roads = sorted(roads, key=lambda x: -x[2])
    start = roads[0][0]
    bfs(roads, start)
    return sum(edges_destruction)


# result = minTime([[2, 1, 8], [1, 0, 5], [2, 4, 5], [1, 3, 4]], [2, 4, 0])
# print('edges for destruction')
# print(edges_destruction)
# print(result)


# print(minTime([[0, 1, 4], [1, 2, 3], [1, 3, 7], [0, 4, 2]], [2, 3, 4]))

print(minTime([[0, 3, 3, ""], [1, 4, 4, "green"], [
      1, 3, 4, "green"], [0, 2, 5, ""]], [1, 3, 4]))
