"""
Regan Collins
Dandy Hacks 2021
"""

from graphics import (GraphWin, Point, Circle, Oval, Line, Rectangle, Polygon,
                      Text)


def main():
    win = GraphWin("Baymax", 600, 600)

# Greeting
    box = Rectangle(Point(210, 140), Point(540, 247))
    box.draw(win)
    box.setFill("royalblue")
    greeting = Text(Point(375, 190), "Happy DandyHacks 2021! \n\
                    \n I hope your day is as wonderful as you!")
    greeting.draw(win)
    greeting.setTextColor("gold")
 
# Arms
    a1 = Point(35, 390)
    a2 = Point(95, 510)
    left_arm = Oval(a1, a2)
    left_arm.draw(win)
    left_arm.setFill("white")

    right_arm = left_arm.clone()
    right_arm.move(120, 0)
    right_arm.draw(win)

# Feet
    f1 = Point(70, 490)
    f2 = Point(124, 575)
    left_foot = Oval(f1, f2)
    left_foot.draw(win)
    left_foot.setFill("white")

    right_foot = left_foot.clone()
    right_foot.move(55, 0)
    right_foot.draw(win)

# Body
    b1 = Point(50, 360)
    b2 = Point(200, 550)
    body = Oval(b1, b2)
    body.draw(win)
    body.setFill("white")

# Head
    h1 = Point(60, 300)
    h2 = Point(190, 380)
    head = Oval(h1, h2)
    head.draw(win)
    head.setFill("white")

    center_eye = Point(90, 340)
    left_eye = Circle(center_eye, 10)
    left_eye.draw(win)
    left_eye.setFill("black")

    right_eye = left_eye.clone()
    right_eye.move(73, 0)
    right_eye.draw(win)

    mouth = Line(Point(90, 340), Point(163, 340))
    mouth.setWidth(2)
    mouth.draw(win)

# Heart
    center = Point(153, 415)
    left_circle = Circle(center, 7)
    left_circle.draw(win)
    left_circle.setFill("red")
    left_circle.setOutline("red")

    right_circle = left_circle.clone()
    right_circle.move(13, 0)
    right_circle.draw(win)

    triangle = Polygon(Point(147, 418),
                       Point(160, 433),
                       Point(173, 418))
    triangle.draw(win)
    triangle.setFill("red")
    triangle.setOutline("red")


if __name__ == "__main__":
    main()
