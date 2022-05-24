from scipy.sparse import *

N, M, *edges = map(int, open(0).read().split())

C=[a:=0]*-~N
for i in csgraph.connected_components(csr_matrix(([1]*M,(edges[::2],edges[1::2])),[N+1]*2),1,"strong")[1]:a+=C[i];C[i]+=1
print(a)