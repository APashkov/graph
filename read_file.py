import csv

def read_nodes(file):
    nodes = []
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='	', quotechar='|')
        next(reader)
        for row in reader:
            #print(', '.join(row))
            if row[3] != 'Россия':
                continue
            nodes.append((row[0], float(row[1]), float(row[2])))
            '''r = tuple(row)
            print(type(r))
            print(row[0], row[1], row[2])'''

    return nodes


if __name__ == '__main__':
    file = 'city_data'
    print(read_nodes(file))