s1="hello my name is Tushar Singh"
#str.endswith("substring"):Returns true if string ends with the substr
print(s1.endswith("gh"))
print(s1.endswith("fo"))
#str.capitalize():Capitalize the first characte but not in the main string
print(s1.capitalize())
print(s1)
#str.replace(old,new):replace all the old word with the new word
print(s1.replace("a","p"))
print(s1.replace("ame","put"))
#str.find(word):It will return the index of the first occurance ofthe word
print(s1.find("a"))
#str.count("substring"):count the occurance of the substring
print(s1.count("a"))