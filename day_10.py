import math
def part_1():
    def calc_slope(spot1,spot2):
        # spot2 is new pos
        #spot 1 is old pos
        try:
            x1,y1=spot1
            x2,y2=spot2
            slope = (y2-y1)/(x2-x1)
            if slope ==0:
                if x2-x1>0:
                    return 'l'
                return 'r'
            elif y2-y1>0:            
                return str(slope)+'u'
            return str(slope)+'d'
        except ZeroDivisionError:
            if y2-y1>0:
                return 'u'
            return 'd'

    file_name=input('enter a file name')

    in_file=open(file_name)
    lines=[]

    for line in in_file:
        lines.append(line.strip())

    in_file.close()

    asteroid_locs=[]

    for index, line in enumerate( lines):
        for index2, letter in enumerate(line):
            if letter != '.':
                asteroid_locs.append([index2,index])


                

    slopes=[]
    for i in asteroid_locs:
        new_line=[i[:]]
        for a in asteroid_locs:
            if i != a:
                slope1=calc_slope(a,i)
                new_line.append(slope1)
        slopes.append(new_line)

    counts=[]
    for i in slopes:
        new_line=[]
        pos=i.pop(0)
        for a in i:
            if a not in new_line:
                new_line.append(a)
        count=len(new_line)
        counts.append([pos,count])

    max_count=0
    max_pos=''

    for i in counts:
        if i[1]>max_count:
            max_count=i[1]
            max_pos=i[0]

    print(max_pos,'has', max_count)
        
            
        
def part_2():
    def calc_angle(spot1,spot2):
        # spot2 is new pos
        #spot 1 is old pos
        x1,y1=spot1
        x2,y2=spot2
        x_change=x2-x1
        y_change=y2-y1
        try:
            angle=math.degrees(math.atan(y_change/x_change))
            if angle < 0:
                angle+=360
            return angle
        except ZeroDivisionError:
            if x_change>0:
                return 0
            return 180
            

    file_name=input('enter a file name')

    in_file=open(file_name)
    lines=[]

    for line in in_file:
        lines.append(line.strip())

    in_file.close()

    asteroid_locs=[]

    for index, line in enumerate( lines):
        for index2, letter in enumerate(line):
            if letter != '.':
                asteroid_locs.append([index2,index])


                

    slopes=[]
    for i in asteroid_locs:
        new_line=[i[:]]
        for a in asteroid_locs:
            if i != a:
                slope1=calc_angle(a,i)
                new_line.append(slope1)
        slopes.append(new_line)

    counts=[]
    for i in slopes:
        new_line=[]
        pos=i.pop(0)
        for a in i:
            if a not in new_line:
                new_line.append(a)
        count=len(new_line)
        counts.append([pos,count])

    max_count=0
    max_pos=''

    for i in counts:
        if i[1]>max_count:
            max_count=i[1]
            max_pos=i[0]
            
    correct_line=slopes[asteroid_locs.index(max_pos)]
    print(correct_line)

    start_num=90
    i=0

    while len(correct_line)>0:
        closest_to_start_num=540
        index=''
        for i in correct_line:
            distance= start_num - i
            print(distance)
            if i<start_num and 0<distance<closest_to_start_num and distance>0:
                closest_to_start_num=i
                index=correct_line.index(i)
        start_num -=1
        print('i',index)
        if start_num <0:
            print('here')
            start_num=360
        print('s',closest_to_start_num)
        print('c',correct_line)
        print('p',correct_line.pop(index))
        
        
        
        
        
 
        
