name = input('camelCase:')
k = 0
j = 0
output = ''
for i in name:
    if i.isupper():
        output += '_'+name[j:k].lower()
        j = k
    k += 1
output += '_'+name[j:k+1].lower()
print(output[1:])