def extendList(item, list=[]):
    list.append(item)
    return list

list1 = extendList(11)      
list2 = extendList(156,[])  
list3 = extendList('c')      

print(list1) 
print(list2)
print(list3)