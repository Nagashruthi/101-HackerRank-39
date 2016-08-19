'''
This python file contains the solution to the question: Find the minimum number of elements to be deleted in the array so as to have the
same element in the resulting array
'''

a=input()
arr=[]
arr=[int(tmp) for tmp in input().strip().split(' ')]

d={}
for i in arr:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
        
mx=max(i for i in d.values())

res=int(a)-mx
print (res)
