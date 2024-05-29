my_input = input('Expression: ')
my_input = my_input.split(' ')

if my_input[1] == '+':
    output = float(my_input[0]) + float(my_input[-1])
elif my_input[1] == '-':
    output = float(my_input[0]) - float(my_input[-1])
elif my_input[1] == '*':
    output = float(my_input[0]) * float(my_input[-1])
elif my_input[1] == '/' and my_input[-1] != '0':
    output = float(my_input[0]) / float(my_input[-1])
print(output)