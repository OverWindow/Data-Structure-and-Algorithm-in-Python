#백준 (11720번)
#N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오

N = input()
print(sum(map(int,input())))   #sum 함수로 감싸면 모두다 더해준다

#다만 sum 함수 안에는 리스트나 튜플과 같은 형태여야 하며 정수 혹은 실수만 요소로
#가지고 있어야한다