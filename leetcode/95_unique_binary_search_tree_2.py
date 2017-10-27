class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution(object):
    # no memorization
    def generate(self,n):
        if n == 0:
            return []
        def genBST(s,e):
            if s > e:
                return[None]
            if s == e:
                return [TreeNode(s)]
            ret = []
            for i in range(s,e+1):
                lefts = genBST(s,i-1)
                rights = genBST(i+1,e)
                for left in lefts:
                    for right in rights:
                        newRoot = TreeNode(i)
                        #print newRoot, newRoot.val
                        newRoot.left = left
                        newRoot.right = right
                        ret.append(newRoot)
            return ret
        return genBST(1,n)

s = Solution()

res = s.generate(3)

def inOrder(root, path):
    if root == None:
        path.append(None)
        return
    inOrder(root.left, path)
    path.append(root.val)
    inOrder(root.right, path)
    return path

for node in res:
    print inOrder(node,[])


