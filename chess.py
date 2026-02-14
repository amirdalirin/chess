import turtle 

turtle.speed(0)

def chess_board():
    chess_board_lins(-200,200,-200,200)
    
def chess_board_lins(startx,endx,starty,endy):
    turtle.penup()
    turtle.goto(startx,starty)
    turtle.pendown()
    
    for i in range(4):
        turtle.fd(400)
        turtle.left(90)
    
    inside()

def inside():
    for  u in range(8):
        turtle.left(90)
        turtle.fd(400)
        turtle.bk(400)
        turtle.right(90)
        turtle.fd(50)
    turtle.right(180)

    for k in range(8):   
        turtle.fd(400)
        turtle.bk(400)
        turtle.right(90)
        turtle.fd(50)
        turtle.left(90)

def Chessـpiece():
     x = -175
     for i in range(8):
          w_pawn(x, -125)
          x = x + 50
def w_pawn(x, y):
        pawn = turtle.Turtle()
        pawn.penup()
        pawn.goto(x, y)
        pawn.pendown()
        pawn.write('wp')
        pawn.hideturtle()




Chessـpiece()
chess_board()
turtle.done()
