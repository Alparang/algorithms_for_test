n = int(input())
m = list(map(int, input().split()))


for i in range(len(m)-1, -1, -1):
    if(i == 0): # 마지막 순열 일 시
        print("-1")
        break
    else:
        if(m[i-1] < m[i]):
            m[i-1], m[i] = m[i], m[i-1] # 뒷자리 수 두 개 바꾸기
            print(' '.join(map(str, m)))
            break
