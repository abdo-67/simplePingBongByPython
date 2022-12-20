import turtle 
#bulding Screan
windo = turtle.Screen()
windo.title('game')
windo.bgcolor('black')
windo.setup(width=800 , height=600)
windo.tracer(0)

#bulding rackets and ball
racket0, racket1 , ball = turtle.Turtle(),turtle.Turtle(),turtle.Turtle()
racket0.color('red')
racket0.speed(0)
racket0.shape('square')
racket0.shapesize(stretch_wid=6 , stretch_len=1)
racket0.penup()
racket0.goto(380 ,0 )

# ball = turtle.Turtle()
ball.color('gray')
ball.speed(0)
ball.shape('circle')
ball.penup()
ball.goto(0 ,0 )

# racket1 = turtle.Turtle()
racket1.color('blue')
racket1.speed(0)
racket1.shape('square')
racket1.shapesize(stretch_wid=6 , stretch_len=1)
racket1.penup()
racket1.goto(-380 ,0 )

# movement rackets
    #racket0
def racket0Up():
    Y = racket0.ycor() 
    if Y >= 225 :
        exit()
    Y +=20
    racket0.sety(Y)

def racket0Down():
    Y = racket0.ycor()
    if Y <= -225 :
        exit()
    Y -=20
    racket0.sety(Y)
    #racket1
def racket1Up():
    Y = racket1.ycor()
    if Y >=225:
        exit()
    Y +=20 
    racket1.sety(Y)

def racket1Down():
    Y = racket1.ycor()
    if Y <= -225:
        exit()
    Y -=20 
    racket1.sety(Y)

windo.listen()
#racket0
windo.onkeypress(racket0Up,"Up")
windo.onkeypress(racket0Down , 'Down')
#racket1
windo.onkeypress(racket1Up , 'w')
windo.onkeypress(racket1Down , 's')

#ball , #this speed ball
# if ball was slow make this .5 or .6 or as you like 
ball_dx = .3 # dlta X
ball_dy = .3 # dlat y

#score
player1 = 0
player2 = 0
score1 = turtle
score1.color('white')
score1.hideturtle()
score1.penup()
score1.goto(-240, 230)
score1.write(f"Player2:{player2}|Player1:{player1}",move= False, font=('Courier', 30, 'bold'))


while True:   # while game
    
    windo.update()
    #move ball
    ball.setx(ball.xcor()+ ball_dx)
    ball.sety(ball.ycor()+ ball_dy)
    if racket0.ycor()+60 >= ball.ycor() >= racket0.ycor()-60 and racket0.xcor()-20 <= ball.xcor():
        ball.setx(360)
        ball_dx = - ball_dx
# i used '60' becuse i stretched rackets 6 <in line 14 and 29> , that mean the racket's heghit become 120 (6 *20)
# and useing '20' becuse wighth ball = 10 and wighth racket= 10
    if racket1.ycor() +60 >= ball.ycor() >= racket1.ycor()-60 and racket1.xcor()+20 >= ball.xcor():
            ball.setx(-360)
            ball_dx = - ball_dx
    #Up screan
    if ball.ycor() > 290:
        ball.sety(290)
        ball_dy = - ball_dy
    #Down screan
    if ball.ycor() < -290:
        ball.sety(-290)
        ball_dy = - ball_dy
    #Right
    if ball.xcor() > 390:
        score1.clear()
        player2 +=1
        score1.write(f"Player2:{player2} | Player1:{player1}",move= False, font=('Courier', 30, 'bold'))

        ball.goto(0,0)
        ball_dx = - ball_dx
        ball_dy = - ball_dy
    #left
    if ball.xcor() < -390:
        score1.clear()
        player1 +=1
        score1.write(f"Player2:{player2} | Player1:{player1}",move= False, font=('Courier', 30, 'bold'))

        ball.goto(0,0)
        ball_dx = - ball_dx
        ball_dy = - ball_dy
# turtle.done()