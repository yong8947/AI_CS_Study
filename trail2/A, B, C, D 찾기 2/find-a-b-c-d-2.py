nums = list(map(int, input().split()))
nums.sort()

def solve():
    for A in range(11):
        for B in range(A,11):
            for C in range(B,11):
                for D in range(C,11):
                    vals = [A,B,C,D] # 하나의 값과 네 게의 합 

                    for i in range(4): # 두 개의 합
                        for j in range(i+1,4):
                            sum_2 = vals[i] + vals[j]
                            vals.append(sum_2)

                    for i in range(4): # 세 개의 합
                        for j in range(i+1,4):
                            for k in range(j+1,4):
                                sum_3 = vals[i] + vals[j] + vals[k]
                                vals.append(sum_3)

                    vals.append(A+B+C+D)

                    vals.sort()
                        
                    if vals == nums:
                        print(A, B, C, D)
                        return

solve()