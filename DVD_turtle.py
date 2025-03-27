import turtle

def if_hit_wall(t:turtle.Turtle,s:turtle.Screen):
    screen_width = s.window_width()
    screen_height = s.window_height()

    print(t.xcor(), t.ycor())
    if t.xcor() >= ((screen_width / 2) - (t.turtlesize()[0] / 2)):
        print("Hit Right")
    if t.xcor() <= -((screen_width / 2) - (t.turtlesize()[0] / 2)):
        print("Hit Left")
    if t.ycor() >= ((screen_height / 2) - (t.turtlesize()[0] / 2)):
        print("Hit Up")
    if t.ycor() >= -((screen_height / 2) - (t.turtlesize()[0] / 2)):
        print("Hit Down")



t = turtle.Turtle() # 🤷
s = turtle.Screen()
image = "larry.gif"
s.addshape(image)
print(s.getshapes())
t.shape(image)
t.turtlesize(125,123,1)
s.setup(1280, 720)
s.bgcolor("#000000")
t.speed(10)
t.penup()
t.setx(0)
t.sety(0)

for i in range(1):
    print(t.turtlesize()[0],t.turtlesize()[1])
    t.forward(((s.window_width() / 2) - (125/2)))
    if_hit_wall(t, s)
    t.setx(0)
    t.sety(0)

    t.backward(((s.window_width() / 2) - (125 / 2)))
    if_hit_wall(t, s)
    t.setx(0)
    t.sety(0)

    t.left(90)

    t.forward(((s.window_height() / 2) - (123 / 2)))
    if_hit_wall(t, s)
    t.setx(0)
    t.sety(0)

    t.backward(((s.window_height() / 2) - (123 / 2)))
    if_hit_wall(t, s)
    t.setx(0)
    t.sety(0)

s.exitonclick()