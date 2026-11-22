def solution(arr1, arr2):
    ans = []
    for i in range(len(arr1)):
        ad = []
        for j,k in zip(arr1[i],arr2[i]):
            ad.append(j+k)
        ans.append(ad)
            
    return ans