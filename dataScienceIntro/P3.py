
def P3(world: list) -> int:
    
    remain = set() # set of all coordinates(tuple) of 1 that isn't visited
    for r in range(len(world)):
        for c in range(len(world[0])):
            if world[r][c]:
                remain.add((r, c))

    
    def DFS(v: tuple):
        remain.remove(v)

        r, c = v
        if (r - 1, c) in remain:
            DFS((r - 1, c))
        if (r + 1, c) in remain:
            DFS((r + 1, c))
        if (r, c - 1) in remain:
            DFS((r, c - 1))
        if (r, c + 1) in remain:
            DFS((r, c + 1))


    count = 0
    while True:
        if not remain:
            break

        # https://stackoverflow.com/questions/59825/how-to-retrieve-an-element-from-a-set-without-removing-it
        v = None
        for w in remain:
            v = w
            break
        
        DFS(v)
        count += 1

    return count
    

# print(P3([[1,1,1,1,0], [1,0,0,1,0], [1,1,0,1,0], [1,1,0,0,0]]))
# print(P3([[1,1,0,0,0], [1,1,0,0,0], [0,0,1,1,0], [0,0,0,0,1]]))
# print(P3([[0,1,0,1,0,1]]))