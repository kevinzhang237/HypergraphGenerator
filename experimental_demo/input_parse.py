

def get_nodes():
    node_id_dict = dict()
    with open("nodes.txt") as nodefile:
        for line in nodefile:
            splitline = line.split()
            node_id_dict[splitline[0]] = node_id_dict[splitline[1]]
    return node_id_dict
