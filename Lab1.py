#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:20:53 2019

@author: polo
"""

import networkx as nx
import pickle
import matplotlib.pylab as plt
from matplotlib import gridspec
#from colorbar_help import add_colorbar

with open("karate_club_coords.pkl", 'rb') as f:
     coords = pickle.load(f, encoding='latin1')
print (coords)

G = nx.karate_club_graph()
G1 = nx.convert_node_labels_to_integers(G,first_label=1)
G1 = nx.relabel_nodes(G1, lambda x: str(x))

print("Node Degree")
for v in G1:
    print('%s %s' % (v, G1.degree(v)))

#nx.draw(G1, pos=coords, with_labels=True)
nx.draw_networkx(G1, pos=coords,)
plt.show()