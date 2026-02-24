import turtle

s = turtle.Screen()
s.title("chess")
turtle.speed(0)

#register shape of peaces
s.register_shape('king',  ((-5,-8),(5,-8),(5,-3),(4,-2),(4,0),(2,1),(2,6),(4,6),(4,7),(2,7),(2,9),(-2,9),(-2,7),(-4,7),(-4,6),(-2,6),(-2,1),(-4,0),(-4,-2),(-5,-3),(-5,-8)))
s.register_shape('queen', ((-5,-8),(5,-8),(5,-3),(4,-2),(4,0),(2,1),(2,5),(3,6),(4,5),(5,6),(5,7),(3,8),(1,7),(0,8),(-1,7),(-3,8),(-5,7),(-5,6),(-4,5),(-3,6),(-2,5),(-2,1),(-4,0),(-4,-2),(-5,-3),(-5,-8)))
s.register_shape('bishop',((0,7),(1,6),(2,5),(1,4),(2,3),(1,2),(3,1),(4,0),(3,-1),(3,-3),(4,-4),(4,-8),(-4,-8),(-4,-4),(-3,-3),(-3,-1),(-4,0),(-3,1),(-1,2),(-2,3),(-1,4),(-2,5),(-1,6),(0,7)))
s.register_shape('knight',((-5,-8),(5,-8),(5,-3),(1,-3),(4,1),(1,5),(-2,4),(-2,0),(-5,0),(-5,-8)))
s.register_shape('rook', ((-4,4),(4,4),(4,2),(3,1),(3,-2),(5,-6),(5,-8),(-5,-8),(-5,-6),(-3,-2),(-3,1),(-4,2),(-4,4)))
s.register_shape('pawn',((0,6),(1,6),(2,5),(2,4),(2,2),(1,1),(2,0),(2,-2),(3,-3),(4,-6),(3,-7),(0,-7),(-3,-7),(-4,-6),(-3,-3),(-2,-2),(-2,0),(-1,1),(-2,2),(-2,4),(-2,5),(-1,6),(0,6)))

# init setting
backgroundcolor = ""

#chess board notation dic 
notation = {
        "a1":[-175, -175],"a2":[-175, -125],"a3":[-175, -75],"a4":[-175, -25],"a5":[-175, 25],"a6":[-175, 75],"a7":[-175, 125],"a8":[-175, 175],
        "b1":[-125,-175],"b2":[-125, -125],"b3":[-125, -75],"b4":[-125, -25],"b5":[-125, 25],"b6":[-125, 75],"b7":[-125, 125],"b8":[-125, 175],
        "c1":[-75, -175],"c2":[-75, -125],"c3":[-75, -75],"c4":[-75, -25],"c5":[-75, 25],"c6":[-75, 75],"c7":[-75, 125],"c8":[-75, 175],
        "d1":[-25, -175],"d2":[-25, -125],"d3":[-25, 75],"d4":[-25, -25],"d5":[-25, 25],"d6":[-25, 75],"d7":[-25,125],"d8":[-25, 175],
        "e1":[25, -175],"e2":[25, -125],"e3":[25, -75],"e4":[25, -25],"e5":[25, 25],"e6":[25, 75],"e7":[25, 125],"e8":[25, 175],
        "f1":[75, -175],"f2":[75, -125],"f3":[75, -75],"f4":[75, -25],"f5":[75, 25],"f6":[75, 75],"f7":[75, 125],"f8":[75, 175],
        "g1":[125, -175],"g2":[125, -125],"g3":[125, -75],"g4":[125, -25],"g5":[125, 25],"g6":[125, 75],"g7":[125, 125],"g8":[125, 175],
        "h1":[175, -175],"h2":[175, -125],"h3":[175, -75],"h4":[175, -25],"h5":[175, 25],"h6":[175, 75],"h7":[175, 125],"h8":[175, 175],
}


#chess board
def chess_board():
    chess_board_lins(-200,200,-200,200)
    gray_sq()
    
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

def gray_sq():
    y = -200
    x = -200
    g = turtle.Turtle()
    g.speed(0)
    for h in range(8):
      
        for k in range(4):
            g.penup()
            g.goto(x, y)
            g.pendown()
            g.color("gray")
            g.begin_fill()
            g.fd(50)
            g.left(90)
            g.fd(50)
            g.left(90)
            g.fd(50)
            g.left(90)
            g.fd(50)
            g.left(90)
            g.end_fill()
            x = x + 100
        y = y + 50 
        if h % 2 == 0 :
            x = -150
        else:
            x = -200
      
#
def peaces():
    pawn()
    king()

print(notation["a"+"1"])
alph = {'a','b','c','d','e','f','g','h'}

def pawn():
   
    for i in alph: 
        p = turtle.Turtle("pawn")
        p.penup()
        p.goto(notation[i+'2'])
        p.pendown()
        p.fd(1)
        p.left(90)
        
def king():
    k = turtle.Turtle("king") 
    k.penup()
    k.goto(notation['e1'])
    k.pendown()
    k.fd(1)
    k.left(90)

    




chess_board()
peaces()
turtle.done()