#These all method return none and change the original list
list=[2,1,3]
list2=["apple","banana","mango","lichi"]
#list.append(x):Adds one element at the end
list.append(4)
print(list)
#list.sort():sort the list in the ascending order
list.sort()
print(list)
#list.sort(reverse=True):sort the list in the descending order
list.sort(reverse=True)
print(list)

list2.sort()
print(list2)
#list.reverse():Reverse the list
list.reverse()
print(list)
#list.insert(idx,el):Insert the element at the inedx:idx=at which index and el=which value
list.insert(2,10)
print(list)
#list.remove(x):Remove the first occurance of the x
list.remove(3)
print(list)

list2.remove("apple")
print(list2)
#list.pop(idx):Remove the element at the idx
list.pop(2)
print(list)

list2.pop(2)
print(list2)




