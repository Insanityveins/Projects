from random import randint


def bubbleSort(list):
    done = False
    while done == False:
        done = True
        for x in range(0, len(list)-1):
            if list[x] > list[x + 1]:
                list[x], list[x+1] = list[x+1], list[x]
                done = False
    print(list)
    return



def randomList():
    list = []
    for x in range(20):
        list.append(randint(0, 100))
    print(list)
    return list


def main():
    list = randomList()
    bubbleSort(list)





if __name__ == '__main__':
    main()