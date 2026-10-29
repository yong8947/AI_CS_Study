def solution(cards1, cards2, goal):
    for s in goal:
        if cards1 and s == cards1[0]:
            del cards1[0]
            
        elif cards2 and s == cards2[0]:
            del cards2[0]
        
        else:
            return 'No'
        
    return 'Yes' 