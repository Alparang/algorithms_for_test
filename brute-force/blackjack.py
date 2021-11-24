#입력
n, m = map(int, input().split())
card_list = list(map(int, input().split()))

#결과값
result = 0
#임시값
tmp_value = 0


# (0~n), (i+1~n), (j+1~n) 으로 중복 없이 3개씩 뽑는다.
for i in range(n):
    for j in range(i+1, n):
        for k in range (j+1, n):
            tmp_value = card_list[i] + card_list[j] + card_list[k]
            if(tmp_value <= m):
                result = max(result, tmp_value)
            else:
                continue

print(result)