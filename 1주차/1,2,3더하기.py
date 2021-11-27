n = int(input()) #테스트 케이스 개수
test_list = []  # 테스트 리스트
for i in range(n):

    test_list.append(int(input()))

dp = [1, 2, 4] #1,2,4 for 점화식

for i in range(3, 10):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

for i in test_list:
    print(dp[i-1])