import sys
 
def main():
    inp = sys.stdin.read
    d = input().split()
    i = 0
    
    t = int(d[i])
    i += 1
    
    res = []
    for _ in range(t):
        n, m = int(d[i]), int(d[i + 1])
        i += 2
        
        g = []
        for _ in range(n):
            g.append([int(d[i + j]) for j in range(m)])
            i += m
        
        mx = n * m
        s = [False] * (mx + 1)
        ni = [False] * (mx + 1)
        dct = []
        
        for r in range(n):
            for c in range(m):
                v = g[r][c]
                if not s[v]:
                    s[v] = True
                    dct.append(v)
                if c + 1 < m and g[r][c + 1] == v:
                    ni[v] = True
                if r + 1 < n and g[r + 1][c] == v:
                    ni[v] = True
        
        tc = 0
        b = 0
        
        for v in dct:
            cost = 2 if ni[v] else 1
            tc += cost
            b = max(b, cost)
        
        res.append(str(tc - b))
    
    sys.stdout.write("\n".join(res) + "\n")
 
if __name__ == "__main__":
    main()