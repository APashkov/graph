from read_file import read_nodes
from data_for_test import nodes as root_nodes
from data_for_test import add_nodes

from for_edges import for_edges
from for_network_x import new_graph
from for_kml import for_kml

file = 'city_data'
nodes = read_nodes(file)

root_edges_list = for_edges(root_nodes)
root_stp_list = new_graph(root_edges_list)

new_nodes = nodes + root_nodes
new_edges_list = for_edges(new_nodes)


for edge_in_root_stp_list in root_stp_list:
    for edge_in_full_list in new_edges_list:
        if (edge_in_full_list[0] == edge_in_root_stp_list[0]) and \
                (edge_in_full_list[1] == edge_in_root_stp_list[1]):
            edge_as_list = list(edge_in_full_list)
            edge_as_list[2] = 0
            new_edges_list.remove(edge_in_full_list)
            new_edges_list.append(edge_as_list)


print(f'new list: {new_edges_list}')
new_stp = new_graph(new_edges_list)
print(f'new graph list: {new_stp}')

for_kml(new_nodes, new_stp)