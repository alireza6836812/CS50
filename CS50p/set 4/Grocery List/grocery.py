my_dict = {}
while True:
    try:
        name = input()
        name = name.upper().strip()
        if name not in my_dict:
            my_dict[name] = 1
        else:
            my_dict[name] += 1
    except EOFError:
        my_dict = list(my_dict.items())
        my_dict = sorted(my_dict)
        my_dict = dict(my_dict)
        for name in my_dict:
            print(my_dict[name], name, sep=" ")
        break
    except KeyError:
        pass
