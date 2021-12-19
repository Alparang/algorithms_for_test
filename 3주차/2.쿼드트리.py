# 행,렬 (n) 입력
n = int(input())    

#출력을 위한 배열
tree = [list(map(int,(input()))) for _ in range(n)]

#결과값을 위한 배열
result = []

def quadTree(x,y,n):
    global result

    color = tree[x][y] 
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != tree[i][j]: # 범위 내에 맨 처음 숫자와 다른 
                result.append("(")  # 괄호 ( 를 추가
                quadTree(x, y, n//2)
                quadTree(x, y+n//2, n//2)
                quadTree(x+n//2, y, n//2)
                quadTree(x+n//2, y+n//2, n//2)
                result.append(")")  # 괄호 ) 를 추가
                return
    result.append(color)

quadTree(0,0,n)
print("".join(map(str,(result))))