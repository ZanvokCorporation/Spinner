from turtle import *
state = {'turn': 0}
val = float(input("Enter speed (in number): "))
def spinner():
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(120, 'red')
    back(100)
    right(120)
    forward(100)
    dot(120, 'purple')
    back(100)
    right(120)
    forward(100)
    dot(120, 'blue')
    back(100)
    right(120)
    update()
def animate():
    if state['turn']>0:
        state['turn']-=1

    spinner()
    ontimer(animate, 20)
def flick():
    state['turn']+=val

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'Right')
onkey(flick, 'Left')
onkey(flick, 'Up')
onkey(flick, 'Down')
onkey(flick, 'space')
onkey(flick, 'w')
onkey(flick, 'a')
onkey(flick, 's')
onkey(flick, 'd')
listen()
animate()
done()
