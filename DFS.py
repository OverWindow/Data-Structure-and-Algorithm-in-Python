#DFS(깊이 우선 서치)
#Depth First Search
#여러 갈래의 초이스가 있을때
#한 갈래 다 끝내고 다음 갈래로 가면서 서치하는 방법


#백준(2606번)
#입력 값:
#7
#6
#1 2
#2 3
#1 5
#5 2
#5 6
#4 7
#visted[] 앞 첫칸은 안쓰는 칸
#graph[]도 마찬가지

n = int(input())
m = int(input())
graph = [[]*n for _ in range(n+1)]

print(graph)                        # [[], [], [], [], [], [], [], []]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
print(graph)                        # [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
    
cnt = 0
visited = [0]*(n+1)                 #[0,0,0,0,0,0,0,0]

print(graph[1])                     # [2, 5]

def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            cnt +=1
 
dfs(1)
print(cnt)                          # 4
