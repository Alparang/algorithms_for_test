n = int(input())
m = list(map(int, input().split()))
ok = 0

for i in range(n-1, 0, -1):
    if(m[i-1] < m[i]):  #
        for j in range(n-1, 0, -1):
            if(m[i-1] < m[j]):
                m[i-1], m[j] = m[j], m[i-1] 
                m = m[:i] + sorted(m[i:]) #바꾸고 정렬됨.
                ok = True
                break
    
    if(ok == True):
        print(' '.join(map(str, m))) #*m 으로 출력하는 방법도 있음
        break

if not ok:
    print('-1') #마지막 순열일 경우 -1 출력