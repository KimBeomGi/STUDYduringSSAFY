import sys
sys.stdin = open('2230404 5249 최소 신장 트리.txt')

# [문제풀이]
# 0. 사이클을 제거하고 모든 노드를 포함하는 트리를 구성 한다했으므로 최소 신장트리를 이용하자.
# 0-1. 이때 kruskal을 이용해보자.

# T = int(input())
# for testcase in range(1, T+1):
#     V, E = map(int, input().split())
    
#     # graph = [tuple(map(int, input().split())) for _ in range(E)]
#     # print(graph)
#     graph = []
#     for _ in range(E):
#         a, b, weight =map(int,input().split())
#         graph.append((a,b,weight))
#     print(graph)
#     mst = set()

#     p = [x for x in range(V+1)]
#     def find_set(x):
#         if x == p[x]:
#             return x
#         else:
#             return find_set(p[x])
    
#     def union(x,y):
#         p[find_set(y)] = find_set(x)
    
#     for i in range(E):
#         if find_set(graph[i][0]) == find_set(graph[i][1]):
#             continue
#         mst.add(graph[i])
#         union(graph[i][0],graph[i][1])
#     print(mst)



# #### 얘는 PRIM으로 풀었음.
T = int(input())
for testcase in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        a, b, w = map(int, input().split())
        graph[a][b] = w
        graph[b][a] = w

    def prim(graph,V, start):
        mst = set()
        pi = [None]*(V+1)
        weight =[0xffffffffff]*(V+1)
        weight[start] = 0
        while len(mst) < V+1:
            min_v = 0xfffff
            min_idx = 0
            for i in range(V+1):
                if i not in mst and weight[i] < min_v:
                    min_v = weight[i]
                    min_idx = i
            mst.add(min_idx)
            for i in range(V+1):
                if i not in mst and graph[min_idx][i] \
                        and weight[i] > graph[min_idx][i]:
                    weight[i] = graph[min_idx][i]
                    pi[i] = min_idx
        return (pi,weight)
    
    result = prim(graph, V, 0)
    print(f'#{testcase} {sum(result[1])}')
    # for row in result:
    #     # print(row)
    #     pass