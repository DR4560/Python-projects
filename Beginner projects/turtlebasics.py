import turtle as t
from random import random

#pen control drawings

import turtle as t
from random import random


for i in range(100):

    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)
    t.screen.mainloop()
    t.screen.title('Object-oriented turtle demo')
    t.screen.bgcolor("orange")

t = Turtle()
for i in range(100):

    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

t.screen.mainloop()

for spiral_steps in range(10):
    for a in ('green', 'pink'):
        t.color(a)
        t.forward(spiral_steps)
        t.right(50)

while True:
    t.forward(200)
    t.left(170)
    if abs(pos()) < 1:
        break