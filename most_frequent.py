from collections import Counter
def counters(s):
    return Counter(s)
def manual(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1 
        else:
            d[i]+=1 
    D = {}
    for i in d:
        if d[i] in D:
            D[d[i]].append(i)
        else:
            D[d[i]] = [i]
    x = list(D.keys())
    x.sort(reverse=True)
    for i in x:
        if len(D[i])==1:
            print(D[i][0],":",i,end=" ")
        else:
            for j in D[i]:
                print(j,":",i,end=" ")  
    
s = input("Please enter a string ")
x = Counter(s)
print(x)
manual(s)
