import networkx as nx
import matplotlib.pyplot as plt

def draw_tree(file_to_check,tupled_dependency):
    G = nx.DiGraph()
    G.add_node(file_to_check)
    G.add_edges_from(tupled_dependency)

    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G,k=1,seed=3)
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='violet', font_size=6, font_weight=None, arrows=True,width=0.3)
    plt.title("File Dependency Tree Structure")
    plt.savefig(f"{file_to_check}py_file_tree", format="png")
    plt.show()
    