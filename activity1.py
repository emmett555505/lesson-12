import turtle as t #importing library
t.Screen().bgcolor("green")
t.Screen().setup(300,400)
polygon = t.Turtle() #defined variable

num_sides = 6 #variable
side_lengths = 70
angle = 360.0 / num_sides
#iterate loop for total nubmer of sides
for i in range(num_sides):
    polygon.forward(side_lengths)
    polygon.right(angle)

t.done()