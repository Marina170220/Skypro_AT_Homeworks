from turtle import *

# Настройка 
t = Turtle()
t.speed(0)
t.pensize(3)
t.color("black")

# Рисуем голову кошки
t.fillcolor("gray")
t.begin_fill()
t.circle(100)
t.end_fill()

# Рисуем глаза
t.penup()
t.goto(-35, 120)
t.pendown()
t.color("black")
t.dot(30)
t.penup()
t.goto(35, 120)
t.pendown()
t.dot(30)

# Рисуем правое ухо
t.penup()
t.goto(30, 190)
t.pendown()
t.setheading(240)
t.begin_fill()
t.circle(50, -60)
t.end_fill()

t.penup()
t.goto(85, 150)
t.pendown()
t.setheading(70)
t.begin_fill()
t.circle(70, 60)
t.end_fill()

# Рисуем левое ухо
t.penup()
t.goto(-80, 210)
t.pendown()
t.setheading(-130)
t.begin_fill()
t.circle(70, 60)
t.end_fill()

t.penup()
t.goto(-85, 210)
t.pendown()
t.setheading(190)
t.begin_fill()
t.circle(50, -60)
t.end_fill()

# Рисуем нос
t.penup()
t.goto(0, 80)
t.pendown()
t.dot(20)

# Рисуем рот
t.penup()
t.goto(0, 70)
t.pendown()
t.setheading(-90)
t.circle(10, 90)

t.penup()
t.goto(0, 70)
t.pendown()
t.setheading(-90)
t.circle(-10, 90)


# Необходимо, чтобы окно не закрывалось само, а только по клику
t.screen.exitonclick()
t.screen.mainloop()