def solution(order):
    Total = 0
    for menu in order:
        if "cafelatte" in menu:
            Total += 5000
        else: Total += 4500
    return Total

"""

if 'americano' or 'anything' in menu: 구문은 파이썬에서 다음과 같이 평가됩니다. 'americano'는 비어있지 않은 문자열이므로 항상 참(True) 입니다. 파이썬의 or 연산자는 앞의 조건이 참이면 뒤의 조건('anything' in menu)을 확인하지 않고 전체 조건을 True로 결론지어 버립니다. 결과적으로 menu에 어떤 값이 들어오든 조건식이 항상 True가 되어, 매번 Total += 4500만 실행된 것입니다.


파이썬은 괄호 안의 표현식 ('americano' or 'anything')을 먼저 계산합니다. 'americano'는 비어있지 않은 문자열이라 참(True) 으로 평가됩니다.
or 연산자는 앞의 값이 참이면 뒤의 'anything'은 보지도 않고 앞의 값 자체 ('americano') 를 반환합니다. 따라서 ('americano' or 'anything') in menu 식은 'americano' in menu 와 완전히 동일한 식으로 바뀌게 됩니다.
결과적으로 'anything'이나 'cafelatte'가 들어왔을 때 'americano'가 포함되어 있지 않으므로 else 조건으로 넘어가 5000원이 더해진 것입니다.

"""