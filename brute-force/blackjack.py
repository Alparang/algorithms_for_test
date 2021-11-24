#입력
n, m = map(int, input().split())
card_list = list(map(int, input().split()))

#결과값
result = 0
tmp = 0

for i in range(n):
    for j in range(n):
        if(i != j):
            tmp = card_list[i] + card_list[j]
        else:
            continue
        for k in range(n):
            if(k != i  and k != j):
                tmp += card_list[k]
                if(tmp <= m and tmp >= result):
                    result = tmp
        else:
             continue             

print(result)