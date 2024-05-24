with open('inputs.in', 'r') as file:
    line = file.readlines()

N = int(line[0])
arr = []
num = 1
for _ in range(N):
    newNN = line[num].split()
    if newNN[0] == 'insert':
        arr.insert(int(newNN[1]),int(newNN[2]))
    elif newNN[0] == 'print':
        print(arr)
    elif newNN[0] == 'remove':
        arr.remove(int(newNN[1]))
    elif newNN[0] == 'append':
        arr.append(int(newNN[1]))
    elif newNN[0] == 'sort':
        arr.sort()
    elif newNN[0] == 'pop':
        arr.pop()
    elif newNN[0] == 'reverse':
        arr.reverse()
    num += 1
