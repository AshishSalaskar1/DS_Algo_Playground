# def solve(s1: str, s2: str, s3: str) -> bool:
#     return False


# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbbaccc"


class UF:
    def __init__(self, n) -> None:
        self.par = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    
    def find_parent(self, node: int) -> int:
        if self.par[node] == node:
            return node
        
        self.par[node] = self.find_parent(self.par[node])
        return self.par[node]

    def union(self, u:int, v: int) -> None:
        upar, vpar = self.find_parent(u), self.find_parent(v)
        if upar == vpar:
            return 

        if self.size[vpar] < self.size[upar]: # add upar in vpar
            self.par[upar] = vpar
            self.size[vpar] += self.size[upar]
        else: # add vpar into upar
            self.par[vpar] = upar
            self.size[upar] += self.size[vpar]

def solve(xr: int, yr: int, circles: list[list[int]]) -> bool:
    # TODO: Filter out circles with centres outside the rectange

    bounds = {
        "left": 0,
        "right": 1,
        "top": 2,
        "bottom": 3
    }

    n = len(circles)
    uf = UF(n+4)

    for i, circle in enumerate(circles):
        x, y, r = circle[0], circle[1], circle[2]
        if x-r <= 0:
            print(f"{x} {y} {r} conneted to left")
            uf.union(i, n+bounds["left"])
        if y-r <= 0:
            print(f"{x} {y} {r} conneted to bottom")
            uf.union(i, n+bounds["bottom"])
        if x+r >= xr:
            print(f"{x} {y} {r} conneted to right")
            uf.union(i, n+bounds["right"])
        if y+r >= yr:
            print(f"{x} {y} {r} conneted to top")
            uf.union(i, n+bounds["top"])
        
        print("PARENTS")
        for I in range(n+4):
            print(I,"=>", uf.find_parent(I))
        print("PARENTS END\n")
        
        for j in range(i):
            x2,y2,r2 = circles[j][0], circles[j][1], circles[j][2]
            print(f"Circles {i} and {j} intersect?")
            if (x-x2)**2 + (y-y2)**2 <= (r+r2)**2: # they coincide
                print("YES")
                uf.union(i,j)
    
    if uf.find_parent(n+bounds["left"]) == uf.find_parent(n+bounds["right"]) \
        or uf.find_parent(n+bounds["top"]) == uf.find_parent(n+bounds["bottom"]) \
        or uf.find_parent(n+bounds["left"]) == uf.find_parent(n+bounds["bottom"]) \
        or uf.find_parent(n+bounds["top"]) == uf.find_parent(n+bounds["right"]):
        return False

    print(uf.find_parent(n+bounds["left"]) == uf.find_parent(n+bounds["right"]))
    print(uf.find_parent(n+bounds["top"]) == uf.find_parent(n+bounds["bottom"]))
    print(uf.find_parent(n+bounds["left"]) == uf.find_parent(n+bounds["bottom"]))
    print(uf.find_parent(n+bounds["top"]) == uf.find_parent(n+bounds["right"]))

    for i in range(n+4):
        print(i,"=>", uf.find_parent(i))

    return True





X = 3
Y = 3
circles = [[2,1,1],[1,2,1]]
print("RES")
print(solve(X, Y, circles)) # FALSE



# X = 5
# Y = 7
# circles = [[2,1,7],[4,5,2],[4,6,7]]
# print("RES")
# print(solve(X, Y, circles)) # FALSE

# X = 8
# Y = 9
# circles = [[3,1,1],[1,5,1],[4,8,2]]
# print("RES")
# print(solve(X, Y, circles)) # TRUE