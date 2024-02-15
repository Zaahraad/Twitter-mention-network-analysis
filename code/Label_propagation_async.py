import networkx as nx
import collections
import numpy as np
import csv


def read_graph_from_file(path):
    print("loading Graph...")
    graph = nx.read_edgelist(path, nodetype=int, edgetype=int, data=(("weight", float),))
    if nx.is_directed(graph):
        UNdir_graph = nx.to_undirected(graph)
        return UNdir_graph
    else:
        return graph


def save_community(community):
    dict_com = {}
    for index, item in enumerate(community):
        for node in item:
            dict_com[node] = index

    print("Saving in file...")
    with open("community/labelPropagation.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Id", "lpa"])
        for key, value in dict_com.items():
            writer.writerow([key, value])


def lpa_communities(G):
    print("compute LPA...")
    # initial label for each node
    labels = {n: i for i, n in enumerate(G)}

    # at least one node label change
    exp = True
    while exp:
        exp = False

        shuffled_nodes = list(G.nodes())
        np.random.shuffle(shuffled_nodes)

        for node in shuffled_nodes:
            u_nbr = G[node]
            if len(u_nbr) > 0:

                nbr_labels = [labels[v] for v in u_nbr]
                nbr_label_counter = dict(collections.Counter(nbr_labels))
                max_freq_label = max(nbr_label_counter.values())

                best_labels = [k for k, v in nbr_label_counter.items() if v == max_freq_label]
                choosed_label = np.random.choice(best_labels)

                if labels[node] != choosed_label:
                    labels[node] = choosed_label
                    exp = True

        label_to_nodes_dict = {}
        for n, label in labels.items():
            if label in label_to_nodes_dict:
                label_to_nodes_dict[label].append(n)
            else:
                label_to_nodes_dict[label] = [n]
        return list(label_to_nodes_dict.values())


G = read_graph_from_file("higgs-mention_network.edgelist")
lpa = lpa_communities(G)
save_community(lpa)
