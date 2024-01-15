def depth(T, v):
    # T : root Node
    if T.isRoot(v):
        return 0
    else:
        return 1 + depth(T, T.parent(v))



def height(T):
    h = 0
    for each v in T.position(v):
        if T.isExternal(v):
            h = max(h,depth(T,v))
    return h

