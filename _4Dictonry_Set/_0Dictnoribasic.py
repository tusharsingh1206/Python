#Dictionary:IT is used to store data values in Key:value pairs They are unordered
#mutable and don't allow to duplicate the keys
dict={
    #key:value,key contains all type of data int,float,string,list,tuple etc.
   "key":"value",
   "name":"Tushar singh",
   "age":20,
   "marks":34.5,
   "is_adult":True,
   "subjects": ["c","c++","python"],#list
   "subject": ("c","c++","python")#Tuple
}
print(dict)
print(type(dict))
#ONly print some specific key of the dictionary
print(dict["name"])
print(dict["age"])
#Change the value of the specific key
dict["name"]="Tarun Singh"
print(dict["name"])
#Adding new key to the dictionary
dict["college"]="KIET"
print(dict)
#creating the null dictionary
null_dict={}
print(null_dict)


for letter in 'Tushar Singh':
    pass
print("Last letter is:",letter)