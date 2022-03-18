#백준 (1978번)
#소수(Prime Number), 색출이 키 포인트다
#생각보다 깔끔하게 풀어서 놀라 여기 집어둔다

N=int(input())
a=list(map(int,input().split()))
sum=0
for i in a:
    if i == 1:
        continue
    for j in range(2,i+1): #여기가 포인트 소수가 아닌 숫자는 아래 if 문을 통해 나가게 되고
        if i%j==0:          #소수가 아닌 숫자는 항상 그 숫자에 j가 도달하기 전에 if를 성립하고 i==j는 성립하지 않는다
            break
    if i==j:        #소수의 특징은  1과 자기 자신이므로 자기자신과 같을때만 +=1
        sum+=1
print(sum)