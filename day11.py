filename=input('file name')

infile=open(filename)

lines_in_file=[]
for line in infile:
    line=line.strip()
    lines_in_file.append(line)

infile.close()

list_of_nums=[]
good_nums=[]
for line in lines_in_file:
    nums=line.split(',')
    list_of_nums+=nums
    for i in nums:
        if i=='0' or i =='1':
            good_nums.append(int(i))

locations=[[0,0]]
direction='u'
current_location=[0,0]
print(good_nums)

while len(good_nums)>1:
    color=good_nums.pop(0)
    move=good_nums.pop(0)
    if move == 1:
        if direction == 'u':
            direction = 'l'
            current_location[0]-=1
        elif direction =='l':
            direction = 'd'
            current_location[1]-=1
        elif direction=='d':
            direction ='r'
            current_location[0]+=1
        elif direction == 'r':
            direction = 'u'
            current_location[1] +=1
    elif move == 0:
        if direction == 'u':
            direction = 'r'
            current_location[0]+=1
        elif direction =='l':
            direction = 'u'
            current_location[1]+=1
        elif direction=='d':
            direction ='l'
            current_location[0]-=1
        elif direction == 'r':
            direction = 'd'
            current_location[1] -=1
    locations.append(current_location[:])


print(locations)

no_repeats=[]
for i in locations:
    if i not in no_repeats:
        no_repeats.append(i)

print(len(no_repeats))
            
    
    
