#creating the nested dictionary
student={
    "name":"Tushar Singh",
    "Subjects":{
        "Python":90,
        "COA":95,
        "DS":100,
        "UHV":97,
        "Sensor":70,
        "DSDL":90
    },
    "age":20,
    "College":"KIET"
}
print(student)
print(student["Subjects"])
print(student["Subjects"]["Python"])
print(type(student))