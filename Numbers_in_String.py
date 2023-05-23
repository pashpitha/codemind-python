a=input()

count=0

for i in a:

    if i in '1234567890':

        count+=int(i)

print(count)