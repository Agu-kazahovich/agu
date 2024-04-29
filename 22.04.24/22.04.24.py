def multiple(x,y=10):
    print(x*y)
    return x*y
a = multiple(4)
print(a)

def check_numbers(x,y):
    if x + y > 100:
        return "100 ден үлкен"
    else:
        return "кіші"

print(check_numbers(50,51))

def find_max(list1):
    max_number = list1[0]
    for i in list1:
        if i > max_number:
            max_number = i
    return max_number

print(find_max([2,20,4,10,3]))