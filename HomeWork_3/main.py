from Triangle import Triangle
import turtle


if __name__ == "__main__":
    turtle.speed(0)
    triangle = Triangle(100, 100, 100, 0)
    triangle.set_scale(3, 3)
    triangle.set_pivot(*triangle.get_incenter())
    for degree in range(0, 366, 6):
        triangle.set_rotation_degree(degree)
        triangle.draw()

    turtle.clear()

    triangle.set_pivot(*triangle.get_centroid())
    scale = 1
    while scale < 8:
        triangle.set_scale(scale, scale)
        triangle.draw()
        scale += 1

    turtle.mainloop()