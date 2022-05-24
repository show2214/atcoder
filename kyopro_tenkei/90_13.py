import networkx as nx

N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]
G = nx.Graph()
G.add_weighted_edges_from(ABC, weight="weight")
from1s = nx.single_source_dijkstra_path_length(G, 1)
toNs = nx.single_source_dijkstra_path_length(G, N)

for k in range(1, N+1):
    print(from1s[k] + toNs[k])