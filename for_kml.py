import simplekml

def for_kml(nodes_list, graph_list):
    kml = simplekml.Kml()
    for node_id, node_lat, node_long in nodes_list:
        kml.newpoint(
            name=node_id,
            coords=[(node_long, node_lat)]
        )  # lon, lat, optional height

    for node_a, node_b, weight in graph_list:
        #print(node_a[0], node_b[1], weight.get('weight'))#.get('distance'))
        node_a_name, node_a_lat, node_a_long = node_a
        node_b_name, node_b_lat, node_b_long = node_b
        distance = weight.get('weight')
        #edge_weight = weight.get('weight').get('weight')

        lin = kml.newlinestring(
            name=f'{node_a_name} - {node_b_name}',
            description=f'{node_a_name} - {node_b_name}, distance: {distance}',
            coords=[(node_a_long, node_a_lat), (node_b_long, node_b_lat)],
        )# lon, lat, optional height

        if distance == 0:
            lin.style.linestyle.color = simplekml.Color.black
        else:
            #kml.style.labelstyle.color = simplekml.Color.red
            #kml.style.iconstyle.color = simplekml.Color.red
            lin.style.linestyle.color = simplekml.Color.red
            lin.style.linestyle.width = 3
    kml.save('graph.kml')

if __name__ == '__main__':
    from data_for_test import nodes
    from for_edges import for_edges
    from for_network_x import for_graph

    edges_list = for_edges(nodes)
    full_mash_graph_list, graph_list = for_graph(nodes, edges_list)
    print(f'full mash list {full_mash_graph_list}')
    print(f'List: {graph_list}')
    for_kml(nodes, graph_list)