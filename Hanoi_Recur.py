#백준(11729번)
#하노이탑에서 원반의 이동을 기록하는 (최소이동)
#재귀함수가 중요
#하노이탑은 크게 3개의 순서가 있따
#1.A에 있는 n-1개의 원반들을 B로 옮긴다
#2.A의 가장 큰 원반을 C로 옮긴다
#3.B에 있는 n-1개의 원반들을 C로 옮긴다



N=int(input())

def hanoi(n,start,target,via):
    if n ==1:
        print(start,target)
        return                              #return을 하게 되면 바로 직전 함수로 돌아간다 빠져나오는 것이 아니라

    hanoi(n-1,start, via, target)           #1.A에 있는 n-1개의 원반들을 B로 옮긴다
    print(start,target)                     #2.A의 가장 큰 원반을 C로 옮긴다
    hanoi(n-1,via,target,start)             #3.B에 있는 n-1개의 원반들을 C로 옮긴다

print(2**N-1)                       #하노이탑 최단이동 횟수 공식
hanoi(N,1,3,2)
