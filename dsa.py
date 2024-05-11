def isvalid(s1, s2):
    """
    Return is s1 is PREDECESSOR of s2
    -> s2 can be created by inserting exactly one more char in s1

    "ab","axx" = False
    "ab","abx" = True
    """
    n1,n2 = len(s1), len(s2)

    if n1 != n2-1:
        return False

    p1,p2 = 0,0

    while p2<n2:
        if p1 < n1 and s1[p1] == s2[p2]:
            p1 += 1
            p2 += 1
        else:
            p2   += 1

    
    return p1==n1 and p2==n2


print(isvalid("ab","axx"))
                