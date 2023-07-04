alphabet = input().upper()
alphabet_list = list(set(alphabet))

cnt_list = []
for i in alphabet_list:
    cnt = alphabet.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    max_index = cnt_list.index(max(cnt_list))
    print(alphabet_list[max_index])