import turtle as t
my_wn = t.Screen()
my_wn.bgcolor("light blue")
my_wn.title("turtle")
my_pen = t.Turtle()
my_pen.color("green")
size = 0
while True: #iterate loop
    for i in range(4):
        my_pen.fd(size + 1)
        my_pen.left(90)
        size = size-5
    size = size + 1