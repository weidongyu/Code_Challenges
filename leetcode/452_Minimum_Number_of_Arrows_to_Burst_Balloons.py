def minArrows(ballons):
    def getKey(item):
        return item[0]

    sBallons = sorted(ballons, key=getKey)

    if sBallons == []:
        return 0

    if len(sBallons) == 1:
        return 1

    arrowS = sBallons[0][0]
    arrowE = sBallons[0][1]
    counter = 1
    for b in sBallons[1:]:
        if b[0] > arrowE:
            counter += 1
            arrowS = b[0]
            arrowE = b[1]
        elif b[0] <= arrowE:
            arrowS = b[0]
            arrowE = min(arrowE, b[1])

    return counter


# 1

ballons = [[10, 16], [2, 8], [1, 6], [7, 12]]

print minArrows(ballons)

# 2

ballons = [[10, 16], [2, 8], [1, 1], [7, 12]]

print minArrows(ballons)

# 3

ballons = [[10, 16], [16, 16]]

print minArrows(ballons)