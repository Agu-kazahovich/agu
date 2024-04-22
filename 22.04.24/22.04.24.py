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
