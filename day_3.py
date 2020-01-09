def part1(list1,list2):
    pos1, pos2= [0,0],[0,0]

    #list1=input('enter string of list').split(',')
    #list2=input('enter string of list').split(',')

    where1_been=[]
    where2_been=[]

    for place in list1:
        direction=place[0]
        number=int(place[1:])
        if direction=='R':
            for i in range(number):
                pos1[0]+=1
                where1_been.append(pos1[:])
        elif direction=='L':
            for i in range(number):
                pos1[0]-=1
                where1_been.append(pos1[:])
        elif direction=='D':
            for i in range(number):
                pos1[1]-=1
                where1_been.append(pos1[:])
        elif direction=='U':
            for i in range(number):
                pos1[1]+=1
                where1_been.append(pos1[:])
    print('a')

    for place in list2:
        direction=place[0]
        number=int(place[1:])
        if direction=='R':
            for i in range(number):
                pos2[0]+=1
                where2_been.append(pos2[:])
        elif direction=='L':
            for i in range(number):
                pos2[0]-=1
                where2_been.append(pos2[:])
        elif direction=='D':
            for i in range(number):
                pos2[1]-=1
                where2_been.append(pos2[:])
        elif direction=='U':
            for i in range(number):
                pos2[1]+=1
                where2_been.append(pos2[:])

    print('b')


    distances=[]
    intersections=[]
    for place in where1_been:
        if place in where2_been:
            distance= abs(place[0])+abs(place[1])
            distances.append(distance)
            intersections.append(place)
    print('c')

    #print(min(distances))
    return intersections

def part2():
    pos1,pos2=[0,0],[0,0]
    lista=input('enter string of list').split(',')
    listb=input('enter string of list').split(',')

    intersects=part1(lista,listb)
    player_distances=[]
    for i in range(len(intersects)):
        player_distances.append([0,0])


    distance1=0
    distance2=0

    print('d')

    for place in lista:
        direction=place[0]
        number=int(place[1:])
        if direction=='R':
            for i in range(number):
                pos1[0]+=1
                distance1+=1
                if pos1 in intersects:
                    loc=intersects.index(pos1)
                    player_distances[loc][0]=distance1
        elif direction=='L':
            for i in range(number):
                pos1[0]-=1
                distance1+=1
                if pos1 in intersects:
                    loc=intersects.index(pos1)
                    player_distances[loc][0]=distance1
        elif direction=='D':
            for i in range(number):
                pos1[1]-=1
                distance1+=1
                if pos1 in intersects:
                    loc=intersects.index(pos1)
                    player_distances[loc][0]=distance1
        elif direction=='U':
            for i in range(number):
                pos1[1]+=1
                distance1+=1
                if pos1 in intersects:
                    loc=intersects.index(pos1)
                    player_distances[loc][0]=distance1

    print('e')

    for place in listb:
        direction=place[0]
        number=int(place[1:])
        if direction=='R':
            for i in range(number):
                pos2[0]+=1
                distance2+=1
                if pos2 in intersects:
                    loc=intersects.index(pos2)
                    player_distances[loc][1]=distance2
        elif direction=='L':
            for i in range(number):
                pos2[0]-=1
                distance2+=1
                if pos2 in intersects:
                    loc=intersects.index(pos2)
                    player_distances[loc][1]=distance2
        elif direction=='D':
            for i in range(number):
                pos2[1]-=1
                distance2+=1
                if pos2 in intersects:
                    loc=intersects.index(pos2)
                    player_distances[loc][1]=distance2
        elif direction=='U':
            for i in range(number):
                pos2[1]+=1
                distance2+=1
                if pos2 in intersects:
                    loc=intersects.index(pos2)
                    player_distances[loc][1]=distance2

        smallest_distance=1000000000
        for i in player_distances:
            new=i[0]+i[1]
            if new<smallest_distance:
                smallest_distance=new
            

    return smallest_distance
    
        
