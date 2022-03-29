#백준(10872번)
#팩토리얼 출력하는문제
#재귀함수가 포인트
#재귀함수란 함수 안에 그 함수를 호출해 무한 루프를 만드는 알고리즘이다
#다만 무한 루프가 되면 프로그램을 끝낼 수 없으니 return으로 끝어주는 경우를 만들어야한다

N=int(input())
Answer = 1

def func(i):
    global Answer
    if i==1 or i==0:
        return              #무한 루프를 빠져나오는 경우 return값은 아무것도 가지고 오지 않아 탈출
    Answer *= i
    i-=1
    func(i)                 #함수 안의 함수

func(N)
print(Answer)