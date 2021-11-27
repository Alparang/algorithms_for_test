height_list = []
total = 0

for i in range(9):
    height_list.append(int(input()))

total = sum(height_list)

for p in range(8):
    for q in range(p + 1, 9):
        if((total - (height_list[p] + height_list[q])) == 100):
            rem_1 = height_list[p]
            rem_2 = height_list[q]

            height_list.remove(rem_1)
            height_list.remove(rem_2)

            height_list.sort()

            print(p, q)
            for k in range(7):
                print(height_list[k])
            break
    
    if(len(height_list) < 9):
        break
