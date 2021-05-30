import networkx as nx
import matplotlib.pyplot as plt
from portrait_divergence import portrait_divergence
from portrait_divergence import portrait_py

# sample graph generated in R using words 1-20 of 2-3 phoneme words from Klattese
sample_graph_1 = nx.read_gml('sample_graph_1.gml', label = 'id')
# Erdos-Renyi graph generated in R
er_graph_r = nx.read_gml('er_graph_r.gml', label = 'id')
# Erdos-Renyi graph generated in Python
er_graph_py = nx.gnm_random_graph(20, 10)
# sample graph generated in R using words 20-40 of 2-3 phoneme words from Klattese
sample_graph_2 = nx.read_gml('sample_graph_2.gml', label = 'id')

print("Comparison of Sample Graph 1 and R-generated ER Graph =", portrait_divergence(sample_graph_1, er_graph_r))
print("Comparison of Sample Graph 1 and Python-generated ER Graph =", portrait_divergence(sample_graph_1, er_graph_py))
print("Comparison of Sample Graph 1 and Sample Graph 2 =", portrait_divergence(sample_graph_1, sample_graph_2))

plt.matshow(portrait_py(sample_graph_1))
plt.colorbar()
plt.show()
plt.matshow(portrait_py(er_graph_r))
plt.colorbar()
plt.show()
plt.matshow(portrait_py(er_graph_py))
plt.colorbar()
plt.show()
plt.matshow(portrait_py(sample_graph_2))
plt.colorbar()
plt.show()