r = 3
k = 1
b = 0
xc = 1
yc = 1
x1 = -1
y1 = -2
x2 = 4
y2 = 1
x = float(input("введите x:"))
y = float(input("введите y:"))

if(y < k*(x+b)):
    if((x-xc)**2+(y-yc)**2 < r**2):
        if(x1 < x < x2) and (y1 < y < y2):
            print("Под прямой линией,в прямоугольнике и круге")
        else:
            if(y>y2):
                print("Под линией,за кругом и над прямоугольником")
            else:
                print("Под линией,в круге и под прямоугольником")
    else:
        if (x1 < x < x2) and (y1 < y < y2):
            print("Под линией,за кругом и в прямоугольнике")
        else:
            print("Под линией,за кругом и за прямоугольником")
else:
    if ((x - xc) ** 2 + (y - yc) ** 2 < r ** 2):
        if (x1 < x < x2) and (y1 < y < y2):
            print("О боже да вы снайпер!")
            print("Над линией,в прямоугольнике и круге")
        else:
            print("Над линией и в кругу")
    else:
        print("Над линией,за кругом и за прямоугольником")
print("Конец")
