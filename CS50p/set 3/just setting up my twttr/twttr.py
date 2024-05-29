string = input('Input:')
output = ''
v_list = ['A','E','O','U','a','i','e','o']
for i in string:
    if i in v_list:
        pass
    else:
        output += i
print('Output:',output)