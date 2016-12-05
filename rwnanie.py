import math
def rownianie_kwadratowe(a, b, c):
    if a == 0 and b == 0:
        return None
    if a == 0:
        x = -c/(b*1.0)
        print "This equation is linear, solutions is: ", x
        return x
    delta = b**2. - (4. * a * c)
    if delta < 0:
        print "This equation has no real solutions"
        return None
    elif delta == 0:
        x0 = -b/(2.*a)
        print "This equation has two solutions: ", x0
        return x0
    else:
        x1 = (-b - math.sqrt(delta))/(2.*a)
        x2 = (-b + math.sqrt(delta))/(2.*a)
        print "This equation has two solutions:", x1, x2
        return x1, x2 a, b, c = input("Enter the a, b and c separeted by commas: ")



a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
rownianie_kwadratowe(a,b,c)
