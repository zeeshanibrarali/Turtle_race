import random
import turtle
import turtle as t

# src.listen()

#
# def forwards():
#     tim.forward(10)
#
#
# def backwards():
#     tim.backward(10)
#
#
# def clockwise():
#     tim.right(10)
#
#
# def counter_clockwise():
#     tim.left(10)
#
#
# def clear():
#     tim.clear()
#     tim.reset()
#
#
# src.onkey(fun=forwards, key='w')
# src.onkey(fun=backwards, key='s')
# src.onkey(fun=counter_clockwise, key='a')
# src.onkey(fun=clockwise, key='d')
# src.onkey(fun=clear, key='c')


src = t.Screen()
src.setup(width=500, height=400)
bet = src.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color : ')
col = ['red', 'purple', 'yellow', 'orange', 'blue', 'green']
y = -100
all_turtles = []
for i in range(6):
    name = f'tim_'+str(i)
    name = t.Turtle(shape='turtle')
    name.color(col[i])
    name.penup()
    name.goto(x=-230, y=y)
    all_turtles.append(name)
    y += 50


if bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        dis = random.randint(0, 10)
        turtle.forward(dis)
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f'You\'ve won, The {winning_color} turtle is the winner!')
            else:
                print(f'You\'ve lost, The {winning_color} turtle is the winner!')
            is_race_on = False


src.exitonclick()


