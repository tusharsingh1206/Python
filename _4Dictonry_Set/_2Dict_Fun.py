myDict={
   "key":"value",
   "name":"Tushar singh",
   "age":20,
   "marks":34.5,
   "is_adult":True,
   "subjects": ["c","c++","python"],#list
   "subject": ("c","c++","python")#Tuple
}
print(myDict.keys())#returns all keys
print(myDict.values())#returns all values
print(myDict.items())#returns all (key,val) pairs as tuples
print(myDict.get("name"))#returns the key according to value
print(myDict.update({"city":"Delhi","age":16}))#inserts the specifies items to the dictionary 
#Type casting of the dictionary in the list
print(list(myDict.keys()))
#length of the dictionary
print(len(myDict))
print(myDict)