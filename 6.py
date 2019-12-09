import networkx as nx

def read_input():
    return open('6.in').readlines()

edge_list = [x.strip().split(')') for x in read_input()]

def p1(edges_list):
    g = nx.DiGraph()
    g.add_edges_from(edge_list)

    return sum([len(nx.ancestors(g, x)) for x in g.nodes()])

def p2(edge_list):
    g = nx.Graph()
    g.add_edges_from(edge_list)
    return nx.dijkstra_path_length(g, source="YOU", target="SAN") -2

print (p1(edge_list))
print (p2(edge_list))
