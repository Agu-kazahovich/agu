def multiple(x,y=10):
    print(x*y)
    return x*y
a = multiple(4)
print(a)

def g(x,y):
    
    j = g(x + y)
    if g > 100:
        print(g,"100 ден үлкен")
    else:
        print(g,"улкен")
    
    return x,y