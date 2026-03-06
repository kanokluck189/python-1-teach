import turtle

t = turtle.Turtle()
t.speed(5)
t.fillcolor("purple")

# แถวบน (3 ลูก)
i = 0
while i < 3:
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    t.penup()
    t.forward(45)
    t.pendown()

    i += 1

# ไปแถวที่ 2
t.penup()
t.backward(67)
t.right(90)
t.forward(35)
t.left(90)
t.pendown()

# แถวกลาง (2 ลูก)
i = 0
while i < 2:
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    t.penup()
    t.backward(45)
    t.pendown()

    i += 1

# ไปแถวล่าง
t.penup()
t.forward(70)
t.right(90)
t.forward(35)
t.left(90)
t.pendown()

# ลูกสุดท้าย
t.begin_fill()
t.circle(20)
t.end_fill()

turtle.done()