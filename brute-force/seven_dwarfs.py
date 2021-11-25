height_list = []
total = 0

for i in range(9):
    height_list.append(int(input()))

total = sum(height_list)
#print("total : ")
#print(total)

for p in range(8):
    for q in range(i + 1, 9):
        if((total - height_list[p] - height_list[q]) == 100):
            height_list.remove(height_list[p])
            height_list.remove(height_list[q])
            break

height_list = sorted(height_list)
#print(height_list)

for k in range(7):
    print(height_list[k])