list=[10,20,30,40,50]
for i in list:
    print(i)

list=[1,2,3,4,5,6,7]
for i in list:
    if i%2 == 0:
        print(i)

list=[12,13,14,15,16]
for i in list:
    if i % 2 != 0:
     print(i)


list=[12,14,15,16,17]
total=0
for i in list:
   total+=i
   print("sum",total)

list=[10,20,5,8]
largest=list[0]
for i in list:
   if i>largest:
      largest=i
      print("largest",largest)

list=[-1,2,3,-4,5]
count = 0
for i in list:
   if i >0:
      count+=1
      print("positive count",count)