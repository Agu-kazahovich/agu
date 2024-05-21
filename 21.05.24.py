# list = [2,5,4,6,4,7]

# max_number = list[0]
# for i in list:
#     if i > max_number:
#         max_number = i

# print(max_number)



# list1 = [5,6,7,2,3]

# def find_max(list1):
#     max_number = list1[0]
#     for i in list1:
#         if i > max_number:
#             max_number = i
#     return max_number

# print(find_max([5,6,7,2,3]))


class Max_num:
    def get_maxnum(self):
        list1 = [1,2,3,4,5]
        max_number = list1[0]
        for i in list1:
            if i > max_number:
                max_number = i
        print(max_number) 


max_obj = Max_num()
max_obj.get_maxnum()