#need a node class to build and iterate over the binary tree 
class node:
    def __init__(self):
        self.lc = -1 #left child node
        self.rc = -1 #right child node
        self.p = -1  #parent node
        self.l = -1  #label, or numbered value

def build_tree(h): #driver function to begin recursive build
    node_count = pow(2, h) - 1
    root_node = build_rec(h, node_count, 0, None)

    return root_node

def build_rec(max_h, cur_h, parent): #recursive build function 
    temp = node() #generates a node per call
    temp.p = parent #keeps track of parent from previous call
    if (cur_h < max_h - 1):
        temp.lc = build_rec(max_h, cur_h + 1, temp) #recurse left children
        temp.rc = build_rec(max_h, cur_h + 1, temp) #recurse right children
        return temp
    
    if cur_h == max_h - 1: #end condition, height reached
        return temp

def number_tree(root): #driver function to number tree by post order traversal
    root = number_rec(root, 1)

    return root

def number_rec(node, val): #recursive function to number nodes 
    if node.lc == -1: #if no child nodes, take passed value 
        node.l = val

    elif node.lc != -1: #if child nodes remain, continue recursion 
        node.lc = number_rec(node.lc, val) #left sub-tree takes priority via POT
        node.rc = number_rec(node.rc, node.lc.l + 1) #right nodes follow 
        node.l = node.rc.l + 1 #current recursed node takes right child val + 1

    return node

def find_parent(root, c): #function to traverse labeled tree to find parent 
    iter = root #iteration node 
    found = False

    if root.l == c: #edge case: root node (no child)
        return -1

    while not found: 
        if iter.l == c: #if iter on child node, return parent label
            return iter.p.l

        elif iter.lc.l != -1: #if child nodes remain, traverse down the tree 
            if c <= iter.lc.l:
                iter = iter.lc
            else: iter = iter.rc

        else: #no child nodes, must be parent node via perfect tree 
            return iter.l 

def solution(h, query): #solution driver 
    root = build_tree(h)
    root = number_tree(root)

    results = []

    for q in query: #iterate through requested nodes
        results.append(find_parent(root, q))

    return results