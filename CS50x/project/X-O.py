import pygame
import time

def page(text,number,screen_width,screen_height):
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 36)
    lines = text.splitlines()
    text_width, text_height = font.size(text)

    text_x = ((screen_width - text_width) // 2) + number
    text_y = ((screen_height - text_height * len(lines)) // 2) - 30

    for line in lines:
        text_surface = font.render(line, True, (0, 0, 0))
        screen.blit(text_surface, (text_x, text_y))
        text_y += font.get_height()
    pygame.display.update()
    time.sleep(5)
    pygame.quit()

text = "Hi welcome to X-O game."+2*'\n'+'This game is created by Alireza Seyfi'
page(text,200,640,400)
text = 'Rules of the game:'
page(text,0,300,200)
text = '1) Enter your movement as row-column.'+2*'\n'+'For example 12 means first row and second column'
page(text,230,700,350)
text = '2) Any movement outside the range of 3*3 will stop the game.'
page(text,0,800,300)
text = '3) Any repeated movement will stop the game.'
page(text,0,600,300)
text = 'Have fun'
page(text,0,200,150)

from IPython.display import clear_output

my_dict = {'11':'|___|','12': '|___|' , '13':'|___|',
           '21':'|___|','22': '|___|' , '23':'|___|',
           '31':'|___|','32': '|___|' , '33':'|___|'}

def dooz(my_dict1):
    j = 0
    string1 = ''
    for column in my_dict1:
        j +=1
        if j < 10:
            string1 += my_dict1[column]

    return(string1[:15]+'\n'+string1[15:30]+'\n'+string1[30:]+'\n')

def replacer(move_number):
    string = '|___|'
    string = list(string)
    if move_number//2 == 0:
        string[2] = 'X'
    elif move_number//2 == 1:
        string[2] = 'O'
    output = ''
    for i in string:
        output += i
    return(output)

k = 1
moves_list1 = ['11','12','13',
               '21','22','23',
               '31','32','33']
moves_list = []
for i in range(0,100):

    # out of range
    move = str(input('please give me your row and column:'))
    if move not in moves_list1:
        text = 'Your movement is not in available range.'+2*'\n'+'*** Please restart the game ***'
        page(text,150,600,300)
        break

    # frequently choice
    if move in moves_list:
        text = ('This block is already filled'+2*'\n'+'*** Please restart the game ***')
        page(text,130,600,300)
        break

    moves_list.append(move)

    if i%2 == 1:
        a = replacer(2)
        my_dict[move] = replacer(2)
        #page(dooz(my_dict))
        page(dooz(my_dict),160,400,400)
    elif i%2 == 0:
        b = replacer(1)
        my_dict[move] = replacer(1)
        #page(dooz(my_dict))
        page(dooz(my_dict),160,400,400)

    win1 = (my_dict['11'] == my_dict['22'] == my_dict['33'] == '|_X_|')
    win2 = (my_dict['11'] == my_dict['12'] == my_dict['13'] == '|_X_|')
    win3 = (my_dict['21'] == my_dict['22'] == my_dict['23'] == '|_X_|')
    win4 = (my_dict['31'] == my_dict['32'] == my_dict['33'] == '|_X_|')
    win5 = (my_dict['31'] == my_dict['22'] == my_dict['13'] == '|_X_|')
    win6 = (my_dict['11'] == my_dict['21'] == my_dict['31'] == '|_X_|')
    win7 = (my_dict['12'] == my_dict['22'] == my_dict['32'] == '|_X_|')
    win8 = (my_dict['13'] == my_dict['23'] == my_dict['33'] == '|_X_|')
    win9 = (my_dict['11'] == my_dict['22'] == my_dict['33'] == '|_O_|')
    win10 = (my_dict['11'] == my_dict['12'] == my_dict['13'] == '|_O_|')
    win11 = (my_dict['21'] == my_dict['22'] == my_dict['23'] == '|_O_|')
    win12 = (my_dict['31'] == my_dict['32'] == my_dict['33'] == '|_O_|')
    win13 = (my_dict['31'] == my_dict['22'] == my_dict['13'] == '|_O_|')
    win14 = (my_dict['11'] == my_dict['21'] == my_dict['31'] == '|_O_|')
    win15 = (my_dict['12'] == my_dict['22'] == my_dict['32'] == '|_O_|')
    win16 = (my_dict['13'] == my_dict['23'] == my_dict['33'] == '|_O_|')

    if win1 or win2 or win3 or win4 or win5 or win6 or win7 or win8:
        text = 'X is winner.'
        page(text,0,300,300)
        break
    elif win9 or win10 or win11 or win12 or win13 or win14 or win15 or win16:
        text = 'O is winner.'
        page(text,0,300,300)
        break

    if i == 8:
        text = 'Draw, no one won the game.'
        page(text,0,400,400)
        break