import networkx as nx
import csv


def save(centrality,name):
    print("Saving in file...")
    with open("centrality/%s.csv" % name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in centrality.items():
            writer.writerow([key, value])


G = nx.read_weighted_edgelist("higgs-mention_network.edgelist",create_using=nx.DiGraph, nodetype=int)

''' compute HIT centrality'''
h, a = nx.hits(G)
h = {k: v for k, v in sorted(h.items(), reverse=True, key=lambda item: item[1])}
save(h,"hubs")

a = {k: v for k, v in sorted(a.items(), reverse=True, key=lambda item: item[1])}
save(a,"authority")


''' compute Page Rank centrality'''
PR = {k: v for k, v in sorted((nx.pagerank(G)).items(),reverse=True, key=lambda item: item[1])}
save(PR,"PageRank")


''' compute K_shell decomposition'''
G.remove_edges_from(nx.selfloop_edges(G))
shell = nx.core_number(G)
save(shell,"K_shell")
