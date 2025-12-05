fresh_ingred = []
avaib_ingred = []

fresh = True
f = open("Day5\in.txt", "r")
for line in f:
    if line == "\n":
        fresh = False 
        continue
    if fresh:
        fresh_ingred.append(line)
    else:
        avaib_ingred.append(line)
f.close()
fresh_ids = set()
count = 0

while len(fresh_ingred) != 0:
    cur_range = fresh_ingred.pop(0)
    hiffen = cur_range.find("-")
    min_val = int(cur_range[:hiffen])
    max_val = int(cur_range[hiffen+1:])

    cur_tupple = (min_val,max_val)
    fresh_ids.add(cur_tupple)

while len(avaib_ingred) != 0:
    cur_ingred = int(avaib_ingred.pop(0))

    for tup in fresh_ids:
        if cur_ingred >= tup[0] and cur_ingred <= tup[1]: 
            count +=1
            break

print(count)