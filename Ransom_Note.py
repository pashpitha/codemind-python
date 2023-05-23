def num(x,y):

    for i in x:

        if i in y:

            y.remove(i)

        else:

            return False

    return True

x,y=map(list,input().split())

print(num(x,y))