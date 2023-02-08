import pickle
import turtle
import random

def draw_bag():
    t.shape('turtle')
    t.pen(pencolor='green', pensize=6)
    t.penup()
    t.goto(-35, 35)
    t.pendown()
    t.right(90)
    t.forward(70)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(70)


def escaped(position):
    x = int(position[0])
    y = int(position[1])
    return x < -35 or x > 35 or y < -35 or y > 35


def store_position_data(t, L):
    position = t.position()
    L.append([position[0], position[1], escaped(position)])
    return L


def draw_line():
    angle = 0
    step = 5
    t = turtle.Turtle()
    while not escaped(t.position()):
        t.pen(pencolor='red', pensize=4)
        t.pendown()
        t.left(angle)
        t.forward(step)


def draw_sequence_of_square():
    t = turtle.Turtle()
    L = []
    t.penup()
    i = 1
    t.pen(pencolor='white', pensize=4)
    t.pendown()
    while not escaped(t.position()):

        for i in range(4):
            i += 1
            t.left(-90)
            t.forward(i*2)
            L.append(store_position_data(t, L))
        print(t.position())
    return L


def draw_squares_until_escaped():
    L = draw_sequence_of_square()
    with open("data_square", "wb") as f:
        pickle.dump(L, f)


def draw_triangles(number):
    t = turtle.Turtle()
    for i in range(1, number):
        t.forward(i*10)
        t.right(120)


def draw_spirals_until_escaped():
    t = turtle.Turtle()
    t.penup()
    t.left(random.randint(0, 360))
    t.pen(pencolor='white', pensize=4)

    t.pendown()
    i = 0
    turn = 360/random.randint(1, 10)
    L = []
    store_position_data(t,L)
    while not escaped(t.position()):
        i += 1
        t.forward(i*5)
        t.right(turn)
        store_position_data(t,L)
    return L


def draw_random_spirangles():
    L = []
    for i in range (10):
        L.extend(draw_spirals_until_escaped())
    with open("data_rand", "wb") as f:
        pickle.dump(L, f)


if __name__ == '__main__':
    t = turtle.Turtle()
    turtle.setworldcoordinates(-70., -70., 70., 70.)
    turtle.bgcolor("black")
    draw_bag()
    # draw_line()
    # draw_squares_until_escaped()
    draw_random_spirangles()
    # draw_spirals_until_escaped()
    turtle.mainloop()
