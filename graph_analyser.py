import networkx as nx # library for graphs
import matplotlib.pyplot as plt # library for plots

# Time duration of works:
a = 3
b = 5
c = 2
d = 4
e = 3
f = 1
g = 4
h = 3
i = 3
j = 2
k = 5

# Initializes directed graph
graph = nx.DiGraph()

# Adds nodes with grid layout
graph.add_node(0, pos = (0, 1))
graph.add_node(1, pos = (1, 2))
graph.add_node(2, pos = (1, 1))
graph.add_node(3, pos = (1, 0))
graph.add_node(4, pos = (2, 2))
graph.add_node(5, pos = (2, 1))
graph.add_node(6, pos = (2, 0.5))
graph.add_node(7, pos = (3, 2))
graph.add_node(8, pos = (3, 1))
graph.add_node(9, pos = (3, 0))
graph.add_node(10, pos = (4, 1))

# Adds directed edges with weight
graph.add_edge(0, 1, weight = a)
graph.add_edge(0, 2, weight = b)
graph.add_edge(0, 3, weight = c)
graph.add_edge(1, 4, weight = d)
graph.add_edge(2, 5, weight = e)
graph.add_edge(2, 6, weight = f)
graph.add_edge(4, 7, weight = g)
graph.add_edge(5, 8, weight = h)
graph.add_edge(6, 9, weight = i)
graph.add_edge(3, 9, weight = i)
graph.add_edge(7, 10, weight = j)
graph.add_edge(8, 10, weight = k)
graph.add_edge(9, 10, weight = k)


# Draws source graph of works
plt.figure()
pos = nx.get_node_attributes(graph, 'pos')
nx.draw(graph, pos, with_labels = True)
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
# Uncomment string below if you want to look at the picture
# plt.show()
print("Saving source graph...")
plt.savefig('screenshots/graph.png')

# Finds and draws graph of critical path
plt.figure()
subgraph = graph.subgraph(nx.dijkstra_path(graph, 0, 10))
pos = nx.get_node_attributes(subgraph, 'pos')
nx.draw(subgraph, pos, with_labels = True)
labels = nx.get_edge_attributes(subgraph, 'weight')
nx.draw_networkx_edge_labels(subgraph, pos, edge_labels=labels)
# Uncomment string below if you want to look at the picture
# plt.show()
print("Saving critical path...")
plt.savefig('screenshots/critical_path.png')

# Prints critical path
print("\nCritical path:")
edges = subgraph.edges.data('weight')
edges = sorted(edges, key = lambda x: (x[0], x[1], x[2]))
counter = 0
total_weight = 0
for (source, destination, weight) in edges:
    if counter % 2 == 0:
        print('(', source, ') ---',weight, '---> (', destination, ')', sep='', end='')
    else:
        print(' ---', weight, '---> ', sep='', end='')
    total_weight += weight
    counter += 1
print("\n\nAmount of works in critical path:", counter)
print("Total duration of works in critical path:", total_weight)
