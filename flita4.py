import math

def stepen(graph, n):
    array = [0] * n
    for point in graph:
        array[int(point[0])-1]+=1
        array[int(point[1])-1]+=1
    return array

#сложность функции stepen - O(n)
#сложность функции shellSort - O(n log(n))

def shellSort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and (array[j - interval])[1] > temp[1]:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k -1
    return array

gr=[]
n = 0
with open("read.txt", 'r') as f:
    for vertices in f:
        point = vertices.strip().split()
        gr.append(point)
        n = max(n, int(point[0]))
        n = max(n, int(point[1]))

vershini = []
for i in range(n):
    versh = [i, stepen(gr, n)[i]]
    vershini.append(versh)

for point in reversed(shellSort(vershini)):
    print(str(point[0]+1) + " - " + str(point[1]))
