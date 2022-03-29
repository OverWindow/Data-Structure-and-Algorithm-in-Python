#백준(2447번)
#분할 정복과 재귀
#맵을 먼저 그리고 난후
#기초 모양을 그리고
#9개로 나누어 그린다
N=int(input())
Map = [[0 for i in range(N)]for i in range(N)]          #먼저 그림판을 그린다
a = 1

def star(n):
    global Map
    global a
    a *=3
    if a==n:
        return
    
    for i in range(3):
        for j in range(3):                      #i와 j를 사용하여 9번 반복할 수 있게 각 위치에 좌표(i,j)를 찍은 셈이다
            if i == 1 and j == 1:               #: (0,0)(0,1)(0,2)
                pass                            #  (1,0)(1,1)(1,2)
            else:                               #  (2,0)(2,1)(2,2)
                for k in range(a):
                    Map[a*i+k][a*j:a*(j+1)] = Map[k][:a]            #a는 기존 모양의 규격 k는 기존모양 하나하나 따라가는 셈
    star(n)

    
if N == 3:
    Map[0][:3]=[1]*3
    Map[1][:3]=[1,0,1]
    Map[2][:3]=[1]*3
else:
    Map[0][:3]=[1]*3
    Map[1][:3]=[1,0,1]
    Map[2][:3]=[1]*3
    star(N)
    
for i in Map:                               #Map에 1과0으로만 되어있는 2차원 배열을
    for j in i:                             #"*" 과 " "으로 변환시켜주는 역할
        if j == 1:
            print("*",end='')
        else:
            print(" ",end='')
    print()

print()
