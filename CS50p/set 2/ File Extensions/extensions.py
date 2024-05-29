my_input = input("File name: ")
my_input = my_input.lower().strip().split(".")

app = ["zip", "pdf"]
img = ["png", "gif"]

if my_input[-1] == "txt":
    print("text/plain")
elif my_input[-1] in app:
    print('application/'+my_input[-1])
elif my_input[-1] == "jpg":
    print('image/jpeg')
elif my_input[-1] == "jpeg":
    print("image/jpeg")
elif my_input[-1] in img:
    print('image/'+my_input[-1])
else:
    print("application/octet-stream")