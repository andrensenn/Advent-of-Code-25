

cur_point = 50
count = 0
list_inst = []

f = open("Day1\in.txt", "r")
for line in f:
    list_inst.append(line)
f.close()

while len(list_inst) != 0:
    cur_inst = list_inst.pop(0)
    cur_rot = 0
    if (cur_inst[0]=='L'):
        cur_rot = - int(cur_inst[1:])
    else:
        cur_rot = int(cur_inst[1:])

    cur_point = cur_point + cur_rot
    if cur_point < 0:
        cur_point = 100 + cur_point

    if cur_point % 100 == 0:
        count += 1
        cur_point = 0

    if cur_point > 100:
        cur_point = cur_point - 100
    print(cur_point)

print("\n") 
print(count)
print("\n") 

