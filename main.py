def on_gesture_tilt_right():
    global x
    led.unplot(x, y)
    x = x + 1
    led.plot(x, y)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_pin_pressed_p0():
    pass
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_gesture_logo_down():
    global y
    led.unplot(x, y)
    y = y - 1
    led.plot(x, y)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def pokyn():
    pass

def on_button_pressed_a():
    global x, y
    led.unplot(x, y)
    x = 3
    y = 3
    led.plot(x, y)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    global x
    led.unplot(x, y)
    x = x - 1
    led.plot(x, y)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_logo_up():
    global y
    led.unplot(x, y)
    y = y + 1
    led.plot(x, y)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

y = 0
x = 0
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")
x = 1
y = 1
led.plot(x, y)