def solution(phone_book):
    phone_book.sort() # 리스트 정렬, 스트링 타입으로 정렬되기 때문에 앞 뒤 번호만 비교해주면 된다.
    for p1, p2 in zip(phone_book, phone_book[1:]): # zip을 이용해 (p1=앞, p2=뒤) 튜플로 이루어진 리스트 생성 
        if p2.startswith(p1): # p2가 p1으로 시작할 때,
            return False # return False, return이 쓰이면 함수 종료
    return True # False인 경우가 없었으면 return True