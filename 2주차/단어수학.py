
#input의 개수
n = int(input())

#문자 딕셔너리
al_dic = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
al_li = []
result = 0
lists = []

# n만큼의 숫자를 입력받고 리스트에 삽입함.

for i in range(n):
    al = input()
    lists.append(al)

# 자릿수에 맞게 10을 곱하여 딕셔너리에 저장.

for al in lists:
    for i in range(len(al)):
        num = 10 ** (len(al) - i - 1)
        al_dic[al[i]] += num


# 딕셔너리에 저장된 알파벳만 따로 저장해줌

for value in al_dic.values():
    if value > 0:
        al_li.append(value)

# 내림차순으로 정렬을 하고 9부터 내림차순으로 곱해줌.

sorted_list = sorted(al_li, reverse=True)
for i in range(len(sorted_list)):
    result += sorted_list[i] * (9 - i)

print(result)