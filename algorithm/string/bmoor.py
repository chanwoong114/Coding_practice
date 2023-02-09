t = 'This pattern matchng algorithm'

def bmoor(P, T):
    lenP = len(P)
    lenT = len(T)
    skip = [lenP]*128
    for i in range(lenP-1):
        skip[ord(P[i])] = lenP-1-i

    idxT = 0
    while idxT+lenP <= lenT:
        idxP = lenP-1
        while idxP>=0 and T[idxT + idxP] == P[idxP]:
            idxP -= 1
        if idxP == -1:
            return idxT
        # ascii = ord(T[idxT + idxP])
        # j = skip[ascii]
        idxT += skip[ord(T[idxT + idxP])]

    return -1

print(bmoor('pat', t))


