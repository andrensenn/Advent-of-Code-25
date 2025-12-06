
matrix = []
f = open("Day4/in.txt", "r")
for line in f:
    cur_line = []
    for char in line :
        if char == "\n":
            break
        cur_line.append(char)
    matrix.append(cur_line)
f.close()

count = 0

for y in range(0,len(matrix)):
    for x in range(0,len(matrix[y])):
        if matrix[y][x] == '@':
            adj_count = 0
            if x - 1 >= 0:
                if matrix[y][x-1] == '@':
                    adj_count += 1
                if y-1 >= 0 and matrix[y-1][x-1] == '@':
                    adj_count += 1
                if y+1 < len(matrix) and matrix[y+1][x-1] == '@':
                    adj_count += 1
            if x + 1 < len(matrix[y]):
                if matrix[y][x+1] == '@':
                    adj_count += 1
                if y-1 >= 0 and matrix[y-1][x+1] == '@':
                    adj_count += 1
                if y+1 < len(matrix) and matrix[y+1][x+1] == '@':
                    adj_count += 1
            if y-1 >= 0 and matrix[y-1][x] == '@':
                    adj_count += 1
            if y+1 < len(matrix) and matrix[y+1][x] == '@':
                    adj_count += 1

            if adj_count < 4 :
                 print(y,x, adj_count)
                 count +=1
                 #y-1,x-1   y-1,x   y-1,x+1
                 #y  ,x-1    self   y  ,x+1   
                 #y+1,x-1   y+1,x   y+1,x+1    
print(count)