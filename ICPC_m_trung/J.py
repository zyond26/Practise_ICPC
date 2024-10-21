import sys
sys.setrecursionlimit(200000)

MAXN = 100005
LOG = 17  

adj = [[] for _ in range(MAXN)]
up = [[-1] * (LOG + 1) for _ in range(MAXN)]  
depth = [0] * MAXN
entry = [0] * MAXN
exit = [0] * MAXN
timer = 0

def dfs(v, parent):
    global timer
    entry[v] = timer
    timer += 1
    up[v][0] = parent  
    for i in range(1, LOG + 1):
        if up[v][i-1] != -1:
            up[v][i] = up[up[v][i-1]][i-1]
    
    for u in adj[v]:
        if u != parent:
            depth[u] = depth[v] + 1
            dfs(u, v)
    
    exit[v] = timer
    timer += 1

def is_ancestor(u, v):
    return entry[u] <= entry[v] and exit[u] >= exit[v]

def lca(u, v):
    if is_ancestor(u, v):
        return u
    if is_ancestor(v, u):
        return v
    for i in range(LOG, -1, -1):
        if up[u][i] != -1 and not is_ancestor(up[u][i], v):
            u = up[u][i]
    return up[u][0]

n, q = map(int, input().split())
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

dfs(1, -1)

results = []

for _ in range(q):
    x, y, z = map(int, input().split())
    lca_xz = lca(x, z)
    if (is_ancestor(lca_xz, y) and (is_ancestor(y, x) or is_ancestor(y, z))):
        results.append("YES")
    else:
        results.append("NO")

print("\n".join(results))
