import turtle


def vecSum(a_v1, a_v2):
    return (a_v1[0] + a_v2[0], a_v1[1] + a_v2[1])


position = (0, 0)

v1 = (-5, 0)
v2 = (0, 20)
#up pos
v3 = (5, 0)
v4 = (0, 20)
v5 = (0, -40)


vv1 = vecSum(v1, position)
vv2 = vecSum(v2, vv1)

vv3 = vecSum(v3, position)
vv4 = vecSum(v4, vv3)
vv5 = vecSum(v5, vv4)

turtle.penup()
turtle.goto(position)
turtle.pendown()

turtle.goto(vv1)
turtle.goto(vv2)

turtle.penup()
turtle.goto(position)
turtle.pendown()

turtle.goto(vv3)
turtle.goto(vv4)
turtle.goto(vv5)
turtle.mainloop()