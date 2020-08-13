print("Input string")
option=input()

def Circle():
    print('Enter Radius of Circle')
    radius=int(input())
    A=3.14*radius**2
    print("Area of circle: ",A)
def Rectangle():
    print("Enter length")
    length=int(input())
    print("Enter wide")
    wide=int(input())
    A= length *  wide
    print("Area of Rectangle: ",A)
def Square():
    print("Enter value of a")
    a=int(input())
    A=a**2
    print("Area of Square: ",A)
def Triangle():
    print('Enter height')
    height=int(input())
    print("Enter base")
    base=int(input())
    A=(height*base) /2
    print("Area of Triangle: ",A)
def Trapezium():
    print("Enter a")
    a=int(input())
    print("Enter b")
    b=int(input())
    A=(a+b)/2
    print("Area of Trapezium: ",A)
if(option=='Circle'):
    Circle()
elif(option=='Rectangle'):
    Rectangle()
elif(option=='Square'):
    Square()
elif(option=='Triangle'):
    Triangle()
elif(option=='Trapezium'):
    Trapezium()
else:
    print("Wrong Selection! Correct selection is Circle,Rectangle,Square,Triangle,Trapezium")              

