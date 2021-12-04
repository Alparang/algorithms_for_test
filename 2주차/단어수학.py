
#input의 개수
n = int(input())

#문자 딕셔너리
al_dic = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
al_li = []
result = 0
pocket = []


for _ in range(n):
    al = input()
    pocket.append(al)

for al in pocket:
    for i in range(len(al)):
        num = 10 ** (len(al) - i - 1)
        al_dic[al[i]] += num

for value in al_dic.values():
    if value > 0:
        al_li.append(value)

sorted_list = sorted(al_li, reverse=True)
for i in range(len(sorted_list)):
    result += sorted_list[i] * (9 - i)

print(result)