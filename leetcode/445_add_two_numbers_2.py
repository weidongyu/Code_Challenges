# add two numbers 2, lc 445

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def constructList(array):
    nullHead = ListNode(-1)
    cur = nullHead
    for n in array:
        newNode = ListNode(n)
        cur.next = newNode
        cur = newNode
    return nullHead.next


def listToArray(l):
    n = []
    cur = l

    while cur != None:
        n.append(cur.val)
        cur = cur.next

    return n


def add2Array(n1, n2):
    l1 = len(n1)
    l2 = len(n2)
    n1 = [0] + n1
    for i in range(l1):
        if i < l2:
            n1[-(i + 1)] += n2[-(i + 1)]

        if n1[-(i + 1)] >= 10:
            n1[-(i + 2)] += 1
            n1[-(i + 1)] %= 10
    if n1[0] == 0:
        return n1[1:]
    else:
        return n1


def add2Nums(l1, l2):
    n1 = listToArray(l1)
    n2 = listToArray(l2)
    len1 = len(n1)
    len2 = len(n2)
    if len1 >= len2:
        res = add2Array(n1, n2)
    else:
        res = add2Array(n2, n1)

    return constructList(res)


l1 = constructList([7, 0, 5, 4])
l2 = constructList([4, 6])

print listToArray(add2Nums(l1, l2))

