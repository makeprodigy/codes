t = int(input())

def minimum_operations(t):
    results = []
    
    for _ in range(t):
        n, k, p = map(int, input().split())

        if k == 0:
            results.append(0)
            continue

        if abs(k) > n * p:
            results.append(-1)
            continue

        operations = (abs(k) + p - 1) // p
        results.append(operations)

    return results

for res in minimum_operations(t):
    print(res)