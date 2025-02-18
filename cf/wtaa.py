t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    to_check = [0] * n
    
    def wtaa(n,nums,to_check):
        for i in range(1,n-1):
            if nums[i-1] == 0:
                if to_check[i] == 2:
                    to_check[i+1] = 3
                else:
                    to_check[i] = 1
                    to_check[i-1] = 1
                    to_check[i+1] = 1
                    
                
            elif nums[i-1] == 1:
                if to_check[i] == 3:
                    return "NO"
                else:
                    to_check[i-1] = 2
                    to_check[i] = 2
                    to_check[i+1] = 2
        return "YES"
    
    print(wtaa(n,nums,to_check))

