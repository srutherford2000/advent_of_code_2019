#It is a six-digit number.
#The value is within the range given in your puzzle input.
#Two adjacent digits are the same (like 22 in 122345).
#Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679)

num_of_valid=0


def has_two_double_letters(word):
    word=str(word)
    last_letter=''
    for i in word:
        if i == last_letter:
            return True
        last_letter = i
    return False

def has_two_double_letters2(word):
    word=str(word)
    word=list(word)
    different_letters=[]
    for i in word:
        if word not in different_letters:
            different_letters.append(i)
    counts_of_letters=[]
    for i in different_letters:
        counts_of_letters.append(word.count(i))
    if 2 in counts_of_letters:
        return True
    else:
        return False

def word_only_increases(word):
    word=str(word)
    last_letter='0'
    for i in word:
        if last_letter >i:
            return False
        last_letter=i
    return True

def part1():
    num_of_valid=0
    for i in range(402328,864247):
        if has_two_double_letters(i) and word_only_increases(i):
            num_of_valid+=1
            print(i)
    return num_of_valid


def part2():
    num_of_valid=0
    for i in range(402328,864247):
        if has_two_double_letters2(i) and word_only_increases(i):
            num_of_valid+=1
            print(i)
    return num_of_valid



        
       
        
    
