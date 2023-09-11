import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
from networkx.algorithms.operators.all import union_all

def LSP_surgery(G_origin: nx.Graph(), weight: str = "weight", resolution: float = 1, best_n: int = None):
    """A surgery function that remove the edges by using modularity

    Parameters
    ----------
    G_origin : NetworkX graph
        A graph with ``weight`` as Ricci flow metric to cut.
    weight: str
        The edge weight used as Ricci flow metric. (Default value = "weight")
    resolution: float
        The resolution of modularity maximization algorithm. (Default value = 1)
    best_n: int
        Maximum number of clusters to be found by the modularity maximization algorithm. (Default value = None)


    Returns
    -------
    G_cut : NetworkX graph
        A graph after surgery.
    c : list
        List of nodes in each community extracted by the modularity algorithm.
    """
    G = G_origin.copy()
    c = greedy_modularity_communities(G, weight = weight, resolution = resolution, best_n=best_n)

    l_graphs = []

    for x in c:
        l_graphs.append(G.subgraph(x))

    G_cut = union_all(l_graphs)
    to_cut = G.number_of_edges() - G_cut.number_of_edges() 
    print("*************** Surgery time ****************")
    print("* Cut %d edges." % to_cut)
    print("* Number of nodes now: %d" % G_cut.number_of_nodes())
    print("* Number of edges now: %d" % G_cut.number_of_edges())
    cc = list(nx.connected_components(G_cut))
    print("* Modularity now: %f " % nx.algorithms.community.quality.modularity(G_cut, c))
    print("*********************************************")
    return G_cut, c