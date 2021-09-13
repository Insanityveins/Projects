
sortList = [9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in range(0, len(sortList)):
    least = sortList[i]

    for j in range(i, len(sortList)):
        if sortList[j] < least:
            least = sortList[j]
            leastPosition = j

    temp = least
    sortList[j] = sortList[i]
    sortList[i] = least

print(sortList)


