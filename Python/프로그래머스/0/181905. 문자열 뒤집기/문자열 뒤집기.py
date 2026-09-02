def solution(my_string, s, e):
  # return my_string[:s] + my_string[e:s-1:-1] + my_string[e+1:]  s=0 이면 오류발생
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]