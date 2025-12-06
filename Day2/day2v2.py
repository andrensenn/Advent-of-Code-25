number_ranges = []
total = 0
content = ""

with open("Day2\in.txt") as f:
    content = f.read()
f.close()

number_ranges = content.split(',')

while len(number_ranges) != 0:

    cur_range = number_ranges.pop(0)
    hiffen = cur_range.find("-")
    
    min_val = int(cur_range[:hiffen])
    max_val = int(cur_range[hiffen+1:])


    for i in range(min_val,max_val+1):
        cur_num = str(i)
        length = int(len(cur_num)/2)
        if (cur_num[:length]) == (cur_num[length:]):
            print(i)
            total += i
        else:
            for j in range(3,len(cur_num)+1):
                if len(cur_num)%j==0:
                    index = int(len(cur_num)/j)
                    part = cur_num[:index]
                    composed = ""
                    for l in range(0,j):
                        composed += part
                    if composed == cur_num:
                        print(i)
                        total += i

print(total)
