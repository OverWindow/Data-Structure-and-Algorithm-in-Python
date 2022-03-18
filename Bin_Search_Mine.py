#(극단적)이진탐색
#Binary Search
#리스트 양 쪽 끝값을 설정하고 가운데 값을 산출하여 찾으려는 값과 대조하여
#만약 가운데 값보다 찾으려는 값이 크면 시작 값을 가운데 값으로 설정하여
#계속 돌려 찾으려는 값을 찾는 방법이다
#(이게 이진탐색인줄 알고 했다가 아니었지만 더 빠르다)

#백준 (1920번)
#N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

import sys

N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))


for i in B:
    start = 0
    end = len(A) - 1
    ofn = 0

    while ofn == 0:
        mid = int((start + end)//2)
        if end - start == 1:
            if A[end] == i:
                print(1)
                ofn = 1
            elif A[start]!=i and A[end]!=i:
                print(0)
                ofn =1
            
        if A[mid] > i:
            end = mid
        elif A[mid] < i:
            start = mid
        elif A[mid] == i:
            print(1)
            ofn = 1
        
        
            