#write here a code for task 
with open ("land.txt", "r") as lines:
    counter = 0
    map = []

    for line in lines:
        row = line.split()
        for column in range(len(row)):
            row[column] = int(row[column])
        map.append(row)
        counter += len(row)

    #printing map
    print(map)

    #printing task 1
    print('T1:')
    print('Number of units:  ' + str(counter))

    #task 2
    element = map[14][8]
    print('T2:')
    print('element is ' + str(element))
    
    #task 3
    strings = [2, 5, 8, 11]
    sum = 0
    for rowindex in strings:
        for column in map[rowindex]:
            sum += column
    print('T3:')
    print('sum is ' + str(sum))

    #Task 4
    sum = 0
    for row in map:
        for column in row:
            sum += column
    print('T4:')
    print('sum is ' + str(sum))

    #Task 5
    sum = 0
    max = 0
    for row in map:
        for column in row:
            if max < column:
                max = column
        sum += max
        max = 0
    print('T5:')
    print('sum of max is ' + str(sum))



