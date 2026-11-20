import turtle
import colorsys
import math
import random

random.seed(7)
TILT = 0.45

screen = turtle.Screen()
screen.setup(780, 480)
screen.bgcolor("#03030b")
screen.colormode(1.0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

def glow(h, v=1.0):
    return colorsys.hsv_to_rgb(h % 1, 0.7, v)

def place(x, y):
    y *= 0.55
    c, s = math.cos(TILT), math.sin(TILT)
    t.goto(x * c - y * s, x*s+y*c)

def stars():
    for _ in range(140):
        x = random.randint(-385, 385)
        y = random.randint(-235, 235)
        t.goto(x,y)
        t.dot(random.randint(1,3), "white")

def dust():
    for _ in range(700):
        r = random.gauss(0,120)
        a = random.uniform(0,6.283)
        place(r * math.cos(a), r * math.sin(a))
        t.dot(random.randint(2,4), glow(0.7, 0.3))

def arms(count):
    for i in range(count):
        for k in range(4):
            d = i / count
            a = k * math.pi / 2 + d * 5.5
            r = 10 + d * 290
            s = 4 + d * 26
            x = r * math.cos(a) + random.gauss(0, s)
            y = r * math.sin(a) + random.gauss(0, s)
            place(x,y)
            hue = 0.13 - d * 0.55
            v = random.uniform(0.6, 1)
            size = random.randint(2, 4)
            t.dot(size, glow(hue, v))

def core():
    for _ in range(260):
        r = random.gauss(0, 26)
        a = random.uniform(0, 6.283)
        place(r * math.cos(a), r * math.sin(a))
        t.dot(random.randint(2, 5), glow(0.12))

def sparkle():
    for _ in range(40):
        r = random.gauss(0, 150)
        a = random.uniform(0, 6.283)
        place(r * math.cos(a), r * math.sin(a))
        t.dot(random.randint(5, 8), "white")

stars()
dust()
arms(900)
core()
sparkle()
t.goto(0,0)
t.dot(26, "#fff3c4")
turtle.done()