#list1 = [1,2,3,4,5]
#for i in list1:
 #   print("Element:",i)
#print(list1[0])
#list1.append(9)
#print(list1)

#for i in range (1,1001):
    #print(i)

#list2=["a", "b", "1", "de"]
#for i in list2:
 #   print(i)

#for i in "втипо":
 #   print(i)

a = 5
b = 8

c = 1

for num in range(a, b + 1):
    c *= num

print(f"{a} мен {b} ның арасындағы сандардың көбейтіндісі {c}.")


N = 5

total_sum = 0.0

for i in range(1, N + 1):
    total_sum += 1 / i

print(f"Сумма ряда 1 + 1/2 + 1/3 + ... + 1/{N} равна {total_sum:.4f}.")