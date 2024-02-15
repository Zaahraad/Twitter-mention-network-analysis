import networkx as nx
import snap
import matplotlib.pyplot as plt

''' calculate Strongly connected component & weakly connected component & assortativity & density  with NetworkX '''
G = nx.read_weighted_edgelist("higgs-mention_network.edgelist",create_using=nx.DiGraph, nodetype=int)

print("information about Graph : ", nx.info(G))
print("number of SCC : ", nx.number_strongly_connected_components(G))
print("number of WCC : ", nx.number_weakly_connected_components(G))
print("Density of network : ", nx.density(G))

# calculate Assortativity
print(nx.degree_pearson_correlation_coefficient(G, x='in', y='in',weight='weight'))
print(nx.degree_pearson_correlation_coefficient(G, x='out', y='out',weight='weight'))
print(nx.degree_pearson_correlation_coefficient(G, x='out', y='in',weight='weight'))
print(nx.degree_pearson_correlation_coefficient(G, x='in', y='out',weight='weight'))

''' calculate Diameter & Clustering Coefficient with snap library'''
G_snap = snap.LoadEdgeList(snap.TNGraph, "higgs-mention_network.edgelist", 0, 1)
Cf = snap.GetClustCf(G_snap, -1)
diameter = G_snap.GetBfsFullDiam(116408, True)

print("Avg Clustering Coefficient : ", Cf)
print("Diameter of Graph : ", diameter)