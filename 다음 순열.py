n = int(input())
m = list(map(int, input().split()))

sorted_m = sorted(m, reverse=True)

for i in len(sorted_m):
    if(i == len(sorted_m)):
        print(-1)
    else:
        if(sorted_m[i] > sorted_m[i+1]):
            sorted_m[i], sorted_m[i+1] = sorted_m[i+1],sorted_m[i]
            print(sorted_m)
            break