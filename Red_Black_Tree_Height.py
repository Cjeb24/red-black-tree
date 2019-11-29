import math

def height(n):
    if not n:
        return 0

    h1 = height(n.left)
    h2 = height(n.right)
    return 1 + max(h1, h2)
