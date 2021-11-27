n, m = map(int, input().split())
visited = [False] * n # 탐사 노드
result = [] # 출력

def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, result))) #결과를 띄어쓰기 하여 출력
        return
    for i in range(len(visited)):
        if visited[i] == False:
            visited[i] = True
            result.append(i + 1)
            solve(depth + 1, n, m) #dfs
            visited[i] = False
            result.pop()
        
solve(0, n, m)