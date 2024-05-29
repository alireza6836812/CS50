my_input = input('What is the Answer to the Great Question of Life, the Universe, and Everything?')
yes_list = ['42','forty-two','forty two']

if my_input.lower().strip() in yes_list:
    print('Yes')
else:
    print('No')