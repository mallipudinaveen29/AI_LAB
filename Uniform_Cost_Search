from collections import deque as d
u=int(input("Enter the no of nodes"))
l=[[] for i in range(u+1)]

n=int(input("Enter the no of edges"))

for i in range(n):
    y=int(input())
    y1=int(input())
    cost=int(input())
    
    l[y].append([y1,cost])
print(l)
    
source=int(input("Enter the source node"))
goal=int(input("Enter the goal node"))
l1=[100000]*(u+1)


q=d()

q.append([source,0])

# print(l[1])
vis=[-1]*(u+1)
while(len(q)>0):
    r=q[0]
    q.popleft()

    y=l[r[0]]

    if(vis[r[0]]!=1):
        vis[r[0]]=1
        for i in y:
            l1[i[0]]=min(l1[i[0]],r[1]+i[1])
            q.append([i[0],l1[i[0]]])
    
    
print(l1)

print("MINIMUM COST TO REACH GOAL STATE IS  ",l1[goal])
    



    
    

