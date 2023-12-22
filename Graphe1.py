import matplotlib.pyplot as plt
import networkx as nx

# Création de l'arbre de jeu pour le scénario décrit
G = nx.DiGraph()

# Ajout des nœuds et des branches
# Niveau 1 (choix de Xavier)
G.add_node("Start", pos=(0, 0))
G.add_node("X_V", pos=(-2, -1))  # Xavier choisit Vanille
G.add_node("X_C", pos=(2, -1))  # Xavier choisit Chocolat

# Niveau 2 (choix de Yvan)
# Si Xavier choisit Vanille
G.add_node("XV_YV", pos=(-3, -2))  # Yvan choisit aussi Vanille
G.add_node("XV_YC", pos=(-1, -2))  # Yvan choisit Chocolat

# Si Xavier choisit Chocolat
G.add_node("XC_YV", pos=(1, -2))  # Yvan choisit Vanille
G.add_node("XC_YC", pos=(3, -2))  # Yvan choisit aussi Chocolat

# Niveau 3 (choix de Zacharie)
# Ajout des feuilles (résultats finaux)
G.add_node("XVYV_ZV", pos=(-3.5, -3))  # Tous choisissent Vanille
G.add_node("XVYV_ZC", pos=(-2.5, -3))  # Zacharie choisit Chocolat
G.add_node("XVYC_ZV", pos=(-1.5, -3))  # Zacharie choisit Vanille
G.add_node("XVYC_ZC", pos=(-0.5, -3))  # Tous choisissent Chocolat
G.add_node("XCYV_ZV", pos=(0.5, -3))  # Tous choisissent Vanille
G.add_node("XCYV_ZC", pos=(1.5, -3))  # Zacharie choisit Chocolat
G.add_node("XCYC_ZV", pos=(2.5, -3))  # Zacharie choisit Vanille
G.add_node("XCYC_ZC", pos=(3.5, -3))  # Tous choisissent Chocolat

# Ajout des branches
G.add_edges_from([
    ("Start", "X_V"), ("Start", "X_C"),
    ("X_V", "XV_YV"), ("X_V", "XV_YC"),
    ("X_C", "XC_YV"), ("X_C", "XC_YC"),
    ("XV_YV", "XVYV_ZV"), ("XV_YV", "XVYV_ZC"),
    ("XV_YC", "XVYC_ZV"), ("XV_YC", "XVYC_ZC"),
    ("XC_YV", "XCYV_ZV"), ("XC_YV", "XCYV_ZC"),
    ("XC_YC", "XCYC_ZV"), ("XC_YC", "XCYC_ZC")
])

# Ajout des labels aux arrêtes
edge_labels = {
    ("Start", "X_V"): "Xavier: Vanille",
    ("Start", "X_C"): "Xavier: Chocolat",
    ("X_V", "XV_YV"): "Yvan: Vanille",
    ("X_V", "XV_YC"): "Yvan: Chocolat",
    ("X_C", "XC_YV"): "Yvan: Vanille",
    ("X_C", "XC_YC"): "Yvan: Chocolat",
    ("XV_YV", "XVYV_ZV"): "Zacharie: Vanille",
    ("XV_YV", "XVYV_ZC"): "Zacharie: Chocolat",
    ("XV_YC", "XVYC_ZV"): "Zacharie: Vanille",
    ("XV_YC", "XVYC_ZC"): "Zacharie: Chocolat",
    ("XC_YV", "XCYV_ZV"): "Zacharie: Vanille",
    ("XC_YV", "XCYV_ZC"): "Zacharie: Chocolat",
    ("XC_YC", "XCYC_ZV"): "Zacharie: Vanille",
    ("XC_YC", "XCYC_ZC"): "Zacharie: Chocolat"
}

# Mise à jour des positions des nœuds
pos = {
    "Start": (0, 0),
    "X_V": (-2, -1), "X_C": (2, -1),
    "XV_YV": (-3, -2), "XV_YC": (-1, -2),
    "XC_YV": (1, -2), "XC_YC": (3, -2),
    "XVYV_ZV": (-3.5, -3), "XVYV_ZC": (-2.5, -3),
    "XVYC_ZV": (-1.5, -3), "XVYC_ZC": (-0.5, -3),
    "XCYV_ZV": (0.5, -3), "XCYV_ZC": (1.5, -3),
    "XCYC_ZV": (2.5, -3), "XCYC_ZC": (3.5, -3)
}

# Labels pour les nœuds feuilles
leaf_labels = {
    "XVYV_ZV": "(500/3,500/3,500/3)",
    "XVYV_ZC": "(250,250,750)",
    "XVYC_ZV": "(250,750,250)",
    "XVYC_ZC": " (500,375,375)",
    "XCYV_ZV": "(750,250,250)",
    "XCYV_ZC": " (375,500,375)",
    "XCYC_ZV": "(375,375,500)",
    "XCYC_ZC": "(250,250,250)"
}

# Mise à jour des labels des nœuds feuilles dans le graphe
for node in leaf_labels:
    G.nodes[node]['label'] = leaf_labels[node]

# Dessin de l'arbre avec les labels
plt.figure(figsize=(15, 9))
nx.draw(G, pos, with_labels=True, labels=nx.get_node_attributes(G, 'label'), arrows=True, node_size=7000, node_color="lightblue")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='green')

plt.show()
