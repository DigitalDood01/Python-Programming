import turtle
roma = turtle.Turtle()
roma.color("blue")
roma.shape("turtle")     #assigns shape to the cursor
roma.up()                #line is not drawn
distance = 50
angle = 36
for _ in range(15):
    roma.stamp()        #at the current position only the foot print is imprinted
    roma.forward(distance)
    roma.left(angle)
    angle = angle - 2
    distance = distance + 1

