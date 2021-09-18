input.onGesture(Gesture.TiltRight, function () {
    led.unplot(x, y)
    x = x + 1
    led.plot(x, y)
})
input.onPinPressed(TouchPin.P0, function () {
	
})
input.onGesture(Gesture.LogoDown, function () {
    led.unplot(x, y)
    y = y - 1
    led.plot(x, y)
})
function pokyn () {
	
}
input.onButtonPressed(Button.A, function () {
    led.unplot(x, y)
    x = 3
    y = 3
    led.plot(x, y)
})
input.onGesture(Gesture.TiltLeft, function () {
    led.unplot(x, y)
    x = x - 1
    led.plot(x, y)
})
input.onGesture(Gesture.LogoUp, function () {
    led.unplot(x, y)
    y = y + 1
    led.plot(x, y)
})
let y = 0
let x = 0
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
x = 1
y = 1
led.plot(x, y)
