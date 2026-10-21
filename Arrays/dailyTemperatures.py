t=[73,74,75,71,69,72,76,73]
def dailyTemperatures(t):
    ans=[0]*len(t)
    stack=[]
    i=0
    while i!=len(t):
        while stack and t[i]>t[stack[-1]]:
            org=stack.pop()
            ans[org]=i-org
        stack.append(i)
        i+=1
    while stack:
        ans[stack.pop()]=0
    return ans
print(dailyTemperatures(t))
print([0]*len(t))