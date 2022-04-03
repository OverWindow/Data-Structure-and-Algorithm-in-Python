
#백준(4673번)
#set 자료구조는
#합집합("|"), 교집합("&"), 차집합("-")을 사용할 수 있다
#리스트는 안됨
#참고로 요소를 추가할려면 append가 아니라 add이다

All_number = set(range(1,10001))
Target_number = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    Target_number.add(i)

Self_number = sorted(All_number - Target_number)    #두 set함수의 차집합

for i in Self_number:
    print(i)