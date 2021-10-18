import turtle
import math

font_height, font_width = (50, 30)

def v(turtle, inverted=False):
	turtle.fd(math.sqrt(font_height**2 + (font_width/2)**2))
	if inverted == True:
		turtle.rt(150)
	else:
		turtle.lt(150
	)
	turtle.fd(math.sqrt(font_height**2 + (font_width/2)**2))


def d_move(turtle, direction, pen_down = True):
	turtle.seth(["right", "up", "left", "down"].index(direction) * 90)
	if pen_down == True:
		turtle.pendown()
	else:
		turtle.penup()
	if direction in ["left", "right"]:
		turtle.fd(font_width)
	elif direction in ["up", "down"]:
		turtle.fd(font_height)

def d1_then_d2(turtle, d1, d2, p1down=True, p2down=True):
	d_move(turtle, d1, p1down)
	d_move(turtle, d2, p2down)

def right_then_down(turtle, p1down=True, p2down=True):
	if p1down == True:
		turtle.pendown()
	else:
		turtle.penup()
	turtle.fd(font_width)
	turtle.rt(90)
	if p2down == True:
		turtle.pendown()
	else:
		turtle.penup()
	turtle.fd(font_height)

def top_p(turtle):
	# make this dynamic in future
	turtle.fd(font_width - font_height / 4)
	turtle.circle(-font_height / 4, 180)
	turtle.fd(font_width - font_height / 4)
	turtle.rt(90)
	turtle.fd(font_height/2)
	turtle.bk(font_height/2)

def cap_c(turtle):
	turtle.fd(font_width)
	turtle.lt(90)
	turtle.bk(font_width / 2)
	turtle.pendown()
	turtle.circle(font_width / 2, 180)
	turtle.fd(font_height - font_width)
	turtle.circle(font_width / 2, 180)

def cap_ef(turtle, letter):
	if letter == "E":
		d1_then_d2(turtle, "down", "right")
	else:
		d1_then_d2(turtle, "down", "right", True, False)
	turtle.lt(90)
	turtle.penup()
	turtle.fd(font_height / 2)
	d_move(turtle, "left")
	turtle.rt(90)
	turtle.fd(font_height / 2)
	d_move(turtle, "right")
	turtle.penup()

def big_curve(turtle):
	turtle.fd(font_width - font_height / 2)
	turtle.circle(-font_height / 2, 180)
	turtle.fd(font_width - font_height / 2)
def cap_o(turtle):
	# starts from top right
	cap_c(turtle)
	turtle.fd(font_height - font_width)
def letter(turtle, string):
	for letter in string:
		if letter == "A":
			turtle.rt(90)
			turtle.fd(font_height)
			turtle.lt(165)
			turtle.pendown()
			v(turtle, True)
			turtle.bk(math.sqrt(font_height**2 + (font_width/2)**2)/2)
			turtle.rt(105)
			turtle.fd(font_width/2)
			turtle.penup()
			turtle.bk(font_width/2)
			turtle.lt(105)
			turtle.fd(math.sqrt(font_height**2 + (font_width/2)**2)/2)
			turtle.lt(165)
			turtle.fd(font_height)
			turtle.rt(90)
		turtle.fd(font_width / 5)
		if letter == "B":
			turtle.pendown()
			top_p(turtle)
			turtle.rt(90)
			top_p(turtle)
			d1_then_d2(turtle, "up", "right", True, False)
		if letter == "C":
			cap_c(turtle)
			turtle.penup()
			turtle.fd(font_height - font_width / 2)
			turtle.rt(90)
		if letter == "D":
			turtle.pendown()
			big_curve(turtle)
			turtle.rt(90)
			d1_then_d2(turtle, "up", "right", True, False)
		if letter == "E":
			cap_ef(turtle, "E")
		if letter == "F":
			cap_ef(turtle, "F")
		if letter == "G":
			cap_c(turtle)
			turtle.lt(90)
			turtle.fd(font_width / 2)
			turtle.bk(font_width / 2)
			turtle.rt(90)
			turtle.penup()
			turtle.fd(font_height - font_width / 2)
			turtle.rt(90)
		if letter == "H":
			right_then_down(turtle, False, True)
			turtle.bk(font_height / 2)
			turtle.rt(90)
			turtle.fd(font_width)
			turtle.rt(90)
			turtle.bk(font_height / 2)
			d1_then_d2(turtle, "up", "right", True, False)
		if letter == "I":
			d1_then_d2(turtle, "right", "down", True, False)
			turtle.rt(90)
			turtle.pendown()
			turtle.fd(font_width / 2)
			turtle.rt(90)
			turtle.fd(font_height)
			turtle.bk(font_height)
			turtle.lt(90)
			turtle.fd(font_width / 2)
			d1_then_d2(turtle, "up", "right", False, False)
		if letter == "J":
			turtle.pendown()
			turtle.fd(font_width / 2)
			turtle.rt(90)
			turtle.fd(font_height - font_width / 2)
			turtle.circle(-font_width / 4, 180)
			turtle.penup()
			turtle.fd(font_height - font_width / 2)
			d_move(turtle, "right")
			turtle.penup()
		if letter == "K":
			d_move(turtle, "down")
			turtle.bk(font_height / 2)
			turtle.left(30)
			# temp
			turtle.fd(math.sqrt((font_height / 2)**2+font_height / 2 / math.sqrt(3)))
			turtle.bk(math.sqrt((font_height / 2)**2+font_height / 2 / math.sqrt(3)))
			turtle.left(120)
			turtle.fd(math.sqrt((font_height / 2)**2+font_height / 2 / math.sqrt(3)))
			turtle.bk(math.sqrt((font_height / 2)**2+font_height / 2 / math.sqrt(3)))
			turtle.left(30)
			turtle.fd(font_height / 2)
			d_move(turtle, "right", False)
		if letter == "L":
			d1_then_d2(turtle, "down", "right")
			d_move(turtle, "up", False)
			turtle.rt(90)
		if letter == "O":
			cap_o(turtle)
			turtle.penup()
			turtle.fd(font_width / 2)
			turtle.rt(90)
		if letter == "P":
			turtle.pendown()
			top_p(turtle)
			turtle.bk(font_height / 2)
			d1_then_d2(turtle, "up", "right", False, False)
		turtle.fd(font_width/5)


screen = turtle.getscreen()
turtle.title("WOAH THIS IS HUGE")
franklin = turtle.Turtle()
franklin.penup()
for i in range(10):
	franklin.goto(-300, 300 - 60 * i)
	letter(franklin, "AAAAAAAAAA")
franklin.pendown()
screen.exitonclick()