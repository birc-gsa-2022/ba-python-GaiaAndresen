"""Module for computing border arrays."""


# def findBorder(ba, i, char, x):
#     if i==0:
#         ba.append(0)
#         return
#     baPrev = ba[i-1]
#     if x[baPrev] == char:
#         ba.append(baPrev+1)
#         return
#     findBorder(ba, baPrev, char, x)


def border_array(x: str) -> list[int]:
    """
    Construct the border array for x.

    >>> border_array("aaba")
    [0, 1, 0, 1]
    >>> border_array("ississippi")
    [0, 0, 0, 1, 2, 3, 4, 0, 0, 1]
    >>> border_array("")
    []
    """
    ba = []

    for i, char in enumerate(x):
        j = i 
        while True:
            if j == 0:
                ba.append(0)
                break
            baPrev = ba[j-1]
            if x[baPrev] == char:
                ba.append(baPrev+1)
                break
            j = baPrev 
    return ba


def strict_border_array(x: str) -> list[int]:
    """
    Construct the strict border array for x.

    A struct border array is one where the border cannot
    match on the next character. If b is the length of the
    longest border for x[:i+1], it means x[:b] == x[i-b:i+1],
    but for a strict border, it must be the longest border
    such that x[b] != x[i+1].

    >>> strict_border_array("aaba")
    [0, 1, 0, 1]
    >>> strict_border_array("aaaba")
    [0, 0, 2, 0, 1]
    >>> strict_border_array("ississippi")
    [0, 0, 0, 0, 0, 0, 4, 0, 0, 1]
    >>> strict_border_array("")
    []
    """
    
    ba = border_array(x)
    bax = []

    n = len(x)
    for i, bai in enumerate(ba):
        if bai == 0:
            bax.append(0)
        elif i+1 == n or x[i+1] != x[bai]:
            bax.append(bai)
        else:
            bax.append(bax[bai-1])        
    return bax


def reverse_border_array(x: str):
    return border_array(x[::-1])


