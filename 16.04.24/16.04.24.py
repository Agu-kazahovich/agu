#def add(x,y): #параметр
   # return x+y

#a = add(4,5)
#print(a)

def add_to_list(x):
    list1 = [1,2,3,4]
    list1.append(x)
    return list1   
a = add_to_list(5)
print(a)


def add(x):
    listt1=[ {
    "name":"Zarina",
    "last_name":"Beisenbekova",
    "Age":20},
    {"name":"Aruzhan",
     "last_name":"Erzhanov",
     "Age":15},
    {"name":"Ersultan",
     "last_name":"Ali",
     "Age":45}
]
    listt1.append(x)
    return listt1

print(add({"name":"Dias",
           "last_name":"Askar",
           "Age":"20"}))