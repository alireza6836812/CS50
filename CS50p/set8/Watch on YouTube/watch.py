import re


def main():
    myinput = input("HTML: ")
    myinput = parse(myinput)
    print(myinput)


def parse(s):
    r = re.match(r'<iframe.*?src="(https?:\/\/(?:www\.)?youtube\.com(?:\/embed)?\/[a-zA-z0-9_-]+)".*?',s)
    if match := r:
        url = match.group(1).split("/")[-1]
        output = "https://youtu.be/" + url
        return(output)
    return None


if __name__ == "__main__":
    main()
