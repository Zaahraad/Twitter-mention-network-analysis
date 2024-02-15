import powerlaw
import networkx as nx
import matplotlib.pyplot as plt


G = nx.read_weighted_edgelist("higgs-mention_network.edgelist",create_using=nx.DiGraph, nodetype=int)

in_degree_sequence = sorted([d for n, d in G.in_degree()], reverse=True)
out_degree_sequence = sorted([d for n, d in G.out_degree()], reverse=True)

fit_in = powerlaw.Fit(in_degree_sequence)
fit_out = powerlaw.Fit(out_degree_sequence)

print(fit_in.alpha, fit_out.alpha, sep='\n' )

fig3 = fit_in.plot_pdf(color='red',linestyle='dotted',linewidth = 4, label = "in_degree")
fig4 = fit_out.plot_pdf(color='blue',linestyle='dotted',linewidth = 4, label = "out_degree")
fit_in.power_law.plot_pdf(color='gray', linestyle='--', ax=fig3, label = "fit")
plt.xlabel("In_Degree")
plt.ylabel("P(k)_in")
plt.title("In_Degree Distribution")
plt.legend(loc="lower left")
# plt.savefig("drive/MyDrive/Degree Distribution.png")
plt.show()

fig4 = fit_out.plot_pdf(color='red',linestyle='dotted',linewidth = 4, label = "emprical")
fit_out.power_law.plot_pdf(color='gray', linestyle='--', ax=fig4, label = "fit")
plt.xlabel("Out_Degree")
plt.ylabel("P(k)_out")
plt.title("Out_Degree Distribution")
plt.legend(loc="lower left")
# plt.savefig("drive/MyDrive/Out_Degree Distribution.png")
plt.show()