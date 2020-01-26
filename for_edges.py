import random
from math import sin, cos, asin, sqrt, radians

def for_edges(nodes):
    edges = []
    for node_a in nodes:
        for node_b in nodes:
            if node_a == node_b: continue
            weight = {
                'distance': edge_distance(node_a, node_b),
                'weight': random.random()
            }
            edges.append([node_a, node_b, edge_distance(node_a, node_b)])#weight])
    return edges

def edge_distance(node_a, node_b):
    node_a_name, node_a_lat, node_a_long = node_a
    node_b_name, node_b_lat, node_b_long = node_b

    dist = 2 * 6371.21 * asin(sqrt(
        sin((radians(node_b_lat) - radians(node_a_lat)) / 2) ** 2 +
        cos(radians(node_a_lat)) * cos(radians(node_b_lat)) *
        sin((radians(node_b_long) - radians(node_a_long)) / 2) ** 2
    ))

    return dist

if __name__ == '__main__':
    from data_for_test import nodes

    for_edges(nodes)
    #for edge in for_edges(nodes):
    #    print(edge)
