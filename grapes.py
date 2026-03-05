import turtle

t = turtle.Turtle()
t.fillcolor("purple")

# ลูกที่ 1
t.begin_fill()
t.circle(20)
t.end_fill()

# ลูกที่ 2
t.penup()
t.forward(40)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

# ลูกที่ 3
t.penup()
t.forward(40)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

# ลงแถวที่ 2
t.penup()
t.backward(60)
t.right(90)
t.forward(40)
t.left(90)
t.pendown()

# ลูกที่ 4
t.begin_fill()
t.circle(20)
t.end_fill()

# ลูกที่ 5
t.penup()
t.forward(40)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

# ลูกที่ 6
t.penup()
t.backward(20)
t.right(90)
t.forward(40)
t.left(90)
t.pendown()

t.begin_fill()
t.circle(20)
t.end_fill()

turtle.done()