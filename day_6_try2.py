def part1():
    file_name=input('enter file name')

    in_file=open(file_name)

    orbit_list=[]

    for line in in_file:
        line=line.strip()
        one_orbit_pos= line.split(')')
        orbit_list.append(one_orbit_pos)

    in_file.close()

    possible_paths=[]

    for i in orbit_list:
        a=i[0]
        b=i[1]
        if a not in possible_paths:
            possible_paths.append(a)
        if b not in possible_paths:
            possible_paths.append(b)

    print(possible_paths)

    orbit_num=0
    for letter in possible_paths:
        while letter != 'COM':
            for orbit in orbit_list:
                if orbit[1]==letter:
                    orbit_num+=1
                    letter = orbit[0]
        print(orbit_num)

    print('here')
                    
        
        
def part2():
    file_name=input('enter file name')

    in_file=open(file_name)

    orbit_list=[]

    for line in in_file:
        line=line.strip()
        one_orbit_pos= line.split(')')
        orbit_list.append(one_orbit_pos)

    in_file.close()

    possible_paths=[]

    for i in orbit_list:
        a=i[0]
        b=i[1]
        if a not in possible_paths:
            possible_paths.append(a)
        if b not in possible_paths:
            possible_paths.append(b)

    santa_path=[]
    my_path=[]

    letter='SAN'
    while letter != 'COM':
        for orbit in orbit_list:
            if orbit[1]==letter:
                santa_path.append(orbit[0])
                letter = orbit[0]
    print(santa_path)

    letter='YOU'
    while letter != 'COM':
        for orbit in orbit_list:
            if orbit[1]==letter:
                my_path.append(orbit[0])
                letter = orbit[0]
    print(my_path)

    unique_places=[]
    for place in santa_path:
        if place not in my_path:
            unique_places.append(place)

    for place in my_path:
        if place not in santa_path and place not in unique_places:
            unique_places.append(place)
    
    print(unique_places)
    print(len(unique_places))
