def dfs(d,limit,node,goal):
    print(node,"node")
    if(node==goal and limit>0):
        return 1
    if(limit<=0):
        return 0
    if(node not in d):
        return 0
    for i in d[node]:
        print(i)
        if(dfs(d,limit-1,i,goal)==1):
            return 1

        
        
n=int(input("Enter the no of edges"))
d=dict()
for i in range(n):
    u=int(input())
    v=int(input())
    if(u not in d):
        d[u]=[v]
    else:
        d[u].append(v)
print(d)

u=int(input("Enter the source node"))
v=int(input("Enter the goal node"))
limit=int(input("Enter limit"))





            
    


if(dfs(d,limit,u,v)==1):
    print("Goal is found")
else:
    print("Goal is not found")


            






