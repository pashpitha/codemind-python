n=input()
a=int(n)**2
b=int(n[::-1])**2
b=str(b)
if(str(a)==b[::-1]):
    print('True')
else:
    print('False')