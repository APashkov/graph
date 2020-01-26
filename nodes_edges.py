class Node:
    def __init__(self, node):
        id = node[0]
        latitude = node[1]
        longitude = node[2]

        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.lat_rad = latitude
        self.long_rad = longitude

class Edge:
    pass

if __name__ == '__main__':
    from data_for_test import nodes
    #nodes = []
    for n in nodes:
        #print(nod[0])
        nodes.append(Node(n))
        #nodes.append(Node(n[0], n[1], n[2]))
    for row in nodes:
        print(row.id, row.latitude, row.longitude)
