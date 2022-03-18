#BinarySearch 정석
#start 와 end를 만들고 중간값 mid를 만들어 mid를 target과 비교하여
#찾는 방법: 특징은 한칸씩 줄어든다.

#백준(1920번)
#N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
import sys
int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))
numbers.sort()
for target in find:
    start, end, result = 0, len(numbers)-1, False
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] == target:
            result = True
            break
        elif numbers[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    print(1 if result else 0)   #이런 방법은 처음 알았다 유용해 보이니 나중에 써보도록 한다