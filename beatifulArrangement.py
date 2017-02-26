def reject(node):
    seen = set(node)
    if len(seen) < len(node):
        return True

def accept(l, node):
    seen = set(node)
    if len(seen) == len(l):
        return True

def first(l, node):
    k = len(node)
    if k == len(l):
        return
    else:
        new_node = node.copy()
        new_node.append(l[k][0])
        return new_node

def nextt(l, node):
    k = len(node)
    if node[-1] == l[k-1][-1]:
        return
    else:
        new_node = node[:-1].copy()
        new_node.append(l[k-1][l[k-1].index(node[-1])+1])
        return new_node




def backTrack(l, node, count):
    if reject(node):
        return
    if accept(l, node):
        count[0] += 1
        return
    s = first(l, node)
    while s:
        backTrack(l, s, count)
        s = nextt(l, s)
    

def countArrangement(N):
    l = []

    for i in range(1, N+1):
        r = []
        for j in range(1, N+1):
            if i % j == 0 or j % i == 0:
                r.append(j)
        l.append(r)
    count = [0]
    backTrack(l, [], count)
    print(count[0])
    
        
for i in range(1, 15):
    countArrangement(i)




