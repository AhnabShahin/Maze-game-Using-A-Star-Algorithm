import math


def take_input():
    # It will take your goal in put. If your goal is (5,6) then here x will 5 and y will 6.
    x = int(input('X of Goal  : '))
    y = int(input('Y of Goal  : '))
    return x, y


def block():
    # Here total_blocks means how many obstacle you want to put in your matrix
    total_blocks = int(input('How many block u want to put : '))

    # This blocks list will store all the obstacle.
    blocks = []

    # This loop will take x and y coordinate for every obstacle.
    for i in range(0, total_blocks):
        blocks.append(int(input('X for block ' + str(i + 1) + ' : ')))
        blocks.append(int(input('y for block ' + str(i + 1) + ' : ')))

    # After that it will return all the obstacles in and list, called blocks.
    return blocks


def matrix(t1, t2):
    # here t1 is the x axis of Goal, which is stored on a variable named x.
    x = t1

    # here t2 is the y axis of Goal, which is stored on a variable named y.
    y = t2

    # Declare a list for store value of g, h and f called g_h_f.
    g_h_f = [0, 0, 0]

    # This y_array will be use to create column.
    y_array = []

    # This matrix list will be use to create full maze.
    matrix = []

    for i in range(0, y + 2):
        y_array.append(g_h_f)  # creating column using loop
    for j in range(0, x + 2):
        matrix.append(y_array)  # creating Maze using y_array
    return matrix, x, y


# This g_h_f_for function will be used to find g, h and f for any position from start to goal
def g_h_f_for(m1, x1, y1, from_x, from_y, to_x, to_y, blk, s):
    blks = blk
    sum = s
    blk_len = len(blk)  # using len() function to take the length of blk (which means obstacle)
    start_x = from_x  # x axis value of start.
    start_y = from_y  # y axis value of start.
    to_x1 = to_x  # x axis value of current or calculating node.
    to_y1 = to_y  # y axis value of current or calculating node.
    m, x, y = m1, x1, y1
    if blk_len > 0:  # checking any block or obstacle is given by user or not.
        for b in range(0, blk_len, 2):  # This loop will run number of obstacles times.
            # Let blk_len is 4 that means there is 2 obstacle and this loop will run 2 times.

            if to_x1 == blk[b] and to_y1 == blk[
                b + 1]:  # checking - the position which i am going to calculate is a obstacle or not
                # print(to_x1,blk[b],to_y1,blk[b+1])
                s = ((start_x - to_x1) ** 2) + ((start_y - to_y1) ** 2)
                m[to_x1][to_y1][0] = 10000
                m[to_x1][to_y1][1] = 10000
                m[to_x1][to_y1][2] = m[to_x1][to_y1][0] + m[to_x1][to_y1][1]
            else:  # if It is not a obstacle then
                s = ((start_x - to_x1) ** 2) + ((start_y - to_y1) ** 2)
                m[to_x1][to_y1][0] = round(math.sqrt(int(s)) + sum, 2)  # calculate g
                m[to_x1][to_y1][1] = abs(to_x1 - x) + abs(to_y1 - y)  # calculate h
                m[to_x1][to_y1][2] = m[to_x1][to_y1][0] + m[to_x1][to_y1][1]  # calculate f
    else:
        s = ((start_x - to_x1) ** 2) + ((start_y - to_y1) ** 2)
        m[to_x1][to_y1][0] = round(math.sqrt(int(s)) + sum, 2)  # calculate g
        m[to_x1][to_y1][1] = abs(to_x1 - x) + abs(to_y1 - y)  # calculate h
        m[to_x1][to_y1][2] = m[to_x1][to_y1][0] + m[to_x1][to_y1][1]  # calculate f
    return m[to_x1][to_y1]  # return the position with g_h_f


def a_b_c(a, b, c, inx, iny, blk):
    step = max(inx, iny)
    v1, v2, v3 = a, b, c
    index = 0
    from_x = 1  # x of start node
    from_y = 1  # y of start node
    blocks = blk
    sum = 0.0

    for l in range(1, step):

        if index == 0:  # in the first time start node and calculation node are same
            from_x = 1
            from_y = 1
            print('from (x,y) ' + '=' + ' (' + str(from_x) + ',' + str(from_y) + ')')

        if index == 1:  # move to neighbour 1
            from_x = from_x - 1
            from_y = from_y + 1
            print('from (x,y) ' + '=' + ' (' + str(from_x) + ',' + str(from_y) + ')')

        if index == 2:  # move to neighbour 2
            from_x = from_x
            from_y = from_y + 1
            print('from (x,y) ' + '=' + ' (' + str(from_x) + ',' + str(from_y) + ')')

        if index == 3:  # move to neighbour 3
            from_x = from_x + 1
            from_y = from_y + 1
            print('from (x,y) ' + '=' + ' (' + str(from_x) + ',' + str(from_y) + ')')

        if index == 4:  # move to neighbour 4
            from_x = from_x + 1
            from_y = from_y
            print('from (x,y) ' + '=' + ' (' + str(from_x) + ',' + str(from_y) + ')')

        if index == 5:  # move to neighbour 5
            from_x = from_x + 1
            from_y = from_y - 1
            print('from (x,y) ' + '=' + ' (' + str(from_x) + ',' + str(from_y) + ')')

        if index == 6:  # move to neighbour 6
            from_x = from_x
            from_y = from_y - 1
            print('from (x,y) ' + '=' + ' (' + str(from_x) + ',' + str(from_y) + ')')

        if index == 7:  # move to neighbour 7
            from_x = from_x - 1
            from_y = from_y - 1
            print('from (x,y) ' + '=' + ' (' + str(from_x) + ',' + str(from_y) + ')')

        if index == 8:  # move to neighbour 8
            from_x = from_x - 1
            from_y = from_y
            print('from (x,y) ' + '=' + ' (' + str(from_x) + ',' + str(from_y) + ')')

        array = []
        tripples = [(v1, v2, v3, from_x, from_y, (from_x - 1), (from_y + 1), blocks, sum),  # neighbour 1
                    (v1, v2, v3, from_x, from_y, from_x, from_y + 1, blocks, sum),          # neighbour 2
                    (v1, v2, v3, from_x, from_y, (from_x + 1), (from_y + 1), blocks, sum),  # neighbour 3
                    (v1, v2, v3, from_x, from_y, from_x + 1, from_y, blocks, sum),          # neighbour 4
                    (v1, v2, v3, from_x, from_y, from_x + 1, from_y - 1, blocks, sum),      # neighbour 5
                    (v1, v2, v3, from_x, from_y, from_x, from_y - 1, blocks, sum),          # neighbour 6
                    (v1, v2, v3, from_x, from_y, from_x - 1, from_y - 1, blocks, sum),      # neighbour 7
                    (v1, v2, v3, from_x, from_y, from_x - 1, from_y, blocks, sum)]          # neighbour 8
        array.append('some')                                                                # put some thing in in 0 index to maintain indexing
        for tripple in tripples:
            array.append(str(g_h_f_for(*tripple)))                                          #calculating g,h and f and append in array

        all_f = []                                                                          # this array to store all f of every neighbour
        store_unpack = []
        for m in range(1, len(array)):
            unpack = (array[m].strip('[')).strip(']').split(', ')                           # to remove [ , ] from the get value
            # print(unpack)
            store_unpack.append(unpack)                                                     # after that store again all of this in new list store_unpack
            all_f.append(round((float(unpack[2])), 2))                                      # make the all f in 2 decimal point
        array.clear()
        sort_f = min(all_f)                                                                 # find the minimum f
        # print(min(all_f))
        all_f.clear()
        # print(all_f)
        # print(store_unpack)
        for m in range(0, len(store_unpack)):
            if sort_f == round(float(store_unpack[m][2]), 2):  # check the all nodes f with minimum f . If it is the neighbour with mimimum f then
                print('g = ' + str(store_unpack[m][0]))        # print g
                print('h = ' + str(store_unpack[m][1]))        # print h
                print('f = ' + str(store_unpack[m][2]))        # print f
                sum = round(float(store_unpack[m][0]), 2)      # and store the g
                # print('Total g = ' + str(sum))

                index = m + 1                                  # put the neighbor number for next iteration in the variable index
                # print(index)
                break

    print('End To (x,y) ' + '=' + ' (' + str(inx) + ',' + str(iny) + ')')        # After go to goal node print goal node


in1, in2 = take_input()                                 # call take_input() function to take goal
blocks = block()                                        # call block() function to take obstacle
value1, value2, value3 = matrix(in1, in2)               # call matrix() function to create maze

a_b_c(value1, value2, value3, in1, in2, blocks)         # main function to calculate g,h and f ,and transition
