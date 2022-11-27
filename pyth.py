import turtle 
def Square():
    turtle.title(dic.get(option))
    ob = turtle.Turtle()
    tk = turtle.Screen()
    ob.hideturtle()
    tk.bgcolor("light green")
    for _ in range(4):
        ob.forward(100)
        ob.left(90)
   
    turtle.done()
def Rectangle():
    turtle.title(dic.get(option))
    ob = turtle.Turtle()
    tk = turtle.Screen()
    ob.hideturtle()
    tk.bgcolor("light green")
    
    x = int(input("Enter the length of the Rectangle: "))
    y = int(input("Enter the width of the Rectangle: "))
    for _ in range(2):
        ob.forward(x) 
        ob.left(90) 
        ob.forward(y) 
        ob.left(90) 
    turtle.done()
    
   
print("**WELCOME TO GEOMETRIC SHAPES**")
print()
print()
print("SELECT THE OPTION YOU WANT :-\n")

def Options():
	print("[1] SQUARE\t [2] RECTANGLE\n")
	
	print("[3] TRIANGLE\t [4] RI;GHT TRIANGLE\n")
	
	print("[5] ELLIPSE\t [6] PARALLELOGRAM\n")
Options()
dic = {"1" :"SQUARE", "2": "RECTANGLE","3" : "TRIANGLE", "4" : "RIGHT TRIANGLE", "5" : "ELLIPSE", "6" : "PARALLELOGRAM"}
option = input()
while(dic.get(option)==None):
	print("ENTER VALID INPUT......")
	option = input()
if(option== "1"):
	Square()
elif(option =="2"):
	Rectangle()
elif(option == "3"):
	Triangle()
elif(option == "4"):
	RightTriangle()
elif(option == "5"):
	print("hi")
elif(option == "6"):
	Parallelogram()
else:
	print(-1)
