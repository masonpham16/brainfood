with open('inputs.in', 'r') as file:
    line = file.readlines()


n = int(line[0].strip())
arr = list(map(int, line[1].strip().split()))
sarr = set(arr)
sorted_list = sorted(sarr)
print(sorted_list[-2])


