n,s = map(int, input().split())
data = list(map(int, input().split()))
data_len = len(data)
count = 0

def dfs(idx ,sum):
    global count
    if(idx >= n):
        return 
    sum += data[idx]
    if sum == s:
        count += 1
    dfs(idx+1, sum)                 # 현재 data 값을 더하는 경우
    dfs(idx+1, sum-data[idx])       # 현재 data 값을 더하지 않는 경우

dfs(0,0)
print(count)
