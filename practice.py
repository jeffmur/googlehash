# Practice Problem Algorithm
# Usage: python3 practice.py
# Specify FILE to the name of .in file to be calculated
# Calculates Maximum slices of pizza in a given set (only single use of each category)
# Algorithm: Starts with the first value (arr[0]) 
#            iteratively adds max -> that are <= target


FILE = "e_also_big"

f = open(FILE+".in", "r")

first_line = str.split(f.readline())
second_line = str.split(f.readline())

k = int(first_line[1])
target = int(first_line[0])
arr = [int(i) for i in second_line]
print("Start",arr)

def checkPossiblity(val, arr):
    arr.reverse()
    adj = [val]
    # compare to reverse array
    for i in arr:
        print(sum(adj))
        if( ( i == val ) | ( sum(adj) == target )): return adj
        s = sum(adj) + i # sum of adj
        if(s <= target):
            adj.append(i)

    return adj

def getIndexArr(adj):
    arr.reverse() # flip back for index calc
    adj.sort()
    #print(adj)
    result = []
    for v in adj:
        i = arr.index(v)
        result.append(i)
        arr[i] = -1

    result.sort() # ascending order
    return result
        
best_case = checkPossiblity(arr[0], arr)
result = getIndexArr(best_case)
string = " ".join(str(item) for item in result)
# print(string)
# print(len(result)) 
# Write To File
n = open(FILE+".out", "w+")
n.write(str(len(result))+"\n")
n.write(string)