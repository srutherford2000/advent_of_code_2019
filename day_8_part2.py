photo_data=input('give photo data')

w=int(input('wide'))
h=int(input('height'))

rows=[]

num=int(w*h)

for i in range(int(len(photo_data)/(num))):
    row=photo_data[(num)*i:((num)*(i+1))]
    rows.append(row)

print(rows)



new_layer=[]
for i in rows:
    layer_row=[]
    for a in range(h):
        row2=i[(w)*a:((w)*(a+1))]
        layer_row.append(row2)
    new_layer.append(layer_row)

final=new_layer[0]
for i in final:
    new=list(str(i))
    loc = final.index(i)
    final[loc]=new


for index, box in enumerate(new_layer):
    print(box)
    print()
    for index2, line in enumerate(box):
        print(line)
        print()
        for index3, letter in enumerate(line):
            print(letter, 'l')
            current_color= final[index2][index3]
            print( current_color, 'c')
            if current_color == '0' or current_color=='1':
                pass
            else:
                final[index2][index3] = letter
          



for i in final:
    print(a)

