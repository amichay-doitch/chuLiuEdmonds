import sys
import os


def file2data(path_f):
    f = open(path_f, 'r')
    f = f.readlines()
    data = []
    sentence = []
    for line in f:
        l = line.strip().split()
        if l:
            sentence.append(l)
        else:
            data.append(sentence)
            sentence = []
    return data


def plot_parse_tree(sentence):
    try:
        import networkx as nx
        import random
        import matplotlib.pyplot as plt
    except:
        return
    labels = dict()
    pos = dict()
    G = nx.DiGraph()

    for w in sentence:
        G.add_node(w[0], word=w[1])
        labels[w[0]] = w[1]
        pos[w[0]] = w[0]
    pos['0'] = 0
    labels['0'] = "ROOT"
    for w in sentence:
        G.add_edge(w[6], w[0], weight=int(random.random() * 100))
    pos = nx.spring_layout(G)
    print labels
    nx.draw_networkx_nodes(G, pos)
    for i, nodes in enumerate(G):
        #f = family_names[(i % 4)]
        # extract the subgraph
        g = G.subgraph(G[i])
        # draw on the labels with different fonts
        nx.draw_networkx_labels(g, pos,  font_size=40)
    nx.draw_networkx_edges(G, pos, labels=labels, font_size=40)
    plt.show()





def main():
    data = file2data("C:\Users\user\Dropbox\NLP\NLPamichayIftah\HW2\code\data\wsj_gold_dependency_sample")
    sentence = data[0]
    plot_parse_tree(sentence)

if __name__ == "__main__":
    main()