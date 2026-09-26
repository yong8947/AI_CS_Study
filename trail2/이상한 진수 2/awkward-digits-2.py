a = input()

# Please write your code here.
ans = 0
for i in range(len(a)):
    if a[i] == '1':
        test = a[:i]+'0'+a[i+1:] 
    else:
        test = a[:i]+'1'+a[i+1:] 

    ans = max(ans, int(test,2)) #2진수를 10진수로 바꾸는 함수 int(str,2)

print(ans)