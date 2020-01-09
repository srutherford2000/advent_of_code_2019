def part_1():
    in_file=open('input.txt')
    sum=0
    for line in in_file:
        line=line.strip()
        num=int(line)
        num=(num//3)-2
        sum+=num
        print(num)

    print(sum)
    in_file.close()

    

def part_2(starting_num):
    if starting_num//3-2<=0:
        return 0
    new_value=starting_num//3-2
    print(new_value)
    return new_value + part_2(new_value)

def part_2_sum():
    in_file=open('input.txt')
    sum=0
    for line in in_file:
        line=line.strip()
        num=int(line)
        fuel=part_2(num)
        sum+=fuel
        print(num)

    print(sum)
    in_file.close()
