photo_data=input('give photo data')

w=int(input('wide'))
h=int(input('height'))

rows=[]

num=int(w*h)

for i in range(int(len(photo_data)/(num))):
    row=photo_data[(num)*i:((num)*(i+1))]
    rows.append(row)

print(rows)

max_count_zero=1000
list_of_max=[]

for i in rows:
    count=i.count('0')
    print(count, rows.index(i))
    if count<max_count_zero:
        print('here')
        max_cout_zero=count
        print(max_count_zero)
        list_of_max=i

print(max_count_zero)

print (list_of_max)


twos=list_of_max.count('2')
ones=list_of_max.count('1')

print(twos*ones)
