with open('input.in', 'r') as file:
    line = file.readlines()
    
    

x = int(line[0].strip())
y = int(line[1].strip())
z = int(line[2].strip())
n = int(line[3].strip())

coord_list = [
    [i,j,k]
    for i in range(x+1)
    for j in range(y+1)
    for k in range(z+1)
    if i+j+k != n
]

#coord_list = [coord_list.append([i,j,k])]
#for i in range(x+1):
#    for j in range(y+1):
#        for k in range(y+1):
#            if i+j+k != n:
#                coord_list.append([i,j,k])

print(coord_list)
