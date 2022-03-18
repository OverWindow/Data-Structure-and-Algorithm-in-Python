#백준 (10867번)
#N개의 정수가 주어진다. 이때, N개의 정수를 오름차순으로 정렬하는 프로그램을 작성하시오. 같은 정수는 한 번만 출력한다

#Set 는 집합과 유사
#저절로 중복 없애줌
#print 했을때 나오는 순서가 정해져있지 않다
#set 선언할때는 직접 set()해줘야한다


import sys 
n=int(sys.stdin.readline()) 
li=list(map(int,sys.stdin.readline().split()))
Sort=sorted(list(set(li))) 
print(*Sort)