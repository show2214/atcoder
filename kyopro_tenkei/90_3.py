# グラフ作成のライブラリをimport
import networkx as nx

if __name__ == "__main__":
    N = int(input())

    G = nx.Graph()
    # グラフに線を追加
    for i in range(N-1):
        a,b = map(int, input().split(" "))
        nx.add_path(G,[a,b])

    # 起点から一番遠い点を取得
    p = nx.shortest_path_length(G,1)
    l = max(p.values())
    lp =[k for k, v in p.items() if v == l][0]

    # 最大となるコストを取得
    p2 = nx.shortest_path_length(G,lp)
    print(max(p2.values())+1)