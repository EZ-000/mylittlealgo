def check(result):
    for x, y, stuff in result:
        if stuff == 0:  # 기둥인 경우
            if y == 0 or [x-1, y, 1] in result or [x, y, 1] in result or [x, y-1, 0] in result:
                continue
            return False
        elif stuff == 1:  # 보인 경우
            if [x, y-1, 0] in result or [x+1, y-1, 0] in result or ([x-1, y, 1] in result and [x+1, y, 1] in result):
                continue
            return False
    return True

def solution(n, build_frame):
    result = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:  # 삭제하는 경우
            result.remove([x, y, stuff])
            if not check(result):
                result.append([x, y, stuff])
        else:  # 설치하는 경우
            result.append([x, y, stuff])
            if not check(result):
                result.remove([x, y, stuff])
    return sorted(result)
