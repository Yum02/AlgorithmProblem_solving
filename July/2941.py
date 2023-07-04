cro_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

#ex) ljes=njak => "lj, e, s=, nj, a, k"

s = input()

for i in cro_list:
    s = s.replace(i, '*')
print(len(s))