#백준(1406번)
#스택을 쓰지 않고 실행할씨 시간 초과가 걸리는 문제
#스택이란
#스택 1 과 스택 2를 만들어 커서가 중간에 있다고 생각하고
#커서가 왼쪽으로 가면 스택 2에 스택 1마지막 요소를 append로 옮기는 것이다
#마지막에는 스택 2를 리버스로 돌려 스택 1과 합하여
#문자열을 완성시킨다
#ps 커서가 문자를 추가하면 스택 1 마지막에 추가하고
#커서가 문자를 지우면 스택 1 마지막 문자를 지운다

import sys

st1 = list(sys.stdin.readline().strip())
st2 = []


for i in range(int(sys.stdin.readline())):
    B = list(map(str, sys.stdin.readline().split()))
    
    if B[0] == "P":
        st1.append(B[1])
    elif B[0] == "L":
        if st1:
            st2.append(st1.pop())
    elif B[0] == "D":
        if st2:
            st1.append(st2.pop())
    elif B[0] == "B":
        if st1:
            del st1[-1]
    
print(*(st1 + list(reversed(st2))), sep = '')