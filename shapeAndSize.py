import matplotlib.pyplot as plt
from numpy import *
class square():
    def plot( side, marker='none', linestyle='solid', color='m'):
        x = array([0, 0, side, side, 0])
        y = array([0, side, side, 0, 0])
        plt.plot(x, y, marker=marker, linestyle=linestyle.lower(), color=color)
        plt.axis('equal')
        plt.title('Square')
        plt.show()
        return()
    def area(side):
        z= side ** 2
        return(float(z))
    def perimeter(side):
        z= 4 * side
        return(float(z))
    def diagonal(side):
        z= ((side ** 2) + (side ** 2)) ** (1 / 2)
        return(float(z))
class ractangle():
    def plot( length, breadth, marker='none', linestyle='solid', color='m'):
        x = array([0, 0, length, length, 0])
        y = array([0, breadth, breadth, 0, 0])
        plt.plot(x, y, marker=marker, linestyle=linestyle.lower(), color=color)
        plt.axis('equal')
        plt.title('Rectangle')
        plt.show()
        return()
    def area( length, breadth):
        area4 = length * breadth
        return(float(area4))
    def perimeter( length, breadth):
        peri = (2 * (length + breadth))
        return(float(peri))
    def diagonal( length, breadth):
        diago = ((length ** 2) + (breadth ** 2)) ** (1 / 2)
        return(float(diago))
class triangle():
    def plot(base ,side1 ,side2 ,marker='none' ,linestyle='solid' ,color='m'):
        peri = (base + side2 + side1)
        s = peri / 2
        area = (s * (s - base) * (s - side2) * (s - side1)) ** (1 / 2)
        height = (2 * area) / base
        if side2 > base:
            ex = base + (((side1 ** 2) - (height ** 2)) ** (1 / 2))
        else:
            ex = base - (((side1 ** 2) - (height ** 2)) ** (1 / 2))
        x = [0, base, ex, 0]
        y = [0, 0, height, 0]
        plt.title('triangle')
        plt.plot(x, y, marker=marker, linestyle=linestyle.lower(), color=color)
        plt.axis('equal')
        plt.show()
        return()
    def area(base ,side1 ,side2):
        peri = (base + side2 + side1)
        s = peri / 2
        area = (s * (s - base) * (s - side2) * (s - side1)) ** (1 / 2)
        return(area)
    def perimeter(base ,side1 ,side2):
        peri = (base + side2 + side1)
        return(float(peri))
    def height(base ,side1 ,side2):
        peri = (base + side2 + side1)
        s = peri / 2
        area = (s * (s - base) * (s - side2) * (s - side1)) ** (1 / 2)
        height = (2 * area) / base
        return(float(height))
class equilateralTriangle():
    def  plot(base ,marker='none' ,linestyle='solid' ,color='m'):
        peri = (base*3)
        s = peri / 2
        area = (s * (s - base) * 3) ** (1 / 2)
        height = (2 * area) / base
        x = [0, base, base/2, 0]
        y = [0, 0, height, 0]
        plt.title('triangle')
        plt.plot(x, y, marker=marker, linestyle=linestyle.lower(), color=color)
        plt.axis('equal')
        plt.show()
        return()
    def area(side):
        peri = (side * 3)
        s = peri / 2
        area = (s * (s - side) * 3) ** (1 / 2)
        return(float(area))
    def perimeter(side):
        peri = (side*3)
        return float(peri)
    def height(side):
        peri = (side * 3)
        s = peri / 2
        area = (s * (s - side) * 3) ** (1 / 2)
        height = (2 * area) / side
        return float(height)
class parallelogram():
    def plot(length ,breadth ,h ,marker='none' ,linestyle='solid' ,color='m'):
        z = length+(((breadth**2)-(h**2))**(1/2))
        p = ((breadth**2)-(h**2))**(1/2)
        x = array([0 ,length ,z ,p ,0])
        y = array([0 ,0 ,h ,h ,0])
        plt.title('Parallelogram')
        plt.plot(x ,y ,marker=marker ,linestyle=linestyle.lower() ,color=color)
        plt.axis('equal')
        plt.show()
        return()
    def area(breadth ,h ):
        area = breadth * h
        return float(area)
    def perimeter(length,breadth ):
        peri = 2*(breadth * length)
        return float(peri)
class rhombus():
    def plot(diagonal_1 ,diagonal_2 ,marker='none' ,linestyle='solid' ,color='m'):
        db2 = diagonal_1/2
        upper_Diagonal2 = diagonal_2/2
        x = array([0, (db2) ,0 , - (db2) ,0 , - (db2) , (db2) ,0 ,0 ,0])
        y = array([0, (upper_Diagonal2) ,diagonal_2 , (upper_Diagonal2) ,0 , (upper_Diagonal2) , (upper_Diagonal2) ,upper_Diagonal2 ,0 ,diagonal_2])
        plt.title('Rhombus')
        plt.plot(x  ,y ,marker=marker ,linestyle=linestyle.lower() ,color=color)
        x = array([0 ,0.3 ,0.3 ,-0.3 ,-0.3 ,0 ,])
        y = array([ (upper_Diagonal2)-0.3 , (upper_Diagonal2)-0.3 , (upper_Diagonal2)+0.3 , (upper_Diagonal2)+0.3 , (upper_Diagonal2)-0.3 , (upper_Diagonal2)-0.3])
        plt.plot(x ,y ,linestyle=linestyle.lower() ,color=color)
        plt.axis('equal')
        plt.show()
        return()
    def area(diagonal_1 ,diagonal_2 ):
        area = (diagonal_1*diagonal_2)/2
        return(float(area))
    def perimeter(diagonal_1 ,diagonal_2 ):
        db2 = diagonal_1 / 2
        upper_Diagonal2 = diagonal_2 / 2
        s = ((db2 ** 2) + (upper_Diagonal2 ** 2)) ** (1 / 2)
        peri = s * 4
        return(float(peri))
    def side(diagonal_1 ,diagonal_2 ):
        db2 = diagonal_1 / 2
        upper_Diagonal2 = diagonal_2 / 2
        s = ((db2 ** 2) + (upper_Diagonal2 ** 2)) ** (1 / 2)
        return(float(s))
class trapeziod():
    def plot(base ,side ,parallel_side ,h ,marker='none' ,linestyle='solid' ,color='m'):
        b =(((side**2)-(h**2))**(1/2))
        if (base >=parallel_side):
            g =-b
        else:
            g =b
        x =array([0 ,base ,base+ (g) ,(base+ (g))-parallel_side ,0])
        y =array([0 ,0 ,h ,h ,0])
        plt.title('Trapeziod')
        plt.plot(x ,y ,marker=marker ,linestyle=linestyle.lower() ,color=color)
        plt.axis('equal')
        plt.show()
        return()
    def area(base ,parallel_side ,h ):
        area =((base+parallel_side)*h)/2
        return(float(area))
    def perimeter(base ,side ,parallel_side ,h ):
        b = (((side ** 2) - (h ** 2)) ** (1 / 2))
        if (base >= parallel_side):
            g = -b
        else:
            g = b
        b1 = base - ((base + (g)) - parallel_side)
        side41 = ((h ** 2) - (b1 ** 2)) ** (1 / 2)
        peri = base + parallel_side + side + side41
        return(float(peri))
    def side(base ,side ,parallel_side ,h ):
        b = (((side ** 2) - (h ** 2)) ** (1 / 2))
        if (base >= parallel_side):
            g = -b
        else:
            g = b
        b1 = base - ((base + (g)) - parallel_side)
        side = ((h ** 2) - (b1 ** 2)) ** (1 / 2)
        return(float(side))
class kite():
    def plot(diagonal_1 ,lower_Diagonal2 ,upper_Diagonal2 ,marker='none' ,linestyle='solid' ,color='m'):
        db2 =diagonal_1/2
        y =array([0 ,lower_Diagonal2 ,(upper_Diagonal2+lower_Diagonal2) ,lower_Diagonal2 ,0])
        x =array([db2 ,diagonal_1 ,db2 ,0 ,db2])
        area4 =((upper_Diagonal2+lower_Diagonal2)*diagonal_1)/2
        side41 =((db2**2)+(lower_Diagonal2**2))**(1/2)
        side42 =((db2**2)+(upper_Diagonal2**2))**(1/2)
        peri =(side41+side42)*2
        plt.title('Kite')
        plt.plot(x ,y ,marker=marker ,linestyle=linestyle.lower() ,color=color)
        plt.axis('equal')
        plt.show()
        return()
    def area(diagonal_1 ,lower_Diagonal2 ,upper_Diagonal2 ):
        area =((upper_Diagonal2+lower_Diagonal2)*diagonal_1)/2
        return float(area)
    def perimeter(diagonal_1 ,lower_Diagonal2 ,upper_Diagonal2 ):
        db2 = diagonal_1 / 2
        side41 =((db2**2)+(lower_Diagonal2**2))**(1/2)
        side42 =((db2**2)+(upper_Diagonal2**2))**(1/2)
        peri =(side41+side42)*2
        return float(peri)
    def sides(diagonal_1 ,lower_Diagonal2 ,upper_Diagonal2 ):
        db2 = diagonal_1 / 2
        side1 =((db2**2)+(lower_Diagonal2**2))**(1/2)
        side2 =((db2**2)+(upper_Diagonal2**2))**(1/2)
        return side1,side2
class anyShape:
    def  plot(no_of_side  ,radius,marker='none'  ,linestyle='solid' ,color='m'):
        n=no_of_side
        theta =linspace(0 ,2*(22/7) ,n+1)
        a = radius * cos(  theta  )
        b = radius * sin(  theta  )
        if n == 3:
            plt.title('Triangle or Trigon')
        elif n == 4:
            plt.title('Quadrilateral or Tetragon')
        elif n == 5:
            plt.title('Pentagon')
        elif n == 6:
            plt.title('hexagon')
        elif n == 7:
            plt.title('heptagon')
        elif n == 8:
            plt.title('octagon')
        elif n == 9:
            plt.title('Nonagon or Enneagon')
        elif n == 10:
            plt.title('decagon')
        elif n == 11:
            plt.title('hendecagon')
        elif n == 12:
            plt.title('Dodecagon or Duodecagon')
        elif n == 13:
            plt.title('Triskaidecagon, Tridecagon')
        elif n == 14:
            plt.title('Tetrakaidecagon, Tetradecagon')
        elif n == 15:
            plt.title('pentadecagon pentakaidecagon or quindecagon')
        elif n ==  16:
            plt.title('hexadecagon')
        elif n == 17:
            plt.title('heptadecagon')
        elif n == 18:
            plt.title('octadecagon')
        elif n == 19:
            plt.title('enneadecagon')
        elif n == 20:
            plt.title('icosagon')
        elif n == 21:
            plt.title('icosikaihenagon or henicosagon')
        elif n == 22:
            plt.title('icosikaidigon or docosagon')
        elif n == 23:
            plt.title('icosikaitrigon or tricosagon')
        elif n == 24:
            plt.title('icosikaitetragon or tetracosagon')
        elif n == 25:
            plt.title('icosikaipentagon or pentacosagon')
        elif n == 26:
            plt.title('icosikaihexagon or hexacosagon')
        elif n == 27:
            plt.title('icosikaiheptagon or heptacosagon')
        elif n == 28:
            plt.title('icosikaioctagon or octacosagon')
        elif n == 29:
            plt.title('icosikaienneagon, enneacosagon or nonacosagon')
        elif n == 30:
            plt.title('triacontagon')
        elif n == 31:
            plt.title('triacontakaihenagon or henitriacontagon')
        elif n == 32:
            plt.title('triacontakaidigon or dotriacontagon')
        elif n == 40:
            plt.title('tetracontagon')
        elif n == 50:
            plt.title('pentacontagon')
        elif n == 60:
            plt.title('hexacontagon')
        elif n == 70:
            plt.title('heptacontagon')
        elif n == 80:
            plt.title('octacontagon')
        elif n == 90:
            plt.title('enneacontagon or nonacontagon')
        elif n == 100:
            plt.title('hectagon')
        elif n == 1000:
            plt.title('chiliagon')
        elif n == 10000:
            plt.title('myriagon')
        elif n == 1000000:
            plt.title('hecatommyriagon or hekatommyriagon')
        else:
            plt.title("This is a polygon with "+n+" numbers of sides")
        plt.plot(b ,a ,marker=marker ,linestyle=linestyle.lower()  ,color=color)
        plt.axis('equal')
        plt.show()
        return()
class semi_Circle():
    def plot(radius ,marker='P' ,linestyle='solid' ,color='m'):
        theta =linspace(0 ,1*pi ,1000)
        a = radius * cos(  theta  )
        b = radius * sin(  theta  )
        plt.title('Semi-Circle')
        plt.plot(a ,b ,(-radius ,radius) ,(0 ,0) ,linestyle=linestyle.lower() ,color=color)
        x =0
        y =0
        plt.plot(x ,y ,marker=marker)
        plt.axis('image')
        plt.show()
        return()
    def area(radius):
        area =(pi*( (radius)**2))/2
        return float(area)
    def circumference(radius):
        peri =(pi*radius)+(2*radius)
        return float(peri)
    def diameter(radius):
        dia = radius * 2
        return float(dia)
class circle():
    def plot(radius , marker='P' , linestyle='solid' ,color='m'):
        theta = linspace(0 ,2*pi ,1000)
        a = radius * cos(  theta  )
        b = radius * sin(  theta  )
        plt.title('Circle')
        plt.plot(a ,b ,(-radius ,0) ,(0 ,0) ,linestyle=linestyle.lower() ,color=color)
        x =0
        y =0
        plt.plot(x  ,y ,marker=marker)
        plt.axis('image')
        plt.show()
        return()
    def area(radius):
        area = pi * (radius ** 2)
        return float(area)
    def circumference(radius):
        peri = 2 * pi * radius
        return float(peri)
    def diameter(radius):
        dia = radius * 2
        return float(dia)
class star():
    def plot(radius , marker='none' , linestyle='solid' ,color='m'):
        theta = linspace(0 ,2*pi ,6)
        a = radius * cos(  theta  )
        b = radius * sin(  theta  )
        plt.title('Star')
        plt.plot((b[0] ,b[2] ,b[4] ,b[1] ,b[3] ,b[0]) ,(a[0] ,a[2] ,a[4] ,a[1] ,a[3] ,a[0]) ,color=color ,linestyle=linestyle.lower() , marker=marker)
        plt.axis('image')
        plt.show()
        return()