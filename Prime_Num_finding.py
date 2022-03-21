#백준 (1929번)
#소수를 True 소수가 아닌 수를 False라 두어 소수를 색출해냄
#에라토스테네스의 채
#2배수인 칸들은 False
#3배수인 칸들은 False
#계속해나가면 저절로 소수만 남는다

import sys
A,B = map(int,sys.stdin.readline().split())

B += 1
L=[True] * B            #이렇게 리스트가지수를 지정할 수있다
L[1]=False
for i in range(2,B):
    if L[i]:
        for j in range(2*i,B,i):
            L[j] = False

for i in range(A,B):
    if L[i] == True:
        print(i)
           