#Bi_Directional_Search
n=int(input("Enter the no of edges"))
d=dict()
for i in range(n):
    u=int(input())
    v=int(input())
    if(u not in d):
        d[u]=[v]
    else:
        d[u].append(v)
    if(v not in d):
        d[v]=[u]
    else:
        d[v].append(u)
print(d)

u=int(input("Enter the source node"))
v=int(input("Enter the goal node"))



def bfs(d,u,v):
    vis1=[u]
    vis2=[v]
    q1=[u]
    q2=[v]
    while(len(q1)>0 and len(q2)>0):
        x=q1.pop(0)
        y=q2.pop(0)
        if(x==y):
              return x
        if(x in vis2):
            return x
        if(y in vis1):
            return y
        for i in d[x]:
            print(i)
            if(i not in vis1):
                vis1.append(i)
                q1.append(i)
        for i in d[y]:
            print(i)
            if(i not in vis2):
                vis2.append(i)
                q2.append(i)
    return -1
t=bfs(d,u,v)
if(t==-1):
    print("There is no intersection point")
else:
    print("Intersection at",t)
