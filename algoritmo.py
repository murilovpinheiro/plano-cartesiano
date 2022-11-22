import math
from heapq import heapify, heappush, heappop

def FairnessOracle(orderedList):
    # exemplo de Fairness Oracle
    if orderedList[0][1] >= 2 and orderedList[1][1] >= 2 :
        return True
    return False

def Del(w1, w2, value):
    r = []
    for i in range(len(value)):
        temp = []
        temp.append(w1 * value[i][0] + w2 * value[i][1])
        temp.append(value[i][0])
        temp.append(value[i][1])
        r.append(temp)
    r.sort(reverse=True)
    return r

def Angle(T1, T2):
    return math.degrees(math.atan((T2[1] - T1[1])/(T1[2] - T2[2])))

def swap(value1, value2, list):
    position1, position2 = 0, 0
    for i in range(len(list)):
        if list[i] == value1:
            position1 = i
        if list[i] == value2:
            position2 = i
    temp = list[position1]
    list[position1] = list[position2]
    list[position2] = temp
    return (list, position1, position2)

def isNeighbour(values, value1, value2):
    pos1, pos2 = 0, 0
    for i in range(len(values)):
        if values[i] == value1: pos1 = i
        if values[i] == value2: pos2 = i
    if (pos1 - pos2) == 1 or (pos1 - pos2) == -1:
        return True
    return False

def checkVisited(values, visited):
    for i in range(len(visited)):
        if visited[i][0] == values[0] and visited[i][1] == values[1]:
            return True
        if visited[i][1] == values[0] and visited[i][0] == values[1]:
            return True
    return False


def findOrder(list):
    visited = []
    r = Del(1, 0, list)
    heap = []
    heapify(heap)
    for i in range(len(r) - 1):
        if r[i][2] >= r[i + 1][2]:
            continue
        heappush(heap, (Angle(r[i], r[i + 1]), r[i], r[i + 1]))
        visited.append([r[i][1:3], r[i + 1][1:3]])
    saida = 0
    i = 0
    angulos = []
    print("Ordenação Inicial: \n", r)
    while len(heap) != 0:
        if FairnessOracle(r):
            angulos.append((saida, 0))
            break
        saida, a, b = heappop(heap)
        if isNeighbour(r, a, b):
            r, pos1, pos2 = swap(a, b, r)
            if pos2 != len(r) - 1 and not(checkVisited([r[pos2][1:3], r[pos2 + 1][1:3]], visited)) and not(r[pos2][2] >= r[pos2 + 1][2]):
                heappush(heap, (Angle(r[pos2], r[pos2 + 1]), r[pos2], r[pos2 + 1]))
                visited.append([r[pos2][1:3], r[pos2 + 1][1:3]])
            if pos1 != 0 and not(checkVisited([r[pos1][1:3], r[pos1 - 1][1:3]], visited)) and not(r[pos2][2] >= r[pos2 + 1][2]):
                heappush(heap, (Angle(r[pos1 - 1], r[pos1]), r[pos1 - 1], r[pos1]))
                visited.append([r[pos1 - 1][1:3], r[pos1][1:3]])
    if len(heap) == 0:
        print("Não a área que Satisfaça a restrição desejada.")
        return
    flag = True
    while len(heap) != 0:
        saida, a, b = heappop(heap)
        if isNeighbour(r, a, b):
            r, pos1, pos2 = swap(a, b, r)
            if pos2 != len(r) - 1 and not(checkVisited([r[pos2][1:3], r[pos2 + 1][1:3]], visited)) and not(r[pos2][2] >= r[pos2 + 1][2]):
                heappush(heap, (Angle(r[pos2], r[pos2 + 1]), r[pos2], r[pos2 + 1]))
                visited.append([r[pos2][1:3], r[pos2 + 1][1:3]])
            if pos1 != 0 and not(checkVisited([r[pos1][1:3], r[pos1 - 1][1:3]], visited)) and not(r[pos2][2] >= r[pos2 + 1][2]):
                heappush(heap, (Angle(r[pos1 - 1], r[pos1]), r[pos1 - 1], r[pos1]))
                visited.append([r[pos1 - 1][1:3], r[pos1][1:3]])
            simbolo = FairnessOracle(r)
            if flag == True and simbolo == False:
                angulos.append((saida, 1))
            elif flag == False and simbolo == True:
                angulos.append((saida, 0))
            flag = simbolo
    if flag == True:
        angulos.append((90, 1))
    print(angulos)
    return

list = [[1, 1.2],  [2.6, 0.9], [2.1, 1.1], [1.1, 0.4], [0.6, 2.2]]
findOrder(list)

##Aparentemente tudo certo