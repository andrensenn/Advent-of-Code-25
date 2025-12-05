soma = 0
bateries = []

f = open("Day3/in.txt", "r")
for line in f:
    bateries.append(line.strip())
f.close()

while len(bateries) != 0:
    
    cur_bat = bateries.pop(0)

    num1 = 0
    num2 = 0

    for i in range(len(cur_bat) - 1):
        d1 = int(cur_bat[i])

        d2 = max(int(x) for x in cur_bat[i+1:])

        cand = d1 * 10 + d2

        if cand > num1 * 10 + num2:
            num1 = d1
            num2 = d2

    soma += num1 * 10 + num2

print(soma)