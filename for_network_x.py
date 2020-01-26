import networkx as nx


def new_graph(edges_list_1):
    print(f'list in def {edges_list_1}')
    g = nx.Graph()
    g.add_weighted_edges_from(edges_list_1)
    stp = nx.minimum_spanning_edges(g, algorithm='kruskal', data=True)
    return list(stp)


if __name__ == '__main__':
    from data_for_test import nodes, add_nodes
    from for_edges import for_edges

    root_full_mash_edges = for_edges(nodes)

    new_graph_list = new_graph(root_full_mash_edges)
    print(new_graph_list)