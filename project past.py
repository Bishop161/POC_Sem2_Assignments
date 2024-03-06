from tkinter import *
root = Tk()
W = "#ffffff"
G = "#6185f8"
R = "#ff3900"
S = "#ffa642"
B = "#000000"
y = "#fffeff"
n = "#00ffff"
l = "#004358"
t = "#008b8b"
v = "#c84c0c"
z = "#17b217"  #bowser green
x = "#ffaa60" # bowser skin
c = "#ffffff" # bowser white and luigi white
w = "#dc4278"
p = "#16052d"
k = "#000000"  # black
r = "#d62b18"  # mario's red
b = "#876f16"  # mario's brown, goomba brown
s = "#fa9644"  # mario's skin tone, goomba lite tan
d = "#6185f8"  # background
g = "#6185f8"  # background
gb = "#c84c0c" #goomba brown
ge = "#fcbcb0" #goomba eye
r = "#c41d0d"  # peach red
i = "#fffeff"  # peach white
o = "#f29900"  # peach crown and skin
pp = "#dc4278"  #lost levels peach pink
bg = "#17b217"  #bowser green
bs = "#ffaa60" # bowser skin
bw = "#ffffff" # bowser white and luigi white
lg = "#0c9300" #luigi green
ls = "#ea9e22" #luigi skin
lw = bw
fr = "#f73804" #fire red
fw = "#ffe1ab" #fire white
fs = "#ffa441" #fire skin
clear_color = "#4d2d44"  # purpley color
pixel_size = 20
small_mario = [
    [g, g, g, r, r, r, r, r, r, g, g, g, g, g, g, g],
    [g, g, r, r, r, r, r, r, r, r, r, r, g, g, g, g],
    [g, g, b, b, b, b, s, s, b, s, g, g, g, g, g, g],
    [g, b, b, s, b, s, s, s, b, s, s, s, g, g, g, g],
    [g, b, b, s, b, b, s, s, s, b, s, s, s, g, g, g],
    [g, b, b, b, s, s, s, s, b, b, b, b, g, g, g, g],
    [g, g, g, s, s, s, s, s, s, s, s, g, g, g, g, g],
    [g, g, b, b, b, r, b, b, b, g, g, g, g, g, g, g],
    [g, b, b, b, b, r, b, b, r, b, b, b, g, g, g, g],
    [b, b, b, b, b, r, r, r, r, b, b, b, b, g, g, g],
    [s, s, s, b, r, s, r, r, s, r, b, s, s, g, g, g],
    [s, s, s, s, r, r, r, r, r, r, s, s, s, g, g, g],
    [s, s, s, r, r, r, r, r, r, r, r, s, s, g, g, g],
    [g, g, r, r, r, r, s, r, r, r, r, g, g, g, g, g],
    [g, b, b, b, b, g, g, g, b, b, b, b, b, g, g, g],
    [b, b, b, b, b, g, g, g ,b, b, b, b, b, b, g, g],
]
gumba = [
    [d, d, d, d, d, d, v, v, v, v, d, d, d, d, d, d],
    [d, d, d, d, d, v, v, v, v, v, v, d, d, d, d, d],
    [d, d, d, d, v, v, v, v, v, v, v, v, d, d, d, d],
    [d, d, d, v, v, v, v, v, v, v, v, v, v, d, d, d],
    [d, d, v, k, k, v, v, v, v, v, v, k, k, v, d, d],
    [d, v, v, v, s, k, v, v, v, v, k, s, v, v, v, d],
    [d, v, v, v, s, k, k, k, k, k, k, s, v, v, v, d],
    [v, v, v, v, s, k, s, v, v, s, k, s, v, v, v, v],
    [v, v, v, v, s, s, s, v, v, s, s, s, v, v, v, v],
    [v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v],
    [d, v, v, v, v, s, s, s, s, s, s, v, v, v, v, d],
    [d, d, d, d, s, s, s, s, s, s, s, s, d, d, d, d],
    [d, d, d, d, s, s, s, s, s, s, s, s, k, k, d, d],
    [d, d, d, k, k, s, s, s, s, s, k, k, k, k, k, d],
    [d, d, d, k, k, k, s, s, s, k, k, k, k, k, k, d],
    [d, d, d, d, k, k, k, d, d, k, k, k, k, k, d, d],
]
big_mario = [
    [g, g, g, g, g, g, r, r, r, r, r, g, g, g, g, g],  # row 0
    [g, g, g, g, r, r, r, r, r, r, s, g, g, g, g, g],  # row 1
    [g, g, g, r, r, r, r, r, r, s, s, g, g, g, g, g],  # row 2
    [g, g, g, r, r, r, r, r, r, r, r, r, r, r, g, g],  # row 3
    [g, g, g, b, b, b, s, s, b, s, s, s, g, g, g, g],  # row 4
    [g, g, b, s, s, b, s, s, b, b, s, s, s, s, g, g],  # row 5
    [g, g, b, s, s, b, b, s, s, s, s, s, s, s, s, g],  # row 6
    [g, b, b, s, s, b, b, s, s, s, b, s, s, s, s, g],  # row 7
    [g, b, s, s, s, s, s, b, b, b, b, b, b, b, g, g],  # row 8
    [g, b, b, b, s, s, s, s, s, b, b, b, b, b, g, g],  # row 9
    [g, g, g, b, b, s, s, s, s, s, s, s, s, g, g, g],  # row 10
    [g, g, g, g, r, s, s, s, s, s, b, g, g, g, g, g],  # row 11
    [g, g, g, g, b, r, b, b, b, b, r, b, g, g, g, g],  # row 12
    [g, g, g, b, b, r, b, b, b, b, r, b, b, g, g, g],  # row 13
    [g, g, b, b, b, r, b, b, b, b, r, b, b, b, g, g],  # row 14
    [g, b, b, b, b, r, b, b, b, b, r, b, b, b, b, g],  # row 15
    [g, b, b, b, r, r, b, b, b, b, r, r, b, b, b, g],  # row 16
    [b, b, b, b, r, r, b, b, b, b, r, r, b, b, b, b],  # row 17
    [b, b, b, b, r, r, r, r, r, r, r, r, b, b, b, b],  # row 18
    [b, b, b, b, r, s, r, r, r, r, s, r, b, b, b, b],  # row 19
    [s, s, s, s, r, r, r, r, r, r, r, r, s, s, s, s],  # row 20
    [s, s, s, s, r, r, r, r, r, r, r, r, s, s, s, s],  # row 21
    [g, s, s, s, r, r, r, r, r, r, r, r, s, s, s, g],  # row 22
    [g, s, s, r, r, r, r, r, r, r, r, r, r, s, s, g],  # row 23
    [g, g, r, r, r, r, r, r, r, r, r, r, r, r, g, g],  # row 24
    [g, g, r, r, r, r, r, g, g, r, r, r, r, r, g, g],  # row 25
    [g, g, r, r, r, r, g, g, g, g, r, r, r, r, g, g],  # row 26
    [g, g, r, r, r, r, g, g, g, g, r, r, r, r, g, g],  # row 27
    [g, g, g, b, b, b, g, g, g, g, b, b, b, g, g, g],  # row 28
    [g, g, g, b, b, b, g, g, g, g, b, b, b, g, g, g],  # row 29
    [g, b, b, b, b, b, g, g, g, g, b, b, b, b, b, g],  # row 30
    [g, b, b, b, b, b, g, g, g, g, b, b, b, b, b, g],  # row 31
]
peach = [
    [p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p],  # row 1
    [p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p],  # row 2
    [p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p],  # row 3
    [p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p],  # row 4
    [p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p],  # row 5
    [p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p],  # row 6
    [p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p],  # row 7
    [p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p],  # row 8
    [p, p, p, o, p, o, o, p, o, p, p, p, p, p, p, p],  # row 9
    [p, p, p, o, o, o, o, o, o, p, p, p, p, p, p, p],  # row 10
    [p, p, r, r, r, r, r, r, r, r, r, p, p, p, p, p],  # row 11
    [p, r, r, r, r, r, r, r, r, r, r, r, p, p, p, p],  # row 12
    [p, p, r, r, r, o, k, o, r, r, r, r, p, p, p, p],  # row 13
    [p, p, p, r, o, o, k, o, o, r, o, r, p, p, p, p],  # row 14
    [p, p, o, o, o, o, o, o, o, r, o, r, p, p, p, p],  # row 15
    [p, p, p, o, o, o, o, o, o, o, o, r, r, p, p, p],  # row 16
    [p, p, o, r, r, r, o, o, o, o, o, r, r, p, p, p],  # row 17
    [p, p, o, r, r, o, o, o, o, r, r, r, r, p, p, p],  # row 18
    [p, p, p, o, o, o, o, o, o, r, r, r, r, p, p, p],  # row 19
    [p, p, p, r, r, i, o, o, r, i, r, r, r, p, p, p],  # row 20
    [p, p, r, r, i, o, o, i, i, i, i, r, r, p, p, p],  # row 21
    [p, p, r, o, i, i, i, i, o, o, i, r, r, p, p, p],  # row 22
    [p, o, o, o, o, o, o, o, o, o, i, r, r, p, p, p],  # row 23
    [p, p, o, o, o, o, o, o, o, i, r, r, r, p, p, p],  # row 24
    [p, p, p, p, r, r, i, i, i, i, r, r, p, p, p, p],  # row 25
    [p, p, p, i, i, i, i, i, i, i, i, i, i, p, p, p],  # row 26
    [p, p, i, i, i, i, i, i, i, i, i, i, i, p, p, p],  # row 27
    [p, p, i, i, i, i, i, i, i, i, i, i, i, p, p, p],  # row 28
    [p, i, i, i, i, r, r, r, r, r, r, i, i, i, i, p],  # row 29
    [p, r, r, r, r, r, r, r, r, r, r, r, r, r, r, p],  # row 30
    [p, r, r, r, r, r, i, i, i, i, r, r, r, r, r, p],  # row 31
    [i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, i],
]
Peach_ll_sprite = [
    [p, p, p, p, o, p, o, o, p, o, p, p, p, p, p, p],
    [p, p, p, p, o, o, o, o, o, o, p, p, p, p, p, p],
    [p, p, p, p, o, o, o, o, o, o, p, p, p, p, p, p],
    [p, p, p, r, r, r, r, r, r, r, r, p, p, p, p, p],
    [p, p, p, r, r, r, r, r, r, r, r, p, p, p, p, p],
    [p, p, r, r, r, r, r, r, r, r, r, r, p, p, p, p],
    [p, r, r, r, s, b, s, s, b, s, r, r, r, p, p, p],
    [p, r, r, r, s, b, s, s, b, s, r, r, r, p, p, p],
    [p, r, r, r, s, s, s, s, s, s, r, r, r, p, p, p],
    [r, r, r, r, s, s, r, r, s, s, r, r, r, r, p, p],
    [r, r, r, r, r, s, s, s, s, r, r, r, r, r, p, p],
    [r, r, w, w, w, r, w, w, r, w, w, w, r, r, p, p],
    [r, w, w, w, r, w, w, w, w, r, w, w, w, r, p, p],
    [p, s, s, w, r, s, s, s, s, r, w, s, s, p, p, p],
    [p, s, s, s, s, s, s, s, s, s, s, s, s, p, p, p],
    [p, p, s, s, s, r, w, w, r, s, s, s, p, p, p, p],
    [p, p, p, w, w, r, w, w, r, w, w, p, p, p, p, p],
    [p, p, w, w, w, r, w, w, r, w, w, w, p, p, p, p],
    [p, w, w, w, w, r, w, w, r, w, w, w, w, p, p, p],
    [p, w, w, w, r, r, w, w, r, r, w, w, w, p, p, p],
    [w, w, w, r, r, w, w, w, w, r, r, w, w, w, p, p],
    [r, r, r, r, w, w, w, w, w, w, r, r, r, r, p, p],
    [w, w, w, w, w, w, w, w, w, w, w, w, w, w, p, p],
    [w, w, w, w, w, w, w, w, w, w, w, w, w, w, p, p],
]
bowser = [
    [k, k, k, k, k, k, k, k, k, k, k, k, c, c, c, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],
    [k, k, k, k, k, k, k, k, z, z, c, c, c, x, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],
    [k, k, k, k, k, k, k, z, z, z, c, c, x, x, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],
    [k, k, k, k, k, c, c, z, z, z, z, x, x, z, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],
    [k, x, k, k, z, c, c, z, z, z, z, z, z, z, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],
    [x, k, x, z, z, c, c, z, z, z, z, z, z, z, z, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],
    [x, x, x, c, c, c, z, z, z, x, z, z, z, z, z, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],
    [x, x, x, x, c, z, z, z, x, x, x, z, z, z, z, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],
    [c, x, x, x, z, z, x, x, c, z, x, z, z, z, z, c, c, z, z, z, c, k, k, k, k, k, k, k, k, k, k, k],
    [k, c, k, x, x, x, x, z, z, z, x, z, z, z, z, c, c, z, z, c, c, x, z, k, k, k, k, k, k, k, k, k],
    [k, c, k, c, c, z, c, z, z, c, x, z, z, z, z, c, c, z, c, c, c, x, x, z, c, c, c, k, k, k, k, k],
    [k, k, k, k, c, k, k, k, z, x, x, z, z, z, c, c, c, z, z, c, x, x, z, z, c, c, x, k, k, k, k, k],
    [k, k, k, k, k, k, k, k, c, x, x, z, z, c, c, c, z, z, z, z, z, z, z, z, z, x, x, z, c, k, k, k],
    [k, k, k, k, k, k, k, k, x, x, z, z, c, c, c, z, z, z, z, z, z, z, z, z, z, z, z, z, c, k, k, k],
    [k, k, k, k, k, k, c, x, x, x, z, z, c, c, c, z, z, z, z, z, z, c, c, c, z, z, z, z, z, k, k, k],
    [k, k, k, k, k, k, k, x, x, k, k, z, z, c, c, c, c, c, c, z, z, c, c, x, z, z, z, c, c, c, k, k],
    [k, k, k, k, k, k, k, k, k, k, k, k, k, z, z, x, x, x, c, c, z, z, x, x, z, z, z, c, c, z, k, k],
    [k, k, k, k, k, k, k, k, k, x, x, x, k, k, c, k, x, x, x, c, c, z, z, z, z, z, z, z, x, x, k, k],
    [k, k, k, k, k, k, k, k, x, x, c, k, x, x, x, k, c, x, x, z, c, z, z, z, z, z, z, z, z, z, c, k],
    [k, k, k, k, k, k, k, k, x, x, k, k, x, x, x, x, k, k, z, z, c, z, z, z, c, c, c, z, z, z, x, c],
    [k, k, k, k, k, k, k, k, x, c, k, x, x, x, x, x, x, c, z, z, c, c, z, z, c, c, x, z, z, z, k, k],
    [k, k, k, k, k, k, k, k, x, k, k, x, x, x, x, x, z, z, z, z, c, c, z, z, z, x, x, z, z, c, c, k],
    [k, k, k, k, k, k, k, k, k, c, k, x, x, x, x, x, z, z, z, z, c, c, z, z, z, z, z, z, z, c, c, c],
    [k, k, k, k, k, k, k, k, k, k, k, c, x, x, x, k, z, z, z, z, z, c, z, z, z, z, c, c, z, x, x, k],
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, z, z, z, z, z, c, c, z, z, z, x, z, z, x, z, k],
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, z, z, z, z, z, c, c, c, z, z, z, z, z, z, k],
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, z, z, z, z, z, c, c, c, c, z, z, z, z, k],
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, x, z, z, z, z, z, z, c, c, c, c, c, c, c],
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, c, c, x, x, z, z, x, x, x, x, c, c, c, c, c],
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, c, c, c, x, x, x, x, x, x, x, x, x, x, c, c, k],
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, c, c, x, x, c, c, x, x, x, x, k, k],
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, c, c, c, x, c, c, c, x, x, x, x, x, k],
]
Toad = [
    [G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],#6
    [G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],#7
    [G, G, G, G, G, G, W, W, W, W, G, G, G, G, G, G],#8
    [G, G, G, G, W, W, W, W, W, W, W, W, G, G, G, G],#9
    [G, G, W, R, R, R, W, W, W, W, R, R, R, W, G, G],#10
    [G, W, W, R, R, R, W, R, R, W, R, R, R, W, W, G],#11
    [G, W, W, R, R, W, R, R, R, R, W, R, R, W, W, G],#12
    [R, R, W, W, W, W, R, R, R, R, W, W, W, W, R, R],#13
    [R, R, R, W, W, W, R, R, R, R, W, W, W, R, R, R],#14
    [R, R, R, W, W, W, W, R, R, W, W, W, W, R, R, R],#15
    [R, R, R, W, W, W, W, W, W, W, W, W, W, R, R, R],#16
    [R, R, W, W, S, S, B, S, S, B, S, S, W, W, R, R],#17
    [G, W, W, R, S, S, B, S, S, B, S, S, R, W, W, G],#18
    [G, S, G, G, S, S, S, S, S, S, S, S, G, G, S, G],#19
    [S, S, S, G, S, S, S, B, B, S, S, S, G, S, S, S],#20
    [S, S, S, S, R, R, S, S, S, S, R, R, S, S, S, S],#21
    [G, G, S, R, R, R, R, R, R, R, R, R, R, S, G, G],#22
    [G, G, R, R, R, R, S, S, S, S, R, R, R, R, G, G],#23
    [G, G, R, R, R, S, S, S, S, S, S, R, R, R, G, G],#24
    [G, G, R, R, R, S, S, S, S, S, S, R, R, R, G, G],#25
    [G, G, G, W, W, W, W, W, W, W, W, W, W, G, G, G],#26
    [G, G, W, W, W, W, W, W, W, W, W, W, W, W, G, G],#27
    [G, R, R, R, W, W, W, W, W, W, W, W, R, R, R, G],#28
    [R, W, R, R, R, W, W, W, W, W, W, R, R, R, W, R],#29
    [R, R, R, R, R, R, W, W, W, W, R, R, R, R, R, R],#30
    [R, R, R, R, R, R, W, W, W, W, R, R, R, R, R, R],#31
]
screen = Canvas(root, width=320, height=320, bg=clear_color)
screen.pack()
options = [
    "Small Mario",
    "Goomba",
    "Big Mario",
    "Bowser",
    "Peach",
    "Peach Lost Levels",
    "Toad"
]
clicked = StringVar()
clicked.set("Small Mario")
drop_down = OptionMenu(root, clicked, *options)
drop_down.pack()
current_sprite = small_mario
current_sprite_name = "Small Mario"
def draw_rectangle(x, y, width, height, color):
    ending_x = x + width
    ending_y = y + height
    screen.create_rectangle(x, y, ending_x, ending_y, fill=color)
def draw_sprite(sprite):
    clear()
    x = 0
    y = 0
    height_in_pixels = len(sprite)
    width_in_pixels = len(sprite[0])
    canvas_height = height_in_pixels * pixel_size
    canvas_width = width_in_pixels * pixel_size
    screen.config(width=canvas_width, height=canvas_height)

    for row in sprite:
        for color in row:
            draw_rectangle(x, y, pixel_size, pixel_size, color)
            x += pixel_size
        x = 0
        y += pixel_size
def clear():
    screen.delete("all")
def draw():
    global current_sprite
    global current_sprite_name
    current_selection = clicked.get()
    current_sprite_name = current_selection
    if current_selection == "Small Mario":
        current_sprite = small_mario
        draw_sprite(small_mario)
    elif current_selection == "Goomba":
        current_sprite = gumba
        draw_sprite(gumba)
    elif current_selection == "Big Mario":
        current_sprite = big_mario
        draw_sprite(big_mario)
    elif current_selection == "Bowser":
        current_sprite = bowser
        draw_sprite(bowser)
    elif current_selection == "Peach":
        current_sprite = peach
        draw_sprite(peach)
    elif current_selection == "Peach Lost Levels":
        current_sprite = Peach_ll_sprite
        draw_sprite(Peach_ll_sprite)
    elif current_selection == "Toad":
        current_sprite = Toad
        draw_sprite(Toad)   
def luigi():
    if(current_sprite_name == "Small Mario" or current_sprite_name == "Big Mario"):       
        luigi_sprite = []
        for row in current_sprite:
            new_row = []
            for color in row:
                if color == r:
                    new_row.append(lw)
                elif color == s:
                    new_row.append(ls)
                elif color == b:
                    new_row.append(lg)
                else:
                    new_row.append(color)
            luigi_sprite.append(new_row)
        draw_sprite(luigi_sprite)
def fire():
    if(current_sprite_name == "Big Mario"):
        fire_sprite = []
        for row in current_sprite:
            new_row = []
            for color in row:
                if color == r:
                    new_row.append(fw)
                elif color == s:
                    new_row.append(fs)
                elif color == b:
                    new_row.append(fr)
                else:
                    new_row.append(color)
            fire_sprite.append(new_row)
        draw_sprite(fire_sprite)
def Blue():
    if(current_sprite_name == "Goomba"):
        blue_sprite = []
        for row in current_sprite:
            new_row = []
            for color in row:
                if color == v:
                    new_row.append(t)
                elif color == k:
                    new_row.append(l)
                elif color == s:
                    new_row.append(n)
                elif color == d:
                    new_row.append(k)
                else:
                    new_row.append(color)
            blue_sprite.append(new_row)
        draw_sprite(blue_sprite)
def white_dress():
    if(current_sprite_name == "Peach Lost Levels"):
        white_dress_sprite = []
        for row in current_sprite:
            new_row = []
            for color in row:
                if color == w:
                    new_row.append(y)
                else:
                    new_row.append(color)
            white_dress_sprite.append(new_row)
        draw_sprite(white_dress_sprite)
#def normal():
    #if(current_sprite_name == "Peach Lost Levels", "Small Mario", "Big Mario", "Goomba"):
        #normal_sprite = []
        #for row in current_sprite:
            #new_row = []
            #for color in row:


draw_button = Button(root, text="Draw Sprite", command=draw)
draw_button.pack()
clear_button = Button(root, text="Clear", command=clear)
clear_button.pack()
#draw_normal = Button(root, text="Normal", command=normal)
#draw_normal.pack()
draw_luigi = Button(root, text="Draw Luigi", command=luigi)
draw_luigi.pack()
draw_fire = Button(root, text="Draw Fire", command=fire)
draw_fire.pack()
draw_Blue = Button(root, text="Draw Blue", command=Blue)
draw_Blue.pack()
draw_White_Dress = Button(root, text="Draw White Dress", command=white_dress)
draw_White_Dress.pack()
mainloop()