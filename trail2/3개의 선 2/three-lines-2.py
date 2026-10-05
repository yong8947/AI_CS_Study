n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

def solution():
    for i in range(11):
        for j in range(11):
            for k in range(11):
            
                success = True
            
                # x축 직선 하나로 다 지나갈 수 있는 경우
                for x,y in points:
                    if x == i or x == j or x == k:
                        continue

                    success = False
                    break

                if success:
                    print(1)
                    return

                # x:2 y:1

                success = True

                for x,y in points:
                    if x == i or x == j or y == k:
                        continue

                    success = False
                    break

                if success:
                    print(1)
                    return

                # x:1 y:2

                success = True

                for x,y in points:
                    if x == i or y == j or y == k:
                        continue

                    success = False
                    break

                if success:
                    print(1)
                    return

                # y:3

                success = True

                for x,y in points:
                    if y == i or y == j or y == k:
                        continue

                    success = False
                    break

                if success:
                    print(1)
                    return

    print(0)

solution()