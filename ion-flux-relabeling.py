class node:
    def __init__(self):
        self.lc = -1
        self.rc = -1
        self.p = -1
        self.l = -1

def build_tree(h):
    node_count = pow(2, h) - 1
    root_node = build_rec(h, node_count, 0, None)

    return root_node

def build_rec(max_h, num, cur_h, parent):
    temp = node()
    temp.p = parent
    temp.l = num
    if (cur_h < max_h - 1):
        temp.lc = build_rec(max_h, int(num/2), cur_h + 1, temp)
        temp.rc = build_rec(max_h, int(num-1), cur_h + 1, temp)
        return temp
    
    if cur_h == max_h - 1: 
        return temp


def number_tree(root):
    root = number_rec(root, 1)

    return root

def number_rec(node, val):
    if node.lc == -1:
        node.l = val

    elif node.lc != -1:
        node.lc = number_rec(node.lc, val)
        node.rc = number_rec(node.rc, node.lc.l + 1)
        node.l = node.rc.l + 1

    return node

def find_parent(root, c):
    iter = root
    found = False

    if root.l == c: 
        return -1

    while not found: 
        if iter.l == c:
            return iter.p.l

        elif iter.lc.l != -1: 
            if c <= iter.lc.l:
                iter = iter.lc
            else: iter = iter.rc


        else: 
            return iter.l


def solution(h, query):
    root = build_tree(h)
    root = number_tree(root)

    results = []

    for q in query: 
        results.append(find_parent(root, q))

    return results

print(solution(5, [19, 14, 28]))