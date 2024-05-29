import re

def main():
    myinput = input("IPv4 Address: ")
    myinput = validate(myinput)
    print(myinput)

def validate(ip):
    a = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip)
    if not a:
        return(False)
    b = ip.split(".")
    for i in b:
        if int(i) < 0:
            return(False)
        if int(i) > 255:
            return(False)
    return(True)
if __name__ == "__main__":
    main()
