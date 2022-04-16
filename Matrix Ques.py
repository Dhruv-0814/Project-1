'''

input : test_list = [[2, 4, 1], [8, 1, 2], 
                    [9, 1, 10], [4, 3, 2]], 
tar_list = [2, 3, 10, 7, 5, 4] 
Output : 8 Explanation : 8 + 9 + 1 + 1 + 1 = 20 
[ Elements in Matrix, not in list ] 
7 + 5 = 12 
[ Elements in list, not in Matrix ] 
Difference = 12 – 20 = 8.
'''

l= [[2, 4, 1], [8, 1, 2], [9, 1, 10], [4, 3, 2]]
l1 = [2, 3, 10, 7, 5, 4] 
o1=[]
for i in l:
    for g in i:
        if g not in l1:
            o1.append(g)
for i in l:
    for g in l1:
        if g in i:
            l1.remove(g)
print(f"Difference = {sum(o1)}-{sum(l1)} = {sum(o1)-sum(l1)}")


'''------------------------------BETTER METHOD------------------------------''' 
l= [[2, 4, 1], [8, 1, 2], [9, 1, 10], [4, 3, 2]]
l1 = [2, 3, 10, 7, 5, 4] 
x=0
for i in l:
    x+=sum(list(filter(lambda a :a not in l1,i)))
print(x)  
    
for i in l:
    list(map(lambda a :l1.remove(a) if (a in i) else None ,l1))
    
print(f"Difference = {x}-{sum(l1)} = {sum(o1)-sum(l1)}")
    

'''---------------------------------BETTER METHOD------------------------------'''   
from functools import reduce 
l= [[2, 4, 1], [8, 1, 2], [9, 1, 10], [4, 3, 2]]
l1 = [2, 3, 10, 7, 5, 4] 
x=sum(list(map(lambda i:sum(list(filter(lambda a :a not in l1,i))),l)))
l=reduce(lambda g,h:g+h,l,[])
y=sum(list(filter(lambda a : a not in l,l1)))
print(f"Difference = {x}-{y} = {x-y}")
    
