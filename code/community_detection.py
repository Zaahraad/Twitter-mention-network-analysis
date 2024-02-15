import community as community_louvain
import networkx as nx
from igraph import *
import csv

G_nx = nx.read_weighted_edgelist("higgs-mention_network.edgelist",create_using=nx.DiGraph, nodetype=int)

'''Louvain community detection'''
# Louvain = community_louvain.best_partition(nx.to_undirected(G_nx))


# with open('centrality/louvaine.csv','w',newline='') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["id", "louvain"])
#     for key, value in Louvain.items():
#        writer.writerow([key, value])


'''Infomap community detection'''
G_ig = Graph.Read_Ncol("higgs-mention_network.edgelist",names=("Source","Target","weight"),weights="if_present",directed=True)
infomap = G_ig.community_infomap()
print(infomap)
#
# membership = infomap.membership
# writer = csv.writer(open(f"centrality/infomap.csv", "w"))
# writer.writerow(['Id','infomap'])
# for id, memb in zip(G_ig.vs['name'], membership):
#     writer.writerow([id, memb])
