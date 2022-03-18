#유클리드 호제법(알고리즘)
#1071과 1029의 최대공약수를 구하면,
#1071은 1029로 나누어 떨어지지 않기 때문에, 1071을 1029로 나눈 나머지를 구한다. ≫ 42
#1029는 42로 나누어 떨어지지 않기 때문에, 1029를 42로 나눈 나머지를 구한다. ≫ 21
#42는 21로 나누어 떨어진다.
#따라서, 최대공약수는 21이다.

#백준(1934번) 최소공배수 구하기
import sys 
T = int(sys.stdin.readline())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())

    AA = A
    BB = B
    
    R=1
    while R != 0:
        R = AA%BB
        AA = BB
        BB = R
        

    print((A*B)//AA)   #AA가 최대공약수임, 이용한식: A*B = 최대공약수 * 최소공배수
