list = [0, 1]

for i in range(0,19):
    list.append(list[i] + list[i+1])

n = int(input())

print(list[n])