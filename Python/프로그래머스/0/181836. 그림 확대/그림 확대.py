def solution(picture, k):
    picture_nx = []
    for pixel in picture:
        s = ''
        for pic in pixel:
            s += pic*k
        for _ in range(k):
            picture_nx.append(s)
    return picture_nx