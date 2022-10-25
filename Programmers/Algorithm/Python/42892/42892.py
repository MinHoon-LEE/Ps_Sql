import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    nodeinfo = sorted(nodeinfo, key = lambda x : (-x[1],x[0]))
    answer = []
    return(preorder(nodeinfo),postorder(nodeinfo))
    
def preorder(tree):
    if len(tree) == 0:
        return []
    if len(tree) == 1:
        return [tree[0][2]]
    left_tree = []
    right_tree = []
    curr_node = tree[0]
    for node in tree:
        if node[0] < curr_node[0]:
            left_tree.append(node)
        elif node[0] > curr_node[0]:
            right_tree.append(node)
    # VLR
    return  [curr_node[2]] + preorder(left_tree) + preorder(right_tree)
    
def postorder(tree):
    if len(tree) == 0:
        return []
    if len(tree) == 1:
        return [tree[0][2]]
    # LRV
    left_tree = []
    right_tree = []
    curr_node = tree[0]
    for node in tree:
        if node[0] < curr_node[0]:
            left_tree.append(node)
        elif node[0] > curr_node[0]:
            right_tree.append(node)
    return  postorder(left_tree) + postorder(right_tree) + [curr_node[2]]
