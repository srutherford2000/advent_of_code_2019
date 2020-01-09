def part_1(in_list,position1,position2):
    list_o_num=in_list[:]#.split(',')
    #for index,value in enumerate(list_o_num):   ###removed for part 2 leave for part 1
    #    list_o_num[index]=int(value)
    list_o_num[1]=position1
    list_o_num[2]=position2
    current_index_pos=0
    opcode=(list_o_num[current_index_pos])
    while opcode==1 or opcode==2:
        index1=(list_o_num[current_index_pos+1])
        index2=(list_o_num[current_index_pos+2])
        pos1=(list_o_num[index1])
        pos2=(list_o_num[index2])
        if opcode==1:
            new_num=pos1+pos2
        elif opcode==2:
            new_num=pos1*pos2
        index3=(list_o_num[current_index_pos+3])
        list_o_num[index3]=new_num
        current_index_pos+=4
        opcode=(list_o_num[current_index_pos])
    return list_o_num


def part_2(in_list,final_goal):
    list_o_num=in_list.split(',')
    for index,value in enumerate(list_o_num):
        list_o_num[index]=int(value)
    for i in range(100):
        for a in range(100):
            new_list=part_1(list_o_num,i,a)
            current_0_pos=new_list[0]
            if current_0_pos==final_goal:
                return i,a
            
    
