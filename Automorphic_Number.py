a=int(input())
a=str(abs(a))
l=len(a)
b=str(int(a)**2)
if a==b[-l:]:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')