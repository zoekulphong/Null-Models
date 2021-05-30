import networkx as nx
import matplotlib.pyplot as plt
from portrait_divergence import portrait_divergence
from portrait_divergence import portrait_py

sample_graph = nx.read_gml('sample_graph.gml', label = 'id')
er_graph = nx.read_gml('er_graph.gml', label = 'id')
#er_graph_py = nx.gnm_random_graph(20, 10)
#sample_graph_2 = nx.read_gml('sample_graph_2.gml', label = 'id')

print("Djs(ER1,ER2) =", portrait_divergence(sample_graph, er_graph))

plt.matshow(portrait_py(sample_graph))
plt.colorbar()
plt.show()

plt.matshow(portrait_py(er_graph))
plt.colorbar()
plt.show()