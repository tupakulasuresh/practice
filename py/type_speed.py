
def measure_speed(keyboard_layout, text):
    previous = 0
    speed = 0
    keyboard_layout = {j: i for i, j in enumerate(keyboard_layout)}
    for w in text:
        current = keyboard_layout.get(w)
        speed +=  abs(previous - current)
        previous = current
    return speed


keyboard = "abcdefghijklmnopqrstuvwxy"
text = "cba"
print measure_speed(keyboard, text)




