#class error(BaseException): pass를 이용해 raise error가 선언되면 에러가 나도록 함
#raise error를 통해 에러를 유발하면 에러가 났을때의 코드인 except error:로 가서 실행함
#raise error를 통해 에러가 유발하지 않으면 try: 코드를 실행함
#여기서 BaseException은 모든 에러를 다 통침
#고로 원래는 에러찾는 구문임



#백준 (2480번)
#1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다. 
#같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
#같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
#모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.  

class error(BaseException): pass

import sys

A,B,C = map(int, sys.stdin.readline().split())
L = [A,B,C]

try:
    for i in range(1,7):
        if L.count(i) == 3:
            print(10000 + i * 1000)
            raise error

    for i in range(1,7):
        if L.count(i) == 2:
            print(1000 + i * 100)
            raise error

    L.sort()
    print(L[2] * 100)
   

except error:
    pass