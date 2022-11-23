from collections import defaultdict
import sys
sys.setrecursionlimit(10000000)

def dfs(curr, sheep, wolf, node_arr):
    global answer,child,infos
    
    if infos[curr] == 0:
        sheep += 1
        answer = max (answer, sheep)
    else:
        wolf += 1
    if sheep <= wolf:
        return
    node_arr.extend(child[curr])
    for node in node_arr:
        dfs(node,sheep,wolf,[j for j in node_arr if j != node])


def solution(info, edges):
    global answer, child, infos
    infos = info
    answer = 0
    child = defaultdict(list)
    for edge in edges:
        child[edge[0]].append(edge[1])
    dfs(0,0,0,[])    
    return answer
