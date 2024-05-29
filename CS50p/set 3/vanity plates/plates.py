def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(string):
    number = ''
    k = 0
    for i in string:
        try:
            try:
                int(i)
                break
            except:
                k += 1
            if string[k] == '0':
                return (False)
        except:
            return (False)
    if string[0].isalpha() and string[1].isalpha():
        if len(string)>2 and len(string)<6:
            string1 = list(string)
            for i in string1:
                try:
                    int(i)
                    number += i
                except:
                    pass
            if number not in string:
                return (False)
            else:
                return (True)
        else:
            return (False)
    else:
        return (False)

main()