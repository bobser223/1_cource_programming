import turtle


def vecSum(a_v1, a_v2):
    return (a_v1[0] + a_v2[0], a_v1[1] + a_v2[1])


position = (0, 0)

v1 = (5, 0)
v2 = (0, 20)
v3 = (-10, 0)
v4 = (0, -10)
#up
#pos

v5 = (-5, 0)
#up
#pos
v6 = (5, 0)
v7 = (0, -20)
v8 = (-10, 0)
v9 = (0, 10)

vv1 = vecSum(v1, position)
vv2 = vecSum(v2, vv1)
vv3 = vecSum(v3, vv2)
vv4 = vecSum(v4, vv3)

vv5 = vecSum(v5, position)

vv6 = vecSum(v6, position)
vv7 = vecSum(v7, vv6)
vv8 = vecSum(v8, vv7)
vv9 = vecSum(v9, vv8)

turtle.speed(1)
turtle.penup()
turtle.goto(position)
turtle.pendown()
turtle.goto(vv1)
turtle.goto(vv2)
turtle.goto(*vv3)
turtle.goto(*vv4)

turtle.penup()
turtle.goto(position)
turtle.pendown()

turtle.goto(*vv5)

turtle.penup()
turtle.goto(position)
turtle.pendown()

turtle.goto(*vv6)
turtle.goto(*vv7)
turtle.goto(*vv8)
turtle.goto(*vv9)
turtle.mainloop()