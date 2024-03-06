import turtle


def vecSum(a_v1, a_v2):
    return (a_v1[0] + a_v2[0], a_v1[1] + a_v2[1])


position = (300, 0)

v1 = (5, 0)
v2 = (0, 20)
v3 = (-10, 0)
v4 = (0, -10)
#up
#pos
v5 = (-5, 0)
v6 = (0, -20)
v7 = (10, 0)
v8 = (0, 10)

vv1 = vecSum(v1, position)
vv2 = vecSum(vv1, v2)
vv3 = vecSum(vv2, v3)
vv4 = vecSum(vv3, v4)

vv5 = vecSum(position, v5)
vv6 = vecSum(vv5, v6)
vv7 = vecSum(vv6, v7)
vv8 = vecSum(vv7, v8)

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
turtle.goto(*vv6)
turtle.goto(*vv7)
turtle.goto(*vv8)
turtle.mainloop()