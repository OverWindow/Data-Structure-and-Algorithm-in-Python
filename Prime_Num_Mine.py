#백준(1978번)
#처음으로 만든 소수 추출기다 매우 지저분하므로 권하지 않고 
#Prime_Num_Perfect.py를 참조하라
#웬만해선 리스트를 쓰지 말것

import sys

T = int(sys.stdin.readline())
L = []
M = []
how_many = 0
j = 1

L = list(map(int,sys.stdin.readline().split()))


for i in range(T):
    j = 1
    M = []
    while j <= L[0]:
        if j == L[0]:
            M.append(j)
            j +=1
            #print(M)
        elif L[0] % j == 0:
            M.append(j)
            j+= 1
        else:
            j += 1
    if len(M) == 2:
        how_many += 1
    del L[0]

print(how_many)
