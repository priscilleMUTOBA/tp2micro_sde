EX1

var1 = "priscille mutoba"
basic.show_string(var1)

def on_forever():
    pass
basic.forever(on_forever)


EX2
def on_forever():
    led.plot(3, 2)
    basic.pause(200)
    led.unplot(3, 2)
basic.forever(on_forever)


EX3
def on_button_pressed_a():
    images.icon_image(IconNames.HAPPY).show_image(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    images.icon_image(IconNames.SAD).show_image(0)
input.on_button_pressed(Button.B, on_button_pressed_b)

EX4
v3 = 0

def on_forever():
    global v3
    for var2 in range(10):
        v3 = var2 % 2
        if v3 == 0:
            basic.show_number(var2)
basic.forever(on_forever)





