#in single variable we can store multiple elements
#mutable
"""
-8  -7  -6  -5  -4  -3  -2  -1
R   i   t   h   e   e   s   h
0   1   2   3   4   5   6   7
"""
lis = []
list1 = ["avinash","python","reddy",["raju","kiran"]]
         #   90        80       70
lis = "Ritheesh"
list2 = [1,2,3,4,5]
list3 = ['a','b','c','d']
list4 = [True,False,True]
print(list1)

#len
print(len(list4))

#slicing
print(list1[0])
print(list1[1:2])
print(list1[:2])
print(list1[1:])
print(lis[-1:-3])



list1[1] = "Ritheesh"
print(list1)
list2[3:2] = [10,11]
print(list2)
print(list1)

#append()

# uses to add elements in a list
list3.append('k')
print(list3)

#extend()
#concardinate two lists
res1 = ["bean","small","big"]
res2 = ["cup","bag"]

res2.extend(res1)
print(res2)


#insert(least priority)
ans = ["Ritheesh","reddy","Laptop"]
ans.insert(2,"window")



#remove()
ans.remove("reddy")
#list1.pop(1)

#type()
print(type(list1))

#clear()
ans.clear()
print(ans)
#del



li = ["washing","clean","floor"]
if "clean" in li:
    print("true")
