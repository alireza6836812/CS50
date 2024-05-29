my_input = input('Greeting: ')
my_input = my_input.lower().strip()
if 'hello' in my_input:
    print('$0')
elif my_input[0] == 'h':
    print('$20')
else:
    print('$100')