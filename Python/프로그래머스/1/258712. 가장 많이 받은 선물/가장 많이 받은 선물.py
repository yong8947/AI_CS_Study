def solution(friends, gifts):
    dic_present = dict()
    n = len(friends)
    
    for friend in friends:
        dic_present[friend] = [0] * n
        
    for gift in gifts: # dic[준사람] = 받은사람
        g,h = gift.split()
        dic_present[g][friends.index(h)] += 1
    
    rate_gift = {} # 선물지수
    for i in range(n):
        a = sum(dic_present[friends[i]])
        b = sum(dic_present[f][i] for f in friends)
        rate_gift[friends[i]] = a-b
        
    get_gift = {f:0 for f in friends}
    
    for i in range(n):
        for j in range(i+1,n):
            a, b = friends[i], friends[j]
            ab = dic_present[a][j]
            ba = dic_present[b][i]
            
            if ab > ba:
                get_gift[a] += 1
            elif ba > ab:
                get_gift[b] += 1
            else:
                if rate_gift[a] > rate_gift[b]:
                    get_gift[a] += 1
                elif rate_gift[b] > rate_gift[a]:
                    get_gift[b] += 1
                    
    return max(get_gift.values())