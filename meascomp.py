import networkx as nx
import numpy as np
from blueqat import Circuit

g = nx.fast_gnp_random_graph(10, 0.75)
# nx.nx_agraph.view_pygraphviz(g1, prog='fdp')

# TODO: Make a new class so that we can call by a method.
def CircRes(g):
    c = Circuit(g.number_of_nodes()).h[:]
    for e in g.edges():
        c.cz[e]
    return c

def StabRes(c, g, i):
    for j in g.neighbors(i):
        c.z[j]
    c.x[i]
    return c

