# #set                   #list                        #tuple                          #dict                     #type
# a={1,2,3,4}            a=[1,2,3]                    a=(1,2,3)                       a={"name":"Dauren"}       print(type(a))
# b=set(1,2,3,1)         b=list(1,2,3)                b=tuple(1,2,3)                                            if type(a)=dict:


# a = 4
# while a < 5:
#     a += 2
#     print("hello world")


# a = 0
# while True:
#     if a == 4:
#         break 
#     print("Hi")
#     a+=1



# a = [(1,2),(1,),(2,3),1]
# while True:
#     b=tuple(a)
#     print(type(a))
#     break


a = [(1,2),(1,),(2,3),1]
for i in range(a):
    b=tuple(a)
    print(type(b))
    break