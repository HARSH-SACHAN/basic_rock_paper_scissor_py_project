from random import randint
import random

selection = 0 #creating global variable to avoid overwriting the fuctional values
cpu = 0 # creating another global variable in case of using it in funciton
select = str(input('R - rock  S - scissor  P - paper \t')).capitalize()
comp = randint(1, 3)  #randint method to generate random integer from 1 to 3


# 1 - rock
# 2 - scissor
# 3 - paper


print('comp = 1 is rock')
print('comp = 2 is scissor')
print('comp = 3 is paper')
print(f'the selection of cpu is {comp}')



def player_dec():


    '''
    using basic if elif and else statements to caary out task
    using and operation to merge two data
    using local variable 
    avoiding global variable
    '''

    if comp == 1 and select == 'R':
        print('you select rock and cpu select rock \nits a tie')
    elif comp == 1 and select == 'S':
        print('you select scissor and cpu selected rock \nyou lose ')
    elif comp == 1 and select == 'P':
        print('you select paper and cpu select rock \nyou won')
    elif comp == 2 and select == 'R':
        print('you select rock and cpu select scissor \nyou won')
    elif comp == 2 and select == 'S':
        print('you select scissor and cpu select scissor \nits a tie')
    elif comp == 2 and select == 'P':
        print('you select paper and cpu select scissor \nyou lose')
    elif comp == 3 and select == 'R':
        print('you select rock and cpu select paper \nyou lose')
    elif comp == 3 and select == 'S':
        print('you select scissor and cpu select paper \nyou won')
    elif comp == 3 and select == 'P':
        print('you select paper and cpu select paper \nits a tie')
    else:
        print('wrong code')

player_dec()        
