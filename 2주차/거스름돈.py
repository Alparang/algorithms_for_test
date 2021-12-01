#가진 지폐
money = 0
list = [500, 100, 50, 10, 5 ,1]
#거스름돈의 개수
cnt = 0

n = 1000 - int(input())

for i in list:
    cnt = cnt + int(n / i)
    n = n % i
print(cnt)