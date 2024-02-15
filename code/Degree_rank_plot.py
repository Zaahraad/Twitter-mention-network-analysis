import networkx as nx
import matplotlib.pyplot as plt


G = nx.read_weighted_edgelist("higgs-mention_network.edgelist",create_using=nx.DiGraph, nodetype=int)

indegree_sequence = sorted([d for n, d in G.in_degree()], reverse=True)
outdegree_sequence = sorted([d for n, d in G.out_degree()], reverse=True)

plt.loglog(indegree_sequence, "b-", marker="o")
plt.title("IN_Degree rank plot")
plt.ylabel("in_degree")
plt.xlabel("rank")
plt.savefig("drive/MyDrive/in_Degree_rank.png")
plt.show()

plt.loglog(outdegree_sequence, "b-", marker="o")
plt.title("Out_Degree rank plot")
plt.ylabel("out_degree")
plt.xlabel("rank")
plt.savefig("drive/MyDrive/Out_Degree_rank.png")
plt.show()