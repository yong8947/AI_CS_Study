def solution(wallpaper):
    coo_x, coo_y = set(), set()
    
    for x in range(len(wallpaper)):
        for y in range(len(wallpaper[0])):
            if wallpaper[x][y] == '#':
                coo_x.add(x)
                coo_y.add(y)
                
    a,b,c,d = min(coo_x), min(coo_y), max(coo_x)+1, max(coo_y)+1
    
    return [a,b,c,d]