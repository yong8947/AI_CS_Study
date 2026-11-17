import re

def solution(new_id):
    # 1step
    ans = new_id.lower()
    # 2step
    ans = re.sub(r'[^a-z0-9\-_.]','',ans)
    # 3step
    ans = re.sub(r'\.+','.',ans)
    # 4step
    ans = ans.strip('.')
    # 5step
    if ans == '':
        ans = 'a'
    # 6step
    if len(ans) > 15:
        ans = ans[:15].strip('.')
    # 7step
    while len(ans) < 3:
        ans += ans[-1]
        
    return ans