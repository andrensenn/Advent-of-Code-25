
soma = 0
bateries = []
f = open("Day3\in.txt", "r")
for line in f:
    bateries.append(line)
f.close()
j = 0
while len(bateries) != 0:
    cur_bat = bateries.pop(0)
    num1 = int(cur_bat[0])
    num2 = int(cur_bat[1])
    for i in range(2, len(cur_bat)-2):
        if int(cur_bat[i]) > num1:
            num1 = int(cur_bat[i])
            num2 = int(cur_bat[i+1])
            i +=1
        elif int(cur_bat[i]) > num2:
            num2 = int(cur_bat[i])
    
    if int(cur_bat[-2]) > num2:
        num2 = int(cur_bat[-2])
    print(j, num1*10+num2)
    j += 1
    soma = soma + num1*10 + num2
print(soma)