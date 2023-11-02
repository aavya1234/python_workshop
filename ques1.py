
n=int(input("enter the number upto which user want the square"))
squares={num:num**2 for num in range(1,n+1)}
print(squares)


dic={'x':10,'y':20,'z':30}
for key,value in dic.items():
    print(f"{key}={value}")


squares={num:num**2 for num in range(1,16)}
print(squares)


my_dic={'data1':100, 'data':-54, 'data3':247}
sum=0
for value in my_dic.values():
    sum=sum+int(value)
print("the sum is",sum)



color_dict={ 'red':'#FF0000',
            'green':'#000000',
            'black':'#000000',
            'white':'#FFFFFF' }
my_keys=list(color_dict.keys())
my_keys.sort()
sorted_dict={i: color_dict[i] for i in my_keys}
print(sorted_dict)


d={1:10,2:20,3:30,4:40,5:50,6:60}
k=int(input("enter the key to be searched:"))
if k in d:
    print("found")
else:
    print("notfound")