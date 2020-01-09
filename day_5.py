#OPCODE 1   add   (opcode, index1, index2, final value index)
#OPCODE 2   multiply  (same as above)
#OPCODE 3   just index (opcode,index) takes an input and puts it at index
#OPCODE 4   just output it at a spot (opcode,index) places an output at the index

#position mode how it works rn with index1 find value there
#immdeiate mode just takes the value as is not the value at that index


#Given 1002
#02=opcode
#hundreds = position mode
#thosands = immdiate mode

input_val=1

list_of_doom=input('i like string seperated by commas')

list_of_doom= list_of_doom.split(',')

going_threw=0
index=0

while going_threw==0:
    try:
        opcode=list_of_doom[index][-1]
        num_of_values=len(list_of_doom[index][:-2])
        print((opcode), num_of_values)
        if opcode=='3':
            where_to_go=list_of_doom[index+1]
            list_of_doom[int(where_to_go)]=input_val
        elif opcode==4:        
            where_to_go=list_of_doom[index+1]
            print(list_of_doom[int(where_to_go)])
        elif opcode==2 or opcode==1:
            things_to_add_or_mult=[]
            print(things_to_add_or_mult)
            for i in range(int(num_of_values)):
                things_to_add_or_mult.append(list_of_doom[index+1+int(i)])
            where_to_go=things_to_add_or_mult.pop()
            print(where_to_go)
            if opcode==2:
                change=1
                for i in where_to_go:
                    change *= int(i)            
            if opcode==1:
                change=0
                for i in where_to_go:
                    change += int(i)
            print(change)
            list_of_doom[where_to_go]=change
        print(list_of_doom)
        index += (num_of_values + 1)

    except IndexError:
        going_threw=1
        

        
        
 
